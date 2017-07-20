# -*- coding:utf-8 -*-

# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
# mbcs
import time
import os
import re

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
        self.modelVolume = [0,0,0]
        self.filePath = file
        self.partLength = {}
        self.partCount = {}
        self.rebarStyle = {}
        self.partSize = {}
        self.allCols = {}
        self.colsPos = {}
        self.colsPart = {}
        self.colsBeamState = {} #用于存储四个布尔值表示柱四周梁的有无[up,down,left,right]
        self.allZBeams = {}
        self.zBeamsPos = {}
        self.zBeamsPart = {}
        self.allXBeams = {}
        self.xBeamsPos = {}
        self.xBeamsPart = {}

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

        self.modelVolume = [13500, 7300, 15900]

        self.createMaterialConcrete('C20/25')
        self.createMaterialSteel('Q235')
        print "materials created"

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
        self.rebarStyle['beam-1'] = [[300], [275,275]]
        self.rebarStyle['beam-2'] = [[250], [275,275]]
        self.rebarStyle['beam-3'] = [[300], [275, 275]]

        for j in range(2):
            if j==0:
                height = 0
            else:
                height = 4000+3300*(j-1)
            for i in range(4):
                cmd = "self.colsPos['col-%d-%d-1'] = [4500*%d, %d, 0];" % ((j+1),(i+1),i,height) +\
                      "self.colsPos['col-%d-%d-2'] = [4500*%d, %d, 6600];"% ((j+1),(i+1),i,height) +\
                      "self.colsPos['col-%d-%d-3'] = [4500*%d, %d, 6600+2700];"% ((j+1),(i+1),i,height) +\
                      "self.colsPos['col-%d-%d-4'] = [4500*%d, %d, 6600+2700+6600]" % ((j+1),(i+1),i,height)
                exec(cmd)

        for colName in self.colsPos.keys():
            if abs(self.colsPos[colName][0] - 0) < 500:
                if abs(self.colsPos[colName][2] - 0) < 500:
                    self.colsBeamState[colName] = [0,1,0,1]
                elif abs(self.colsPos[colName][2] - self.modelVolume[2]) < 500:
                    self.colsBeamState[colName] = [1,0,0,1]
                else:
                    self.colsBeamState[colName] = [1, 1, 0, 1]
            elif abs(self.colsPos[colName][0] - self.modelVolume[0]) < 500:
                if abs(self.colsPos[colName][2] - 0) < 500:
                    self.colsBeamState[colName] = [0,1,1,0]
                elif abs(self.colsPos[colName][2] - self.modelVolume[2]) < 500:
                    self.colsBeamState[colName] = [1,0,1,0]
                else:
                    self.colsBeamState[colName] = [1, 1, 1, 0]
            elif abs(self.colsPos[colName][2] - 0) < 500:
                self.colsBeamState[colName] = [0, 1, 1, 1]
            elif abs(self.colsPos[colName][2] - self.modelVolume[2]) < 500:
                self.colsBeamState[colName] = [1, 0, 1, 1]
            else:
                self.colsBeamState[colName] = [1, 1, 1, 1]

        for j in range(2):
            height = 4000 + 3300 * j
            for i in range(4):
                cmd = "self.zBeamsPos['zbeam-%d-%d-1'] = [4500*%d, %d, 0];" % ((j + 1), (i + 1), i, height) + \
                      "self.zBeamsPos['zbeam-%d-%d-2'] = [4500*%d, %d, 6600];" % ((j + 1), (i + 1), i, height) + \
                      "self.zBeamsPos['zbeam-%d-%d-3'] = [4500*%d, %d, 6600+2700]" % ((j + 1), (i + 1), i, height)
                exec (cmd)

        for j in range(2):
            height = 4000 + 3300 * j
            for i in range(3):
                cmd = "self.xBeamsPos['xbeam-%d-%d-1'] = [4500*%d, %d, 0];" % ((j + 1), (i + 1), i, height) + \
                      "self.xBeamsPos['xbeam-%d-%d-2'] = [4500*%d, %d, 6600];" % ((j + 1), (i + 1), i, height) + \
                      "self.xBeamsPos['xbeam-%d-%d-3'] = [4500*%d, %d, 6600+2700];" % ((j + 1), (i + 1), i, height) + \
                      "self.xBeamsPos['xbeam-%d-%d-4'] = [4500*%d, %d, 6600+2700+6600]" % ((j + 1), (i + 1), i, height)
                exec (cmd)
        # print self.zBeamsPos.keys()
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
                self.allCols[colName] = self.assemblyRebarIntoConcrete('col-1', 'rebar-1',colName)
            else:
                self.allCols[colName] = self.assemblyRebarIntoConcrete('col-2', 'rebar-2',colName)


        for beamName in self.zBeamsPos.keys():
            if re.match('zbeam-\d-\d+-2', beamName):
                self.allZBeams[beamName] = self.assemblyRebarIntoConcrete('beam-2', 'rebar-4',beamName)
            else:
                self.allZBeams[beamName] = self.assemblyRebarIntoConcrete('beam-1', 'rebar-3',beamName)

        for beamName in self.xBeamsPos.keys():
            self.allXBeams[beamName] = self.assemblyRebarIntoConcrete('beam-3', 'rebar-5', beamName)
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
        # mdb.models['structure'].rootAssembly.instances['col-2-3-3'].faces.getSequenceFromMask(mask=('[#1 ]', ), )

        for colName in self.allCols.keys():
            assembly.translate(instanceList=tuple(self.allCols[colName]), vector=self.colsPos[colName])

        for beamName in self.allZBeams.keys():
            assembly.translate(instanceList=tuple(self.allZBeams[beamName]), vector=self.zBeamsPos[beamName])

        for beamName in self.allXBeams.keys():
            assembly.translate(instanceList=tuple(self.allXBeams[beamName]), vector=self.xBeamsPos[beamName])


        for beamName in self.allZBeams.keys():
            vector = [(self.partSize[self.colsPart['col'+beamName[5:]]][0] - self.partSize[self.zBeamsPart[beamName]][0])/2,
                      0,self.partSize[self.colsPart['col'+beamName[5:]]][1]]
            if abs(self.zBeamsPos[beamName][0] - 0) < 500:
                vector[0] = vector[0]-(self.partSize[self.colsPart['col'+beamName[5:]]][0] - self.partSize[self.zBeamsPart[beamName]][0])/2
            if abs(self.zBeamsPos[beamName][0] - self.modelVolume[0]) < 500:
                vector[0] = vector[0] + (self.partSize[self.colsPart['col'+beamName[5:]]][0] - self.partSize[self.zBeamsPart[beamName]][0])/2
            self.updateInstancePos(self.zBeamsPos[beamName],vector)
            assembly.translate(instanceList=tuple(self.allZBeams[beamName]), vector=vector)

        for beamName in self.allXBeams.keys():
            vector = [self.partSize[self.colsPart['col' + beamName[5:]]][0],
                      0, (self.partSize[self.colsPart['col' + beamName[5:]]][1] -
                       self.partSize[self.xBeamsPart[beamName]][0]) / 2]
            if abs(self.xBeamsPos[beamName][2] - 0) < 500:
                vector[2] = vector[2]-(self.partSize[self.colsPart['col' + beamName[5:]]][1] - self.partSize[self.xBeamsPart[beamName]][0]) / 2
            if abs(self.xBeamsPos[beamName][2] - self.modelVolume[2]) < 500:
                vector[2] = vector[2] + (self.partSize[self.colsPart['col' + beamName[5:]]][1] - self.partSize[self.xBeamsPart[beamName]][0]) / 2
            self.updateInstancePos(self.xBeamsPos[beamName], vector)
            assembly.translate(instanceList=tuple(self.allXBeams[beamName]), vector=vector)
        surfStr = '';
        for colName in self.allCols.keys():待解决
            # surfs = self.getColSurfToBeam(colName)
            # if surfs is not None:
            #     surfs =
            surfStr = surfStr + "self.getColSurfToBeam(%s)+" % colName

        cmd = "assembly.Surface(side1Faces=%s, name='col-beam-surf')" % surfStr[:-1]
        exec (cmd)
            # cmd = "newpos = (self.zBeamsPos['%s'][0]+0,self.zBeamsPos['%s'][1]+0,self.zBeamsPos['%s'][2]+" % (beamName, beamName, beamName) +\
            #       "self.partSize[self.colsPart['col'+beamName[4:]]][1]);" +\
            #       "del self.zBeamsPos['%s'];"  % beamName +\
            #       "self.zBeamsPos['%s'] = newpos;" % beamName +\
            #       "assembly.translate(instanceList=tuple(self.allZBeams['%s']), vector=vector)" % beamName
            # exec (cmd)
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

    def assemblyRebarIntoConcrete(self,concretePart,rebarPart,instanceName = '',rebarStyle=[]):
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
        a.Instance(name=name, part=p, dependent=OFF)

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
        a.Instance(name=rebarInstanceName,part=p, dependent=OFF)
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
            self.colsPart[name] = concretePart

        if concretePart[:4] == 'beam' and instanceName[:5] == 'zbeam':
            vector = (0, -self.partSize[concretePart][1], 0)
            a.translate(instanceList=tuple(concreteAndRebarSet),
                        vector=vector)
            self.zBeamsPart[name] = concretePart

        if concretePart[:4] == 'beam' and instanceName[:5] == 'xbeam':
            vector = (0, -self.partSize[concretePart][1], 0)
            a.translate(instanceList=tuple(concreteAndRebarSet),
                        vector=vector)
            self.xBeamsPart[name] = concretePart
            a.rotate(instanceList=tuple(concreteAndRebarSet),
                     axisPoint=(0.0, 0.0, 0.0),
                     axisDirection=(0.0, -1.0, 0.0), angle=90.0)
            vector = (self.partLength[concretePart],0,0)
            a.translate(instanceList=tuple(concreteAndRebarSet),
                        vector=vector)

        return concreteAndRebarSet

    def updateInstancePos(self,pos,vector):
        pos[0] = pos[0]+vector[0]
        pos[1] = pos[1] + vector[1]
        pos[2] = pos[2] + vector[2]
        return pos
        # if instanceName[:3] == 'col':
        #     self.colsPos[instanceName] = (self.colsPos[instanceName][0]+vector[0],self.colsPos[instanceName][1]+vector[1],self.colsPos[instanceName][2]+vector[2])
        #
        # if instanceName[:4] == 'beam':
        #     self.zBeamsPos[instanceName] = (self.zBeamsPos[instanceName][0] + vector[0], self.zBeamsPos[instanceName][1] + vector[1],
        #               self.zBeamsPos[instanceName][2] + vector[2])

    def getColSurfToBeam(self,colName):
        if colName.count('-') != 3:
            return
        floor = int(colName[colName.find('-')+1:colName.find('-',colName.find('-')+1)])
        xcount = int(colName[colName.find('-', colName.find('-') + 1) + 1:colName.find('-', colName.find('-', colName.find('-') + 1) + 1)])
        zcount = int(colName[colName.rfind('-')+1:])
        a = mdb.models[self.modelName].rootAssembly
        if(self.colsBeamState[colName] == [1,1,1,1]):
            leftSize = self.partSize[self.xBeamsPart['xbeam-%d-%d-%d' % (floor, xcount-1, zcount)]][:2]
            rightSize = self.partSize[self.xBeamsPart['xbeam-%d-%d-%d' % (floor, xcount, zcount)]][:2]
            upSize = self.partSize[self.zBeamsPart['zbeam-%d-%d-%d' % (floor, xcount, zcount-1)]][:2]
            downSize = self.partSize[self.zBeamsPart['zbeam-%d-%d-%d' % (floor, xcount, zcount)]][:2]
            if(leftSize[1]== rightSize[1] and upSize[1] == downSize[1] and leftSize[1] == upSize[1]):
                c1 = a.instances[colName].cells
                pickedCells = c1.getSequenceFromMask(mask=('[#1 ]',), )
                v1 = a.instances['xbeam-%d-%d-%d' % (floor, xcount, zcount)].vertices
                e1 = a.instances['xbeam-%d-%d-%d' % (floor, xcount, zcount)].edges
                a.PartitionCellByPlanePointNormal(point=v1[6], normal=e1[7],cells=pickedCells)
                if leftSize[0] == rightSize[0]:
                    # 柱子右侧梁剖切面，下部线
                    pickedCells = c1.getSequenceFromMask(mask=('[#2 ]',), )
                    v1 = a.instances['xbeam-%d-%d-%d' % (floor, xcount, zcount)].vertices
                    e1 = a.instances['xbeam-%d-%d-%d' % (floor, xcount, zcount)].edges
                    a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[4], cells=pickedCells)
                    # 柱子右侧梁剖切面，上部线
                    pickedCells = c1.getSequenceFromMask(mask=('[#1 ]',), )
                    v1 = a.instances['xbeam-%d-%d-%d' % (floor, xcount, zcount)].vertices
                    e1 = a.instances['xbeam-%d-%d-%d' % (floor, xcount, zcount)].edges
                    a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[4], cells=pickedCells)
                    # 柱子下侧梁剖切面，右部线
                    pickedCells = c1.getSequenceFromMask(mask=('[#8 ]',), )
                    v1 = a.instances['zbeam-%d-%d-%d' % (floor, xcount, zcount)].vertices
                    e1 = a.instances['zbeam-%d-%d-%d' % (floor, xcount, zcount)].edges
                    a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[6], cells=pickedCells)
                    # 柱子下侧梁剖切面，左部线
                    pickedCells = c1.getSequenceFromMask(mask=('[#1 ]',), )
                    v1 = a.instances['zbeam-%d-%d-%d' % (floor, xcount, zcount)].vertices
                    e1 = a.instances['zbeam-%d-%d-%d' % (floor, xcount, zcount)].edges
                    a.PartitionCellByPlanePointNormal(point=v1[2], normal=e1[6], cells=pickedCells)
                    # 柱子上侧梁剖切面，右部线
                    pickedCells = c1.getSequenceFromMask(mask=('[#4 ]',), )
                    v1 = a.instances['zbeam-%d-%d-%d' % (floor, xcount, zcount-1)].vertices
                    e1 = a.instances['zbeam-%d-%d-%d' % (floor, xcount, zcount-1)].edges
                    a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[4], cells=pickedCells)
                    # 柱子上侧梁剖切面，左部线
                    pickedCells = c1.getSequenceFromMask(mask=('[#1 ]',), )
                    v1 = a.instances['zbeam-%d-%d-%d' % (floor, xcount, zcount - 1)].vertices
                    e1 = a.instances['zbeam-%d-%d-%d' % (floor, xcount, zcount - 1)].edges
                    a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[4], cells=pickedCells)

                    s1 = a.instances[colName].faces
                    side1Faces1 = s1.getSequenceFromMask(mask=('[#88400000 #10 ]',), )
                    return side1Faces1



mymodel = AbaqusStructureClass()
mymodel.startBuilding()