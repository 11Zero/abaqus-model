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
### abaqus cae startup=Beam.py为cmd下启动执行的py方法
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
        self.colsColState = {} #用于存储两个布尔值表示柱子上下是否有柱子[up,down]
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

        mdb.models.changeKey(fromName='Model-1', toName=self.modelName)  # 重命名模型
        session.viewports['Viewport: 1'].setValues(displayedObject=None)  # 设置视口
        mdb.saveAs(pathName=self.filePath)  # 存储

        self.modelVolume = [18000, 7300, 22500]

        self.createMaterialConcrete('C20/25')
        self.createMaterialSteel('Q235')
        print "materials created"

        self.createSectionConcrete('concrete CS','C20/25')
        self.createSectionRebar('rebar-r7',7,'Q235')



        self.createCol('col-1',[450, 450, 4000], 'concrete CS')
        self.createCol('col-2',[450, 450, 3300], 'concrete CS')
        self.createBeam('beam-1',[350, 600, 6150], 'concrete CS')
        self.createBeam('beam-2',[350, 700, 2250], 'concrete CS')
        self.createBeam('beam-3',[350, 600, 4050], 'concrete CS')
        self.createBeam('beam-4', [450, 600, 4050], 'concrete CS')
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
            for i in range(5):#沿x方向有5个柱子
                #沿z方向有5个柱子
                cmd = "self.colsPos['col-%d-%d-1'] = [4500*%d, %d, 0];" % ((j+1),(i+1),i,height) +\
                      "self.colsPos['col-%d-%d-2'] = [4500*%d, %d, 6600];"% ((j+1),(i+1),i,height) +\
                      "self.colsPos['col-%d-%d-3'] = [4500*%d, %d, 6600+2700];"% ((j+1),(i+1),i,height) +\
                      "self.colsPos['col-%d-%d-4'] = [4500*%d, %d, 6600+2700+6600];" % ((j+1),(i+1),i,height) +\
                      "self.colsPos['col-%d-%d-5'] = [4500*%d, %d, 6600+2700+6600+6600]" % ((j + 1), (i + 1), i, height)
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
            for i in range(5):#沿x方向布置5次
                #每次沿z方向有4段梁
                cmd = "self.zBeamsPos['zbeam-%d-%d-1'] = [4500*%d, %d, 0];" % ((j + 1), (i + 1), i, height) + \
                      "self.zBeamsPos['zbeam-%d-%d-2'] = [4500*%d, %d, 6600];" % ((j + 1), (i + 1), i, height) + \
                      "self.zBeamsPos['zbeam-%d-%d-3'] = [4500*%d, %d, 6600+2700];" % ((j + 1), (i + 1), i, height) + \
                      "self.zBeamsPos['zbeam-%d-%d-4'] = [4500*%d, %d, 6600+2700+6600]" % ((j + 1), (i + 1), i, height)
                exec (cmd)

        for j in range(2):
            height = 4000 + 3300 * j
            for i in range(4):#沿x方向布置4段
                #每段有5个梁
                cmd = "self.xBeamsPos['xbeam-%d-%d-1'] = [4500*%d, %d, 0];" % ((j + 1), (i + 1), i, height) + \
                      "self.xBeamsPos['xbeam-%d-%d-2'] = [4500*%d, %d, 6600];" % ((j + 1), (i + 1), i, height) + \
                      "self.xBeamsPos['xbeam-%d-%d-3'] = [4500*%d, %d, 6600+2700];" % ((j + 1), (i + 1), i, height) + \
                      "self.xBeamsPos['xbeam-%d-%d-4'] = [4500*%d, %d, 6600+2700+6600];" % ((j + 1), (i + 1), i, height) +\
                      "self.xBeamsPos['xbeam-%d-%d-5'] = [4500*%d, %d, 6600+2700+6600+6600]" % ((j + 1), (i + 1), i, height)
                exec (cmd)



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
        # for colName in self.allCols.keys():
        #     # surfs = self.getColSurfToBeam(colName)
        #     # if surfs is not None:
        #     #     surfs =
        #     surfStr = surfStr + "self.getColSurfToBeam(%s)+" % colName
        #
        # cmd = "assembly.Surface(side1Faces=%s, name='col-beam-surf')" % surfStr[:-1]
        # exec (cmd)
        bottomColBottomSurfs = []
        for colName in self.allCols.keys():
            self.colsColState[colName] = [1, 1]
            if abs(self.colsPos[colName][1] - 0) < 500:
                bottomColBottomSurfs.append(self.getColBottomSurf(colName))
                self.colsColState[colName][1] = 0
            if abs(self.colsPos[colName][1] + self.partSize[self.colsPart[colName]][2] - self.modelVolume[1]) < 500:
                self.colsColState[colName][0] = 0

        totalSurfs = None
        validIndex = 0
        for i in range(len(bottomColBottomSurfs)):
            if bottomColBottomSurfs[i] is not None:
                totalSurfs = bottomColBottomSurfs[i]
                validIndex = i
                break
        for i in range(validIndex + 1, len(bottomColBottomSurfs)):
            if bottomColBottomSurfs[i] is not None:
                totalSurfs = totalSurfs + bottomColBottomSurfs[i]
        if totalSurfs is not None:
            assembly.Set(faces=totalSurfs, name='set-bottomcol-bottomsurf')
            # assembly.Surface(side1Faces=totalSurfs, name='col-top-surf')

        # c1 = assembly.instances['col-2-4-2'].cells
        # # cells1 = c1.getSequenceFromMask(mask=('[#ffff ]',), )
        # assembly.Set(cells=c1, name='Set-4')

        concreteInstance = []
        rebarInstance = []
        for instanceName in assembly.instances.keys():
            if (not ('rebar' in instanceName)) and ('col' in instanceName or 'xbeam' in instanceName or 'zbeam' in instanceName):
                concreteInstance.append(assembly.instances[instanceName])
            if 'rebar' in instanceName:
                rebarInstance.append(assembly.instances[instanceName])

        concreteCells = concreteInstance[0].cells
        for i in range(1,len(concreteInstance)):
            concreteCells = concreteCells + concreteInstance[i].cells
        assembly.Set(cells=concreteCells, name='set-concrete')

        rebarEdges = rebarInstance[0].edges
        for i in range(1, len(rebarInstance)):
            rebarEdges = rebarEdges + rebarInstance[i].edges
        assembly.Set(edges=rebarEdges, name='set-rebar')


        surfs = []
        for colName in self.allCols.keys():
            surfs.append(self.getColTopSurf(colName))
        totalSurfs = None
        validIndex = 0
        for i in range(len(surfs)):
            if surfs[i] is not None:
                totalSurfs = surfs[i]
                validIndex = i
                break
        for i in range(validIndex + 1, len(surfs)):
            if surfs[i] is not None:
                totalSurfs = totalSurfs + surfs[i]
        if totalSurfs is not None:
            assembly.Surface(side1Faces=totalSurfs, name='col-top-surf')

        surfs = []
        for colName in self.allCols.keys():
            surfs.append(self.getColBottomSurf(colName))
        totalSurfs = None
        validIndex = 0
        for i in range(len(surfs)):
            if surfs[i] is not None:
                totalSurfs = surfs[i]
                validIndex = i
                break
        for i in range(validIndex + 1, len(surfs)):
            if surfs[i] is not None:
                totalSurfs = totalSurfs + surfs[i]
        if totalSurfs is not None:
            assembly.Surface(side1Faces=totalSurfs, name='col-bottom-surf')

        surfs = []
        for colName in self.allCols.keys():
            surfs.append(self.getColSurfToBeam(colName))
        totalSurfs = None
        validIndex = 0
        for i in range(len(surfs)):
            if surfs[i] is not None:
                totalSurfs = surfs[i]
                validIndex = i
                break
        for i in range(validIndex+1, len(surfs)):
            if surfs[i] is not None:
                totalSurfs = totalSurfs + surfs[i]
        if totalSurfs is not None:
            assembly.Surface(side1Faces=totalSurfs, name='col-beam-surf')

        surfs = []
        for xBeamName in self.allXBeams.keys():
            surfs.append(self.getBeamSurfToCol(xBeamName))
        xtotalSurfs = None
        validIndex = 0
        for i in range(len(surfs)):
            if surfs[i] is not None:
                xtotalSurfs = surfs[i]
                validIndex = i
                break
        for i in range(validIndex + 1, len(surfs)):
            if surfs[i] is not None:
                xtotalSurfs = xtotalSurfs + surfs[i]

        surfs = []
        for zBeamName in self.allZBeams.keys():
            surfs.append(self.getBeamSurfToCol(zBeamName))
        ztotalSurfs = None
        validIndex = 0
        for i in range(len(surfs)):
            if surfs[i] is not None:
                ztotalSurfs = surfs[i]
                validIndex = i
                break
        for i in range(validIndex + 1, len(surfs)):
            if surfs[i] is not None:
                ztotalSurfs = ztotalSurfs + surfs[i]

        totalSurfs = None
        if xtotalSurfs is not None and ztotalSurfs is not None:
            totalSurfs = xtotalSurfs+ztotalSurfs
        elif xtotalSurfs is not None:
            totalSurfs = xtotalSurfs
        elif ztotalSurfs is not None:
            totalSurfs = ztotalSurfs

        if totalSurfs is not None:
            assembly.Surface(side1Faces=totalSurfs, name='beam-col-surf')


        region1 = assembly.surfaces['col-beam-surf']
        region2 = assembly.surfaces['beam-col-surf']
        mdb.models[self.modelName].Tie(name='constraint-col-beam', master=region1, slave=region2,
                                    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

        region1 = assembly.surfaces['col-top-surf']
        region2 = assembly.surfaces['col-bottom-surf']
        mdb.models[self.modelName].Tie(name='constraint-col-col', master=region1, slave=region2,
                                       positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

        region1 = assembly.sets['set-rebar']
        region2 = assembly.sets['set-concrete']
        mdb.models[self.modelName].EmbeddedRegion(name='constraint-concrete-rebar',
                                               embeddedRegion=region1, hostRegion=region2, weightFactorTolerance=1e-06,
                                               absoluteTolerance=0.0, fractionalTolerance=0.05, toleranceMethod=BOTH)

        print '设置地震分析步'
        import json
        data = None
        ProgramPath = 'F:/documents/Abaqus/abaqus-model/'
        amplitudeName = 'Vrance N-S Acc'
        with open(ProgramPath + 'EQ/' + amplitudeName+'.json') as json_file:
            data = json.load(json_file)
        if data is not None:
            mdb.models[self.modelName].TabularAmplitude(name=amplitudeName, timeSpan=STEP,smooth=SOLVER_DEFAULT, data=data)
        EQStepName= 'step-EQ'
        mdb.models[self.modelName].ImplicitDynamicsStep(name=EQStepName,
                                                     previous='Initial',timePeriod=data[-1][0], maxNumInc=int(100000*data[-1][0]),
                                                     initialInc=data[1][0],
                                                     minInc=1e-05)
        print '地震分析步设置完成'
        #该句为地震分析步的几何非线性开关
        print '设置地震分析步的几何非线性'
        mdb.models[self.modelName].steps[EQStepName].setValues(nlgeom=ON)
        print '地震分析步的几何非线性设置完成'
        #添加重力荷载
        print '添加重力荷载'
        mdb.models[self.modelName].Gravity(name='load-gravity', createStepName=EQStepName,
                                        comp2=-9807.0, distributionType=UNIFORM, field='')
        print '重力荷载添加完成'
        #添加底部xy方向位移约束
        print '设置结构底部约束'
        region = assembly.sets['set-bottomcol-bottomsurf']
        mdb.models[self.modelName].DisplacementBC(name='FS', createStepName=EQStepName,
                                               region=region, u1=0.0, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
                                               amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                               localCsys=None)
        #添加底部z方向加速度，加速度在时程分析步中以下面输入的初值v3乘以幅值来进行计算，切记abaqus当前单位为mm，而地震步中加速度按m/s2输入的，因此v3需记得变换
        region = assembly.sets['set-bottomcol-bottomsurf']
        mdb.models[self.modelName].VelocityBC(name='MS', createStepName=EQStepName,
                                           region=region, v1=UNSET, v2=UNSET, v3=100000.0, vr1=UNSET, vr2=UNSET,
                                           vr3=UNSET, amplitude=amplitudeName, localCsys=None,
                                           distributionType=UNIFORM, fieldName='')
        print '结构底部约束设置完成'


        #撒种子
        print '开始实例网格划分'
        assembly.seedPartInstance(regions=concreteInstance, size=75.0, deviationFactor=0.1,
                            minSizeFactor=0.1)
        assembly.generateMesh(regions=concreteInstance)

        assembly.seedPartInstance(regions=rebarInstance, size=200.0, deviationFactor=0.1,
                                  minSizeFactor=0.1)
        assembly.generateMesh(regions=rebarInstance)
        print '实例网格划分完成'

        #历程输出请求
        GV = tuple(['GV'])  # 广义速度
        GA = tuple(['GA'])  # 广义加速度
        IRA = 'IRA1', 'IRA2', 'IRA3', 'IRAR1', 'IRAR2', 'IRAR3'#惯性释放等同于刚体加速度,
        IRF = 'IRF1', 'IRF2', 'IRF3', 'IRM1', 'IRM2', 'IRM3'#作用力反作用力-惯性释放荷载相应于同等的刚体加速度
        ALLEN = 'ALLAE', 'ALLCD', 'ALLDMD','ALLEE', 'ALLFD', 'ALLIE', 'ALLJD', \
                'ALLKE', 'ALLKL', 'ALLPD', 'ALLQB','ALLSE', 'ALLSD', 'ALLVD', 'ALLWK', 'ETOTAL'#总能量
        BROKEN = 'DBS11', 'DBS12', 'DBT', 'DBSF', 'OPENBC', 'CRSTS11', \
                 'CRSTS12', 'CRSTS13', 'ENRRT11', 'ENRRT12', 'ENRRT13', \
                 'EFENRRTR', 'BDSTAT', 'CSDMG',  'CSMAXSCRT', 'CSMAXUCRT',\
                 'CSQUADSCRT', 'CSQUADUCRT'#破坏断裂
        variables = GV+GA+ALLEN+BROKEN
        mdb.models[self.modelName].historyOutputRequests['H-Output-1'].setValues(variables=variables)
        #创建任务
        print '创建任务'
        jobName = 'Job-1'
        mdb.Job(name=jobName, model=self.modelName, description='', type=ANALYSIS,
                atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
                memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
                explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
                modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
                scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1,
                numGPUs=0)
        #任务数据检查
        print '任务数据检查'
        mdb.jobs[jobName].submit(consistencyChecking=OFF, datacheckJob=True)
        print '任务数据检查中...'


        session.viewports['Viewport: 1'].setValues(displayedObject=mdb.models[self.modelName].rootAssembly)
        session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])








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
        # session.viewports['Viewport: 1'].setValues(displayedObject=p)
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
        # session.viewports['Viewport: 1'].setValues(displayedObject=p)
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
            return None
        floor = int(colName[colName.find('-')+1:colName.find('-',colName.find('-')+1)])
        xcount = int(colName[colName.find('-', colName.find('-') + 1) + 1:colName.find('-', colName.find('-', colName.find('-') + 1) + 1)])
        zcount = int(colName[colName.rfind('-')+1:])
        a = mdb.models[self.modelName].rootAssembly
        result = None
        colSize = self.partSize[self.colsPart[colName]]
        colTopCenterAxis = [self.colsPos[colName][0]+colSize[0]/2 , self.colsPos[colName][1]+colSize[2],self.colsPos[colName][2]+colSize[1]/2]
        surfPoints = []

        v11 = a.instances[colName].vertices
        c1 = a.instances[colName].cells
        pickedCells = c1.getSequenceFromMask(mask=('[#1 ]',), )

        a.PartitionCellByPlaneThreePoints(point1=v11[3], point2=v11[5], point3=v11[4],
                                          cells=pickedCells)

        c1 = a.instances[colName].cells
        pickedCells = c1.getSequenceFromMask(mask=('[#1 ]',), )
        v11 = a.instances[colName].vertices
        a.PartitionCellByPlaneThreePoints(point1=v11[6], point2=v11[5], point3=v11[7],
                                          cells=pickedCells)

        c1 = a.instances[colName].cells
        pickedCells = c1.getSequenceFromMask(mask=('[#4 ]',), )
        v11 = a.instances[colName].vertices
        a.PartitionCellByPlaneThreePoints(point1=v11[2], point2=v11[8], point3=v11[9],
                                          cells=pickedCells)
        # if(self.colsBeamState[colName] == [1,1,1,1]):
        if self.colsBeamState[colName][0] == 1:
            upSize = self.partSize[self.zBeamsPart['zbeam-%d-%d-%d' % (floor, xcount, zcount - 1)]][:2]
            upName = 'zbeam-%d-%d-%d' % (floor, xcount, zcount - 1)
            # 柱子上侧横向剖切
            c1 = a.instances[colName].cells
            # pickedCells = c1.getSequenceFromMask(mask=('[#8 ]',), )
            pickedCells = c1.findAt(
                ((colTopCenterAxis[0], colTopCenterAxis[1] - 5, colTopCenterAxis[2] - 5),), )
            f1 = a.instances[upName].faces
            a.PartitionCellByExtendFace(extendFace=f1[3], cells=pickedCells)

            if self.zBeamsPos[upName][0] > self.colsPos[colName][0]:
                c1 = a.instances[colName].cells
                pickedCells = c1.findAt(
                    ((colTopCenterAxis[0], colTopCenterAxis[1] - 5, colTopCenterAxis[2] - 5),), )
                f1 = a.instances[upName].faces
                a.PartitionCellByExtendFace(extendFace=f1[0], cells=pickedCells)
                # v1 = a.instances[upName].vertices
                # e1 = a.instances[upName].edges
                # a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[4], cells=pickedCells)

            if self.zBeamsPos[upName][0] + upSize[0] < self.colsPos[colName][0] + colSize[0]:
                c1 = a.instances[colName].cells
                pickedCells = c1.findAt(
                    ((colTopCenterAxis[0], colTopCenterAxis[1] - 5, colTopCenterAxis[2] - 5),), )
                f1 = a.instances[upName].faces
                a.PartitionCellByExtendFace(extendFace=f1[2], cells=pickedCells)
                # v1 = a.instances[upName].vertices
                # e1 = a.instances[upName].edges
                # a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[4], cells=pickedCells)
            surfPoints.append([self.colsPos[colName][0] + colSize[0] / 2, self.colsPos[colName][1] + colSize[2] - 5,
                               self.colsPos[colName][2]])
        if self.colsBeamState[colName][1] == 1:
            downSize = self.partSize[self.zBeamsPart['zbeam-%d-%d-%d' % (floor, xcount, zcount)]][:2]
            downName = 'zbeam-%d-%d-%d' % (floor, xcount, zcount)
            # 柱子下侧横向剖切
            c1 = a.instances[colName].cells
            # pickedCells = c1.getSequenceFromMask(mask=('[#10 ]',), )
            pickedCells = c1.findAt(
                ((colTopCenterAxis[0], colTopCenterAxis[1] - 5, colTopCenterAxis[2] + 5),), )
            f1 = a.instances[downName].faces
            a.PartitionCellByExtendFace(extendFace=f1[3], cells=pickedCells)
            # 柱子下侧竖向左部剖切
            if self.zBeamsPos[downName][0] > self.colsPos[colName][0]:
                c1 = a.instances[colName].cells
                pickedCells = c1.findAt(
                    ((colTopCenterAxis[0], colTopCenterAxis[1] - 5, colTopCenterAxis[2] + 5),), )
                f1 = a.instances[downName].faces
                a.PartitionCellByExtendFace(extendFace=f1[0], cells=pickedCells)
                # v1 = a.instances[downName].vertices
                # e1 = a.instances[downName].edges
                # a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[6], cells=pickedCells)
            # 柱子下侧竖向右部剖切
            if self.zBeamsPos[downName][0] + downSize[0] < self.colsPos[colName][0] + colSize[0]:
                c1 = a.instances[colName].cells
                pickedCells = c1.findAt(
                    ((colTopCenterAxis[0], colTopCenterAxis[1] - 5, colTopCenterAxis[2] + 5),), )
                f1 = a.instances[downName].faces
                a.PartitionCellByExtendFace(extendFace=f1[2], cells=pickedCells)
                # v1 = a.instances[downName].vertices
                # e1 = a.instances[downName].edges
                # a.PartitionCellByPlanePointNormal(point=v1[2], normal=e1[6], cells=pickedCells)
            surfPoints.append([self.colsPos[colName][0] + colSize[0] / 2, self.colsPos[colName][1] + colSize[2] - 5,
                               self.colsPos[colName][2] + colSize[1]])
        if self.colsBeamState[colName][2] == 1:
            leftSize = self.partSize[self.xBeamsPart['xbeam-%d-%d-%d' % (floor, xcount-1, zcount)]][:2]
            leftName = 'xbeam-%d-%d-%d' % (floor, xcount - 1, zcount)
            # 柱子左侧横向剖切
            c1 = a.instances[colName].cells
            # pickedCells = c1.getSequenceFromMask(mask=('[#2 ]',), )
            pickedCells = c1.findAt(((colTopCenterAxis[0] - 5, colTopCenterAxis[1] - 5, colTopCenterAxis[2]),), )
            f1 = a.instances[leftName].faces
            a.PartitionCellByExtendFace(extendFace=f1[3], cells=pickedCells)

            # 柱子左侧竖向上部剖切
            if self.xBeamsPos[leftName][2] > self.colsPos[colName][2]:
                c1 = a.instances[colName].cells
                # pickedCells = c1.getSequenceFromMask(mask=('[#20 ]',), )
                pickedCells = c1.findAt(((colTopCenterAxis[0] - 5, colTopCenterAxis[1] - 5, colTopCenterAxis[2]),), )
                f1 = a.instances[leftName].faces
                a.PartitionCellByExtendFace(extendFace=f1[0], cells=pickedCells)
                # v1 = a.instances[leftName].vertices
                # e1 = a.instances[leftName].edges
                # a.PartitionCellByPlanePointNormal(point=v1[2], normal=e1[6], cells=pickedCells)
            # 柱子左侧竖向下部剖切
            if self.xBeamsPos[leftName][2] + leftSize[0] < self.colsPos[colName][2] + colSize[1]:
                c1 = a.instances[colName].cells
                pickedCells = c1.findAt(
                    ((colTopCenterAxis[0] - 5, colTopCenterAxis[1] - 5, colTopCenterAxis[2]),), )
                f1 = a.instances[leftName].faces
                a.PartitionCellByExtendFace(extendFace=f1[2], cells=pickedCells)

            surfPoints.append([self.colsPos[colName][0], self.colsPos[colName][1] + colSize[2] - 5,
                               self.colsPos[colName][2] + colSize[1] / 2])
        if self.colsBeamState[colName][3] == 1:
            rightSize = self.partSize[self.xBeamsPart['xbeam-%d-%d-%d' % (floor, xcount, zcount)]][:2]
            rightName = 'xbeam-%d-%d-%d' % (floor, xcount, zcount)
            # 柱子右侧横向剖切
            c1 = a.instances[colName].cells
            # pickedCells = c1.getSequenceFromMask(mask=('[#10 ]',), )
            pickedCells = c1.findAt(
                ((colTopCenterAxis[0] + 5, colTopCenterAxis[1] - 5, colTopCenterAxis[2]),), )
            f1 = a.instances[rightName].faces
            a.PartitionCellByExtendFace(extendFace=f1[3], cells=pickedCells)
            # 柱子左侧竖向上部剖切
            if self.xBeamsPos[rightName][2] > self.colsPos[colName][2]:
                c1 = a.instances[colName].cells
                pickedCells = c1.findAt(
                    ((colTopCenterAxis[0] + 5, colTopCenterAxis[1] - 5, colTopCenterAxis[2]),), )
                f1 = a.instances[rightName].faces
                a.PartitionCellByExtendFace(extendFace=f1[0], cells=pickedCells)
                # v1 = a.instances[rightName].vertices
                # e1 = a.instances[rightName].edges
                # a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[4], cells=pickedCells)
            # 柱子左侧竖向下部剖切
            if self.xBeamsPos[rightName][2] + rightSize[0] < self.colsPos[colName][2] + colSize[1]:
                c1 = a.instances[colName].cells
                pickedCells = c1.findAt(
                    ((colTopCenterAxis[0] + 5, colTopCenterAxis[1] - 5, colTopCenterAxis[2]),), )
                f1 = a.instances[rightName].faces
                a.PartitionCellByExtendFace(extendFace=f1[2], cells=pickedCells)
                # v1 = a.instances[rightName].vertices
                # e1 = a.instances[rightName].edges
                # a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[4], cells=pickedCells)
            surfPoints.append([self.colsPos[colName][0] + colSize[0], self.colsPos[colName][1] + colSize[2] - 5,
                               self.colsPos[colName][2] + colSize[1] / 2])

        cmd = 'result = a.instances[colName].faces.findAt('
        for i in range(len(surfPoints)):
            cmd += "((surfPoints[%d]),)," % i
        # result = a.instances[colName].faces.findAt(((surfPoints[0]),),((surfPoints[1]),),((surfPoints[2]),),((surfPoints[3]),),)  # 1
        cmd += ')'
        exec (cmd)

        return result
    def getBeamSurfToCol(self,BeamName,ends = [1,1]):
        result = None
        surfPoints = []
        a = mdb.models[self.modelName].rootAssembly
        if BeamName[:5] == 'xbeam':
            if ends[0] == 1:
                surfPoints.append([self.xBeamsPos[BeamName][0], self.xBeamsPos[BeamName][1]-5,self.xBeamsPos[BeamName][2]+self.partSize[self.xBeamsPart[BeamName]][0]/2])
            if ends[1] == 1:
                surfPoints.append([self.xBeamsPos[BeamName][0]+self.partSize[self.xBeamsPart[BeamName]][2], self.xBeamsPos[BeamName][1] - 5,
                                   self.xBeamsPos[BeamName][2] + self.partSize[self.xBeamsPart[BeamName]][0] / 2])
        if BeamName[:5] == 'zbeam':
            if ends[0] == 1:
                surfPoints.append([self.zBeamsPos[BeamName][0] + self.partSize[self.zBeamsPart[BeamName]][0] / 2, self.zBeamsPos[BeamName][1]-5,self.zBeamsPos[BeamName][2]])
            if ends[1] == 1:
                surfPoints.append([self.zBeamsPos[BeamName][0] + self.partSize[self.zBeamsPart[BeamName]][0] / 2, self.zBeamsPos[BeamName][1]-5,
                                   self.zBeamsPos[BeamName][2] + self.partSize[self.zBeamsPart[BeamName]][2]])

        cmd = 'result = a.instances[BeamName].faces.findAt('
        for i in range(len(surfPoints)):
            cmd += "((surfPoints[%d]),)," % i
        # result = a.instances[colName].faces.findAt(((surfPoints[0]),),((surfPoints[1]),),((surfPoints[2]),),((surfPoints[3]),),)  # 1
        cmd += ')'
        exec (cmd)

        return result

    def getColTopSurf(self,colName):
        result = None
        surfPoints = []
        a = mdb.models[self.modelName].rootAssembly
        if self.colsColState[colName][0] == 1:
            surfPoints.append([self.colsPos[colName][0]+self.partSize[self.colsPart[colName]][0] / 2,
                               self.colsPos[colName][1]+self.partSize[self.colsPart[colName]][2],
                               self.colsPos[colName][2] + self.partSize[self.colsPart[colName]][1] / 2])

            result = a.instances[colName].faces.findAt(((surfPoints[0]),),)

        return result

    def getColBottomSurf(self, colName):
        result = None
        surfPoints = []
        a = mdb.models[self.modelName].rootAssembly
        if self.colsColState[colName][1] == 1:
            surfPoints.append([self.colsPos[colName][0] + self.partSize[self.colsPart[colName]][0] / 2,
                               self.colsPos[colName][1],
                               self.colsPos[colName][2] + self.partSize[self.colsPart[colName]][1] / 2])

            result = a.instances[colName].faces.findAt(((surfPoints[0]),), )

        return result




mymodel = AbaqusStructureClass()
mymodel.startBuilding()