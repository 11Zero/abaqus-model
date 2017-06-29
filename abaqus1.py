#! /user/bin/python
# coding:utf-8

# """
# modelAExample.py
# A simple example: Creating a part.
# """
# from abaqus import *
# from abaqusConstants import *
# backwardCompatibility.setValues(includeDeprecated=True,reportDeprecated=False)
# import sketch
# import part
# myModel = mdb.Model(name='Model A')
# mySketch = myModel.ConstrainedSketch(name='Sketch A',sheetSize=200.0)
# xyCoordsInner = ((-5 , 20), (5, 20), (15, 0),(-15, 0), (-5, 20))
# xyCoordsOuter = ((-10, 30), (10, 30),
#                  (40, -30),(30, -30),
#                  (20, -10), (-20, -10),
#                  (-30, -30), (-40, -30), (-10, 30))
# for i in range(len(xyCoordsInner)-1):
#     mySketch.Line(point1=xyCoordsInner[i],point2=xyCoordsInner[i+1])
# for i in range(len(xyCoordsOuter)-1):
#     mySketch.Line(point1=xyCoordsOuter[i],point2=xyCoordsOuter[i+1])
# myPart = myModel.Part(name='Part A', dimensionality=THREE_D,type=DEFORMABLE_BODY)
# myPart.BaseSolidExtrude(sketch=mySketch, depth=20.0)
# myViewport = session.Viewport(name='Viewport for Model A',
#                               origin=(10, 10), width=150, height=100)
# myViewport.setValues(displayedObject=myPart)
# myViewport.partDisplay.setValues(renderStyle=SHADED)
#
#




from abaqus import *
import testUtils

testUtils.setBackwardCompatibility()
from abaqusConstants import *

myModel = mdb.Model(name='Beam')

print '创建新视窗来显示模型和分析结果'
myViewport = session.Viewport(name='Cantilever Beam Example',
                              origin=(20, 20), width=150, height=120)
myViewport.makeCurrent()
myViewport.maximize()
print '导入part模块'
import part

print '创建基础特征的草图'
mySketch = myModel.ConstrainedSketch(name='beamProfile', sheetSize=250.)

print '绘制矩形截面'
mySketch.rectangle(point1=(-100, 10), point2=(100, -10))

print '创建三维变形体部件'
myBeam = myModel.Part(name='Beam', dimensionality=THREE_D, type=DEFORMABLE_BODY)

print '通过对草图拉伸25.0来创建部件'
myBeam.BaseSolidExtrude(sketch=mySketch, depth=25.0)

print '导入material模块'
import material

print '创建材料'
mySteel = myModel.Material(name='Steel')

print '定义弹性材料属性，杨氏模量209.E3，泊松比0.3'
elasticProperties = (209.E3, 0.3)
mySteel.Elastic(table=(elasticProperties,))

print '导入section模块'
import section

print '创建实体截面'
mySection = myModel.HomogeneousSolidSection(name='beamSection',
                                            material='Steel', thickness=1.0)

print '为部件分配截面属性'
region = (myBeam.cells,)
myBeam.SectionAssignment(region=region, sectionName='beamSection')

print '导入assembly模块'
import assembly

print '创建部件实例'
myAssembly = myModel.rootAssembly
myInstance = myAssembly.Instance(name='beamInstance', part=myBeam, dependent=OFF)

print '导入step模块'
import step

print '在初始分析步initial之后创建一个分析步，静力分析步的时间为1.0，初始增量为0.1'
myModel.StaticStep(name='beamLoad', previous='Initial', timePeriod=1.0,
                   initialInc=0.1, description='Load the top of the beam.')

print '导入Load模块'
import load

print '通过坐标找出端部所在面'
endFaceCenter = (-100, 0, 12.5)
endFace = myInstance.faces.findAt((endFaceCenter,))

print '在梁端部创建固定端约束'
endRegion = (endFace,)
myModel.EncastreBC(name='Fixed', createStepName='beamLoad', region=endRegion)

print '通过坐标找到上面'
topFaceCenter = (0, 10, 12.5)
topFace = myInstance.faces.findAt((topFaceCenter,))

print '在梁的上表面施加压力荷载'
topSurface = ((topFace, SIDE1),)
myModel.Pressure(name='Pressure', createStepName='beamLoad',
                 region=topSurface, magnitude=0.5)

print '导入mesh模块'
import mesh

print '为部件实例指定单元类型'
region = (myInstance.cells,)
elemType = mesh.ElemType(elemCode=C3D8I, elemLibrary=STANDARD)
myAssembly.setElementType(regions=region, elemTypes=(elemType, 0))

print '为部件实例撒种子'
myAssembly.seedPartInstance(regions=(myInstance,), size=10.0)

print '为部件实例划分网格'
myAssembly.generateMesh(regions=(myInstance,))

print '显示划分网格后的梁模型'
myViewport.assemblyDisplay.setValues(mesh=ON)
myViewport.assemblyDisplay.meshOptions.setValues(meshTechnique=ON)
myViewport.setValues(displayedObject=myAssembly)

print '导入job模块'
import job

print '为模型创建并提交分析作业'
jobName = 'beam_tutorial'
myJob = mdb.Job(name=jobName, model='Beam',
                description='Cantilever beam tutorial')

print '等待分析作业完成'
myJob.submit()
myJob.waitForCompletion()
print '分析完成，进入后处理'

print '导入visualization模块'
import visualization

print '打开输出数据库，显示默认云图'
myOdb = visualization.openOdb(path=jobName + '.odb')
myViewport.setValues(displayedObject=myOdb)
myViewport.odbDisplay.display.setValues(plotState=CONTOURS_ON_DEF)
myViewport.odbDisplay.commonOptions.setValues(renderStyle=FILLED)

print '将Mises云图输出为png文件'
session.printToFile(fileName='Mises', format=PNG, canvasObjects=(myViewport,))
print '文件Mises.png保存于工作目录，请查看'
