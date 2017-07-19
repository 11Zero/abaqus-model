# -*- coding:utf-8 -*-

# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
# mbcs
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
import visualization ###通过run-script执行该脚本时需引用这句
# from odbAccess import * ###官方解释，通过shell或cmd执行该脚本时需引用这句
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior

### 采用SI(mm)国际单位制

class AbaqusStructureClass:

    def __init__(self,model='structure',file = 'D:/pymodel.cae'):
        #初始化信息
        if not os.path.exists('c:/Abaqus_TempSave'):
            os.makedirs('c:/Abaqus_TempSave')
        mdb.saveAs(pathName='c:/Abaqus_TempSave/abaqus_model_'+time.strftime("%Y%m%d-%H%M%S", time.localtime()))
        Mdb()
        self.modelName = model
        self.filePath = file
        self.partLength = {}
        self.partCount = {}
        self.rebarStyle = {}
        self.partSize = {}
        self.allCols = {}
        self.colsPos = {}

    def __del__(self):
        #退出前保存
        mdb.save()

    def startBuilding(self):
        # keys = mdb.models.keys()
        # for key in keys:
        #     del mdb.models[key]
        # mdb.Model(name=self.modelName, modelType=STANDARD_EXPLICIT)
        mdb.models.changeKey(fromName='Model-1', toName=self.modelName)  # 重命名模型
        session.viewports['Viewport: 1'].setValues(displayedObject=None)  # 设置视口
        mdb.saveAs(pathName=self.filePath)  # 存储

        self.createMaterialConcrete('C20/25')
        self.createMaterialSteel('Q235')
        print "材料创建完成"

        self.createSectionConcrete('concrete CS','C20/25')
        self.createSectionRebar('rebar-r7',7,'Q235')



        self.createCol('col-1',[450, 450, 4000], 'concrete CS')
        self.createCol('col-2',[450, 450, 3300], 'concrete CS')
        self.createBeam('beam-1',[350, 600, 6150], 'concrete CS')
        self.createBeam('beam-2',[300, 600, 2250], 'concrete CS')
        self.createBeam('beam-3',[350, 600, 4050], 'concrete CS')
        self.createRebar('rebar-1',[4000],'rebar-r7')
        self.createRebar('rebar-2', [3300], 'rebar-r7')
        self.createRebar('rebar-3', [6150], 'rebar-r7')
        self.createRebar('rebar-4', [2250], 'rebar-r7')
        self.createRebar('rebar-5', [4050], 'rebar-r7')

        # self.rebarStyle['col-1'] = [[0 for i in range(3)] for i in range(3)]
        self.rebarStyle['col-1']= [[400],[400]]
        self.rebarStyle['col-2'] = [[400], [400]]

        for j in range(6):
            if j==0:
                height = 0
            else:
                height = 4000+3300*(j-1)
            for i in range(10):
                cmd = "self.colsPos['col-%d-%d-1'] = (4500*%d, %d, 0);" % ((j+1),(i+1),i,height) +\
                      "self.colsPos['col-%d-%d-2'] = (4500*%d, %d, 6600);"% ((j+1),(i+1),i,height) +\
                      "self.colsPos['col-%d-%d-3'] = (4500*%d, %d, 6600+2700);"% ((j+1),(i+1),i,height) +\
                      "self.colsPos['col-%d-%d-4'] = (4500*%d, %d, 6600+2700+6600)" % ((j+1),(i+1),i,height)
                exec(cmd)
        # self.colsPos['col-1-1-1'] = (4500*0, 0, 0)
        # self.colsPos['col-1-1-2'] = (4500*0, 0, 6600)
        # self.colsPos['col-1-1-3'] = (4500*0, 0, 6600+2700)
        # self.colsPos['col-1-1-4'] = (4500*0, 0, 6600+2700+6600)
        #
        # self.colsPos['col-1-2-1'] = (4500*1, 0, 0)
        # self.colsPos['col-1-2-2'] = (4500*1, 0, 6600)
        # self.colsPos['col-1-2-3'] = (4500*1, 0, 6600 + 2700)
        # self.colsPos['col-1-2-4'] = (4500*1, 0, 6600 + 2700 + 6600)
        #
        # self.colsPos['col-1-3-1'] = (4500*2, 0, 0)
        # self.colsPos['col-1-3-2'] = (4500*2, 0, 6600)
        # self.colsPos['col-1-3-3'] = (4500*2, 0, 6600 + 2700)
        # self.colsPos['col-1-3-4'] = (4500*2, 0, 6600 + 2700 + 6600)


        for colName in self.colsPos.keys():
            if colName[:5]=='col-1':
                cmd = "self.allCols['%s'] = self.assemblyRebarIntoConcrete('col-1', 'rebar-1','%s')" % (colName,colName)
            else:
                cmd = "self.allCols['%s'] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2','%s')" % (colName,colName)
            exec(cmd)
        # for i in range(4):
        #     cmd = "self.allCols['col-1-1-%d'] = self.assemblyRebarIntoConcrete('col-1', 'rebar-1')" % (i+1)
        #     exec(cmd)
        # self.allCols['col-1-1-1'] = self.assemblyRebarIntoConcrete( 'col-1', 'rebar-1')
        # self.allCols['col-1-1-2'] = self.assemblyRebarIntoConcrete('col-1', 'rebar-1')
        # self.allCols['col-1-1-3'] = self.assemblyRebarIntoConcrete('col-1', 'rebar-1')
        # self.allCols['col-1-1-4'] = self.assemblyRebarIntoConcrete('col-1', 'rebar-1')

        # for i in range(4):
        #     cmd = "self.allCols['col-1-2-%d'] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2')" % (i+1)
        #     exec(cmd)
        # self.allCols['col-1-2-1'] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2')
        # self.allCols['col-1-2-2'] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2')
        # self.allCols['col-1-2-3'] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2')
        # self.allCols['col-1-2-4'] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2')

        # for i in range(4):
        #     cmd = "self.allCols['col-1-3-%d'] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2')" % (i+1)
        #     exec(cmd)
        # self.allCols['col-1-3-1'] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2')
        # self.allCols['col-1-3-2'] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2')
        # self.allCols['col-1-3-3'] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2')
        # self.allCols['col-1-3-4'] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2')

        # for i in range(4):
        #     cmd = "self.allCols['col-1-2-%d'] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2')" % (i+1)
        #     exec(cmd)
        # beam1 = self.assemblyRebarIntoConcrete('beam-1', 'rebar-3',[[300],[275,275]],True)
        # beam2 = self.assemblyRebarIntoConcrete('beam-1', 'rebar-3',[[300],[275,275]])
        # beam3 = self.assemblyRebarIntoConcrete('beam-1', 'rebar-3',[[300],[275,275]])
        # beam4 = self.assemblyRebarIntoConcrete('beam-1', 'rebar-3',[[300],[275,275]])

        assembly = mdb.models[self.modelName].rootAssembly
        assembly.DatumCsysByDefault(CARTESIAN)


        for colName in self.allCols.keys():
            cmd = "assembly.translate(instanceList=tuple(self.allCols['%s']), vector=self.colsPos['%s'])" % (colName,colName)
            exec(cmd)
        # for i in range(4):
        #     cmd = "assembly.translate(instanceList=tuple(self.allCols['col-1-1-%d']), vector=self.colsPos['col-1-1-%d'])" % ((i+1),(i+1))
        #     exec(cmd)
        # assembly.translate(instanceList=tuple(self.allCols['col-1-1-1']), vector=self.colsPos['col-1-1-1'])
        # assembly.translate(instanceList=tuple(self.allCols['col-1-1-2']), vector=self.colsPos['col-1-1-2'])
        # assembly.translate(instanceList=tuple(self.allCols['col-1-1-3']), vector=self.colsPos['col-1-1-3'])
        # assembly.translate(instanceList=tuple(self.allCols['col-1-1-4']), vector=self.colsPos['col-1-1-4'])

        # for i in range(4):
        #     cmd = "assembly.translate(instanceList=tuple(self.allCols['col-1-2-%d']), vector=self.colsPos['col-1-2-%d'])" % ((i+1),(i+1))
        #     exec(cmd)
        # assembly.translate(instanceList=tuple(self.allCols['col-1-2-1']), vector=self.colsPos['col-1-2-1'])
        # assembly.translate(instanceList=tuple(self.allCols['col-1-2-2']), vector=self.colsPos['col-1-2-2'])
        # assembly.translate(instanceList=tuple(self.allCols['col-1-2-3']), vector=self.colsPos['col-1-2-3'])
        # assembly.translate(instanceList=tuple(self.allCols['col-1-2-4']), vector=self.colsPos['col-1-2-4'])

        # for i in range(4):
        #     cmd = "assembly.translate(instanceList=tuple(self.allCols['col-1-3-%d']), vector=self.colsPos['col-1-3-%d'])" % ((i+1),(i+1))
        #     exec(cmd)
        # assembly.translate(instanceList=tuple(self.allCols['col-1-3-1']), vector=self.colsPos['col-1-3-1'])
        # assembly.translate(instanceList=tuple(self.allCols['col-1-3-2']), vector=self.colsPos['col-1-3-2'])
        # assembly.translate(instanceList=tuple(self.allCols['col-1-3-3']), vector=self.colsPos['col-1-3-3'])
        # assembly.translate(instanceList=tuple(self.allCols['col-1-3-4']), vector=self.colsPos['col-1-3-4'])

        # assembly.translate(instanceList=beam1, vector=(0, 4000, 0))
        # assembly.translate(instanceList=beam2, vector=(0, 4000, 0))


        session.viewports['Viewport: 1'].setValues(displayedObject=mdb.models[self.modelName].rootAssembly)
        session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])



        # for key in mdb.models[self.modelName].parts.keys():
        #     if key[:2] == 'col' or key [:3] == 'beam':
        #         self.assignConcrete2Part('C20/25', mdb.models[self.modelName].parts[key])




    def createCol(self,name,size,section):
        width, height, length = size[0],size[1],size[2]
        s = mdb.models[self.modelName].ConstrainedSketch(name='__profile__',
            sheetSize=length)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.rectangle(point1=(0, 0), point2=(width, height))
        s.ObliqueDimension(vertex1=v[0], vertex2=v[3],
                           textPoint=(width/2,(width < height and width/2 or height/2)), value=width)
        s.ObliqueDimension(vertex1=v[0], vertex2=v[1],
                           textPoint=(-(width < height and width / 2 or height / 2),height/2), value=height)
        p = mdb.models[self.modelName].Part(name=name,
                                            dimensionality=THREE_D,type=DEFORMABLE_BODY)
        p = mdb.models[self.modelName].parts[name]
        p.BaseSolidExtrude(sketch=s, depth=length)
        self.partLength[name] = length
        self.partSize[name] = size
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

    def createBeam(self,name,size,section):
        return self.createCol(name,size,section)

    def createRebar(self,name,size,section):
        length = size[0]
        s = mdb.models[self.modelName].ConstrainedSketch(name='__profile__',
                                                      sheetSize=length)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.Line(point1=(0, 0.0), point2=(length, 0.0))
        s.HorizontalConstraint(entity=g[2], addUndoState=False)
        s.HorizontalDimension(vertex1=v[0], vertex2=v[1], textPoint=(length/2,length/20), value=length)
        p = mdb.models[self.modelName].Part(name=name, dimensionality=THREE_D,
                                         type=DEFORMABLE_BODY)
        self.partLength[name] = length
        self.partSize[name] = size
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

    def assemblyRebarIntoConcrete(self,concretePart,rebarPart,instanceName = '',rebarStyle=[],beamXDirection = False):
        if rebarStyle == []:
            rebarStyle = self.rebarStyle[concretePart]

        concreteAndRebarSet = []
        a = mdb.models[self.modelName].rootAssembly

        p = mdb.models[self.modelName].parts[concretePart]


        if not self.partCount.has_key(concretePart):
            self.partCount[concretePart] = 0
        self.partCount[concretePart] = self.partCount[concretePart] +1
        name = ''
        if self.allCols.has_key(instanceName) or instanceName == '':
            name = concretePart+'-%d' % self.partCount[concretePart]
        else:
            name = instanceName
        a.Instance(name=name, part=p, dependent=ON)

        p = mdb.models[self.modelName].parts[rebarPart]
        if not self.partCount.has_key(name+'-'+rebarPart):
            self.partCount[name+'-'+rebarPart] = 0
        self.partCount[name+'-'+rebarPart] = \
            self.partCount[name+'-'+rebarPart] +1
        # if not self.partCount.has_key(concretePart+'-%d-' % self.partCount[concretePart]+rebarPart):
        #     self.partCount[concretePart+'-%d-' % self.partCount[concretePart]+rebarPart] = 0
        # self.partCount[concretePart+'-%d-' % self.partCount[concretePart]+rebarPart] = \
        #     self.partCount[concretePart+'-%d-' % self.partCount[concretePart]+rebarPart] +1
        # rebarInstanceSubName =
        rebarInstanceName = name+'-'+rebarPart +\
                            '-%d' % self.partCount[name+'-'+rebarPart]
        a.Instance(name=rebarInstanceName,part=p, dependent=ON)
        concreteAndRebarSet.append(rebarInstanceName)
        #a.translate(instanceList=('rebar-1-1',), vector=(2000.0, 0.0, 0.0))
        a.rotate(instanceList=(rebarInstanceName,),
                 axisPoint=(0.0, 0.0, 0.0),
                 axisDirection=(0.0, -1.0, 0.0), angle=90.0)
        for iy in range(len(rebarStyle[1])):
            if iy == 0:
                firstRebarInstanceName = rebarInstanceName
                for ix in range(len(rebarStyle[0])):
                    a.LinearInstancePattern(instanceList=(rebarInstanceName,),
                                             direction1=(1.0,0.0, 0.0),
                                             direction2=(0.0, 0.0, 0.0),
                                             number1=2,
                                             number2=1,
                                             spacing1=rebarStyle[0][ix],
                                             spacing2=100.0)
                    self.partCount[name+'-'+rebarPart] = \
                        self.partCount[name+'-'+rebarPart] + 1
                    rebarInstanceName = name+'-'+rebarPart + \
                                        '-%d' % self.partCount[name+'-'+rebarPart]
                    mdb.models[self.modelName].rootAssembly.features.changeKey(
                        fromName=mdb.models[self.modelName].rootAssembly.instances.keys()[-1], toName=rebarInstanceName)
                    concreteAndRebarSet.append(rebarInstanceName)
                rebarInstanceName = firstRebarInstanceName

            a.LinearInstancePattern(instanceList=(rebarInstanceName,),
                                    direction1=(0.0, 1.0, 0.0),
                                    direction2=(0.0, 0.0, 0.0),
                                    number1=2,
                                    number2=1,
                                    spacing1=rebarStyle[1][iy],
                                    spacing2=100.0)
            self.partCount[name + '-' + rebarPart] = \
                self.partCount[name + '-' + rebarPart] + 1
            rebarInstanceName = name + '-' + rebarPart + \
                                '-%d' % self.partCount[name + '-' + rebarPart]
            mdb.models[self.modelName].rootAssembly.features.changeKey(
                fromName=mdb.models[self.modelName].rootAssembly.instances.keys()[-1], toName=rebarInstanceName)
            concreteAndRebarSet.append(rebarInstanceName)

            firstRebarInstanceName = rebarInstanceName

            for ix in range(len(rebarStyle[0])):
                a.LinearInstancePattern(instanceList=(rebarInstanceName,),
                                         direction1=(1.0,0.0, 0.0),
                                         direction2=(0.0, 0.0, 0.0),
                                         number1=2,
                                         number2=1,
                                         spacing1=rebarStyle[0][ix],
                                         spacing2=100.0)
                self.partCount[name + '-' + rebarPart] = \
                    self.partCount[name + '-' + rebarPart] + 1
                rebarInstanceName = name + '-' + rebarPart + \
                                    '-%d' % self.partCount[name + '-' + rebarPart]
                mdb.models[self.modelName].rootAssembly.features.changeKey(
                    fromName=mdb.models[self.modelName].rootAssembly.instances.keys()[-1], toName=rebarInstanceName)
                concreteAndRebarSet.append(rebarInstanceName)

            rebarInstanceName = firstRebarInstanceName

        # for i in range(self.partCount[concretePart + '-%d-' % self.partCount[concretePart] + rebarPart]):
        #     i= i+1
        rebarWidth = 0
        rebarHeight = 0
        for width in rebarStyle[0]:
            rebarWidth = rebarWidth+width

        for height in rebarStyle[1]:
            rebarHeight = rebarHeight+height

        vector = ((self.partSize[concretePart][0]-rebarWidth)/2,(self.partSize[concretePart][1]-rebarHeight)/2,0)
        a.translate(instanceList=tuple(concreteAndRebarSet),
                    vector=vector)
            # a.translate(instanceList=(concretePart + '-%d-' % self.partCount[concretePart] + rebarPart + '-%d' % i,), vector=vector)

        concreteAndRebarSet.append(name)

        if concretePart[:3] == 'col':
            a.rotate(instanceList=tuple(concreteAndRebarSet),
                     axisPoint=(0.0, 0.0, 0.0),
                     axisDirection=(1.0, 0.0, 0.0), angle=90.0)
            vector = (0,self.partLength[concretePart],0)
            a.translate(instanceList=tuple(concreteAndRebarSet),
                        vector=vector)

        if concretePart[:4] == 'beam':
            vector = (0, -self.partSize[concretePart][1], 0)
            a.translate(instanceList=tuple(concreteAndRebarSet),
                        vector=vector)

        if beamXDirection:
            a.rotate(instanceList=tuple(concreteAndRebarSet),
                     axisPoint=(0.0, 0.0, 0.0),
                     axisDirection=(0.0, -1.0, 0.0), angle=90.0)
            vector = (self.partLength[concretePart],0,0)
            a.translate(instanceList=tuple(concreteAndRebarSet),
                        vector=vector)

        return concreteAndRebarSet



mymodel = AbaqusStructureClass()
mymodel.startBuilding()