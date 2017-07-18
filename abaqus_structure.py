# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *

import time
import os

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization ###??run-script???????????
# from odbAccess import * ###???????shell?cmd???????????
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior

### ??SI(mm)?????

class AbaqusStructureClass:

    def __init__(self,model='structure',file = 'D:/pymodel.cae'):
        #?????
        if not os.path.exists('c:/Abaqus_TempSave'):
            os.makedirs('c:/Abaqus_TempSave')
        mdb.saveAs(pathName='c:/Abaqus_TempSave/abaqus_model_'+time.strftime("%Y%m%d-%H%M%S", time.localtime()))
        Mdb()
        self.modelName = model
        self.filePath = file

    def __del__(self):
        #?????
        mdb.save()

    def startBuilding(self):
        # keys = mdb.models.keys()
        # for key in keys:
        #     del mdb.models[key]
        # mdb.Model(name=self.modelName, modelType=STANDARD_EXPLICIT)
        mdb.models.changeKey(fromName='Model-1', toName=self.modelName)  # ?????
        session.viewports['Viewport: 1'].setValues(displayedObject=None)  # ????
        mdb.saveAs(pathName=self.filePath)  # ??

        self.createMaterialConcrete('C20/25')
        self.createMaterialSteel('Q235')

        self.createSectionConcrete('concrete CS','C20/25')
        self.createSectionRebar('rebar-r7',7,'Q235')

        parts = {}
        self.createCol('col-1',450, 450, 4000, 'concrete CS')
        self.createCol('col-1',450, 450, 3300, 'concrete CS')
        self.createBeam('beam-1',350, 600, 6150, 'concrete CS')
        self.createBeam('beam-2',300, 600, 2250, 'concrete CS')
        self.createBeam('beam-3',350, 600, 4050, 'concrete CS')
        self.createRebar('rebar-1',4000,'rebar-r7')


        # for key in mdb.models[self.modelName].parts.keys():
        #     if key[:2] == 'col' or key [:3] == 'beam':
        #         self.assignConcrete2Part('C20/25', mdb.models[self.modelName].parts[key])




    def createCol(self,name,width,height,length,section):
        s = mdb.models[self.modelName].ConstrainedSketch(name='__profile__',
            sheetSize=length)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.rectangle(point1=(-width/2, height/2), point2=(width/2, -height/2))
        s.ObliqueDimension(vertex1=v[0], vertex2=v[3],
                           textPoint=(0,(width < height and width/2 or height/2)+height/2), value=width)
        s.ObliqueDimension(vertex1=v[0], vertex2=v[1],
                           textPoint=(-(width < height and width / 2 or height / 2) - width / 2,0), value=height)
        p = mdb.models[self.modelName].Part(name=name,
                                            dimensionality=THREE_D,type=DEFORMABLE_BODY)
        p = mdb.models[self.modelName].parts[name]
        p.BaseSolidExtrude(sketch=s, depth=length)
        s.unsetPrimaryObject()

        c = p.cells
        cells = c.getSequenceFromMask(mask=('[#1 ]',), )
        region = regionToolset.Region(cells=cells)
        p.SectionAssignment(region=region, sectionName=section, offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models[self.modelName].sketches['__profile__']
        return p

    def createBeam(self,name,width,height,length,section):
        return self.createCol(name,width,height,length,section)

    def createRebar(self,name,length,section):
        s = mdb.models[self.modelName].ConstrainedSketch(name='__profile__',
                                                      sheetSize=length)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.Line(point1=(-length/2, 0.0), point2=(length/2, 0.0))
        s.HorizontalConstraint(entity=g[2], addUndoState=False)
        s.HorizontalDimension(vertex1=v[0], vertex2=v[1], textPoint=(0,length/20), value=length)
        p = mdb.models[self.modelName].Part(name=name, dimensionality=THREE_D,
                                         type=DEFORMABLE_BODY)
        p = mdb.models[self.modelName].parts[name]
        p.BaseWire(sketch=s)
        s.unsetPrimaryObject()

        e = p.edges
        edges = e.getSequenceFromMask(mask=('[#1 ]',), )
        region = regionToolset.Region(edges=edges)
        p.SectionAssignment(region=region, sectionName=section, offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)
        p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0,-1.0))
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models[self.modelName].sketches['__profile__']
        return p

    def createMaterialConcrete(self,name,grade='C20/25'):
        mdb.models[self.modelName].Material(name=name)
        mdb.models[self.modelName].materials[name].Density(table=((2.4e-09,),))
        mdb.models[self.modelName].materials[name].Elastic(table=((20000.0, 0.18),))
        mdb.models[self.modelName].materials[name].ConcreteDamagedPlasticity(table=((31.0, 0.1, 1.16, 0.667, 0.0),))
        mdb.models[self.modelName].materials[name].concreteDamagedPlasticity.ConcreteCompressionHardening(table=((25.0, 0.0),))
        mdb.models[self.modelName].materials[name].concreteDamagedPlasticity.ConcreteTensionStiffening(table=((2.25, 0.0),))

    def createMaterialSteel(self,name,grade = 'Q235'):
        mdb.models[self.modelName].Material(name=name)
        mdb.models[self.modelName].materials[name].Density(table=((7.85e-09,),))
        mdb.models[self.modelName].materials[name].Elastic(table=((210000.0, 0.3),))
        mdb.models[self.modelName].materials[name].Plastic(table=((350.0, 0.0),))

    def createSectionConcrete(self,sectionName,materialName):
        mdb.models[self.modelName].HomogeneousSolidSection(name=sectionName,
                                                        material=materialName, thickness=None)

    def createSectionRebar(self,sectionName,radius,materialName):
        mdb.models[self.modelName].CircularProfile(name='rebar-r%d' % radius, r=radius)
        mdb.models[self.modelName].BeamSection(name=sectionName,
                                            integration=DURING_ANALYSIS, poissonRatio=0.3, profile='rebar-r%d' % radius,
                                            material=materialName, temperatureVar=LINEAR, consistentMassMatrix=False)


mymodel = AbaqusStructureClass()
mymodel.startBuilding()