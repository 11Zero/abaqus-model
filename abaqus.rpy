# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-1 replay file
# Internal Version: 2014_06_05-06.11.02 134264
# Run by Administrator on Fri Jul 21 12:01:24 2017
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=348.020294189453, 
    height=245.886108398438)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('abaqus_structure.py', __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-120127.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: materials created
p = mdb.models['structure'].parts['rebar-5']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37422.9, 
    farPlane=60310.1, width=4768.19, height=3147.84, viewOffsetX=-3995.28, 
    viewOffsetY=1179.69)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37457.2, 
    farPlane=60275.8, width=4772.56, height=3150.72, viewOffsetX=-5016.13, 
    viewOffsetY=1006.02)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-4949.35, 
    viewOffsetY=795.287)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36710.6, 
    farPlane=61022.4, width=11881.3, height=7843.71, viewOffsetX=-3573.02, 
    viewOffsetY=-136.749)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36633.4, 
    farPlane=61099.6, width=11856.3, height=7827.22, viewOffsetX=-2467.93, 
    viewOffsetY=1446.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36791.1, 
    farPlane=60941.9, width=9890.04, height=6529.15, viewOffsetX=-2944.33, 
    viewOffsetY=1510.66)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36859.8, 
    farPlane=60873.2, width=9908.51, height=6541.34, viewOffsetX=-4240.39, 
    viewOffsetY=1097.31)
a = mdb.models['structure'].rootAssembly
p = mdb.models['structure'].parts['beam-3']
a.Instance(name='beam-3-1', part=p, dependent=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36041.9, 
    farPlane=63094.4, width=21568.9, height=14239.2, cameraPosition=(33791, 
    -2249.8, 49451), cameraUpVector=(-0.176225, 0.970434, -0.164932), 
    cameraTarget=(7303.74, 2799, 8697.26))
session.viewports['Viewport: 1'].view.setValues(nearPlane=36445.9, 
    farPlane=62476.9, width=21810.7, height=14398.8, cameraPosition=(28229, 
    4641.38, 52832.8), cameraUpVector=(-0.146196, 0.930219, -0.33663), 
    cameraTarget=(7225.01, 2896.55, 8745.13))
session.viewports['Viewport: 1'].view.setValues(nearPlane=36472.3, 
    farPlane=62450.5, width=22643.4, height=14948.6, viewOffsetX=1649.68, 
    viewOffsetY=-237.503)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36334.6, 
    farPlane=62588.3, width=22557.9, height=14892.1, viewOffsetX=-1246.09, 
    viewOffsetY=1561.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35948.7, 
    farPlane=63563.8, width=22318.3, height=14734, cameraPosition=(33684.6, 
    26249.1, 43568.9), cameraUpVector=(-0.301726, 0.658289, -0.689649), 
    cameraTarget=(7440.99, 3177.36, 9409.02), viewOffsetX=-1232.85, 
    viewOffsetY=1544.56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38308.9, 
    farPlane=61203.5, width=2129.44, height=1405.8, viewOffsetX=-5426.95, 
    viewOffsetY=461.47)
a = mdb.models['structure'].rootAssembly
a.translate(instanceList=('beam-3-1', ), vector=(4550.0, 6700.0, 16350.0))
#: The instance beam-3-1 was translated by 4.55E+03, 6.7E+03, 16.35E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34541.9, 
    farPlane=62139.3, width=10946.6, height=7226.64, viewOffsetX=-3873.38, 
    viewOffsetY=631.721)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34470.7, 
    farPlane=62210.6, width=10924, height=7211.74, viewOffsetX=-3336.25, 
    viewOffsetY=6.89129)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35931.4, 
    farPlane=62453, width=11386.9, height=7517.34, cameraPosition=(23594.7, 
    32106.5, 46735.6), cameraUpVector=(-0.291832, 0.57476, -0.764517), 
    cameraTarget=(7994.03, 3787.36, 10094.4), viewOffsetX=-3477.62, 
    viewOffsetY=7.18331)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34884.8, 
    farPlane=62270.7, width=11055.2, height=7298.38, cameraPosition=(30663.1, 
    30248.7, 43252.9), cameraUpVector=(-0.433493, 0.613307, -0.660256), 
    cameraTarget=(7589.63, 3852.4, 9211.96), viewOffsetX=-3376.33, 
    viewOffsetY=6.97408)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35655.2, 
    farPlane=61500.4, width=4466.55, height=2948.7, viewOffsetX=-4454.85, 
    viewOffsetY=128.546)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36699.9, 
    farPlane=61297.3, width=4597.42, height=3035.1, cameraPosition=(26111.2, 
    35278, 42379.2), cameraUpVector=(-0.421398, 0.509015, -0.750552), 
    cameraTarget=(7872.01, 3912.84, 9645.52), viewOffsetX=-4585.38, 
    viewOffsetY=132.312)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36685.4, 
    farPlane=61311.8, width=4595.6, height=3033.9, viewOffsetX=-4529.15, 
    viewOffsetY=-278.529)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37091.5, 
    farPlane=61272.8, width=4646.48, height=3067.49, cameraPosition=(24092.8, 
    36515.3, 42555.6), cameraUpVector=(-0.402098, 0.481263, -0.778912), 
    cameraTarget=(7984.03, 3973.63, 9852.62), viewOffsetX=-4579.29, 
    viewOffsetY=-281.613)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37486.1, 
    farPlane=60878.3, width=1280.58, height=845.403, viewOffsetX=-4738.64, 
    viewOffsetY=-621.569)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-2-4'].vertices
e1 = a.instances['col-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[6], normal=e1[5], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37477.2, 
    farPlane=60887.2, width=1280.27, height=845.203, viewOffsetX=-4723.73, 
    viewOffsetY=-431.147)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37592.3, 
    farPlane=60772.1, width=273.42, height=180.505, viewOffsetX=-4741.5, 
    viewOffsetY=-259.751)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37594.3, 
    farPlane=60770.1, width=273.435, height=180.515, viewOffsetX=-4726.44, 
    viewOffsetY=-229.434)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-2-4'].vertices
e11 = a.instances['col-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[5], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37506.8, 
    farPlane=60857.6, width=1091.24, height=720.406, viewOffsetX=-4737.9, 
    viewOffsetY=-308.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37499.2, 
    farPlane=60865.2, width=1091.02, height=720.26, viewOffsetX=-4846.16, 
    viewOffsetY=-386.216)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-4994.14, 
    viewOffsetY=-484.914)
session.viewports['Viewport: 1'].view.setValues(width=1102.04, height=727.539, 
    viewOffsetX=-4994.69, viewOffsetY=-486.107)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36569.5, 
    farPlane=62198.3, width=1074.72, height=709.501, cameraPosition=(27795.8, 
    23448.4, 50383), cameraUpVector=(-0.370405, 0.735536, -0.567262), 
    cameraTarget=(7964.72, 4439.04, 9968.77), viewOffsetX=-4870.86, 
    viewOffsetY=-474.055)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35723.4, 
    farPlane=63044.3, width=8896.47, height=5873.22, viewOffsetX=-4018.51, 
    viewOffsetY=-230.087)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35664.7, 
    farPlane=63103.1, width=8881.83, height=5863.55, viewOffsetX=-3400.02, 
    viewOffsetY=1147.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36020.2, 
    farPlane=63029.7, width=8970.36, height=5922, cameraPosition=(27460.3, 
    28215.3, 48021.3), cameraUpVector=(-0.344385, 0.65696, -0.670673), 
    cameraTarget=(7967.72, 4181.8, 10201.1), viewOffsetX=-3433.91, 
    viewOffsetY=1159.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36725.1, 
    farPlane=62324.8, width=2653.29, height=1751.63, viewOffsetX=-4317.47, 
    viewOffsetY=755.319)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36744.4, 
    farPlane=62305.4, width=2654.68, height=1752.55, viewOffsetX=-4411.19, 
    viewOffsetY=735.704)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36811.8, 
    farPlane=62238, width=1951.85, height=1288.56, viewOffsetX=-4484.41, 
    viewOffsetY=697.04)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36826.1, 
    farPlane=62223.7, width=1952.61, height=1289.06, viewOffsetX=-4530.3, 
    viewOffsetY=653.15)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['beam-3-1'].vertices
e1 = a.instances['beam-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[6], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['beam-3-1'].vertices
e11 = a.instances['col-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e11[6], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v1 = a.instances['zbeam-2-2-3'].vertices
e1 = a.instances['col-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[26], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-2-3'].vertices
e11 = a.instances['col-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[6], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35285.2, 
    farPlane=63764.6, width=16124.4, height=10644.9, viewOffsetX=-3213.4, 
    viewOffsetY=1554.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35183.5, 
    farPlane=63866.4, width=16077.9, height=10614.2, viewOffsetX=-1300.41, 
    viewOffsetY=1255.68)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35183.2, 
    farPlane=63866.7, width=16077.8, height=10614.1, viewOffsetX=-1404.24, 
    viewOffsetY=822.793)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36020.3, 
    farPlane=63029.6, width=9431.68, height=6226.55, viewOffsetX=-2639.81, 
    viewOffsetY=815.876)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-121738.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x000000001079E6A8>materials created
#* TypeError:  ??????????: side1Faces
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 651, in 
#* <module>
#*     mymodel.startBuilding()
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 271, in 
#* startBuilding
#*     assembly.Surface(side1Faces=totalSurfs, name='col-beam-surf')
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=36366.5, 
    farPlane=61366.5, width=15013.7, height=9911.69, viewOffsetX=-2062.24, 
    viewOffsetY=238.561)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36270.9, 
    farPlane=61462.1, width=14974.3, height=9885.61, viewOffsetX=-1927.87, 
    viewOffsetY=1431.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36569.2, 
    farPlane=61163.8, width=13169.3, height=8694.05, viewOffsetX=-984.474, 
    viewOffsetY=3253.21)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36484.3, 
    farPlane=61248.7, width=13138.8, height=8673.86, viewOffsetX=-4022.91, 
    viewOffsetY=1491.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37749.6, 
    farPlane=59983.4, width=2124.21, height=1402.35, viewOffsetX=-5966.1, 
    viewOffsetY=1392.34)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 
    'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 
    'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6'), vector=(4550.0, 0.0, 
    6600.0))
#: The instances were translated by 4.55E+03, 0., 6.6E+03 (????????????????)




session.viewports['Viewport: 1'].view.setValues(nearPlane=34378, 
    farPlane=59804.3, width=675.678, height=446.065, viewOffsetX=-5488.85, 
    viewOffsetY=884.731)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-2-4'].vertices
e1 = a.instances['col-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[6], normal=e1[5], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34305.4, 
    farPlane=59876.9, width=1428.35, height=942.957, viewOffsetX=-5369.79, 
    viewOffsetY=958.243)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-2-4'].vertices
e11 = a.instances['xbeam-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['zbeam-2-1-3'].vertices
e1 = a.instances['zbeam-2-1-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[6], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-1-3'].vertices
e11 = a.instances['zbeam-2-1-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e11[6], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v1 = a.instances['zbeam-2-2-3'].vertices
e1 = a.instances['zbeam-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[4], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34295.5, 
    farPlane=59886.8, width=1427.93, height=942.685, viewOffsetX=-5285.25, 
    viewOffsetY=1153.27)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-2-3'].vertices
e11 = a.instances['col-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[6], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34114.3, 
    farPlane=60068, width=3175.01, height=2096.06, viewOffsetX=-4753.78, 
    viewOffsetY=1318.19)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34092.6, 
    farPlane=60089.7, width=3172.99, height=2094.73, viewOffsetX=-4935.19, 
    viewOffsetY=869.701)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34664.9, 
    farPlane=60781.2, width=3226.26, height=2129.89, cameraPosition=(31058.4, 
    32636.9, 40596.5), cameraUpVector=(-0.512585, 0.544741, -0.663712), 
    cameraTarget=(8074.33, 2881.29, 9383.18), viewOffsetX=-5018.04, 
    viewOffsetY=884.301)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=36477.7, 
    farPlane=58327.4, width=3394.97, height=2241.27, cameraPosition=(41770.3, 
    28773.4, 28331.3), cameraUpVector=(-0.628857, 0.601508, -0.492674), 
    cameraTarget=(6602.57, 2008.09, 7479.86), viewOffsetX=-5280.45, 
    viewOffsetY=930.545)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36500.2, 
    farPlane=58304.8, width=3397.07, height=2242.66, viewOffsetX=-6091.84, 
    viewOffsetY=949.413)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35383.5, 
    farPlane=52557.6, width=3293.14, height=2174.05, cameraPosition=(44853.9, 
    25787.8, 4897.42), cameraUpVector=(-0.7598, 0.607856, -0.230684), 
    cameraTarget=(2867.03, 868.631, 6915.29), viewOffsetX=-5905.47, 
    viewOffsetY=920.367)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28977.6, 
    farPlane=48702.4, width=2696.95, height=1780.46, cameraPosition=(5974.7, 
    7431.68, -31075.2), cameraUpVector=(-0.392711, 0.839088, 0.376444), 
    cameraTarget=(-1278.9, 1911.03, 16933.6), viewOffsetX=-4836.34, 
    viewOffsetY=753.743)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28722.2, 
    farPlane=49909.1, width=2673.19, height=1764.77, cameraPosition=(-12332.2, 
    5734.67, -26666.9), cameraUpVector=(-0.228263, 0.833238, 0.503597), 
    cameraTarget=(3820.8, 1929.66, 19295.5), viewOffsetX=-4793.72, 
    viewOffsetY=747.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28725.7, 
    farPlane=49905.6, width=2673.51, height=1764.99, viewOffsetX=-3882.03, 
    viewOffsetY=1233.79)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29170.4, 
    farPlane=52187.1, width=2714.91, height=1792.31, cameraPosition=(-18461.9, 
    18283.3, -20772.6), cameraUpVector=(-0.0219447, 0.644993, 0.763874), 
    cameraTarget=(5083.32, -962.679, 17478.6), viewOffsetX=-3942.12, 
    viewOffsetY=1252.89)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29165.6, 
    farPlane=52191.9, width=2714.46, height=1792.02, viewOffsetX=-2451.29, 
    viewOffsetY=1930.9)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-2264.29, 
    viewOffsetY=2500.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28775.2, 
    farPlane=52582.3, width=6449.05, height=4257.5, viewOffsetX=-1846.4, 
    viewOffsetY=2927.87)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28732.4, 
    farPlane=52625.1, width=6439.44, height=4251.15, viewOffsetX=-1538.66, 
    viewOffsetY=3630.88)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29260.2, 
    farPlane=52097.3, width=1788.29, height=1180.58, viewOffsetX=-2015.75, 
    viewOffsetY=3733.63)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-4'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1100820 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-1')
#: ???? 'Surf-1' ?????? (4 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=29197.2, 
    farPlane=52160.3, width=2597.22, height=1714.62, viewOffsetX=-1958.72, 
    viewOffsetY=3715.53)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'xbeam-2-3-4-rebar-5-6', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 
    'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 
    'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 
    'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 
    'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 
    'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 
    'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 
    'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 
    'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 
    'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 
    'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 
    'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 
    'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 
    'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 
    'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 
    'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 
    'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 
    'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 
    'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 
    'zbeam-2-4-2-rebar-4-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 
    'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 
    'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 
    'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 
    'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 
    'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 
    'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 
    'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    ))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=43698, 
    farPlane=74830.3, width=24516.1, height=16184.9, viewOffsetX=6359.93, 
    viewOffsetY=4198.03)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45651.3, 
    farPlane=72876.9, width=8982.34, height=5929.91, viewOffsetX=6691.97, 
    viewOffsetY=5041.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45591.2, 
    farPlane=72937, width=8970.53, height=5922.11, viewOffsetX=6277.61, 
    viewOffsetY=5199.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45900.3, 
    farPlane=72627.9, width=6709.82, height=4429.65, viewOffsetX=5578.53, 
    viewOffsetY=6381.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45854.9, 
    farPlane=72673.3, width=6703.19, height=4425.27, viewOffsetX=7665.51, 
    viewOffsetY=6079.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46260.4, 
    farPlane=72267.8, width=3025.29, height=1997.22, viewOffsetX=7600.18, 
    viewOffsetY=5981.66)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46282.5, 
    farPlane=72245.7, width=3026.74, height=1998.18, viewOffsetX=6463.49, 
    viewOffsetY=5710.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46210.3, 
    farPlane=72317.9, width=3684.42, height=2432.36, viewOffsetX=6605.63, 
    viewOffsetY=5751.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46206.1, 
    farPlane=72322.1, width=3684.08, height=2432.14, viewOffsetX=5304.3, 
    viewOffsetY=6298.38)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=3690.28, 
    viewOffsetY=5655.62)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=2310.24, 
    viewOffsetY=5302.5)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=5609.66, 
    viewOffsetY=5643.71)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=8238.88, 
    viewOffsetY=6111.89)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 
    'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 
    'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6'), vector=(4500.0, 0.0, 
    -6600.0))
#: The instances were translated by 4.5E+03, 0., -6.6E+03 (????????????????)



session.viewports['Viewport: 1'].view.setValues(nearPlane=46509.5, 
    farPlane=75569.5, width=1011.25, height=667.599, viewOffsetX=7660.51, 
    viewOffsetY=5570.07)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-3-1'].vertices
e1 = a.instances['xbeam-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[6], normal=e1[7], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46416.6, 
    farPlane=75662.3, width=1993.34, height=1315.95, viewOffsetX=7880.87, 
    viewOffsetY=5746.42)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['xbeam-2-3-1'].vertices
e11 = a.instances['col-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[4], normal=e11[18], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v1 = a.instances['zbeam-2-3-1'].vertices
e1 = a.instances['col-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[5], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-3-1'].vertices
e11 = a.instances['col-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e11[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v1 = a.instances['zbeam-2-2-1'].vertices
e1 = a.instances['col-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[33], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-2-1'].vertices
e11 = a.instances['col-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[38], 
    cells=pickedCells)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=56945.5, 
    farPlane=74068.8, width=2445.51, height=1614.46, cameraPosition=(57801.7, 
    44873.1, 16893), cameraUpVector=(-0.912909, 0.40518, 0.0492623), 
    cameraTarget=(16967.4, 2410.47, 10433.8), viewOffsetX=9668.53, 
    viewOffsetY=7049.91)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59456.1, 
    farPlane=78039.6, width=2553.33, height=1685.64, cameraPosition=(55525.4, 
    50281.2, -8876.42), cameraUpVector=(-0.878965, 0.352581, 0.321103), 
    cameraTarget=(20409.8, 4998.72, 6243.86), viewOffsetX=10094.8, 
    viewOffsetY=7360.72)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59443.4, 
    farPlane=78052.2, width=2552.78, height=1685.28, viewOffsetX=9603.52, 
    viewOffsetY=7359.15)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61139.2, 
    farPlane=82207.7, width=2625.61, height=1733.36, cameraPosition=(46718.9, 
    46452.9, -34974.9), cameraUpVector=(-0.687832, 0.428751, 0.585713), 
    cameraTarget=(21382.4, 5193.99, -799), viewOffsetX=9877.49, 
    viewOffsetY=7569.09)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61130.8, 
    farPlane=82216.1, width=2625.25, height=1733.12, viewOffsetX=8969.02, 
    viewOffsetY=7686.79)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=8141.03, 
    viewOffsetY=7924.28)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62951, 
    farPlane=83523.4, width=2703.42, height=1784.73, cameraPosition=(32745.2, 
    41455.4, -50346.4), cameraUpVector=(-0.524585, 0.494676, 0.692897), 
    cameraTarget=(19405.5, 4776.17, -5749.22), viewOffsetX=8383.44, 
    viewOffsetY=8160.24)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62941.9, 
    farPlane=83532.4, width=2703.03, height=1784.47, viewOffsetX=7404.6, 
    viewOffsetY=8310.44)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=7107.82, 
    viewOffsetY=9119.72)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=6700.47, 
    viewOffsetY=10176.4)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=6165.1, 
    viewOffsetY=10843)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=5850.86, 
    viewOffsetY=11367)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61474, 
    farPlane=85000.4, width=16275.4, height=10744.6, viewOffsetX=6324.11, 
    viewOffsetY=12858.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61366.7, 
    farPlane=85107.7, width=16247, height=10725.9, viewOffsetX=6557.92, 
    viewOffsetY=9476.17)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62595.5, 
    farPlane=86933.6, width=16572.4, height=10940.7, cameraPosition=(-28432.7, 
    47293.1, -43402.9), cameraUpVector=(0.367572, 0.41284, 0.833339), 
    cameraTarget=(1354.27, 6377.79, -12566.4), viewOffsetX=6689.24, 
    viewOffsetY=9665.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62558.8, 
    farPlane=86970.2, width=16562.7, height=10934.3, viewOffsetX=-143.019, 
    viewOffsetY=9927.81)
session.viewports['Viewport: 1'].view.setValues(nearPlane=64191.1, 
    farPlane=85338, width=2377.62, height=1569.64, viewOffsetX=-21.5059, 
    viewOffsetY=9925.3)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#9101000 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-2')
#: ???? 'Surf-2' ?????? (4 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=61610.1, 
    farPlane=87919, width=26226.7, height=17314.2, viewOffsetX=7982.55, 
    viewOffsetY=10209.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61443.4, 
    farPlane=88085.6, width=26155.8, height=17267.4, viewOffsetX=10297.8, 
    viewOffsetY=10576.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60702, 
    farPlane=85819.7, width=25840.2, height=17059.1, cameraPosition=(-12825.5, 
    50551.1, -46788.3), cameraUpVector=(0.388771, 0.352941, 0.851052), 
    cameraTarget=(4260.65, 5259.4, -12598.5), viewOffsetX=10173.6, 
    viewOffsetY=10449)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60736.9, 
    farPlane=85784.8, width=25855.2, height=17068.9, viewOffsetX=7952.96, 
    viewOffsetY=13044.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62519.2, 
    farPlane=84002.5, width=11191.8, height=7388.52, viewOffsetX=5147.89, 
    viewOffsetY=13778.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62444.1, 
    farPlane=84077.6, width=11178.3, height=7379.64, viewOffsetX=4864.95, 
    viewOffsetY=13521.3)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'xbeam-2-3-4-rebar-5-6', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 
    'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 
    'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 
    'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 
    'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 
    'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 
    'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 
    'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 
    'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 
    'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 
    'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 
    'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 
    'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 
    'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 
    'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 
    'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 
    'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 
    'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 
    'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 
    'zbeam-2-4-2-rebar-4-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 
    'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 
    'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 
    'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 
    'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 
    'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 
    'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 
    'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=60393.5, 
    farPlane=85516.2, width=10811.2, height=7137.3, cameraPosition=(-51082.7, 
    40908.1, -20020), cameraUpVector=(0.836274, 0.484018, 0.257629), 
    cameraTarget=(-9972.71, 1703.89, -3131.78), viewOffsetX=4705.19, 
    viewOffsetY=13077.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58848.4, 
    farPlane=87410.8, width=10534.6, height=6954.7, cameraPosition=(-28711.1, 
    48413.9, -39826.1), cameraUpVector=(0.73024, 0.360287, 0.580468), 
    cameraTarget=(-4062.26, 4029.36, -9253.94), viewOffsetX=4584.81, 
    viewOffsetY=12742.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59614.8, 
    farPlane=86644.4, width=3965.38, height=2617.84, viewOffsetX=3626.32, 
    viewOffsetY=13397.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59643.7, 
    farPlane=86615.4, width=3967.31, height=2619.11, viewOffsetX=3632.35, 
    viewOffsetY=13904)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=3679.33, 
    viewOffsetY=14126.2)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=3760.47, 
    viewOffsetY=13844.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58950.1, 
    farPlane=87309.1, width=10552.9, height=6966.73, viewOffsetX=4737.77, 
    viewOffsetY=13632.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58879.3, 
    farPlane=87379.9, width=10540.2, height=6958.36, viewOffsetX=4981.69, 
    viewOffsetY=14081.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58879.3, 
    width=10540.2, height=6958.36, viewOffsetX=7568.51, viewOffsetY=15534.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58879.3, 
    width=10540.2, height=6958.36, viewOffsetX=11426.1, viewOffsetY=15148.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58879.3, 
    width=10540.2, height=6958.36, viewOffsetX=12152.2, viewOffsetY=13355.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58879.3, 
    width=10540.2, height=6958.36, viewOffsetX=13377.5, viewOffsetY=13343.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59820.7, 
    farPlane=86438.5, width=2601.51, height=1717.45, viewOffsetX=13676, 
    viewOffsetY=13452.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59802.7, 
    farPlane=86456.4, width=2600.72, height=1716.93, viewOffsetX=13764.3, 
    viewOffsetY=13198.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51730, 
    farPlane=81517, width=2249.65, height=1485.16, cameraPosition=(32238.1, 
    36745.3, -45801.8), cameraUpVector=(-0.0805146, 0.532956, 0.842304), 
    cameraTarget=(20263.1, 436.449, -519.636), viewOffsetX=11906.3, 
    viewOffsetY=11417.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51770.6, 
    farPlane=81476.3, width=2251.41, height=1486.33, viewOffsetX=12620.9, 
    viewOffsetY=11401.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50782.1, 
    farPlane=81365.2, width=2208.43, height=1457.95, cameraPosition=(38855.8, 
    34168.2, -43121.4), cameraUpVector=(-0.149174, 0.559437, 0.815339), 
    cameraTarget=(21111.3, -432.343, 1601.52), viewOffsetX=12379.9, 
    viewOffsetY=11184.2)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-1-4'].vertices
e1 = a.instances['xbeam-2-1-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[0], normal=e1[0], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50787.1, 
    farPlane=81360.2, width=2208.65, height=1458.09, viewOffsetX=11729.7, 
    viewOffsetY=11047.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50210.1, 
    farPlane=81937.2, width=7619.51, height=5030.2, viewOffsetX=11411.5, 
    viewOffsetY=11147.7)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6'), vector=(2025.0, 0.0, 
    0.0))
#: The instances were translated by 2.025E+03, 0., 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48562.6, 
    farPlane=83584.8, width=22629.9, height=14939.6, viewOffsetX=9666.43, 
    viewOffsetY=11776.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48420.1, 
    farPlane=83727.3, width=22563.4, height=14895.8, viewOffsetX=11726.8, 
    viewOffsetY=9385.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56504, 
    farPlane=85377.3, width=26330.5, height=17382.7, cameraPosition=(-43549.1, 
    40199.6, -29569.9), cameraUpVector=(0.690164, 0.538484, 0.483434), 
    cameraTarget=(-77.2739, 4471.25, -10971.7), viewOffsetX=13684.6, 
    viewOffsetY=10951.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56560.8, 
    farPlane=93377.3, width=26357, height=17400.2, cameraPosition=(-58481.7, 
    21188.4, 45273.8), cameraUpVector=(0.703205, 0.708738, -0.0565061), 
    cameraTarget=(-17265.5, 5025.79, 5875.7), viewOffsetX=13698.4, 
    viewOffsetY=10962.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58783.6, 
    farPlane=91154.6, width=6600.52, height=4357.49, viewOffsetX=14750.8, 
    viewOffsetY=11404.9)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-1-4'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#6a ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-3')
#: ???? 'Surf-3' ?????? (4 ??).
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-124417.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35625, 
    farPlane=62108.1, width=21670.4, height=14306.2, viewOffsetX=1500.62, 
    viewOffsetY=-372.238)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35501.2, 
    farPlane=62231.8, width=21595.1, height=14256.5, viewOffsetX=3424.79, 
    viewOffsetY=1815.21)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36700.5, 
    farPlane=61032.5, width=10624.8, height=7014.19, viewOffsetX=3171.67, 
    viewOffsetY=3571.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36774, 
    farPlane=60959, width=10646, height=7028.23, viewOffsetX=3120.72, 
    viewOffsetY=4186.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37336, 
    farPlane=60397.1, width=5472.43, height=3612.76, viewOffsetX=3090.86, 
    viewOffsetY=4816.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37375.1, 
    farPlane=60357.9, width=5478.17, height=3616.55, viewOffsetX=3076.42, 
    viewOffsetY=4261.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36764.3, 
    farPlane=60968.7, width=11368.9, height=7505.47, viewOffsetX=3080.86, 
    viewOffsetY=3587.88)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36692.7, 
    farPlane=61040.4, width=11346.8, height=7490.84, viewOffsetX=4577.17, 
    viewOffsetY=1100.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36692.6, 
    farPlane=61040.5, width=11346.8, height=7490.84, viewOffsetX=6506.96, 
    viewOffsetY=2884.34)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37093.3, 
    farPlane=60639.7, width=7438.5, height=4910.71, viewOffsetX=5964.65, 
    viewOffsetY=3283.57)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37145.9, 
    farPlane=60587.1, width=7449.04, height=4917.67, viewOffsetX=5973.1, 
    viewOffsetY=3560.98)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36907.8, 
    farPlane=60825.2, width=10084.8, height=6657.75, viewOffsetX=6532.94, 
    viewOffsetY=3462.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36841.5, 
    farPlane=60891.5, width=10066.7, height=6645.79, viewOffsetX=5936.06, 
    viewOffsetY=3066.11)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36861, 
    farPlane=60872, width=10491.8, height=6926.4, viewOffsetX=4567.7, 
    viewOffsetY=3089.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36794.3, 
    farPlane=60938.7, width=10472.8, height=6913.85, viewOffsetX=5224.55, 
    viewOffsetY=4933.19)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37490.8, 
    farPlane=60242.2, width=4218.18, height=2784.74, viewOffsetX=4070.34, 
    viewOffsetY=5467.16)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 
    'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 
    'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6'), vector=(-4500.0, 0.0, 
    -6600.0))
#: The instances were translated by -4.5E+03, 0., -6.6E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37521.3, 
    farPlane=63762.4, width=4221.61, height=2787, viewOffsetX=3296.57, 
    viewOffsetY=5471.6)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=3037.55, 
    viewOffsetY=5371.58)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37534.5, 
    farPlane=63816.7, width=4223.1, height=2787.98, cameraPosition=(33045.5, 
    32027.3, 38174.5), cameraUpVector=(-0.564615, 0.55741, -0.608691), 
    cameraTarget=(7103.4, 2864.93, 8772.1), viewOffsetX=3038.62, 
    viewOffsetY=5373.47)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37316.9, 
    farPlane=64034.4, width=6474.57, height=4274.34, viewOffsetX=3352.96, 
    viewOffsetY=5319.03)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37273.4, 
    farPlane=64077.9, width=6467.02, height=4269.36, viewOffsetX=2283.98, 
    viewOffsetY=5103.89)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37852.6, 
    farPlane=63498.7, width=1398.29, height=923.116, viewOffsetX=1289.17, 
    viewOffsetY=2299.77)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37862.9, 
    farPlane=63488.4, width=1398.67, height=923.367, viewOffsetX=1351.25, 
    viewOffsetY=2164.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36780.3, 
    farPlane=64570.9, width=11366.7, height=7504.03, viewOffsetX=3573.72, 
    viewOffsetY=3736.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36706.2, 
    farPlane=64645, width=11343.8, height=7488.91, viewOffsetX=4335.8, 
    viewOffsetY=4559.56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36706.1, 
    farPlane=64645.1, width=11343.8, height=7488.9, viewOffsetX=4335.79, 
    viewOffsetY=4034.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36706.1, 
    farPlane=64645.1, width=11343.8, height=7488.91, viewOffsetX=2394.28, 
    viewOffsetY=3423.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36706.1, 
    farPlane=64645.1, width=11343.9, height=7488.92, viewOffsetX=2589.66, 
    viewOffsetY=3936.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36706.1, 
    farPlane=64645.2, width=11343.9, height=7488.96, viewOffsetX=1698.27, 
    viewOffsetY=3362.31)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36760.9, 
    farPlane=64676.8, width=11360.9, height=7500.15, cameraPosition=(31200, 
    32726, 39030), cameraUpVector=(-0.545293, 0.543669, -0.638028), 
    cameraTarget=(6937.13, 2926.14, 8843.65), viewOffsetX=1700.81, 
    viewOffsetY=3367.33)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37150.2, 
    farPlane=64287.5, width=8495.19, height=5608.3, viewOffsetX=1376.95, 
    viewOffsetY=3722.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37093.8, 
    farPlane=64343.9, width=8482.3, height=5599.79, viewOffsetX=954.851, 
    viewOffsetY=3351.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37321.8, 
    farPlane=64115.9, width=6929.53, height=4574.7, viewOffsetX=-26.2462, 
    viewOffsetY=3436.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37275.4, 
    farPlane=64162.3, width=6920.91, height=4569.01, viewOffsetX=2514.18, 
    viewOffsetY=4729)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36389, 
    farPlane=65048.7, width=15428.3, height=10185.4, viewOffsetX=2780.25, 
    viewOffsetY=4492.41)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36290.9, 
    farPlane=65146.7, width=15386.8, height=10157.9, viewOffsetX=6002.48, 
    viewOffsetY=5971.68)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37852.7, 
    farPlane=63585, width=1840.44, height=1215.01, viewOffsetX=5433.52, 
    viewOffsetY=7246.07)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6'), vector=(0.0, 0.0, 
    -15450.0))
#: The instances were translated by 0., 0., -15.45E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37657.7, 
    farPlane=65169.9, width=3862.94, height=2550.21, viewOffsetX=5524.74, 
    viewOffsetY=7155.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37631.3, 
    farPlane=65196.2, width=3860.24, height=2548.43, viewOffsetX=5603.98, 
    viewOffsetY=7295.57)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37890.3, 
    farPlane=64937.3, width=1536.42, height=1014.31, viewOffsetX=5916.58, 
    viewOffsetY=7754.72)
a1 = mdb.models['structure'].rootAssembly
a1.rotate(instanceList=('zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6'), axisPoint=(4575.0, 
    7300.0, -8400.0), axisDirection=(0.0, -600.0, 0.0), angle=90.0)
#: The instances were rotated by 90. ??(???????? 4.575E+03, 7.3E+03, -8.4E+03 ?????? 0., -600., 0. ??????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37019.6, 
    farPlane=65808, width=9685.58, height=6394.17, viewOffsetX=7109.06, 
    viewOffsetY=7455.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36955.8, 
    farPlane=65871.8, width=9668.88, height=6383.14, viewOffsetX=6368.25, 
    viewOffsetY=6015.95)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37413.4, 
    farPlane=65414.1, width=6093.4, height=4022.71, viewOffsetX=4651.61, 
    viewOffsetY=6157.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37372.4, 
    farPlane=65455.2, width=6086.72, height=4018.3, viewOffsetX=5662.06, 
    viewOffsetY=5396.93)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-6'), vector=(4500.0, 0.0, -350.0))
#: The instances were translated by 4.5E+03, 0., -350. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37872.3, 
    farPlane=64955.3, width=1682.05, height=1110.45, viewOffsetX=5759.86, 
    viewOffsetY=5027.91)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-2-1-rebar-5-5', ), vector=(4500.0, 0.0, 
    -225.0))
#: The instance xbeam-2-2-1-rebar-5-5 was translated by 4.5E+03, 0., -225. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37219.8, 
    farPlane=65607.7, width=7859.87, height=5188.88, viewOffsetX=5757.51, 
    viewOffsetY=5492.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37167.5, 
    farPlane=65660.1, width=7848.81, height=5181.58, viewOffsetX=5774.75, 
    viewOffsetY=6110.54)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37354.3, 
    farPlane=65473.2, width=6632.61, height=4378.68, viewOffsetX=5098.47, 
    viewOffsetY=6064.26)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37309.8, 
    farPlane=65517.7, width=6624.7, height=4373.46, viewOffsetX=3922.91, 
    viewOffsetY=5129.55)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36898.2, 
    farPlane=65929.4, width=10791.9, height=7124.55, viewOffsetX=4703.5, 
    viewOffsetY=5034.84)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36827.6, 
    farPlane=66000, width=10771.3, height=7110.92, viewOffsetX=1888.64, 
    viewOffsetY=2821.17)
session.viewports['Viewport: 1'].view.setValues(width=11458.8, height=7564.8, 
    viewOffsetX=1933.41, viewOffsetY=2844.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36750.4, 
    farPlane=66077.1, width=11434.8, height=7548.97, viewOffsetX=4046.47, 
    viewOffsetY=2863.16)
session.viewports['Viewport: 1'].view.setValues(farPlane=66077.2, 
    viewOffsetX=4871.15, viewOffsetY=4156.21)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=5252.72, 
    viewOffsetY=4907.41)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37096.7, 
    farPlane=65730.9, width=7962.86, height=5256.87, viewOffsetX=4710.74, 
    viewOffsetY=5333.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37152.7, 
    farPlane=65674.8, width=7974.89, height=5264.82, viewOffsetX=5078.4, 
    viewOffsetY=6208.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37233.5, 
    farPlane=65594, width=7734.97, height=5106.43, viewOffsetX=5364.58, 
    viewOffsetY=7753.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37181.9, 
    farPlane=65645.6, width=7724.26, height=5099.35, viewOffsetX=4825.02, 
    viewOffsetY=6394.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37928, 
    farPlane=64899.5, width=1231.18, height=812.793, viewOffsetX=3318.71, 
    viewOffsetY=6056.12)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6'), vector=(2625.0, 0.0, 
    8400.0))
#: The instances were translated by 2.625E+03, 0., 8.4E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37761.5, 
    farPlane=63676.2, width=2914.88, height=1924.33, viewOffsetX=3668.69, 
    viewOffsetY=6119.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37741.5, 
    farPlane=63696.2, width=2913.33, height=1923.31, viewOffsetX=3613.43, 
    viewOffsetY=5868.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37839.1, 
    farPlane=63598.6, width=2205.78, height=1456.2, viewOffsetX=3608.81, 
    viewOffsetY=6066.75)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37823.9, 
    farPlane=63613.8, width=2204.9, height=1455.62, viewOffsetX=3286.95, 
    viewOffsetY=5591.78)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=3213.37, 
    viewOffsetY=5484.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37432.3, 
    farPlane=64005.3, width=5920.67, height=3908.67, viewOffsetX=4586.6, 
    viewOffsetY=5985.78)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37392.4, 
    farPlane=64045.2, width=5914.35, height=3904.5, viewOffsetX=3473.97, 
    viewOffsetY=5743.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38031.4, 
    farPlane=63406.2, width=395.269, height=260.946, viewOffsetX=2983.36, 
    viewOffsetY=5932.34)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('col-2-2-1', 'col-2-2-1-rebar-2-1', 
    'col-2-2-1-rebar-2-2', 'col-2-2-1-rebar-2-3', 'col-2-2-1-rebar-2-4', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 
    'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 
    'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6'), vector=(0.0, 0.0, 
    -75.0))
#: The instances were translated by 0., 0., -75. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37910.9, 
    farPlane=63573.1, width=1549.7, height=1023.07, viewOffsetX=3153.66, 
    viewOffsetY=5951.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37900.1, 
    farPlane=63583.9, width=1549.26, height=1022.78, viewOffsetX=3227.82, 
    viewOffsetY=5878.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37819.6, 
    farPlane=63664.4, width=2384, height=1573.85, viewOffsetX=3430.69, 
    viewOffsetY=5911.16)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37803.2, 
    farPlane=63680.8, width=2382.96, height=1573.17, viewOffsetX=3262.48, 
    viewOffsetY=5854.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38940.1, 
    farPlane=62892.5, width=2454.63, height=1620.48, cameraPosition=(10598.7, 
    36908.9, 43788.3), cameraUpVector=(-0.12234, 0.466679, -0.875924), 
    cameraTarget=(2771.79, 3843.95, 8668.78), viewOffsetX=3360.59, 
    viewOffsetY=6030.77)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38931.8, 
    farPlane=62900.7, width=2454.1, height=1620.14, viewOffsetX=2707.38, 
    viewOffsetY=5770.47)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41645.7, 
    farPlane=62927.4, width=2625.19, height=1733.08, cameraPosition=(-3712.2, 
    43629.5, 37505.7), cameraUpVector=(0.0559068, 0.298958, -0.952627), 
    cameraTarget=(1475.23, 4659.99, 8481.66), viewOffsetX=2896.11, 
    viewOffsetY=6172.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41625.9, 
    farPlane=62947, width=2623.94, height=1732.26, viewOffsetX=2699.85, 
    viewOffsetY=6477.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40109.7, 
    farPlane=62431.4, width=2528.37, height=1669.16, cameraPosition=(6100.57, 
    38769.7, 42697.4), cameraUpVector=(-0.140001, 0.415589, -0.898713), 
    cameraTarget=(3268.82, 3692.4, 8793.25), viewOffsetX=2601.51, 
    viewOffsetY=6241.87)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39990.3, 
    farPlane=63167.5, width=2520.84, height=1664.2, cameraPosition=(19650.2, 
    41869.8, 37514), cameraUpVector=(-0.391289, 0.350772, -0.850795), 
    cameraTarget=(5582.53, 4450.04, 9410.81), viewOffsetX=2593.77, 
    viewOffsetY=6223.29)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39991.3, 
    farPlane=63166.6, width=2520.91, height=1664.24, viewOffsetX=2715.94, 
    viewOffsetY=6370.05)


session.viewports['Viewport: 1'].view.setValues(viewOffsetY=6340.18)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-2-2'].vertices
e11 = a.instances['zbeam-2-2-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40144.4, 
    farPlane=63013.4, width=1132.09, height=747.374, viewOffsetX=2607.18, 
    viewOffsetY=6418.78)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['zbeam-2-2-2'].vertices
e1 = a.instances['col-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[18], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40187.8, 
    farPlane=62970.1, width=781.835, height=516.147, viewOffsetX=2611.11, 
    viewOffsetY=6481.93)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-2-2'].vertices
e11 = a.instances['col-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[9], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40160.6, 
    farPlane=62997.2, width=1132.54, height=747.676, viewOffsetX=2691.96, 
    viewOffsetY=6485.31)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40152.8, 
    farPlane=63005.1, width=1132.32, height=747.53, viewOffsetX=2584.17, 
    viewOffsetY=6466.97)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40225, 
    farPlane=62932.9, width=544.29, height=359.326, viewOffsetX=2326.17, 
    viewOffsetY=6468.03)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v1 = a.instances['xbeam-2-1-1'].vertices
e1 = a.instances['xbeam-2-1-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[6], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39523.1, 
    farPlane=63634.7, width=6955.93, height=4592.13, viewOffsetX=2888.09, 
    viewOffsetY=6128.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39476.4, 
    farPlane=63681.4, width=6947.71, height=4586.7, viewOffsetX=3789.6, 
    viewOffsetY=5799.54)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38806.4, 
    farPlane=64351.5, width=13489.7, height=8905.52, viewOffsetX=4696.66, 
    viewOffsetY=5525.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38719.2, 
    farPlane=64438.7, width=13459.3, height=8885.51, viewOffsetX=4410.83, 
    viewOffsetY=2193.58)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38719, 
    farPlane=64438.8, width=13459.3, height=8885.47, viewOffsetX=2556.36, 
    viewOffsetY=773.055)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-51.4705, 
    viewOffsetY=-1618.63)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39569.6, 
    farPlane=63588.3, width=5784.29, height=3818.64, viewOffsetX=-1565.02, 
    viewOffsetY=-1597.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39611, 
    farPlane=63546.9, width=5790.34, height=3822.63, viewOffsetX=-2077.76, 
    viewOffsetY=-1655.78)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39314.1, 
    farPlane=63843.7, width=8862.21, height=5850.6, viewOffsetX=-1819.07, 
    viewOffsetY=-1973.84)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39255.3, 
    farPlane=63902.5, width=8848.94, height=5841.84, viewOffsetX=-901.925, 
    viewOffsetY=-436.566)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39607.6, 
    farPlane=63550.2, width=6184.61, height=4082.92, viewOffsetX=-357.175, 
    viewOffsetY=1046.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39565.9, 
    farPlane=63591.9, width=6178.09, height=4078.62, viewOffsetX=-1507.29, 
    viewOffsetY=-1103.35)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-2125.76, 
    viewOffsetY=-2227.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40119.5, 
    farPlane=63038.3, width=1333.78, height=880.53, viewOffsetX=-3275.86, 
    viewOffsetY=-2559.69)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6'), vector=(0.0, 0.0, 
    6600.0))
#: The instances were translated by 0., 0., 6.6E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36243.7, 
    farPlane=63377.3, width=4605.31, height=3040.31, viewOffsetX=-1901.39, 
    viewOffsetY=-3113.26)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 
    'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 
    'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6'), vector=(0.0, 3300.0, 
    0.0))
#: The instances were translated by 0., 3.3E+03, 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36399, 
    farPlane=63222, width=2819.28, height=1861.22, viewOffsetX=-2305.52, 
    viewOffsetY=-2747.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36419.5, 
    farPlane=63201.5, width=2820.87, height=1862.27, viewOffsetX=-2455.61, 
    viewOffsetY=-2381.55)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36457.5, 
    farPlane=63163.4, width=2345.42, height=1548.39, viewOffsetX=-2542.89, 
    viewOffsetY=-2344.11)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36474.7, 
    farPlane=63146.3, width=2346.52, height=1549.11, viewOffsetX=-2622.38, 
    viewOffsetY=-2340.16)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-2-4'].vertices
e11 = a.instances['xbeam-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e11[7], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['zbeam-2-2-3'].vertices
e1 = a.instances['zbeam-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[6], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-2-3'].vertices
e11 = a.instances['zbeam-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e11[6], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36173.7, 
    farPlane=63447.3, width=5244.56, height=3462.32, viewOffsetX=-2134.39, 
    viewOffsetY=-2287.86)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=38715.6, 
    farPlane=60905.4, width=14316.3, height=9451.25, viewOffsetX=-986.858, 
    viewOffsetY=-2031.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36079, 
    farPlane=57492.9, width=13341.3, height=8807.61, cameraPosition=(42876.9, 
    32887.7, 1041.6), cameraUpVector=(-0.839046, 0.517628, -0.167521), 
    cameraTarget=(4150.2, 4235.81, 9241.71), viewOffsetX=-919.653, 
    viewOffsetY=-1893.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32988.7, 
    farPlane=58344.6, width=12198.6, height=8053.22, cameraPosition=(41400.8, 
    18765.9, -17890.4), cameraUpVector=(-0.683853, 0.729139, 0.026475), 
    cameraTarget=(4029.47, 5026.76, 10439), viewOffsetX=-840.882, 
    viewOffsetY=-1731.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32442.2, 
    farPlane=57189.5, width=11996.5, height=7919.81, cameraPosition=(30539.9, 
    9463.13, -29591.4), cameraUpVector=(-0.680965, 0.731387, 0.0368707), 
    cameraTarget=(4343.64, 5275.11, 11447), viewOffsetX=-826.952, 
    viewOffsetY=-1702.34)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32446.9, 
    farPlane=57970.8, width=11998.3, height=7920.96, cameraPosition=(34568.8, 
    18465.8, -24545.5), cameraUpVector=(-0.672289, 0.722927, 0.159385), 
    cameraTarget=(4140.32, 4825.05, 11175.2), viewOffsetX=-827.072, 
    viewOffsetY=-1702.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32447.9, 
    farPlane=57969.8, width=11998.7, height=7921.22, viewOffsetX=658.207, 
    viewOffsetY=-1146.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32850, 
    farPlane=57529.3, width=12147.4, height=8019.39, cameraPosition=(41033, 
    23751, -13840), cameraUpVector=(-0.623493, 0.72518, 0.292182), 
    cameraTarget=(3699.26, 4160.31, 10864.8), viewOffsetX=666.363, 
    viewOffsetY=-1161.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=33988.2, 
    farPlane=56812.9, width=12568.3, height=8297.27, cameraPosition=(-7114.17, 
    5607.23, -35036.2), cameraUpVector=(-0.203553, 0.88845, 0.411366), 
    cameraTarget=(8105.54, 5928.23, 11398.6), viewOffsetX=689.452, 
    viewOffsetY=-1201.43)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32891.4, 
    farPlane=58284.4, width=12162.7, height=8029.51, cameraPosition=(-23409.4, 
    13896.1, -24343.8), cameraUpVector=(0.101349, 0.815214, 0.570224), 
    cameraTarget=(9522.78, 5262.7, 10711.5), viewOffsetX=667.203, 
    viewOffsetY=-1162.66)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32934.5, 
    farPlane=58241.4, width=12178.7, height=8040.03, viewOffsetX=4273.17, 
    viewOffsetY=317.91)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34107.4, 
    farPlane=57068.5, width=1970.76, height=1301.05, viewOffsetX=4393.74, 
    viewOffsetY=2467.59)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-4'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#34004 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-2')
#: ???? 'Surf-2' ?????? (4 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=34039.2, 
    farPlane=57136.7, width=2851.01, height=1882.16, viewOffsetX=4622.43, 
    viewOffsetY=2532.65)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'xbeam-2-3-4-rebar-5-6', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 
    'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 
    'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 
    'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 
    'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 
    'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 
    'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 
    'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 
    'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 
    'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 
    'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 
    'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 
    'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 
    'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 
    'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 
    'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 
    'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 
    'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 
    'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 
    'zbeam-2-4-2-rebar-4-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 
    'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 
    'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 
    'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 
    'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 
    'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 
    'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 
    'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    ))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=53080.1, 
    farPlane=88609.7, width=27944.2, height=18448.1, viewOffsetX=5955.82, 
    viewOffsetY=3250.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55468.2, 
    farPlane=86221.6, width=8681.63, height=5731.39, viewOffsetX=1883.95, 
    viewOffsetY=3918.17)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55409.7, 
    farPlane=86280.1, width=8672.47, height=5725.34, viewOffsetX=1723.26, 
    viewOffsetY=2559.75)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-115.789, 
    viewOffsetY=3783.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=54535.4, 
    farPlane=87154.5, width=17117.2, height=11300.3, viewOffsetX=665.011, 
    viewOffsetY=3504.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=54431.4, 
    farPlane=87258.4, width=17084.6, height=11278.8, viewOffsetX=1417.74, 
    viewOffsetY=1749.43)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57490.5, 
    farPlane=84926.9, width=18044.8, height=11912.7, cameraPosition=(52475.9, 
    52432.1, 33111.7), cameraUpVector=(-0.728247, 0.434254, -0.530171), 
    cameraTarget=(7605.54, 2892.98, 9627.1), viewOffsetX=1497.42, 
    viewOffsetY=1847.75)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58854.7, 
    farPlane=83562.7, width=5037.58, height=3325.68, viewOffsetX=2483.28, 
    viewOffsetY=2624.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58891.3, 
    farPlane=83526.1, width=5040.72, height=3327.75, viewOffsetX=2571.64, 
    viewOffsetY=2420.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58915.1, 
    farPlane=83498.8, width=5042.76, height=3329.1, cameraPosition=(51685.3, 
    53107.5, 33206.2), cameraUpVector=(-0.73202, 0.423047, -0.534021), 
    cameraTarget=(7609.8, 2902.51, 9630.52), viewOffsetX=2572.68, 
    viewOffsetY=2421.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58914.9, 
    height=3329.09, viewOffsetX=2567.24, viewOffsetY=2111.48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58802.4, 
    farPlane=87314.6, width=5033.12, height=3322.74, cameraPosition=(63121.8, 
    37590.7, -24091.9), cameraUpVector=(-0.867458, 0.424255, -0.259856), 
    cameraTarget=(9873.08, 4720.95, 9122), viewOffsetX=2562.34, 
    viewOffsetY=2107.45)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59086, 
    farPlane=84436.6, width=5057.4, height=3338.76, cameraPosition=(48466.8, 
    54266, 37713.4), cameraUpVector=(-0.678833, 0.40879, -0.609981), 
    cameraTarget=(6877.6, 3409.42, 11200.2), viewOffsetX=2574.7, 
    viewOffsetY=2117.61)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57385.9, 
    farPlane=86136.5, width=20805.2, height=13735.1, viewOffsetX=2898.69, 
    viewOffsetY=2450.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57257.1, 
    farPlane=86265.3, width=20758.5, height=13704.3, viewOffsetX=4322.26, 
    viewOffsetY=1863.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57256.9, 
    farPlane=86265.6, width=20758.5, height=13704.3, viewOffsetX=4568.04, 
    viewOffsetY=1349.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58806, 
    farPlane=84716.5, width=6999.93, height=4621.17, viewOffsetX=3010.82, 
    viewOffsetY=2011.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=64826, 
    farPlane=79757.8, width=7716.52, height=5094.25, cameraPosition=(42614.9, 
    66534.6, 11411.4), cameraUpVector=(-0.846205, 0.0962443, -0.524093), 
    cameraTarget=(7830.88, 4817.27, 11181.3), viewOffsetX=3319.04, 
    viewOffsetY=2217.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65536.9, 
    farPlane=79047, width=840.933, height=555.162, viewOffsetX=3530.86, 
    viewOffsetY=2562.27)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6'), vector=(0.0, 0.0, 
    350.0))
#: The instances were translated by 0., 0., 350. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65024.5, 
    farPlane=79559.4, width=5634.88, height=3720.01, viewOffsetX=4366.44, 
    viewOffsetY=2953.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60668, 
    farPlane=82351.9, width=5257.35, height=3470.77, cameraPosition=(37881.1, 
    63999.8, 31078.4), cameraUpVector=(-0.74174, 0.200766, -0.639933), 
    cameraTarget=(6704.22, 3523.41, 11339.6), viewOffsetX=4073.89, 
    viewOffsetY=2755.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60711, 
    farPlane=82308.8, width=5261.08, height=3473.23, viewOffsetX=3833.26, 
    viewOffsetY=2117.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59089, 
    farPlane=83930.8, width=20387.6, height=13459.4, viewOffsetX=6681.09, 
    viewOffsetY=2331.81)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58957.2, 
    farPlane=84062.7, width=20342.1, height=13429.4, viewOffsetX=4542.19, 
    viewOffsetY=1406.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=64636.1, 
    farPlane=77961.7, width=22301.6, height=14723, cameraPosition=(7221.38, 
    74991.4, 10233.2), cameraUpVector=(-0.193064, -0.303968, -0.932915), 
    cameraTarget=(3801.42, 4246.07, 8678.44), viewOffsetX=4979.7, 
    viewOffsetY=1541.97)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58783.5, 
    farPlane=82179.3, width=20282.3, height=13389.9, cameraPosition=(6118.51, 
    68425.8, 36088.9), cameraUpVector=(-0.216228, 0.0526412, -0.974923), 
    cameraTarget=(3876.63, 3071.34, 8834.84), viewOffsetX=4528.8, 
    viewOffsetY=1402.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56845.6, 
    farPlane=84301.4, width=19613.7, height=12948.5, cameraPosition=(17878.8, 
    64279.6, 42725.2), cameraUpVector=(-0.236303, 0.195645, -0.951779), 
    cameraTarget=(3818.04, 3620.05, 8935.7), viewOffsetX=4379.5, 
    viewOffsetY=1356.12)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57453.5, 
    farPlane=83495.9, width=19823.5, height=13087, cameraPosition=(12530.7, 
    65535, 41557.5), cameraUpVector=(-0.191384, 0.159729, -0.968431), 
    cameraTarget=(3714.69, 3409.43, 8668.18), viewOffsetX=4426.33, 
    viewOffsetY=1370.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57267.1, 
    farPlane=83682.3, width=22545.6, height=14884, viewOffsetX=4145.7, 
    viewOffsetY=1292.01)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57122.9, 
    farPlane=83826.5, width=22488.8, height=14846.5, viewOffsetX=5587.71, 
    viewOffsetY=3371.63)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59426.3, 
    farPlane=81523.1, width=2521.96, height=1664.93, viewOffsetX=2728.57, 
    viewOffsetY=7108.42)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59444.8, 
    farPlane=81504.6, width=2522.74, height=1665.45, viewOffsetX=2471.45, 
    viewOffsetY=7241.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59289.7, 
    farPlane=81495.4, width=2516.16, height=1661.1, cameraPosition=(11900.9, 
    65094.1, 42282), cameraUpVector=(-0.194593, 0.169765, -0.966082), 
    cameraTarget=(3777.01, 3292.09, 8614.07), viewOffsetX=2465, 
    viewOffsetY=7222.15)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57696.4, 
    farPlane=83088.7, width=17223.8, height=11370.7, viewOffsetX=3716.3, 
    viewOffsetY=5925.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57583.8, 
    farPlane=83201.3, width=17190.2, height=11348.5, viewOffsetX=7280.31, 
    viewOffsetY=3155.37)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57583.7, 
    farPlane=83201.4, viewOffsetX=6318.09, viewOffsetY=-1361.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57583.7, 
    viewOffsetX=5836.98, viewOffsetY=-5730.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57812.7, 
    farPlane=82972.4, width=14334.6, height=9463.36, viewOffsetX=5506.12, 
    viewOffsetY=-5607.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57791.1, 
    farPlane=85559.7, width=14329.3, height=9459.83, cameraPosition=(28591.7, 
    62255.9, 43452.6), cameraUpVector=(-0.262818, 0.250253, -0.931826), 
    cameraTarget=(4099.92, 5017.32, 9645.58), viewOffsetX=5504.07, 
    viewOffsetY=-5605.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58830.6, 
    farPlane=84520.3, width=5766.14, height=3806.66, viewOffsetX=3478.53, 
    viewOffsetY=-4797.98)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58791.2, 
    farPlane=84559.7, width=5762.28, height=3804.11, viewOffsetX=3011, 
    viewOffsetY=-4676.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58051.7, 
    farPlane=85299.2, width=12875.2, height=8499.88, viewOffsetX=3990.22, 
    viewOffsetY=-5008.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57966.1, 
    farPlane=85384.8, width=12856.2, height=8487.35, viewOffsetX=3956.66, 
    viewOffsetY=-4364.54)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58740.8, 
    farPlane=84610.1, width=5828.29, height=3847.69, viewOffsetX=3114.41, 
    viewOffsetY=-4325.95)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57786.6, 
    farPlane=88159.2, width=5733.62, height=3785.19, cameraPosition=(32624.4, 
    51110.6, 57472.2), cameraUpVector=(-0.350648, 0.501844, -0.790695), 
    cameraTarget=(3920.55, 5560.68, 11425.3), viewOffsetX=3063.82, 
    viewOffsetY=-4255.68)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57559.1, 
    farPlane=88386.8, width=7860.34, height=5189.19, viewOffsetX=3378.36, 
    viewOffsetY=-4781.77)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57550.9, 
    farPlane=88395, width=7859.22, height=5188.46, viewOffsetX=3538.62, 
    viewOffsetY=-3714.63)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58100.4, 
    farPlane=87845.5, width=2948.17, height=1946.31, viewOffsetX=2745.21, 
    viewOffsetY=-3027.43)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58918.4, 
    farPlane=86150.3, width=2989.68, height=1973.71, cameraPosition=(23717.2, 
    58589.8, 52631.6), cameraUpVector=(-0.294478, 0.366497, -0.882589), 
    cameraTarget=(3556.67, 5332.33, 10486.4), viewOffsetX=2783.86, 
    viewOffsetY=-3070.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58913.7, 
    farPlane=86154.9, width=2989.44, height=1973.55, viewOffsetX=3298.51, 
    viewOffsetY=-3626.78)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58832.8, 
    farPlane=86235.8, width=3918.5, height=2586.9, viewOffsetX=3547.92, 
    viewOffsetY=-3247.33)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58348.2, 
    farPlane=87402.4, width=3886.22, height=2565.58, cameraPosition=(30480.3, 
    52973.1, 56699.1), cameraUpVector=(-0.624729, 0.444346, -0.642082), 
    cameraTarget=(3238.23, 4454.24, 12849.2), viewOffsetX=3518.69, 
    viewOffsetY=-3220.58)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58351.7, 
    farPlane=87398.9, width=3886.45, height=2565.74, cameraPosition=(31213.1, 
    54266.1, 54813.2), cameraUpVector=(-0.302239, 0.444897, -0.843041), 
    cameraTarget=(3970.99, 5747.23, 10963.3), viewOffsetX=3518.9, 
    viewOffsetY=-3220.77)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58671.9, 
    farPlane=87078.7, width=1065.65, height=703.517, viewOffsetX=2457.47, 
    viewOffsetY=-3044.57)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58679.8, 
    farPlane=87070.8, width=1065.8, height=703.611, viewOffsetX=2380.93, 
    viewOffsetY=-3065.64)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58506.1, 
    farPlane=87244.5, width=2721.38, height=1796.59, viewOffsetX=2873.5, 
    viewOffsetY=-3139.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58487.3, 
    farPlane=87263.3, width=2720.51, height=1796.01, viewOffsetX=2925.29, 
    viewOffsetY=-3004.18)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=2787.65, 
    viewOffsetY=-3220.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58711.2, 
    farPlane=87039.4, width=747.77, height=493.658, viewOffsetX=2242.5, 
    viewOffsetY=-2959.77)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('col-2-3-4', 'col-2-3-4-rebar-2-1', 
    'col-2-3-4-rebar-2-2', 'col-2-3-4-rebar-2-3', 'col-2-3-4-rebar-2-4', 
    'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 
    'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 
    'zbeam-2-3-3-rebar-3-6'), vector=(0.0, 0.0, 50.0))
#: The instances were translated by 0., 0., 50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58251.1, 
    farPlane=87499.5, width=5051.6, height=3334.94, viewOffsetX=3231.78, 
    viewOffsetY=-2665.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58196.3, 
    farPlane=87579.4, width=5046.85, height=3331.8, cameraPosition=(31251.1, 
    54049.8, 55048.9), cameraUpVector=(-0.308273, 0.449501, -0.838401), 
    cameraTarget=(3958.34, 5729.9, 11011.2), viewOffsetX=3228.73, 
    viewOffsetY=-2662.54)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58196.5, 
    width=5046.86, height=3331.81, viewOffsetX=3391.72, viewOffsetY=-3505.01)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56772.9, 
    farPlane=89002.8, width=17424.7, height=11503.3, viewOffsetX=5471.37, 
    viewOffsetY=-3786.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56757.3, 
    farPlane=89018.3, width=17419.9, height=11500.2, viewOffsetX=4588.56, 
    viewOffsetY=-2021.66)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57860.3, 
    farPlane=87915.3, width=7467.86, height=4930.09, viewOffsetX=1880.24, 
    viewOffsetY=-1691.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57914, 
    farPlane=87861.6, width=7474.79, height=4934.67, viewOffsetX=1415.31, 
    viewOffsetY=-1146.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57914.1, 
    viewOffsetX=1721.06, viewOffsetY=-83.4156)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57489.2, 
    farPlane=88286.5, width=11822, height=7804.59, viewOffsetX=2054.84, 
    viewOffsetY=549.544)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57410.4, 
    farPlane=88365.3, width=11805.8, height=7793.89, viewOffsetX=3348.25, 
    viewOffsetY=-2833.22)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58466.8, 
    farPlane=87308.9, width=2559.83, height=1689.93, viewOffsetX=2457.21, 
    viewOffsetY=-3112.06)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 
    'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 
    'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6'), vector=(4500.0, 0.0, 
    6650.0))
#: The instances were translated by 4.5E+03, 0., 6.65E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58454.7, 
    farPlane=87289.9, width=2559.3, height=1689.58, viewOffsetX=2586.18, 
    viewOffsetY=-3296.08)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-3-4'].vertices
e1 = a.instances['xbeam-2-3-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[6], normal=e1[7], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['xbeam-2-3-4'].vertices
e11 = a.instances['xbeam-2-3-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[4], normal=e11[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-3-4'].vertices
e1 = a.instances['xbeam-2-3-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[4], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-3-3'].vertices
e11 = a.instances['zbeam-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[4], normal=e11[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['zbeam-2-3-3'].vertices
e1 = a.instances['zbeam-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[4], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57072.2, 
    farPlane=88672.4, width=15342.1, height=10128.4, viewOffsetX=6168.62, 
    viewOffsetY=-2478.13)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56971.2, 
    farPlane=88773.4, width=15314.9, height=10110.5, viewOffsetX=7014.94, 
    viewOffsetY=-1649.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56971.1, 
    farPlane=88773.5, width=15314.9, height=10110.5, viewOffsetX=4064.05, 
    viewOffsetY=511.575)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56971.1, 
    width=15314.9, height=10110.5, viewOffsetX=2217.69, viewOffsetY=528.068)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56971.1, 
    width=15314.9, height=10110.5, viewOffsetX=1986.89, viewOffsetY=-659.462)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55842.4, 
    farPlane=89902.2, width=26536.4, height=17518.7, viewOffsetX=3583.68, 
    viewOffsetY=130.955)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-140917.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x0000000012EE3C68>materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37256, 
    farPlane=60477, width=6909.06, height=4561.18, viewOffsetX=517.66, 
    viewOffsetY=1937.31)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37209.7, 
    farPlane=60523.3, width=6900.47, height=4555.51, viewOffsetX=1653.48, 
    viewOffsetY=2863.84)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37626.3, 
    farPlane=60106.7, width=3121.59, height=2060.8, viewOffsetX=538.109, 
    viewOffsetY=3524.26)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37649, 
    farPlane=60084, width=3123.48, height=2062.04, viewOffsetX=407.308, 
    viewOffsetY=3916.59)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=454.379, 
    viewOffsetY=3489.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36776.6, 
    farPlane=60956.4, width=11280.2, height=7446.92, viewOffsetX=1502.39, 
    viewOffsetY=3226.84)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36703, 
    farPlane=61030, width=11257.7, height=7432.02, viewOffsetX=1487.26, 
    viewOffsetY=1814)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36702.9, 
    farPlane=61030.1, width=11257.7, height=7432.03, viewOffsetX=348.159, 
    viewOffsetY=359.113)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36625.8, 
    farPlane=61107.3, width=11234, height=7416.43, viewOffsetX=344.29, 
    viewOffsetY=344.064)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36702.8, 
    farPlane=61030.2, width=11257.7, height=7432.03, viewOffsetX=-685.021, 
    viewOffsetY=-516.018)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36702.9, 
    farPlane=61030.1, width=11257.7, height=7432.07, viewOffsetX=-1799.89, 
    viewOffsetY=938.872)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36702.9, 
    farPlane=61030.1, width=11257.7, height=7432.08, viewOffsetX=-1375.76, 
    viewOffsetY=732.763)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38081, 
    farPlane=61152.7, width=11680.5, height=7711.14, cameraPosition=(19701.6, 
    30649.7, 47827.1), cameraUpVector=(-0.423984, 0.574352, -0.700255), 
    cameraTarget=(7609.68, 3119.6, 9306.71), viewOffsetX=-1427.42, 
    viewOffsetY=760.277)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37817.3, 
    farPlane=61042, width=11599.6, height=7657.77, cameraPosition=(22519.9, 
    33969.4, 44007.1), cameraUpVector=(-0.429477, 0.514822, -0.741962), 
    cameraTarget=(7616.1, 3049.05, 9225.66), viewOffsetX=-1417.54, 
    viewOffsetY=755.013)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37824.7, 
    farPlane=61034.6, width=11601.9, height=7659.27, viewOffsetX=705.241, 
    viewOffsetY=-456.828)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39056.9, 
    farPlane=59802.4, width=947.75, height=625.68, viewOffsetX=-1304.08, 
    viewOffsetY=-848.632)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('col-2-3-4', 'col-2-3-4-rebar-2-1', 
    'col-2-3-4-rebar-2-2', 'col-2-3-4-rebar-2-3', 'col-2-3-4-rebar-2-4', 
    'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 
    'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 
    'zbeam-2-3-3-rebar-3-6'), vector=(0.0, 0.0, 50.0))
#: The instances were translated by 0., 0., 50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38510.6, 
    farPlane=60313.1, width=5737.65, height=3787.85, viewOffsetX=-399.144, 
    viewOffsetY=-337.589)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38471.9, 
    farPlane=60351.8, width=5731.87, height=3784.04, viewOffsetX=-1244.02, 
    viewOffsetY=557.833)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38118.3, 
    farPlane=60705.4, width=9316.75, height=6150.68, viewOffsetX=-823.412, 
    viewOffsetY=1176.34)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38056.7, 
    farPlane=60767, width=9301.69, height=6140.74, cameraPosition=(22460.9, 
    33916.5, 44079.4), cameraUpVector=(-0.380769, 0.518191, -0.765828), 
    cameraTarget=(7557.13, 2996.11, 9297.99), viewOffsetX=-822.081, 
    viewOffsetY=1174.44)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38203.8, 
    farPlane=60491.8, width=9337.64, height=6164.47, cameraPosition=(24631, 
    37571.3, 39418.9), cameraUpVector=(-0.384054, 0.429758, -0.817197), 
    cameraTarget=(7549.63, 3041.31, 9354.86), viewOffsetX=-825.258, 
    viewOffsetY=1178.98)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38171.7, 
    farPlane=60523.9, width=10171.4, height=6714.93, viewOffsetX=-785.077, 
    viewOffsetY=2779.21)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38104.8, 
    farPlane=60590.9, width=10153.6, height=6703.15, viewOffsetX=-958.574, 
    viewOffsetY=248.353)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-652.543, 
    viewOffsetY=-1009.17)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38976.2, 
    farPlane=59719.4, width=2502.54, height=1652.11, viewOffsetX=-1488.6, 
    viewOffsetY=-1759.08)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6'), vector=(4500.0, 0.0, 
    6650.0))
#: The instances were translated by 4.5E+03, 0., 6.65E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35239.1, 
    farPlane=59672.9, width=2262.59, height=1493.7, viewOffsetX=-844.154, 
    viewOffsetY=-1648.89)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35519, 
    farPlane=59241.3, width=2280.56, height=1505.57, cameraPosition=(20985.8, 
    38803.5, 39830.2), cameraUpVector=(-0.332384, 0.396308, -0.855839), 
    cameraTarget=(7760.32, 2976.2, 9343.63), viewOffsetX=-850.859, 
    viewOffsetY=-1661.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35516.9, 
    farPlane=59243.4, width=2280.43, height=1505.48, viewOffsetX=-494.875, 
    viewOffsetY=-1725.75)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35732, 
    farPlane=59028.3, width=405.713, height=267.841, viewOffsetX=-832.74, 
    viewOffsetY=-1757.79)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6'), vector=(50.0, 0.0, 0.0))
#: The instances were translated by 50., 0., 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35457.9, 
    farPlane=59302.4, width=2963.98, height=1956.75, viewOffsetX=-411.135, 
    viewOffsetY=-1646.69)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35437.6, 
    farPlane=59322.7, width=2962.29, height=1955.63, viewOffsetX=-315.239, 
    viewOffsetY=-1859.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35281.1, 
    farPlane=59479.2, width=4579.4, height=3023.2, viewOffsetX=43.2511, 
    viewOffsetY=-1804.75)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35250, 
    farPlane=59510.3, width=4575.37, height=3020.54, viewOffsetX=-79.9132, 
    viewOffsetY=-1965.77)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35527, 
    farPlane=59233.3, width=2062.95, height=1361.9, viewOffsetX=-627.798, 
    viewOffsetY=-2022.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35542.1, 
    farPlane=59218.2, width=2063.82, height=1362.48, viewOffsetX=-616.957, 
    viewOffsetY=-1971.81)


a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-3-4'].vertices
e11 = a.instances['xbeam-2-3-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35616.3, 
    farPlane=59144, width=1341.13, height=885.382, viewOffsetX=-753.235, 
    viewOffsetY=-1988.06)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['xbeam-2-3-4'].vertices
e1 = a.instances['xbeam-2-3-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[4], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-3-4'].vertices
e11 = a.instances['xbeam-2-3-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v1 = a.instances['zbeam-2-2-3'].vertices
e1 = a.instances['zbeam-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[6], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-2-3'].vertices
e11 = a.instances['zbeam-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e11[6], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35582.5, 
    farPlane=59177.8, width=1825.66, height=1205.26, viewOffsetX=-643.202, 
    viewOffsetY=-2085.72)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v1 = a.instances['zbeam-2-3-3'].vertices
e1 = a.instances['col-2-3-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[30], 
    cells=pickedCells)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=38748.8, 
    farPlane=59848.3, width=7948.2, height=5247.19, viewOffsetX=231.548, 
    viewOffsetY=-2286.34)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38890.8, 
    farPlane=58278.6, width=7977.3, height=5266.41, cameraPosition=(35341, 
    40999.8, 21020.5), cameraUpVector=(-0.788357, 0.31399, -0.529059), 
    cameraTarget=(6929.25, 2824.93, 9912.5), viewOffsetX=232.396, 
    viewOffsetY=-2294.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38886.1, 
    farPlane=58283.1, width=7976.35, height=5265.78, viewOffsetX=-2549.48, 
    viewOffsetY=-2766.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36516.4, 
    farPlane=56763, width=7490.28, height=4944.89, cameraPosition=(44098.3, 
    31123.3, 1376.77), cameraUpVector=(-0.836684, 0.529219, -0.14102), 
    cameraTarget=(5252.93, 2943.85, 10590.4), viewOffsetX=-2394.12, 
    viewOffsetY=-2598.29)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36571.6, 
    farPlane=56707.8, width=7501.6, height=4952.36, viewOffsetX=-3560.53, 
    viewOffsetY=-1608.51)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29606.7, 
    farPlane=49871.1, width=6072.95, height=4009.2, cameraPosition=(-4244.15, 
    3823.52, -30216.8), cameraUpVector=(-0.303043, 0.872534, 0.383208), 
    cameraTarget=(3810.62, 4121.83, 17980.3), viewOffsetX=-2882.44, 
    viewOffsetY=-1302.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28644.4, 
    farPlane=51116, width=5875.57, height=3878.9, cameraPosition=(-13556.6, 
    6210.39, -26218.8), cameraUpVector=(-0.204966, 0.835192, 0.510336), 
    cameraTarget=(6328.54, 3373.41, 18328.4), viewOffsetX=-2788.76, 
    viewOffsetY=-1259.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28670.7, 
    farPlane=51089.7, width=5880.96, height=3882.46, viewOffsetX=-2272.22, 
    viewOffsetY=360.37)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28891.2, 
    farPlane=51892.9, width=5926.18, height=3912.31, cameraPosition=(-11224.2, 
    17984.4, -25221.9), cameraUpVector=(-0.145545, 0.683944, 0.714868), 
    cameraTarget=(5521.22, 848.618, 17367.7), viewOffsetX=-2289.69, 
    viewOffsetY=363.141)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28886, 
    farPlane=51898, width=5925.12, height=3911.61, viewOffsetX=-2786.76, 
    viewOffsetY=2200.83)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29406.2, 
    farPlane=51377.9, width=1366.21, height=901.935, viewOffsetX=-3477.49, 
    viewOffsetY=2214.92)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-4'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#84420000 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-2')
#: ???? 'Surf-2' ?????? (4 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=29262.7, 
    farPlane=51521.4, width=2856.65, height=1885.89, viewOffsetX=-3035.69, 
    viewOffsetY=2338.73)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'xbeam-2-3-4-rebar-5-6', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 
    'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 
    'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 
    'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 
    'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 
    'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 
    'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 
    'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 
    'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 
    'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 
    'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 
    'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 
    'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 
    'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 
    'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 
    'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 
    'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 
    'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 
    'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 
    'zbeam-2-4-2-rebar-4-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 
    'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 
    'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 
    'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 
    'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 
    'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 
    'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 
    'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    ))
session.viewports['Viewport: 1'].view.setValues(width=3036.94, height=2004.91, 
    viewOffsetX=-2981.57, viewOffsetY=2325.87)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=43769.9, 
    farPlane=74937.4, width=24543.4, height=16202.9, viewOffsetX=3936.45, 
    viewOffsetY=1004.42)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45219.5, 
    farPlane=73487.8, width=12067.6, height=7966.69, viewOffsetX=2507.64, 
    viewOffsetY=1003.93)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45303.4, 
    farPlane=73403.9, width=12089.9, height=7981.47, viewOffsetX=2863.67, 
    viewOffsetY=1070.89)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45303.5, 
    farPlane=73403.8, width=12090, height=7981.49, viewOffsetX=1523.24, 
    viewOffsetY=719.342)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-1561.08, 
    viewOffsetY=2021.38)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1939.68, 
    viewOffsetY=3583.83)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=4360.28, 
    viewOffsetY=4234.85)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=4997.97, 
    viewOffsetY=4260.89)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46121.8, 
    farPlane=72585.5, width=5372.78, height=3546.97, viewOffsetX=4521.23, 
    viewOffsetY=4216.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46085.3, 
    farPlane=72622.1, width=5368.52, height=3544.16, viewOffsetX=5205.33, 
    viewOffsetY=6178.48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46604.7, 
    farPlane=72102.6, width=848.317, height=560.037, viewOffsetX=4908, 
    viewOffsetY=6918.08)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 
    'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 
    'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6'), vector=(-4550.0, 0.0, 
    -6600.0))
#: The instances were translated by -4.55E+03, 0., -6.6E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46271.6, 
    farPlane=75986.4, width=4004.66, height=2643.77, viewOffsetX=5237.86, 
    viewOffsetY=6758.95)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46244.2, 
    farPlane=76013.9, width=4002.29, height=2642.21, viewOffsetX=5239.06, 
    viewOffsetY=6267.88)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47394.1, 
    farPlane=75831.9, width=4101.82, height=2707.91, cameraPosition=(30551.7, 
    45589.2, 46899.8), cameraUpVector=(-0.494547, 0.436793, -0.751423), 
    cameraTarget=(5773.71, 3920.39, 12656.3), viewOffsetX=5369.34, 
    viewOffsetY=6423.74)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47749.9, 
    farPlane=75476.1, width=887.089, height=585.633, viewOffsetX=4512.32, 
    viewOffsetY=7444.69)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('col-2-2-1', 'col-2-2-1-rebar-2-1', 
    'col-2-2-1-rebar-2-2', 'col-2-2-1-rebar-2-3', 'col-2-2-1-rebar-2-4', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 
    'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 
    'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6'), vector=(0.0, 0.0, 
    -50.0))
#: The instances were translated by 0., 0., -50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47477.1, 
    farPlane=75777.8, width=3497.5, height=2308.96, viewOffsetX=4854.87, 
    viewOffsetY=7234.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47453.1, 
    farPlane=75801.8, width=3495.74, height=2307.79, viewOffsetX=5085.71, 
    viewOffsetY=6990.22)


a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-2-1'].vertices
e11 = a.instances['xbeam-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47698.1, 
    farPlane=75556.7, width=1305.63, height=861.946, viewOffsetX=4755.13, 
    viewOffsetY=7262.94)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['xbeam-2-2-1'].vertices
e1 = a.instances['col-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[18], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-2-1'].vertices
e11 = a.instances['col-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[9], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v1 = a.instances['zbeam-2-2-1'].vertices
e1 = a.instances['zbeam-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[6], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-2-1'].vertices
e11 = a.instances['zbeam-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e11[6], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v1 = a.instances['zbeam-2-3-1'].vertices
e1 = a.instances['col-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[30], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47364.7, 
    farPlane=75890.1, width=4524.15, height=2986.73, viewOffsetX=5710.59, 
    viewOffsetY=7600.59)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=47227.4, 
    farPlane=76027.5, width=38048.8, height=25118.8, viewOffsetX=14268, 
    viewOffsetY=11425.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47005.3, 
    farPlane=76249.6, width=37869.9, height=25000.7, viewOffsetX=9146.15, 
    viewOffsetY=5049.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55564.1, 
    farPlane=79802.4, width=44765.3, height=29552.9, cameraPosition=(58063.9, 
    48580.8, 12079.1), cameraUpVector=(-0.89451, 0.395547, -0.208313), 
    cameraTarget=(16725.4, 6025.12, 13809), viewOffsetX=10811.5, 
    viewOffsetY=5969.42)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61772.6, 
    farPlane=89843.3, width=49767.2, height=32855, cameraPosition=(23088.9, 
    20835.8, -65533.7), cameraUpVector=(-0.593688, 0.637575, 0.490951), 
    cameraTarget=(22624.3, 6992.13, -7818.97), viewOffsetX=12019.5, 
    viewOffsetY=6636.42)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59534.4, 
    farPlane=93502, width=47964, height=31664.6, cameraPosition=(-30434.3, 
    16772.8, -59266), cameraUpVector=(-0.151792, 0.656578, 0.738826), 
    cameraTarget=(8050.02, 6331.8, -15302.4), viewOffsetX=11584, 
    viewOffsetY=6395.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59601.7, 
    farPlane=93173.9, width=48018.2, height=31700.4, cameraPosition=(-39146.7, 
    20995.1, -52432.6), cameraUpVector=(-0.0242472, 0.622174, 0.782503), 
    cameraTarget=(4887.42, 7446.78, -15012.1), viewOffsetX=11597.1, 
    viewOffsetY=6403.19)
session.viewports['Viewport: 1'].view.setValues(nearPlane=64652.2, 
    farPlane=88123.4, width=4383.74, height=2894.03, viewOffsetX=7715.67, 
    viewOffsetY=8230.8)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#80420002 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-3')
#: ???? 'Surf-3' ?????? (4 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=64580.8, 
    farPlane=88194.8, width=5990.99, height=3955.1, viewOffsetX=7812.13, 
    viewOffsetY=8153.13)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'xbeam-2-3-4-rebar-5-6', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 
    'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 
    'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 
    'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 
    'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 
    'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 
    'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 
    'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 
    'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 
    'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 
    'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 
    'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 
    'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 
    'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 
    'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 
    'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 
    'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 
    'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 
    'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 
    'zbeam-2-4-2-rebar-4-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 
    'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 
    'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 
    'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 
    'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 
    'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 
    'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 
    'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    ))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=53119.2, 
    farPlane=88666.6, width=27958.1, height=18457.2, viewOffsetX=7072.28, 
    viewOffsetY=812.961)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55205.2, 
    farPlane=86580.6, width=10148.7, height=6699.9, viewOffsetX=5315.25, 
    viewOffsetY=3921.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55277.1, 
    farPlane=86508.6, width=10161.9, height=6708.64, viewOffsetX=4994.03, 
    viewOffsetY=5437.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55277.2, 
    width=10161.9, height=6708.65, viewOffsetX=6339.48, viewOffsetY=3412.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55277.2, 
    width=10161.9, height=6708.65, viewOffsetX=6131.64, viewOffsetY=4080.31)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55277.2, 
    width=10161.9, height=6708.65, viewOffsetX=4633.05, viewOffsetY=4299.19)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56025.3, 
    farPlane=85760.5, width=3508.11, height=2315.97, viewOffsetX=6001.54, 
    viewOffsetY=5021.94)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 
    'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 
    'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6'), vector=(4500.0, 0.0, 
    50.0))
#: The instances were translated by 4.5E+03, 0., 50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56050.9, 
    farPlane=85734.9, width=3509.72, height=2317.03, viewOffsetX=6457.64, 
    viewOffsetY=4770.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55493.1, 
    farPlane=86292.6, width=8826.43, height=5826.98, viewOffsetX=7122.42, 
    viewOffsetY=4299.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55433.6, 
    farPlane=86352.1, width=8816.97, height=5820.73, viewOffsetX=6488.39, 
    viewOffsetY=4190.84)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-142749.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x00000000116A6708>materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['structure'].rootAssembly
p = mdb.models['structure'].parts['beam-4']
a1.Instance(name='beam-4-1', part=p, dependent=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35461.6, 
    farPlane=62271.4, width=21221.6, height=14010, viewOffsetX=1667.58, 
    viewOffsetY=1394.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35794.1, 
    farPlane=61938.9, width=20217.8, height=13347.3, viewOffsetX=1824.94, 
    viewOffsetY=2064.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34286.4, 
    farPlane=60069.6, width=19366.2, height=12785.1, cameraPosition=(26116.3, 
    5683.3, 51287.3), cameraUpVector=(-0.416879, 0.870751, -0.260777), 
    cameraTarget=(6605.6, 1684.89, 6663.55), viewOffsetX=1748.07, 
    viewOffsetY=1977.29)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34092.8, 
    farPlane=60263.2, width=23115.6, height=15260.3, viewOffsetX=2476.3, 
    viewOffsetY=2554.72)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36050.4, 
    farPlane=62917.4, width=24442.9, height=16136.6, cameraPosition=(41309.5, 
    28406.1, 33899.8), cameraUpVector=(-0.507282, 0.611542, -0.607191), 
    cameraTarget=(6794.52, 3048.67, 10370), viewOffsetX=2618.48, 
    viewOffsetY=2701.41)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37626.4, 
    farPlane=61341.4, width=8910.66, height=5882.59, viewOffsetX=3402.52, 
    viewOffsetY=4897.37)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37688.8, 
    farPlane=63699.4, width=8925.43, height=5892.34, viewOffsetX=4551.46, 
    viewOffsetY=6135.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36800.4, 
    farPlane=62167.4, width=17568.3, height=11598.1, viewOffsetX=6721.31, 
    viewOffsetY=7941.63)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36690.1, 
    farPlane=62277.7, width=17515.6, height=11563.3, viewOffsetX=4306.67, 
    viewOffsetY=2843.54)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34025.8, 
    farPlane=58675.6, width=16243.7, height=10723.6, cameraPosition=(22315.8, 
    1994.04, 52058.6), cameraUpVector=(-0.303251, 0.910381, -0.281507), 
    cameraTarget=(4676.6, -66.6216, 6533.32), viewOffsetX=3993.93, 
    viewOffsetY=2637.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34345.5, 
    farPlane=58356, width=15666.3, height=10342.5, viewOffsetX=3324.3, 
    viewOffsetY=2291.81)
session.viewports['Viewport: 1'].view.setValues(nearPlane=33824.3, 
    farPlane=59622.5, width=15428.6, height=10185.6, cameraPosition=(24917.1, 
    21938.8, 47384.8), cameraUpVector=(-0.0411945, 0.668124, -0.742909), 
    cameraTarget=(3631.99, 1623.94, 8369.52), viewOffsetX=3273.86, 
    viewOffsetY=2257.03)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35329.6, 
    farPlane=58117.4, width=2518.11, height=1662.39, viewOffsetX=1672.78, 
    viewOffsetY=5629.76)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('beam-4-1', ), vector=(4500.0, 6700.0, -4050.0))
#: The instance beam-4-1 was translated by 4.5E+03, 6.7E+03, -4.05E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=34942.8, 
    farPlane=61737.6, width=6378.15, height=4210.69, viewOffsetX=2301.01, 
    viewOffsetY=5285.53)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36684.1, 
    farPlane=60919.8, width=6695.99, height=4420.52, cameraPosition=(11826, 
    30193.8, 47054.6), cameraUpVector=(0.0130649, 0.553003, -0.833077), 
    cameraTarget=(3765.84, 1500.68, 8328.94), viewOffsetX=2415.67, 
    viewOffsetY=5548.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36305.7, 
    farPlane=61298.2, width=10219.2, height=6746.45, viewOffsetX=3235.65, 
    viewOffsetY=5362.54)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36238.7, 
    farPlane=61365.2, width=10200.3, height=6734, cameraPosition=(14617.9, 
    28872.4, 47452.5), cameraUpVector=(-0.328745, 0.555491, -0.763778), 
    cameraTarget=(6557.78, 179.324, 8726.88), viewOffsetX=3229.68, 
    viewOffsetY=5352.64)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=2537.93, 
    viewOffsetY=6813.66)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36647.9, 
    farPlane=60955.8, width=6288.03, height=4151.19, viewOffsetX=2129.67, 
    viewOffsetY=7178.41)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37930.2, 
    farPlane=61851.6, width=6508.03, height=4296.43, cameraPosition=(23059.8, 
    36636.1, 40262.9), cameraUpVector=(-0.34968, 0.418347, -0.838278), 
    cameraTarget=(6259.68, 1763.89, 10436.5), viewOffsetX=2204.18, 
    viewOffsetY=7429.56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38517.9, 
    farPlane=61263.9, width=1168.71, height=771.552, viewOffsetX=1784.87, 
    viewOffsetY=8206.37)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('col-2-2-1', 'col-2-2-1-rebar-2-1', 
    'col-2-2-1-rebar-2-2', 'col-2-2-1-rebar-2-3', 'col-2-2-1-rebar-2-4', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'beam-4-1'), vector=(0.0, 0.0, -50.0))
#: The instances were translated by 0., 0., -50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38221.5, 
    farPlane=61590.8, width=4030.34, height=2660.72, viewOffsetX=1908.65, 
    viewOffsetY=7946.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38194, 
    farPlane=61618.3, width=4027.44, height=2658.81, viewOffsetX=2223.74, 
    viewOffsetY=7876.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40258.5, 
    farPlane=61259.1, width=4245.13, height=2802.53, cameraPosition=(16914.8, 
    42511.9, 37589.4), cameraUpVector=(-0.322331, 0.280097, -0.904239), 
    cameraTarget=(6185.83, 2862.21, 11118.2), viewOffsetX=2343.94, 
    viewOffsetY=8301.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38591.6, 
    farPlane=61916.2, width=4069.37, height=2686.49, cameraPosition=(31111.4, 
    36970.1, 35347.1), cameraUpVector=(-0.422613, 0.399368, -0.813574), 
    cameraTarget=(7140.67, 2228.11, 10723.3), viewOffsetX=2246.89, 
    viewOffsetY=7958.13)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38757.3, 
    farPlane=61750.5, width=2650.23, height=1749.61, viewOffsetX=2216.59, 
    viewOffsetY=8042.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38776.7, 
    farPlane=61731.2, width=2651.55, height=1750.48, viewOffsetX=2223.41, 
    viewOffsetY=8206.51)


a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-2-1'].vertices
e11 = a.instances['xbeam-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38858.3, 
    farPlane=61649.5, width=1833.08, height=1210.15, viewOffsetX=2157.57, 
    viewOffsetY=8273.93)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['xbeam-2-2-1'].vertices
e1 = a.instances['col-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[18], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-2-1'].vertices
e11 = a.instances['col-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[9], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v1 = a.instances['zbeam-2-2-1'].vertices
e1 = a.instances['col-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[17], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-2-1'].vertices
e11 = a.instances['col-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e11[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    'beam-4-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=37856.8, 
    farPlane=60610.2, width=11190.9, height=7387.91, viewOffsetX=3019.83, 
    viewOffsetY=7752.84)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41962.8, 
    farPlane=65360, width=12404.6, height=8189.21, cameraPosition=(55181.1, 
    19293.9, -10007.5), cameraUpVector=(-0.75173, 0.59801, -0.278004), 
    cameraTarget=(13312, 2726.54, 8977.78), viewOffsetX=3347.36, 
    viewOffsetY=8593.72)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48973.2, 
    farPlane=71393.8, width=14477, height=9557.32, cameraPosition=(448.038, 
    4500.02, -52212.6), cameraUpVector=(-0.290167, 0.820565, 0.492418), 
    cameraTarget=(10212.8, -755.794, -4621), viewOffsetX=3906.58, 
    viewOffsetY=10029.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50046.9, 
    farPlane=76048, width=14794.4, height=9766.89, cameraPosition=(-33817.5, 
    18262.3, -38542.2), cameraUpVector=(0.281753, 0.738564, 0.612486), 
    cameraTarget=(-1277.68, 1190.05, -6329.87), viewOffsetX=3992.23, 
    viewOffsetY=10249.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50003.1, 
    farPlane=76091.8, width=14781.5, height=9758.35, viewOffsetX=-148.165, 
    viewOffsetY=7725.13)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51029.4, 
    farPlane=75065.6, width=5605.15, height=3700.38, viewOffsetX=-982.957, 
    viewOffsetY=7735.17)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#221010 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-2')
#: ???? 'Surf-2' ?????? (4 ??).
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'beam-4-1', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 
    'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 
    'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 
    'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 
    'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 
    'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 
    'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 
    'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 
    'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 
    'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 
    'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 
    'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 
    'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 
    'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 
    'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 
    'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 
    'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 
    'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 
    'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 
    'zbeam-2-4-2-rebar-4-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 
    'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 
    'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 
    'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 
    'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 
    'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 
    'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 
    'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    'xbeam-2-3-4-rebar-5-6', ))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=40807.9, 
    farPlane=70495.7, width=23402.4, height=15449.7, viewOffsetX=3904.6, 
    viewOffsetY=2495.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42348.2, 
    farPlane=68955.5, width=11558.1, height=7630.37, viewOffsetX=3254.08, 
    viewOffsetY=3827.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42272.2, 
    farPlane=69031.4, width=11537.4, height=7616.68, viewOffsetX=4924.83, 
    viewOffsetY=2739.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44652.2, 
    farPlane=67404.5, width=12187, height=8045.53, cameraPosition=(26198.9, 
    49338.2, 32259.9), cameraUpVector=(-0.585528, 0.262387, -0.767014), 
    cameraTarget=(6958.07, 3574.99, 7107.55), viewOffsetX=5202.11, 
    viewOffsetY=2894.11)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44579, 
    farPlane=67477.6, width=12167, height=8032.35, viewOffsetX=3805.31, 
    viewOffsetY=3256.26)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45382.8, 
    farPlane=66673.9, width=5586.68, height=3688.18, viewOffsetX=563.628, 
    viewOffsetY=3149.26)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45344.8, 
    farPlane=66711.8, width=5582, height=3685.09, viewOffsetX=2401.79, 
    viewOffsetY=4517.27)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=3849.87, 
    viewOffsetY=4956.12)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 
    'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 
    'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6'), vector=(4500.0, 0.0, 
    -6550.0))
#: The instances were translated by 4.5E+03, 0., -6.55E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=5604.39, 
    viewOffsetY=4445.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45324.1, 
    farPlane=67659.1, width=6122.58, height=4041.97, viewOffsetX=5620.64, 
    viewOffsetY=4461.32)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45282.6, 
    farPlane=67700.5, width=6116.98, height=4038.27, viewOffsetX=5569.4, 
    viewOffsetY=3818.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45797.9, 
    farPlane=67185.3, width=1585.86, height=1046.94, viewOffsetX=5048.98, 
    viewOffsetY=4482.54)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('col-2-3-1', 'col-2-3-1-rebar-2-1', 
    'col-2-3-1-rebar-2-2', 'col-2-3-1-rebar-2-3', 'col-2-3-1-rebar-2-4', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-4', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 
    'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 
    'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6'), vector=(0.0, 0.0, 
    -50.0))
#: The instances were translated by 0., 0., -50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45604.6, 
    farPlane=67401.2, width=3558.86, height=2349.47, viewOffsetX=5248.44, 
    viewOffsetY=4404.77)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45580.4, 
    farPlane=67425.4, width=3556.97, height=2348.22, viewOffsetX=5444.75, 
    viewOffsetY=3958.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46945.3, 
    farPlane=67682.6, width=3663.48, height=2418.54, cameraPosition=(30447.6, 
    51274.5, 26738.9), cameraUpVector=(-0.559012, 0.220205, -0.799385), 
    cameraTarget=(6785.35, 4813.52, 7281.35), viewOffsetX=5607.79, 
    viewOffsetY=4076.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47255.6, 
    farPlane=67372.2, width=835.266, height=551.421, viewOffsetX=5146.17, 
    viewOffsetY=4340.19)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 
    'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-5'), vector=(50.0, 0.0, 0.0))
#: The instances were translated by 50., 0., 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46900.3, 
    farPlane=67727.6, width=4193.16, height=2768.22, viewOffsetX=5739.38, 
    viewOffsetY=4157.19)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46871.6, 
    farPlane=67756.3, width=4190.59, height=2766.52, viewOffsetX=5839.62, 
    viewOffsetY=3915.45)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46898, 
    farPlane=67230.3, width=4192.95, height=2768.08, cameraPosition=(25687.3, 
    52790.7, 27323.9), cameraUpVector=(-0.524544, 0.175797, -0.833036), 
    cameraTarget=(6314.19, 4697.15, 7104.81), viewOffsetX=5842.91, 
    viewOffsetY=3917.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46897.7, 
    width=4192.93, height=2768.06, viewOffsetX=5842.87, viewOffsetY=3967.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46653.6, 
    farPlane=67786, width=4171.1, height=2753.66, cameraPosition=(30376.7, 
    50856.2, 27470.1), cameraUpVector=(-0.559411, 0.232265, -0.795683), 
    cameraTarget=(6766.91, 4683.34, 7276.89), viewOffsetX=5812.46, 
    viewOffsetY=3946.65)


session.viewports['Viewport: 1'].view.setValues(nearPlane=46936.1, 
    farPlane=67503.5, width=1658.79, height=1095.09, viewOffsetX=5380.62, 
    viewOffsetY=4027.76)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-3-1'].vertices
e1 = a.instances['xbeam-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[6], normal=e1[7], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46980.9, 
    farPlane=67458.7, width=1296.34, height=855.807, viewOffsetX=5338.12, 
    viewOffsetY=4187.31)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['xbeam-2-3-1'].vertices
e11 = a.instances['col-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[4], normal=e11[18], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46922.9, 
    farPlane=67516.7, width=1996.58, height=1318.09, viewOffsetX=5458.47, 
    viewOffsetY=4032.22)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-3-1'].vertices
e1 = a.instances['xbeam-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[4], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v11 = a.instances['zbeam-2-3-1'].vertices
e11 = a.instances['zbeam-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e11[6], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46909.1, 
    farPlane=67530.5, width=1995.99, height=1317.7, viewOffsetX=5510.58, 
    viewOffsetY=4372.82)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['zbeam-2-2-1'].vertices
e1 = a.instances['zbeam-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[4], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-2-1'].vertices
e11 = a.instances['zbeam-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46228.2, 
    farPlane=68211.4, width=8331.69, height=5500.37, viewOffsetX=7112.82, 
    viewOffsetY=4292.21)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46173.4, 
    farPlane=68266.2, width=8321.81, height=5493.84, viewOffsetX=6629.62, 
    viewOffsetY=3605.99)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(31609.5, 
    50043.8, 27886.3), cameraUpVector=(-0.675482, 0.24742, -0.694628), 
    cameraTarget=(7999.75, 3870.92, 7693.11))
session.viewports['Viewport: 1'].view.setValues(nearPlane=46017.5, 
    farPlane=69248.2, width=8293.72, height=5475.3, cameraPosition=(39670.2, 
    45375, 27865.4), cameraUpVector=(-0.715391, 0.366062, -0.595159), 
    cameraTarget=(8943.69, 3501.55, 7875.15), viewOffsetX=6607.24, 
    viewOffsetY=3593.82)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    'beam-4-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=45755, 
    farPlane=67301.5, width=11236.4, height=7417.95, viewOffsetX=7066.8, 
    viewOffsetY=3198.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48442.7, 
    farPlane=69570.4, width=11896.4, height=7853.7, cameraPosition=(55672.2, 
    35189.9, 19180), cameraUpVector=(-0.723945, 0.569185, -0.389785), 
    cameraTarget=(11135.4, 3656.81, 8259.76), viewOffsetX=7481.92, 
    viewOffsetY=3386.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55123.6, 
    farPlane=79698.7, width=13537.1, height=8936.83, cameraPosition=(62012.5, 
    9684.82, -30513.5), cameraUpVector=(-0.542321, 0.840039, 0.0149173), 
    cameraTarget=(18508.6, 3077.05, 3557.86), viewOffsetX=8513.78, 
    viewOffsetY=3853.03)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59128.2, 
    farPlane=83436.7, width=14520.5, height=9586.08, cameraPosition=(38133, 
    10325.6, -55802.4), cameraUpVector=(-0.519028, 0.816256, 0.253646), 
    cameraTarget=(17210.2, 3850.19, -4641.72), viewOffsetX=9132.28, 
    viewOffsetY=4132.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65939.4, 
    farPlane=90752.4, width=16193.2, height=10690.3, cameraPosition=(-45203.5, 
    1568.32, -51146.2), cameraUpVector=(0.08659, 0.899947, 0.427314), 
    cameraTarget=(-3612.28, 627.88, -14181.4), viewOffsetX=10184.3, 
    viewOffsetY=4609.03)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65747.1, 
    farPlane=90944.7, width=16146, height=10659.2, viewOffsetX=5062.27, 
    viewOffsetY=4925.97)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65358.2, 
    farPlane=91094.8, width=16050.5, height=10596.1, cameraPosition=(-49973.1, 
    18478.2, -44406.8), cameraUpVector=(0.247103, 0.790855, 0.5599), 
    cameraTarget=(-5781.21, 5897.24, -13007.7), viewOffsetX=5032.32, 
    viewOffsetY=4896.83)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65443.5, 
    farPlane=91465.2, width=16071.4, height=10610, cameraPosition=(-43253.8, 
    33547.7, -45211.6), cameraUpVector=(0.233695, 0.633053, 0.737991), 
    cameraTarget=(-3504.79, 11083.4, -13392.1), viewOffsetX=5038.89, 
    viewOffsetY=4903.22)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66685.7, 
    farPlane=90223, width=5054.2, height=3336.65, viewOffsetX=2051.55, 
    viewOffsetY=4326.91)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4420800 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-3')
#: ???? 'Surf-3' ?????? (4 ??).
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'beam-4-1', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 
    'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 
    'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 
    'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 
    'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 
    'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 
    'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 
    'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 
    'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 
    'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 
    'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 
    'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 
    'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 
    'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 
    'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 
    'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 
    'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 
    'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 
    'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 
    'zbeam-2-4-2-rebar-4-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 
    'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 
    'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 
    'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 
    'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 
    'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 
    'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 
    'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    'xbeam-2-3-4-rebar-5-6', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=62117, 
    farPlane=91275.3, width=15317, height=10111.9, viewOffsetX=4360.57, 
    viewOffsetY=4207.57)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62015.8, 
    farPlane=91376.6, width=15292, height=10095.4, viewOffsetX=7036.56, 
    viewOffsetY=4316)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61109.7, 
    farPlane=91651.1, width=15068.6, height=9947.9, cameraPosition=(-36338.5, 
    27392.5, -53740.6), cameraUpVector=(0.205709, 0.728381, 0.653563), 
    cameraTarget=(-1133.23, 8262.41, -15117.6), viewOffsetX=6933.75, 
    viewOffsetY=4252.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62612.2, 
    farPlane=90551.9, width=15439.1, height=10192.5, cameraPosition=(-36884.9, 
    47740, -40337.9), cameraUpVector=(0.379435, 0.49773, 0.779932), 
    cameraTarget=(-2101.77, 14557.8, -12298.9), viewOffsetX=7104.23, 
    viewOffsetY=4357.51)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62584.4, 
    farPlane=90008.9, width=15432.3, height=10188, cameraPosition=(-27046.3, 
    53768.9, -42029.8), cameraUpVector=(0.454001, 0.435703, 0.777204), 
    cameraTarget=(444.214, 15312.8, -12661.3), viewOffsetX=7101.08, 
    viewOffsetY=4355.58)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62584, 
    farPlane=90009.3, width=15432.2, height=10187.9, viewOffsetX=10240.6, 
    viewOffsetY=7446.84)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62677.9, 
    farPlane=89915.4, width=15508.8, height=10238.5, viewOffsetX=10015.8, 
    viewOffsetY=6101.15)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62578.1, 
    farPlane=90015.3, width=15484, height=10222.2, viewOffsetX=13050, 
    viewOffsetY=8359.32)
session.viewports['Viewport: 1'].view.setValues(nearPlane=64203, 
    farPlane=88390.4, width=1422.35, height=938.996, viewOffsetX=14891.6, 
    viewOffsetY=10534.5)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6'), vector=(-4550.0, 0.0, 
    6600.0))
#: The instances were translated by -4.55E+03, 0., 6.6E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63740.4, 
    farPlane=92098.4, width=5837.04, height=3853.46, viewOffsetX=15282.1, 
    viewOffsetY=10213.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63700.5, 
    farPlane=92138.4, width=5833.38, height=3851.05, viewOffsetX=14431.1, 
    viewOffsetY=9641.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63337.6, 
    farPlane=92501.2, width=9515.18, height=6281.67, viewOffsetX=15048.7, 
    viewOffsetY=9339.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63273.4, 
    farPlane=92565.5, width=9505.53, height=6275.3, viewOffsetX=13549.8, 
    viewOffsetY=10179.8)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=10408.6, 
    viewOffsetY=11868.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62945.1, 
    farPlane=92893.7, width=13097, height=8646.28, viewOffsetX=11593.5, 
    viewOffsetY=11868.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62857.8, 
    farPlane=92981, width=13078.8, height=8634.28, viewOffsetX=14350.8, 
    viewOffsetY=10443.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=64005.9, 
    farPlane=91833, width=3016.46, height=1991.39, viewOffsetX=14911.2, 
    viewOffsetY=10570)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6'), vector=(-9000.0, 0.0, 
    -50.0))
#: The instances were translated by -9.E+03, 0., -50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62225.8, 
    farPlane=91612.4, width=1233.21, height=814.135, viewOffsetX=14314.1, 
    viewOffsetY=10319.7)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6'), vector=(0.0, 0.0, 
    -50.0))
#: The instances were translated by 0., 0., -50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61813.1, 
    farPlane=92025.2, width=5167.72, height=3411.6, viewOffsetX=14582.4, 
    viewOffsetY=10274.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62536.5, 
    farPlane=92409.8, width=5228.2, height=3451.53, cameraPosition=(-30981.2, 
    54395.9, -39529.5), cameraUpVector=(0.475487, 0.429494, 0.767754), 
    cameraTarget=(-1116.03, 16055.4, -12415.3), viewOffsetX=14753.1, 
    viewOffsetY=10394.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62880.2, 
    farPlane=92066.1, width=2078.03, height=1371.86, viewOffsetX=14613.3, 
    viewOffsetY=10295.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62895.5, 
    farPlane=92050.9, width=2078.53, height=1372.19, viewOffsetX=14773.4, 
    viewOffsetY=10273.2)


session.viewports['Viewport: 1'].view.setValues(nearPlane=62970.3, 
    farPlane=91976, width=1349.48, height=890.894, viewOffsetX=14718.3, 
    viewOffsetY=10153.6)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-2-4'].vertices
e1 = a.instances['xbeam-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[3], normal=e1[2], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['xbeam-2-2-4'].vertices
e11 = a.instances['xbeam-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e11[6], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v1 = a.instances['xbeam-2-2-4'].vertices
e1 = a.instances['xbeam-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[6], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['zbeam-2-1-3'].vertices
e11 = a.instances['zbeam-2-1-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[4], normal=e11[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v1 = a.instances['zbeam-2-2-3'].vertices
e1 = a.instances['zbeam-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[6], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62353.7, 
    farPlane=92592.6, width=7161.24, height=4727.66, viewOffsetX=14755.9, 
    viewOffsetY=9602.44)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62304.9, 
    farPlane=92641.4, width=7155.64, height=4723.97, viewOffsetX=16138.6, 
    viewOffsetY=9710.53)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62007.4, 
    farPlane=92938.9, width=10322.9, height=6814.93, viewOffsetX=16669.8, 
    viewOffsetY=9476.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61937.9, 
    farPlane=93008.4, width=10311.4, height=6807.29, viewOffsetX=15752, 
    viewOffsetY=8988.13)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62561, 
    farPlane=92385.3, width=4659.37, height=3076, viewOffsetX=15183.6, 
    viewOffsetY=9691.46)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62595, 
    farPlane=92351.3, width=4661.9, height=3077.67, viewOffsetX=15196.8, 
    viewOffsetY=9832.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61685.3, 
    farPlane=93261, width=13261.1, height=8754.62, viewOffsetX=17651.1, 
    viewOffsetY=9555.29)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61597.1, 
    farPlane=93349.2, width=13242.1, height=8742.09, viewOffsetX=14219.1, 
    viewOffsetY=6931.83)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62244.6, 
    farPlane=92701.7, width=8156.83, height=5384.93, viewOffsetX=13396.4, 
    viewOffsetY=7070.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62189.3, 
    farPlane=92757, width=8149.58, height=5380.15, viewOffsetX=11454.5, 
    viewOffsetY=6028.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62189.3, 
    width=8149.59, height=5380.15, viewOffsetX=10936.9, viewOffsetY=6669.46)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=9208.73, 
    viewOffsetY=7678.79)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=8340.26, 
    viewOffsetY=8284.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62164.8, 
    farPlane=92781.6, width=8886.39, height=5866.57, viewOffsetX=8299.2, 
    viewOffsetY=8271.06)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62104.6, 
    farPlane=92841.7, width=8877.8, height=5860.9, viewOffsetX=11951.2, 
    viewOffsetY=6188.33)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62671.3, 
    farPlane=92275, width=3767.39, height=2487.13, viewOffsetX=11956.2, 
    viewOffsetY=6719.8)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 
    'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 
    'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6'), vector=(-9000.0, 0.0, 
    0.0))
#: The instances were translated by -9.E+03, 0., 0. (????????????????)


session.viewports['Viewport: 1'].view.setValues(nearPlane=62952.2, 
    farPlane=91994.2, width=1495.89, height=987.549, viewOffsetX=11916.7, 
    viewOffsetY=6715.27)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-2-3'].vertices
e11 = a.instances['xbeam-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[3], normal=e11[2], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63024.3, 
    farPlane=91922, width=912.895, height=602.669, viewOffsetX=11876.2, 
    viewOffsetY=6919.42)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['xbeam-2-2-3'].vertices
e1 = a.instances['col-2-1-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[2], normal=e1[13], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62983.4, 
    farPlane=91962.9, width=1406.84, height=928.757, viewOffsetX=11923, 
    viewOffsetY=6883.41)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v11 = a.instances['xbeam-2-2-3'].vertices
e11 = a.instances['col-2-1-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[5], normal=e11[9], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62020.9, 
    farPlane=92925.4, width=10199, height=6733.11, viewOffsetX=13348.1, 
    viewOffsetY=6344.97)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61952.3, 
    farPlane=92994, width=10187.7, height=6725.66, viewOffsetX=12510.8, 
    viewOffsetY=7709.41)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61383.1, 
    farPlane=93563.2, width=16017.1, height=10574.1, viewOffsetX=14026, 
    viewOffsetY=5915.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61277.5, 
    farPlane=93668.8, width=15989.6, height=10555.9, viewOffsetX=11592.2, 
    viewOffsetY=5750.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62056.9, 
    farPlane=92889.4, width=9870.74, height=6516.41, viewOffsetX=11299.3, 
    viewOffsetY=5664.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61990.4, 
    farPlane=92955.9, width=9860.16, height=6509.42, viewOffsetX=12337.9, 
    viewOffsetY=4628.79)
session.viewports['Viewport: 1'].view.setValues(nearPlane=64322.7, 
    farPlane=91148.5, width=10231.1, height=6754.33, cameraPosition=(-28955.2, 
    65789.7, -25830.5), cameraUpVector=(0.390546, 0.207998, 0.896778), 
    cameraTarget=(223.241, 22007.3, -7697.09), viewOffsetX=12802.1, 
    viewOffsetY=4802.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=64817.9, 
    farPlane=90653.2, width=5955.95, height=3931.97, viewOffsetX=12765.2, 
    viewOffsetY=5910.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=64777.2, 
    farPlane=90693.9, width=5952.21, height=3929.5, viewOffsetX=12430.4, 
    viewOffsetY=4790.98)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65158.1, 
    farPlane=90313.1, width=2517.76, height=1662.16, viewOffsetX=11581.3, 
    viewOffsetY=4519.6)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 
    'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 
    'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6'), vector=(0.0, 0.0, 
    -2700.0))
#: The instances were translated by 0., 0., -2.7E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=64771.1, 
    farPlane=90700, width=6383.46, height=4214.2, viewOffsetX=12508.5, 
    viewOffsetY=4667.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61983.7, 
    farPlane=87703.1, width=6108.75, height=4032.84, cameraPosition=(13322.3, 
    57787.1, -44199.9), cameraUpVector=(0.109228, 0.337888, 0.934827), 
    cameraTarget=(14586.2, 14744.3, -8946.25), viewOffsetX=11970.2, 
    viewOffsetY=4466.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62014.8, 
    farPlane=87672, width=6111.82, height=4034.86, viewOffsetX=14778.8, 
    viewOffsetY=4238.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59688.2, 
    farPlane=87180.3, width=5882.52, height=3883.49, cameraPosition=(29011.1, 
    57251.4, -37412.9), cameraUpVector=(-0.0899802, 0.315166, 0.944761), 
    cameraTarget=(18997.9, 13725.5, -4211.59), viewOffsetX=14224.3, 
    viewOffsetY=4079.26)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60276.8, 
    farPlane=86591.5, width=987.492, height=651.917, viewOffsetX=13924.5, 
    viewOffsetY=4648.92)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-1', 
    'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 
    'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6'), 
    vector=(75.0, 0.0, 0.0))
#: The instances were translated by 75., 0., 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59738.9, 
    farPlane=87129.4, width=6033.52, height=3983.18, viewOffsetX=14586.5, 
    viewOffsetY=4528.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65093.3, 
    farPlane=90077.5, width=6574.3, height=4340.19, cameraPosition=(-16770.4, 
    68813.7, -30468.6), cameraUpVector=(0.403234, 0.17546, 0.898118), 
    cameraTarget=(5064.54, 21715.7, -10415.9), viewOffsetX=15893.9, 
    viewOffsetY=4934.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65428.9, 
    farPlane=89741.9, width=2956.28, height=1951.66, viewOffsetX=14658.5, 
    viewOffsetY=5025.72)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65450.6, 
    farPlane=89720.2, width=2957.26, height=1952.31, viewOffsetX=14227.2, 
    viewOffsetY=5059.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65450.6, 
    width=2957.27, height=1952.31, cameraPosition=(-17275.4, 68352.5, -31002), 
    cameraUpVector=(0.442796, 0.184954, 0.877339), cameraTarget=(4559.51, 
    21254.5, -10949.3), viewOffsetX=14227.2, viewOffsetY=5059.23)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-2-3'].vertices
e1 = a.instances['xbeam-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[3], normal=e1[2], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65571.2, 
    farPlane=89599.7, width=1809.87, height=1192.26, viewOffsetX=14019.4, 
    viewOffsetY=5121.5)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['xbeam-2-2-3'].vertices
e11 = a.instances['col-2-1-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e11[13], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v1 = a.instances['xbeam-2-2-3'].vertices
e1 = a.instances['col-2-1-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[9], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=55571.4, 
    farPlane=93842.4, width=29771.1, height=19611.9, viewOffsetX=7738.57, 
    viewOffsetY=831.826)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56758.2, 
    farPlane=92655.7, width=21584.9, height=14219.2, viewOffsetX=4106.97, 
    viewOffsetY=2804.01)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56619.7, 
    farPlane=92794.2, width=21532.3, height=14184.5, viewOffsetX=2547.37, 
    viewOffsetY=1431.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56619.4, 
    farPlane=92794.4, width=21532.2, height=14184.5, viewOffsetX=1529.72, 
    viewOffsetY=1478.21)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56619.4, 
    farPlane=92794.5, width=21532.3, height=14184.5, viewOffsetX=1437.21, 
    viewOffsetY=876.584)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=2015.41, 
    viewOffsetY=645.189)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=8606.93, 
    viewOffsetY=506.351)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57903.7, 
    farPlane=91510.1, width=9851.31, height=6489.61, viewOffsetX=7907.86, 
    viewOffsetY=1980.83)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57973.7, 
    farPlane=91440.2, width=9863.22, height=6497.45, viewOffsetX=7546.62, 
    viewOffsetY=1686.44)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=7938.61, 
    viewOffsetY=2152.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58821.5, 
    farPlane=90592.4, width=2406.06, height=1585.01, viewOffsetX=6959.76, 
    viewOffsetY=1264.68)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 
    'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 
    'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6'), vector=(4500.0, 0.0, 
    6650.0))
#: The instances were translated by 4.5E+03, 0., 6.65E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55545, 
    farPlane=91530.6, width=11307.3, height=7448.76, viewOffsetX=7062.18, 
    viewOffsetY=1140.83)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55469.7, 
    farPlane=91605.9, width=11292, height=7438.66, viewOffsetX=8677.87, 
    viewOffsetY=-195.546)
session.viewports['Viewport: 1'].view.setValues(nearPlane=54888, 
    farPlane=89708, width=11173.6, height=7360.67, cameraPosition=(37347.4, 
    51024, 53587.5), cameraUpVector=(-0.497402, 0.497849, -0.710449), 
    cameraTarget=(4106.29, 2341.49, 7694.48), viewOffsetX=8586.87, 
    viewOffsetY=-193.495)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56004.3, 
    farPlane=88591.7, width=1574.09, height=1036.94, viewOffsetX=7196.78, 
    viewOffsetY=97.2698)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-3-1'].vertices
e11 = a.instances['xbeam-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56087.1, 
    farPlane=88508.9, width=903.277, height=595.039, viewOffsetX=7154.53, 
    viewOffsetY=261.407)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['xbeam-2-3-1'].vertices
e1 = a.instances['col-2-4-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[18], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56121.3, 
    farPlane=88474.7, width=626.074, height=412.43, viewOffsetX=7154.38, 
    viewOffsetY=386.723)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-3-1'].vertices
e11 = a.instances['col-2-4-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[9], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56023.9, 
    farPlane=88572.1, width=1600.56, height=1054.38, viewOffsetX=7298.63, 
    viewOffsetY=207.212)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56012.8, 
    farPlane=88583.1, width=1600.25, height=1054.17, viewOffsetX=7231.87, 
    viewOffsetY=336.148)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56078, 
    farPlane=88518, width=976.598, height=643.34, viewOffsetX=7038.59, 
    viewOffsetY=386.619)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v1 = a.instances['zbeam-2-4-2'].vertices
e1 = a.instances['col-2-4-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[2], normal=e1[17], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['zbeam-2-4-1'].vertices
e11 = a.instances['col-2-4-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[19], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55781.5, 
    farPlane=88814.4, width=3820.74, height=2516.93, viewOffsetX=7398.35, 
    viewOffsetY=498.082)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55755.3, 
    farPlane=88840.6, width=3818.94, height=2515.75, viewOffsetX=7907.62, 
    viewOffsetY=452.704)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=7657.4, 
    viewOffsetY=149.008)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    'beam-4-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=60539.6, 
    farPlane=84056.4, width=11343.4, height=7472.53, viewOffsetX=9586.08, 
    viewOffsetY=-58.6231)
session.viewports['Viewport: 1'].view.setValues(nearPlane=69331.6, 
    farPlane=90417.8, width=12990.8, height=8557.74, cameraPosition=(77948.5, 
    40245.5, 605.322), cameraUpVector=(-0.755997, 0.650833, -0.0698945), 
    cameraTarget=(13458.8, 5053.29, 14159.9), viewOffsetX=10978.2, 
    viewOffsetY=-67.1368)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72173.5, 
    farPlane=96970, width=13523.3, height=8908.56, cameraPosition=(63795.7, 
    8634.39, -54987.3), cameraUpVector=(-0.50754, 0.856054, 0.0978504), 
    cameraTarget=(20259.2, 4985.2, 5612.96), viewOffsetX=11428.2, 
    viewOffsetY=-69.8888)
session.viewports['Viewport: 1'].view.setValues(nearPlane=74933, 
    farPlane=95933.3, width=14040.4, height=9249.18, cameraPosition=(17937.3, 
    24928.2, -74441.8), cameraUpVector=(-0.405954, 0.751778, 0.519645), 
    cameraTarget=(16835.1, 7285.07, -1856.4), viewOffsetX=11865.2, 
    viewOffsetY=-72.561)
session.viewports['Viewport: 1'].view.setValues(nearPlane=74883.5, 
    farPlane=100217, width=14031.1, height=9243.09, cameraPosition=(-49602, 
    18891.6, -57542.6), cameraUpVector=(-0.294037, 0.472474, 0.830849), 
    cameraTarget=(2844.47, 11570.3, -4846.24), viewOffsetX=11857.4, 
    viewOffsetY=-72.5131)
session.viewports['Viewport: 1'].view.setValues(nearPlane=74574.8, 
    farPlane=91253, width=13973.3, height=9204.99, cameraPosition=(828.947, 
    84241, -13856.5), cameraUpVector=(0.270861, -0.0722632, 0.959902), 
    cameraTarget=(16385.9, 12987.6, 2332.27), viewOffsetX=11808.5, 
    viewOffsetY=-72.2142)
session.viewports['Viewport: 1'].view.setValues(nearPlane=74581.4, 
    farPlane=91246.5, width=13974.5, height=9205.81, viewOffsetX=7066.31, 
    viewOffsetY=2075.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=75781, 
    farPlane=90046.9, width=3421.43, height=2253.89, viewOffsetX=5160.63, 
    viewOffsetY=1917.33)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-4-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4221000 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-4')
#: ???? 'Surf-4' ?????? (4 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=75662.8, 
    farPlane=90165, width=4951.8, height=3262.03, viewOffsetX=5365.7, 
    viewOffsetY=1821.86)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'beam-4-1', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 
    'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 
    'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 
    'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 
    'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 
    'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 
    'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 
    'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 
    'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 
    'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 
    'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 
    'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 
    'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 
    'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 
    'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 
    'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 
    'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 
    'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 
    'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 
    'zbeam-2-4-2-rebar-4-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 
    'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 
    'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 
    'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 
    'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 
    'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 
    'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 
    'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    'xbeam-2-3-4-rebar-5-6', ))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=58883.5, 
    farPlane=99934.9, width=31648.6, height=20848.7, viewOffsetX=5099.13, 
    viewOffsetY=-476.153)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58972.5, 
    farPlane=99845.9, width=31696.4, height=20880.2, viewOffsetX=3847.15, 
    viewOffsetY=-681.247)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61779.5, 
    farPlane=97038.9, width=7069.71, height=4657.21, viewOffsetX=-814.785, 
    viewOffsetY=150.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61830.4, 
    farPlane=96988, width=7075.53, height=4661.05, viewOffsetX=-2046.64, 
    viewOffsetY=-160.665)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59941.2, 
    farPlane=98877.1, width=24778.8, height=16323.2, viewOffsetX=-473.173, 
    viewOffsetY=-1436.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59783.7, 
    farPlane=99034.7, width=24713.7, height=16280.3, viewOffsetX=350.975, 
    viewOffsetY=4516.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60727.5, 
    farPlane=98090.8, width=17603.5, height=11596.4, viewOffsetX=1574.23, 
    viewOffsetY=6394.28)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60612.5, 
    farPlane=98205.9, width=17570.2, height=11574.5, viewOffsetX=325.666, 
    viewOffsetY=5419.21)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62082.3, 
    farPlane=96736, width=4613.14, height=3038.93, viewOffsetX=711.906, 
    viewOffsetY=7019.04)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62115.9, 
    farPlane=96702.5, width=4615.63, height=3040.58, viewOffsetX=-566.799, 
    viewOffsetY=6333.37)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62115.9, 
    viewOffsetX=-462.687, viewOffsetY=5792.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59516.8, 
    farPlane=99301.6, width=28651.8, height=18874.5, viewOffsetX=2477.54, 
    viewOffsetY=5224.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59336.9, 
    farPlane=99481.5, width=28565.2, height=18817.5, viewOffsetX=3206.43, 
    viewOffsetY=2722.57)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60005.8, 
    farPlane=98812.6, width=24190, height=15935.3, viewOffsetX=7585.55, 
    viewOffsetY=2137.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59851.6, 
    farPlane=98966.7, width=24127.8, height=15894.4, viewOffsetX=5855.61, 
    viewOffsetY=5477.26)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61349.3, 
    farPlane=97469.1, width=11922.2, height=7853.84, viewOffsetX=3253.95, 
    viewOffsetY=6661.33)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61269.7, 
    farPlane=97548.6, width=11906.8, height=7843.65, viewOffsetX=858.145, 
    viewOffsetY=5795.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61632.4, 
    farPlane=97185.9, width=8262.77, height=5443.15, viewOffsetX=-175.174, 
    viewOffsetY=5903.56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61691.7, 
    farPlane=97126.7, width=8270.71, height=5448.38, viewOffsetX=-3826.54, 
    viewOffsetY=4558.25)
session.viewports['Viewport: 1'].view.setValues(farPlane=97126.7, 
    viewOffsetX=-4865.93, viewOffsetY=4033.85)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-3231.33, 
    viewOffsetY=4176.06)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60245.4, 
    farPlane=98573, width=22004.6, height=14495.7, viewOffsetX=-978.892, 
    viewOffsetY=4355.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60104, 
    farPlane=98714.4, width=21952.9, height=14461.6, viewOffsetX=4211, 
    viewOffsetY=4108.91)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61609.7, 
    farPlane=97208.6, width=9540.56, height=6284.9, viewOffsetX=2475.84, 
    viewOffsetY=6359.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61545.5, 
    farPlane=97272.9, width=9530.61, height=6278.35, viewOffsetX=3312.69, 
    viewOffsetY=6261.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61663.4, 
    farPlane=97155, width=9049.53, height=5961.43, viewOffsetX=4792.43, 
    viewOffsetY=5922.48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61602.3, 
    farPlane=97216, width=9040.57, height=5955.53, viewOffsetX=3272.83, 
    viewOffsetY=7607.09)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62206.2, 
    farPlane=96612.1, width=3608.7, height=2377.25, viewOffsetX=1878.51, 
    viewOffsetY=7778.49)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6'), vector=(-9000.0, 0.0, 
    50.0))
#: The instances were translated by -9.E+03, 0., 50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61923.4, 
    farPlane=96894.9, width=6669.5, height=4393.57, viewOffsetX=2038.39, 
    viewOffsetY=7721.24)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61878.1, 
    farPlane=96940.3, width=6664.61, height=4390.35, viewOffsetX=1807.82, 
    viewOffsetY=6899.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62284.3, 
    farPlane=96918.4, width=6708.35, height=4419.17, cameraPosition=(49597, 
    50642.8, 56262.8), cameraUpVector=(-0.559341, 0.546114, -0.623616), 
    cameraTarget=(7328.82, 2381.1, 9465.04), viewOffsetX=1819.69, 
    viewOffsetY=6944.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62843.6, 
    farPlane=96359, width=1735.05, height=1142.97, viewOffsetX=1093.34, 
    viewOffsetY=7759.14)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6'), 
    vector=(0.0, 0.0, 50.0))
#: The instances were translated by 0., 0., 50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62043, 
    farPlane=97159.7, width=9293, height=6121.82, viewOffsetX=2534.61, 
    viewOffsetY=7385.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61980.3, 
    farPlane=97222.3, width=9283.62, height=6115.64, viewOffsetX=2053.41, 
    viewOffsetY=7088.72)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62990.1, 
    farPlane=96212.5, width=547.795, height=360.863, viewOffsetX=772.559, 
    viewOffsetY=7906.92)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6'), vector=(25.0, 0.0, 0.0))
#: The instances were translated by 25., 0., 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61674.5, 
    farPlane=97528.1, width=12662.5, height=8341.48, viewOffsetX=2951.11, 
    viewOffsetY=7318.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61590.2, 
    farPlane=97612.4, width=12645.2, height=8330.07, viewOffsetX=3762.01, 
    viewOffsetY=6275.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62128.4, 
    farPlane=97074.3, width=8511.59, height=5607.06, viewOffsetX=6140.32, 
    viewOffsetY=6054.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62070.8, 
    farPlane=97131.8, width=8503.71, height=5601.87, viewOffsetX=3147.83, 
    viewOffsetY=7785.06)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62901.5, 
    farPlane=96301.1, width=1265.74, height=833.817, viewOffsetX=1033.14, 
    viewOffsetY=8125.65)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 
    'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 
    'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6'), vector=(-9100.0, 0.0, 
    -400.0))
#: The instances were translated by -9.1E+03, 0., -400. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61969.2, 
    farPlane=97233.5, width=9967.78, height=6566.34, viewOffsetX=2263.79, 
    viewOffsetY=8089.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61902.2, 
    farPlane=97300.5, width=9957, height=6559.24, viewOffsetX=2154.39, 
    viewOffsetY=6914.64)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=528.755, 
    viewOffsetY=5951.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62917.4, 
    farPlane=97123.8, width=10120.3, height=6666.81, cameraPosition=(45690.3, 
    55468.4, 55314.7), cameraUpVector=(-0.480156, 0.479616, -0.734452), 
    cameraTarget=(6750.02, 2844.9, 10367.6), viewOffsetX=537.427, 
    viewOffsetY=6049.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62898.8, 
    farPlane=97142.3, width=10117.3, height=6664.83, viewOffsetX=3340.99, 
    viewOffsetY=3742.47)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=6916.27, 
    viewOffsetY=4525.28)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=7437.89, 
    viewOffsetY=4405.68)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=8557.2, 
    viewOffsetY=4742.73)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=8633.27, 
    viewOffsetY=5112.39)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=8426.79, 
    viewOffsetY=4666.62)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=6242.5, 
    viewOffsetY=4025.14)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=5394.86, 
    viewOffsetY=3742.46)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62873.7, 
    farPlane=97167.4, width=10980.7, height=7233.58, viewOffsetX=5187.1, 
    viewOffsetY=3771.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62800.1, 
    farPlane=97241, width=10967.8, height=7225.11, viewOffsetX=8997.97, 
    viewOffsetY=4980.61)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63563.9, 
    farPlane=96477.1, width=4124.92, height=2717.32, viewOffsetX=8846.01, 
    viewOffsetY=5319.18)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-3-2', 
    'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 
    'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6'), 
    vector=(4500.0, 0.0, -6600.0))
#: The instances were translated by 4.5E+03, 0., -6.6E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63546.6, 
    farPlane=96494.4, width=4822, height=3176.52, viewOffsetX=7193.41, 
    viewOffsetY=6329.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63513.6, 
    farPlane=96527.5, width=4819.49, height=3174.87, viewOffsetX=9400.11, 
    viewOffsetY=5771.76)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=10782.3, 
    viewOffsetY=5326.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63312.7, 
    farPlane=97322.2, width=6963.99, height=4587.57, viewOffsetX=11329.3, 
    viewOffsetY=5227.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63265.3, 
    farPlane=96775.7, width=6958.79, height=4584.14, viewOffsetX=8712.22, 
    viewOffsetY=7107.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63915, 
    farPlane=96126.1, width=1280.01, height=843.214, viewOffsetX=8971.05, 
    viewOffsetY=5870.06)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 
    'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 
    'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6'), vector=(4450.0, 0.0, 
    50.0))
#: The instances were translated by 4.45E+03, 0., 50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63447.6, 
    farPlane=96565.2, width=5725.62, height=3771.79, viewOffsetX=8955.7, 
    viewOffsetY=6322.64)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63408.9, 
    farPlane=96603.9, width=5722.13, height=3769.49, viewOffsetX=9890.6, 
    viewOffsetY=4910.61)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66573.2, 
    farPlane=93071, width=6007.69, height=3957.6, cameraPosition=(26407.3, 
    71749, 45084.4), cameraUpVector=(-0.35446, 0.207297, -0.911804), 
    cameraTarget=(4817.39, 4324.03, 9118.21), viewOffsetX=10384.2, 
    viewOffsetY=5155.67)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67881.9, 
    farPlane=95505.4, width=6125.79, height=4035.4, cameraPosition=(41278.7, 
    70490.9, 40331.5), cameraUpVector=(-0.499438, 0.236316, -0.833496), 
    cameraTarget=(6754.94, 5363.63, 10795.6), viewOffsetX=10588.3, 
    viewOffsetY=5257.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=68278.2, 
    farPlane=95109.2, width=2435.61, height=1604.47, viewOffsetX=10034.2, 
    viewOffsetY=5259.97)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-3-2'].vertices
e1 = a.instances['xbeam-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[6], normal=e1[7], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['xbeam-2-3-2'].vertices
e11 = a.instances['xbeam-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[4], normal=e11[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-3-2'].vertices
e1 = a.instances['xbeam-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[4], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v11 = a.instances['zbeam-2-4-1'].vertices
e11 = a.instances['zbeam-2-4-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e11[6], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['zbeam-2-2-1'].vertices
e1 = a.instances['zbeam-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[4], cells=pickedCells)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    'beam-4-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=71200.7, 
    farPlane=92205.3, width=13058.6, height=8602.45, viewOffsetX=12378.8, 
    viewOffsetY=5583.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=78811, 
    farPlane=97656.3, width=14454.4, height=9521.92, cameraPosition=(70703.3, 
    65182.3, 7588.92), cameraUpVector=(-0.884132, 0.319717, -0.340722), 
    cameraTarget=(17518.1, 6445.1, 12794.2), viewOffsetX=13701.9, 
    viewOffsetY=6180.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=83317.4, 
    farPlane=108961, width=15280.9, height=10066.4, cameraPosition=(66736.4, 
    47828.5, -54050.7), cameraUpVector=(-0.90354, 0.415706, 0.103941), 
    cameraTarget=(26018.5, 8992.46, 1981.75), viewOffsetX=14485.4, 
    viewOffsetY=6533.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=85876.9, 
    farPlane=107655, width=15750.4, height=10375.6, cameraPosition=(27908.1, 
    54329.8, -73477.9), cameraUpVector=(-0.604078, 0.420323, 0.677065), 
    cameraTarget=(24038.5, 8020.35, -9086.3), viewOffsetX=14930.4, 
    viewOffsetY=6734.64)
session.viewports['Viewport: 1'].view.setValues(nearPlane=81603.5, 
    farPlane=103327, width=14966.6, height=9859.36, cameraPosition=(-31171.2, 
    77307.5, -37717.7), cameraUpVector=(0.175223, 0.0679512, 0.982181), 
    cameraTarget=(10533.5, 14092.6, -13834.3), viewOffsetX=14187.4, 
    viewOffsetY=6399.51)
session.viewports['Viewport: 1'].view.setValues(nearPlane=81691.4, 
    farPlane=103239, width=14982.7, height=9869.97, viewOffsetX=7475.73, 
    viewOffsetY=10222.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=82874.2, 
    farPlane=102057, width=4506.14, height=2968.44, viewOffsetX=4551.62, 
    viewOffsetY=9819.29)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-4-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#221040 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-5')
#: ???? 'Surf-5' ?????? (4 ??).
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'beam-4-1', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 
    'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 
    'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 
    'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 
    'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 
    'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 
    'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 
    'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 
    'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 
    'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 
    'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 
    'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 
    'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 
    'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 
    'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 
    'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 
    'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 
    'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 
    'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 
    'zbeam-2-4-2-rebar-4-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 
    'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 
    'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 
    'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 
    'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 
    'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 
    'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 
    'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    'xbeam-2-3-4-rebar-5-6', ))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=58817.1, 
    farPlane=99833.4, width=31622.2, height=20831.3, viewOffsetX=7540.41, 
    viewOffsetY=1733.11)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60984.5, 
    farPlane=97666.1, width=12960.6, height=8537.88, viewOffsetX=2512.09, 
    viewOffsetY=-325.731)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61075.6, 
    farPlane=97575, width=12980, height=8550.64, viewOffsetX=2376.43, 
    viewOffsetY=-61.1905)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61652.1, 
    farPlane=95693.8, width=13102.5, height=8631.37, cameraPosition=(39455, 
    57279.5, 55720.5), cameraUpVector=(-0.518553, 0.446023, -0.729497), 
    cameraTarget=(7100.53, 2139.98, 8759.72), viewOffsetX=2398.86, 
    viewOffsetY=-61.7681)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 
    'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 
    'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6'), vector=(0.0, 0.0, 
    -9725.0))
#: The instances were translated by 0., 0., -9.725E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62700.9, 
    farPlane=94645, width=3708.79, height=2443.19, viewOffsetX=1773.39, 
    viewOffsetY=-2088.14)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-2-3', 
    'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 
    'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6'), 
    vector=(4500.0, 3300.0, 6600.0))
#: The instances were translated by 4.5E+03, 3.3E+03, 6.6E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61690.7, 
    farPlane=95655.2, width=13435.9, height=8850.97, viewOffsetX=2699.51, 
    viewOffsetY=-238.716)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61601.5, 
    farPlane=95744.4, width=13416.5, height=8838.17, viewOffsetX=3171.16, 
    viewOffsetY=-2675)
session.viewports['Viewport: 1'].view.setValues(nearPlane=63027.3, 
    farPlane=94318.7, width=1063.97, height=700.894, viewOffsetX=1413.58, 
    viewOffsetY=-2945.46)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6'), vector=(0.0, 0.0, 
    6600.0))
#: The instances were translated by 0., 0., 6.6E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62690, 
    farPlane=94656, width=4293.71, height=2828.51, viewOffsetX=1915.14, 
    viewOffsetY=-2615.04)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62660.5, 
    farPlane=94685.4, width=4291.69, height=2827.18, viewOffsetX=1785.16, 
    viewOffsetY=-3582.34)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62960.8, 
    farPlane=94385.1, width=1602.33, height=1055.54, viewOffsetX=1468.58, 
    viewOffsetY=-3507.69)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-1-3-3'].vertices
e11 = a.instances['xbeam-1-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62905.4, 
    farPlane=94440.6, width=2320.61, height=1528.71, viewOffsetX=1585.95, 
    viewOffsetY=-3562.99)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['xbeam-1-3-3'].vertices
e1 = a.instances['col-2-4-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[18], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-1-3-3'].vertices
e11 = a.instances['col-2-4-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[9], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v1 = a.instances['zbeam-2-4-3'].vertices
e1 = a.instances['zbeam-2-4-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[2], normal=e1[6], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62767.3, 
    farPlane=94578.6, width=3585.3, height=2361.84, viewOffsetX=1835.47, 
    viewOffsetY=-3763.27)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    'beam-4-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=66313.9, 
    farPlane=91061.7, width=19554.9, height=12881.9, viewOffsetX=4282.71, 
    viewOffsetY=-6060.77)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72967.1, 
    farPlane=93470.2, width=21516.9, height=14174.4, cameraPosition=(83636.3, 
    35836.7, 13120), cameraUpVector=(-0.628789, 0.657869, -0.414528), 
    cameraTarget=(10471.4, 5219.04, 11723.3), viewOffsetX=4712.39, 
    viewOffsetY=-6668.84)
session.viewports['Viewport: 1'].view.setValues(nearPlane=68088.3, 
    farPlane=94524.9, width=20078.2, height=13226.7, cameraPosition=(70499.2, 
    40282.6, -27022.6), cameraUpVector=(-0.850362, 0.442786, -0.284297), 
    cameraTarget=(9111.77, 5190.05, 8929.98), viewOffsetX=4397.31, 
    viewOffsetY=-6222.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65725, 
    farPlane=90549.1, width=19381.4, height=12767.6, cameraPosition=(49363.8, 
    60473.9, -24878.3), cameraUpVector=(-0.968073, 0.250628, -0.00446367), 
    cameraTarget=(7271.27, 4041.05, 11673.5), viewOffsetX=4244.69, 
    viewOffsetY=-6006.95)
session.viewports['Viewport: 1'].view.setValues(nearPlane=66256.8, 
    farPlane=79475.2, width=19538.2, height=12870.9, cameraPosition=(5469, 
    76787.4, 14029.4), cameraUpVector=(-0.715675, -0.365967, 0.594876), 
    cameraTarget=(10899.1, -2317.74, 16346.1), viewOffsetX=4279.03, 
    viewOffsetY=-6055.55)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60604.1, 
    farPlane=80737.2, width=17871.3, height=11772.8, cameraPosition=(-20067.7, 
    66095.3, 29518.5), cameraUpVector=(-0.36971, -0.696066, 0.615473), 
    cameraTarget=(15308.4, -3426.39, 15105.3), viewOffsetX=3913.97, 
    viewOffsetY=-5538.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58091, 
    farPlane=82063.4, width=17130.2, height=11284.6, cameraPosition=(-17475.2, 
    61776.1, -23912), cameraUpVector=(-0.596605, -0.162429, 0.785926), 
    cameraTarget=(12467.3, 3148.28, 20345.1), viewOffsetX=3751.67, 
    viewOffsetY=-5309.24)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59709.1, 
    farPlane=80445.3, width=3748.79, height=2469.54, viewOffsetX=332.515, 
    viewOffsetY=-3296.74)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-4-4'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#11082 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-6')
#: ???? 'Surf-6' ?????? (4 ??).
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=37409.9, 
    farPlane=60480, width=5403.42, height=3559.53, viewOffsetX=-106.603, 
    viewOffsetY=-1693.31)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=35522.4, 
    farPlane=62367.5, width=21293.3, height=14027.1, viewOffsetX=-160.1, 
    viewOffsetY=549.185)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35730.9, 
    farPlane=62159, width=21418.3, height=14109.5, viewOffsetX=-165.098, 
    viewOffsetY=568.177)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'beam-4-1', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 
    'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 
    'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 
    'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 
    'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 
    'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 
    'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 
    'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 
    'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 
    'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 
    'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 
    'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 
    'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 
    'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 
    'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 
    'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 
    'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 
    'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 
    'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 
    'zbeam-2-4-2-rebar-4-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 
    'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 
    'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 
    'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 
    'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 
    'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 
    'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 
    'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    'xbeam-2-3-4-rebar-5-6', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=31616, 
    farPlane=66245, width=5231.81, height=3446.49, viewOffsetX=-3725.13, 
    viewOffsetY=-337.089)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 
    'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 
    'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6'), vector=(0.0, 3300.0, 
    -50.0))
#: The instances were translated by 0., 3.3E+03, -50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31580.8, 
    farPlane=66280.2, width=5225.99, height=3442.65, viewOffsetX=-3760.28, 
    viewOffsetY=831.429)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31572.8, 
    farPlane=66288.2, width=5626.65, height=3706.59, viewOffsetX=-3607.41, 
    viewOffsetY=750.789)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31535.1, 
    farPlane=66325.9, width=5619.94, height=3702.17, viewOffsetX=-4152.42, 
    viewOffsetY=369.41)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29758.3, 
    farPlane=68102.7, width=19767.6, height=13022, viewOffsetX=-689.956, 
    viewOffsetY=382.622)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29882.7, 
    farPlane=67978.3, width=19850.2, height=13076.4, viewOffsetX=1673.84, 
    viewOffsetY=1088.17)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30123.1, 
    farPlane=65133.3, width=20009.9, height=13181.6, cameraPosition=(12003.9, 
    28473.8, 48520.6), cameraUpVector=(-0.307412, 0.599049, -0.73935), 
    cameraTarget=(6421.06, 2280.8, 7552.73), viewOffsetX=1687.31, 
    viewOffsetY=1096.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29890.8, 
    farPlane=66896.8, width=19855.6, height=13080, cameraPosition=(25748.6, 
    33809.8, 41053.4), cameraUpVector=(-0.443523, 0.516366, -0.732566), 
    cameraTarget=(6380.42, 2717.1, 8592.28), viewOffsetX=1674.3, 
    viewOffsetY=1088.46)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30824.1, 
    farPlane=65963.5, width=12686.8, height=8357.48, viewOffsetX=-201.869, 
    viewOffsetY=549.996)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30743.3, 
    farPlane=66044.2, width=12653.5, height=8335.6, viewOffsetX=-201.341, 
    viewOffsetY=-444.101)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30743.2, 
    farPlane=66044.4, viewOffsetX=-160.567, viewOffsetY=-36.1597)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30743.2, 
    viewOffsetX=-255.705, viewOffsetY=154.212)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30291.2, 
    farPlane=66510.8, width=12467.4, height=8213, cameraPosition=(27254.4, 
    31822, 41921), cameraUpVector=(-0.470714, 0.559755, -0.681985), 
    cameraTarget=(6358.55, 2743.01, 8553.57), viewOffsetX=-251.945, 
    viewOffsetY=151.945)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30311.8, 
    farPlane=66490.3, width=12475.9, height=8218.58, viewOffsetX=-975.745, 
    viewOffsetY=366.562)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30990.6, 
    farPlane=65811.5, width=7040.56, height=4638.01, viewOffsetX=-494.368, 
    viewOffsetY=581.302)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30943.9, 
    farPlane=65858.1, width=7029.96, height=4631.03, viewOffsetX=-2207.7, 
    viewOffsetY=-190.152)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31603.1, 
    farPlane=65198.9, width=1269.66, height=836.396, viewOffsetX=-3933.61, 
    viewOffsetY=298.948)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 
    'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 
    'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6'), vector=(-50.0, 3300.0, 
    6600.0))
#: The instances were translated by -50., 3.3E+03, 6.6E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31364.3, 
    farPlane=65437.7, width=3622.38, height=2386.26, viewOffsetX=-3410.37, 
    viewOffsetY=204.029)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31339.7, 
    farPlane=65462.3, width=3619.54, height=2384.39, viewOffsetX=-3878.12, 
    viewOffsetY=-165.653)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31558.6, 
    farPlane=65243.5, width=1630.56, height=1074.14, viewOffsetX=-3943.91, 
    viewOffsetY=-102.29)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-1-2-4'].vertices
e11 = a.instances['xbeam-1-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31486.3, 
    farPlane=65315.8, width=2216.68, height=1460.25, viewOffsetX=-3868.88, 
    viewOffsetY=-186.699)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31502.4, 
    farPlane=65299.6, width=2217.81, height=1461, viewOffsetX=-3766.05, 
    viewOffsetY=25.3242)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31570.4, 
    farPlane=65231.6, width=1735.3, height=1143.14, viewOffsetX=-3819.44, 
    viewOffsetY=-65.1323)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['xbeam-1-2-4'].vertices
e1 = a.instances['xbeam-1-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[4], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-1-2-4'].vertices
e11 = a.instances['xbeam-1-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31558.5, 
    farPlane=65243.6, width=1734.64, height=1142.71, viewOffsetX=-3829.18, 
    viewOffsetY=177.228)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31684.1, 
    farPlane=65117.9, width=613.276, height=403.999, viewOffsetX=-4046.37, 
    viewOffsetY=304.572)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v1 = a.instances['zbeam-1-2-3'].vertices
e1 = a.instances['col-2-2-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[17], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31102.8, 
    farPlane=65699.2, width=6014.55, height=3962.12, viewOffsetX=-3740.99, 
    viewOffsetY=383.259)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31062.7, 
    farPlane=65739.4, width=6006.79, height=3957.01, viewOffsetX=-2581.25, 
    viewOffsetY=-656.515)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-2671.57, 
    viewOffsetY=-572.597)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31034, 
    farPlane=65099.3, width=6001.25, height=3953.36, cameraPosition=(28734.9, 
    33051.2, 39386.7), cameraUpVector=(-0.419947, 0.518735, -0.744687), 
    cameraTarget=(6437.77, 2233.73, 8585.27), viewOffsetX=-2669.11, 
    viewOffsetY=-572.07)
a1 = mdb.models['structure'].rootAssembly
a1.LinearInstancePattern(instanceList=('col-2-2-4', 'col-2-2-4-rebar-2-1', 
    'col-2-2-4-rebar-2-2', 'col-2-2-4-rebar-2-3', 'col-2-2-4-rebar-2-4', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5'), 
    direction1=(0.0, -1.0, 0.0), direction2=(0.0, 1.0, 0.0), number1=2, 
    number2=1, spacing1=5000.0, spacing2=3300.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28803.5, 
    farPlane=67959.4, width=26700.5, height=17589.1, viewOffsetX=853.37, 
    viewOffsetY=-1874.72)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28532.4, 
    farPlane=68548.3, width=26449.2, height=17423.5, cameraPosition=(26177.6, 
    31049.2, 42968.4), cameraUpVector=(-0.444931, 0.564767, -0.695036), 
    cameraTarget=(6313.63, 2207.58, 8775.02), viewOffsetX=845.338, 
    viewOffsetY=-1857.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30713.4, 
    farPlane=66367.3, width=7298.19, height=4807.72, viewOffsetX=-2378.88, 
    viewOffsetY=35.7394)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31500.2, 
    farPlane=65314.7, width=7485.15, height=4930.88, cameraPosition=(24854.4, 
    34877.6, 40099.2), cameraUpVector=(-0.404963, 0.471392, -0.783451), 
    cameraTarget=(6416.71, 1912.89, 8970.68), viewOffsetX=-2439.82, 
    viewOffsetY=36.655)
session.viewports['Viewport: 1'].view.setValues(nearPlane=31139.7, 
    farPlane=64975.6, width=7399.48, height=4874.45, cameraPosition=(27491.8, 
    35120.6, 37646.4), cameraUpVector=(-0.437477, 0.458006, -0.77385), 
    cameraTarget=(6267.6, 1748.96, 8811.03), viewOffsetX=-2411.9, 
    viewOffsetY=36.2355)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30121.8, 
    farPlane=65993.6, width=17230.5, height=11350.7, viewOffsetX=-1097.07, 
    viewOffsetY=125.309)
a1 = mdb.models['structure'].rootAssembly
a1.LinearInstancePattern(instanceList=('col-2-2-4', 'col-2-2-4-rebar-2-1', 
    'col-2-2-4-rebar-2-2', 'col-2-2-4-rebar-2-3', 'col-2-2-4-rebar-2-4', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6'), direction1=(0.0, 1.0, 
    0.0), direction2=(0.0, 1.0, 0.0), number1=5, number2=1, spacing1=5000.0, 
    spacing2=3300.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19407.8, 
    farPlane=65260.9, width=11101.8, height=7313.37, cameraPosition=(39197.7, 
    26494.2, 33456.6), cameraUpVector=(-0.582186, 0.67295, -0.456288), 
    cameraTarget=(3624.9, 3399.03, 9027.1), viewOffsetX=-706.858, 
    viewOffsetY=80.7377)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19939, 
    farPlane=64729.7, width=4508.58, height=2970.05, viewOffsetX=-1633.72, 
    viewOffsetY=461.998)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20960.6, 
    farPlane=64580.9, width=4739.57, height=3122.22, cameraPosition=(40761, 
    23345.4, 33547.9), cameraUpVector=(-0.565979, 0.73455, -0.374305), 
    cameraTarget=(3208.29, 4017.16, 8812.72), viewOffsetX=-1717.42, 
    viewOffsetY=485.668)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21408.8, 
    farPlane=64132.8, width=615.894, height=405.724, viewOffsetX=-2558.22, 
    viewOffsetY=515.599)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 
    'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 
    'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6'), vector=(4550.0, 0.0, 
    0.0))
#: The instances were translated by 4.55E+03, 0., 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21237.2, 
    farPlane=64304.4, width=2268.01, height=1494.07, viewOffsetX=-2538.79, 
    viewOffsetY=581.991)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21221.8, 
    farPlane=64319.9, width=2266.36, height=1492.98, viewOffsetX=-2271.6, 
    viewOffsetY=218.674)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18752.6, 
    farPlane=64953.6, width=2002.66, height=1319.27, cameraPosition=(28465.3, 
    36121.1, 37038), cameraUpVector=(-0.557104, 0.450023, -0.697936), 
    cameraTarget=(6237.2, 2254.71, 9568.06), viewOffsetX=-2007.29, 
    viewOffsetY=193.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18959, 
    farPlane=64747.2, width=458.598, height=302.104, viewOffsetX=-2190.99, 
    viewOffsetY=314.632)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['zbeam-2-1-3'].vertices
e11 = a.instances['zbeam-2-1-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[4], normal=e11[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['zbeam-2-1-3'].vertices
e1 = a.instances['zbeam-2-1-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[4], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=72769.7, 
    farPlane=120072, width=7747.08, height=5103.43, viewOffsetX=-3486.95, 
    viewOffsetY=-3910.42)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    'beam-4-1', 'col-2-2-4-lin-2-1', 'zbeam-1-2-3-lin-2-1', 
    'zbeam-1-2-3-rebar-3-2-lin-2-1', 'zbeam-1-2-3-rebar-3-4-lin-2-1', 
    'zbeam-1-2-3-rebar-3-6-lin-2-1', 'xbeam-1-2-4-lin-2-1', 
    'xbeam-1-2-4-rebar-5-2-lin-2-1', 'xbeam-1-2-4-rebar-5-4-lin-2-1', 
    'xbeam-1-2-4-rebar-5-6-lin-2-1', 'xbeam-2-1-4-lin-2-1', 
    'xbeam-2-1-4-rebar-5-2-lin-2-1', 'xbeam-2-1-4-rebar-5-4-lin-2-1', 
    'zbeam-1-2-3-rebar-3-1-lin-2-1', 'xbeam-1-2-4-rebar-5-1-lin-2-1', 
    'xbeam-1-2-4-rebar-5-3-lin-2-1', 'xbeam-1-2-4-rebar-5-5-lin-2-1', 
    'xbeam-2-1-4-rebar-5-1-lin-2-1', 'xbeam-2-1-4-rebar-5-3-lin-2-1', 
    'xbeam-2-1-4-rebar-5-5-lin-2-1', 'col-2-2-4-rebar-2-1-lin-2-1', 
    'col-2-2-4-rebar-2-2-lin-2-1', 'col-2-2-4-rebar-2-4-lin-2-1', 
    'col-2-2-4-rebar-2-3-lin-2-1', 'col-2-2-4-lin-2-1-1', 'col-2-2-4-lin-3-1', 
    'col-2-2-4-lin-4-1', 'col-2-2-4-lin-5-1', 'zbeam-1-2-3-lin-2-1-1', 
    'zbeam-1-2-3-lin-3-1', 'zbeam-1-2-3-lin-4-1', 'zbeam-1-2-3-lin-5-1', 
    'zbeam-1-2-3-rebar-3-2-lin-2-1-1', 'zbeam-1-2-3-rebar-3-2-lin-3-1', 
    'zbeam-1-2-3-rebar-3-2-lin-4-1', 'zbeam-1-2-3-rebar-3-2-lin-5-1', 
    'zbeam-1-2-3-rebar-3-4-lin-2-1-1', 'zbeam-1-2-3-rebar-3-4-lin-3-1', 
    'zbeam-1-2-3-rebar-3-4-lin-4-1', 'zbeam-1-2-3-rebar-3-4-lin-5-1', 
    'zbeam-1-2-3-rebar-3-6-lin-2-1-1', 'zbeam-1-2-3-rebar-3-6-lin-3-1', 
    'zbeam-1-2-3-rebar-3-6-lin-4-1', 'zbeam-1-2-3-rebar-3-6-lin-5-1', 
    'xbeam-1-2-4-lin-2-1-1', 'xbeam-1-2-4-lin-3-1', 'xbeam-1-2-4-lin-4-1', 
    'xbeam-1-2-4-lin-5-1', 'xbeam-1-2-4-rebar-5-2-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-2-lin-3-1', 'xbeam-1-2-4-rebar-5-2-lin-4-1', 
    'xbeam-1-2-4-rebar-5-2-lin-5-1', 'xbeam-1-2-4-rebar-5-4-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-4-lin-3-1', 'xbeam-1-2-4-rebar-5-4-lin-4-1', 
    'xbeam-1-2-4-rebar-5-4-lin-5-1', 'xbeam-1-2-4-rebar-5-6-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-6-lin-3-1', 'xbeam-1-2-4-rebar-5-6-lin-4-1', 
    'xbeam-1-2-4-rebar-5-6-lin-5-1', 'xbeam-2-1-4-lin-2-1-1', 
    'xbeam-2-1-4-lin-3-1', 'xbeam-2-1-4-lin-4-1', 'xbeam-2-1-4-lin-5-1', 
    'xbeam-2-1-4-rebar-5-2-lin-2-1-1', 'xbeam-2-1-4-rebar-5-2-lin-3-1', 
    'xbeam-2-1-4-rebar-5-2-lin-4-1', 'xbeam-2-1-4-rebar-5-2-lin-5-1', 
    'xbeam-2-1-4-rebar-5-4-lin-2-1-1', 'xbeam-2-1-4-rebar-5-4-lin-3-1', 
    'xbeam-2-1-4-rebar-5-4-lin-4-1', 'xbeam-2-1-4-rebar-5-4-lin-5-1', 
    'xbeam-2-1-4-rebar-5-6-lin-2-1', 'xbeam-2-1-4-rebar-5-6-lin-3-1', 
    'xbeam-2-1-4-rebar-5-6-lin-4-1', 'xbeam-2-1-4-rebar-5-6-lin-5-1', 
    'zbeam-1-2-3-rebar-3-1-lin-2-1-1', 'zbeam-1-2-3-rebar-3-1-lin-3-1', 
    'zbeam-1-2-3-rebar-3-1-lin-4-1', 'zbeam-1-2-3-rebar-3-1-lin-5-1', 
    'zbeam-1-2-3-rebar-3-3-lin-2-1', 'zbeam-1-2-3-rebar-3-3-lin-3-1', 
    'zbeam-1-2-3-rebar-3-3-lin-4-1', 'zbeam-1-2-3-rebar-3-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-1-lin-2-1-1', 'xbeam-1-2-4-rebar-5-1-lin-3-1', 
    'xbeam-1-2-4-rebar-5-1-lin-4-1', 'xbeam-1-2-4-rebar-5-1-lin-5-1', 
    'xbeam-1-2-4-rebar-5-3-lin-2-1-1', 'xbeam-1-2-4-rebar-5-3-lin-3-1', 
    'xbeam-1-2-4-rebar-5-3-lin-4-1', 'xbeam-1-2-4-rebar-5-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-5-lin-2-1-1', 'xbeam-1-2-4-rebar-5-5-lin-3-1', 
    'xbeam-1-2-4-rebar-5-5-lin-4-1', 'xbeam-1-2-4-rebar-5-5-lin-5-1', 
    'xbeam-2-1-4-rebar-5-1-lin-2-1-1', 'xbeam-2-1-4-rebar-5-1-lin-3-1', 
    'xbeam-2-1-4-rebar-5-1-lin-4-1', 'xbeam-2-1-4-rebar-5-1-lin-5-1', 
    'xbeam-2-1-4-rebar-5-3-lin-2-1-1', 'xbeam-2-1-4-rebar-5-3-lin-3-1', 
    'xbeam-2-1-4-rebar-5-3-lin-4-1', 'xbeam-2-1-4-rebar-5-3-lin-5-1', 
    'xbeam-2-1-4-rebar-5-5-lin-2-1-1', 'xbeam-2-1-4-rebar-5-5-lin-3-1', 
    'xbeam-2-1-4-rebar-5-5-lin-4-1', 'xbeam-2-1-4-rebar-5-5-lin-5-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=78249.6, 
    farPlane=114043, width=11490.8, height=7569.63, viewOffsetX=-3682.56, 
    viewOffsetY=-3598.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=78172.1, 
    farPlane=114121, width=11479.4, height=7562.13, viewOffsetX=-3863.87, 
    viewOffsetY=-5383.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=75412.3, 
    farPlane=106996, width=11074.1, height=7295.16, cameraPosition=(81584.6, 
    64645.5, -4285.22), cameraUpVector=(-0.797243, 0.60206, 0.043894), 
    cameraTarget=(2231.78, 11879.8, 10407.6), viewOffsetX=-3727.46, 
    viewOffsetY=-5193.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70510.1, 
    farPlane=101013, width=10354.3, height=6820.94, cameraPosition=(32138.7, 
    43889.1, -68095), cameraUpVector=(-0.525666, 0.717858, 0.45646), 
    cameraTarget=(2353.29, 12144, 17940.1), viewOffsetX=-3485.16, 
    viewOffsetY=-4856.04)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67509.7, 
    farPlane=97581.9, width=9913.69, height=6530.71, cameraPosition=(-22512.5, 
    43137.7, -63277), cameraUpVector=(0.245009, 0.801055, 0.546151), 
    cameraTarget=(12596.8, 14494.1, 21833.7), viewOffsetX=-3336.86, 
    viewOffsetY=-4649.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=67561.4, 
    farPlane=97530.2, width=9921.29, height=6535.71, viewOffsetX=-877.741, 
    viewOffsetY=-7947.47)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=3715.25, 
    viewOffsetY=-7819.53)
session.viewports['Viewport: 1'].view.setValues(nearPlane=68374.9, 
    farPlane=96716.7, width=2738.11, height=1803.75, viewOffsetX=3851.81, 
    viewOffsetY=-7599.73)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-4'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4420800 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-7')
#: ???? 'Surf-7' ?????? (4 ??).
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'xbeam-2-1-4-rebar-5-5-lin-5-1', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 
    'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 
    'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 
    'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 
    'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 
    'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 
    'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 
    'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 
    'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 
    'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 
    'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 
    'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 
    'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 
    'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 
    'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 
    'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 
    'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 
    'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 
    'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 
    'zbeam-2-4-2-rebar-4-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 
    'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 
    'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 
    'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 
    'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 
    'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 
    'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 
    'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    'xbeam-2-3-4-rebar-5-6', 'beam-4-1', 'col-2-2-4-lin-2-1', 
    'zbeam-1-2-3-lin-2-1', 'zbeam-1-2-3-rebar-3-2-lin-2-1', 
    'zbeam-1-2-3-rebar-3-4-lin-2-1', 'zbeam-1-2-3-rebar-3-6-lin-2-1', 
    'xbeam-1-2-4-lin-2-1', 'xbeam-1-2-4-rebar-5-2-lin-2-1', 
    'xbeam-1-2-4-rebar-5-4-lin-2-1', 'xbeam-1-2-4-rebar-5-6-lin-2-1', 
    'xbeam-2-1-4-lin-2-1', 'xbeam-2-1-4-rebar-5-2-lin-2-1', 
    'xbeam-2-1-4-rebar-5-4-lin-2-1', 'zbeam-1-2-3-rebar-3-1-lin-2-1', 
    'xbeam-1-2-4-rebar-5-1-lin-2-1', 'xbeam-1-2-4-rebar-5-3-lin-2-1', 
    'xbeam-1-2-4-rebar-5-5-lin-2-1', 'xbeam-2-1-4-rebar-5-1-lin-2-1', 
    'xbeam-2-1-4-rebar-5-3-lin-2-1', 'xbeam-2-1-4-rebar-5-5-lin-2-1', 
    'col-2-2-4-rebar-2-1-lin-2-1', 'col-2-2-4-rebar-2-2-lin-2-1', 
    'col-2-2-4-rebar-2-4-lin-2-1', 'col-2-2-4-rebar-2-3-lin-2-1', 
    'col-2-2-4-lin-2-1-1', 'col-2-2-4-lin-3-1', 'col-2-2-4-lin-4-1', 
    'col-2-2-4-lin-5-1', 'zbeam-1-2-3-lin-2-1-1', 'zbeam-1-2-3-lin-3-1', 
    'zbeam-1-2-3-lin-4-1', 'zbeam-1-2-3-lin-5-1', 
    'zbeam-1-2-3-rebar-3-2-lin-2-1-1', 'zbeam-1-2-3-rebar-3-2-lin-3-1', 
    'zbeam-1-2-3-rebar-3-2-lin-4-1', 'zbeam-1-2-3-rebar-3-2-lin-5-1', 
    'zbeam-1-2-3-rebar-3-4-lin-2-1-1', 'zbeam-1-2-3-rebar-3-4-lin-3-1', 
    'zbeam-1-2-3-rebar-3-4-lin-4-1', 'zbeam-1-2-3-rebar-3-4-lin-5-1', 
    'zbeam-1-2-3-rebar-3-6-lin-2-1-1', 'zbeam-1-2-3-rebar-3-6-lin-3-1', 
    'zbeam-1-2-3-rebar-3-6-lin-4-1', 'zbeam-1-2-3-rebar-3-6-lin-5-1', 
    'xbeam-1-2-4-lin-2-1-1', 'xbeam-1-2-4-lin-3-1', 'xbeam-1-2-4-lin-4-1', 
    'xbeam-1-2-4-lin-5-1', 'xbeam-1-2-4-rebar-5-2-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-2-lin-3-1', 'xbeam-1-2-4-rebar-5-2-lin-4-1', 
    'xbeam-1-2-4-rebar-5-2-lin-5-1', 'xbeam-1-2-4-rebar-5-4-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-4-lin-3-1', 'xbeam-1-2-4-rebar-5-4-lin-4-1', 
    'xbeam-1-2-4-rebar-5-4-lin-5-1', 'xbeam-1-2-4-rebar-5-6-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-6-lin-3-1', 'xbeam-1-2-4-rebar-5-6-lin-4-1', 
    'xbeam-1-2-4-rebar-5-6-lin-5-1', 'xbeam-2-1-4-lin-2-1-1', 
    'xbeam-2-1-4-lin-3-1', 'xbeam-2-1-4-lin-4-1', 'xbeam-2-1-4-lin-5-1', 
    'xbeam-2-1-4-rebar-5-2-lin-2-1-1', 'xbeam-2-1-4-rebar-5-2-lin-3-1', 
    'xbeam-2-1-4-rebar-5-2-lin-4-1', 'xbeam-2-1-4-rebar-5-2-lin-5-1', 
    'xbeam-2-1-4-rebar-5-4-lin-2-1-1', 'xbeam-2-1-4-rebar-5-4-lin-3-1', 
    'xbeam-2-1-4-rebar-5-4-lin-4-1', 'xbeam-2-1-4-rebar-5-4-lin-5-1', 
    'xbeam-2-1-4-rebar-5-6-lin-2-1', 'xbeam-2-1-4-rebar-5-6-lin-3-1', 
    'xbeam-2-1-4-rebar-5-6-lin-4-1', 'xbeam-2-1-4-rebar-5-6-lin-5-1', 
    'zbeam-1-2-3-rebar-3-1-lin-2-1-1', 'zbeam-1-2-3-rebar-3-1-lin-3-1', 
    'zbeam-1-2-3-rebar-3-1-lin-4-1', 'zbeam-1-2-3-rebar-3-1-lin-5-1', 
    'zbeam-1-2-3-rebar-3-3-lin-2-1', 'zbeam-1-2-3-rebar-3-3-lin-3-1', 
    'zbeam-1-2-3-rebar-3-3-lin-4-1', 'zbeam-1-2-3-rebar-3-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-1-lin-2-1-1', 'xbeam-1-2-4-rebar-5-1-lin-3-1', 
    'xbeam-1-2-4-rebar-5-1-lin-4-1', 'xbeam-1-2-4-rebar-5-1-lin-5-1', 
    'xbeam-1-2-4-rebar-5-3-lin-2-1-1', 'xbeam-1-2-4-rebar-5-3-lin-3-1', 
    'xbeam-1-2-4-rebar-5-3-lin-4-1', 'xbeam-1-2-4-rebar-5-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-5-lin-2-1-1', 'xbeam-1-2-4-rebar-5-5-lin-3-1', 
    'xbeam-1-2-4-rebar-5-5-lin-4-1', 'xbeam-1-2-4-rebar-5-5-lin-5-1', 
    'xbeam-2-1-4-rebar-5-1-lin-2-1-1', 'xbeam-2-1-4-rebar-5-1-lin-3-1', 
    'xbeam-2-1-4-rebar-5-1-lin-4-1', 'xbeam-2-1-4-rebar-5-1-lin-5-1', 
    'xbeam-2-1-4-rebar-5-3-lin-2-1-1', 'xbeam-2-1-4-rebar-5-3-lin-3-1', 
    'xbeam-2-1-4-rebar-5-3-lin-4-1', 'xbeam-2-1-4-rebar-5-3-lin-5-1', 
    'xbeam-2-1-4-rebar-5-5-lin-2-1-1', 'xbeam-2-1-4-rebar-5-5-lin-3-1', 
    'xbeam-2-1-4-rebar-5-5-lin-4-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=59515.2, 
    farPlane=105918, width=21385.5, height=14087.8, viewOffsetX=8077.74, 
    viewOffsetY=-6155.54)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59377.6, 
    farPlane=106055, width=21336, height=14055.2, viewOffsetX=7371.55, 
    viewOffsetY=-5407.59)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=71864.3, 
    farPlane=120977, width=14204.4, height=9357.21, viewOffsetX=-3760.87, 
    viewOffsetY=154.496)
session.viewports['Viewport: 1'].view.setValues(nearPlane=71964.5, 
    farPlane=120877, width=14224.2, height=9370.26, viewOffsetX=-2971.64, 
    viewOffsetY=475.715)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-3048.03, 
    viewOffsetY=-3361.06)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72927.8, 
    farPlane=119507, width=14414.6, height=9495.7, cameraPosition=(78821.4, 
    57404.9, 54421.3), cameraUpVector=(-0.574419, 0.672604, -0.466526), 
    cameraTarget=(6933.35, 12152.3, 8800.2), viewOffsetX=-3088.83, 
    viewOffsetY=-3406.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=71486.9, 
    farPlane=120258, width=14129.8, height=9308.09, cameraPosition=(63115.9, 
    72208.6, 58707), cameraUpVector=(-0.598939, 0.525164, -0.604546), 
    cameraTarget=(7082.91, 11822.5, 8599.16), viewOffsetX=-3027.8, 
    viewOffsetY=-3338.75)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73041.8, 
    farPlane=118703, width=952.476, height=627.449, viewOffsetX=-5139.26, 
    viewOffsetY=-1800.81)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 
    'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 
    'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6'), vector=(50.0, 5000.0, 
    0.0))
#: The instances were translated by 50., 5.E+03, 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72748.9, 
    farPlane=118996, width=3761.74, height=2478.07, viewOffsetX=-4688.08, 
    viewOffsetY=-2094.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72723, 
    farPlane=119022, width=3760.4, height=2477.18, viewOffsetX=-4799.51, 
    viewOffsetY=-2016.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72986.3, 
    farPlane=118759, width=1402.33, height=923.791, viewOffsetX=-5226.85, 
    viewOffsetY=-2043.57)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-2-1-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-1-2-4-lin-2-1-1'].vertices
e11 = a.instances['xbeam-1-2-4-lin-2-1-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e11[7], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-2-1-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['xbeam-1-2-4-lin-2-1-1'].vertices
e1 = a.instances['col-2-2-4-lin-2-1-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[18], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-2-1-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-1-2-4-lin-2-1-1'].vertices
e11 = a.instances['col-2-2-4-lin-2-1-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[9], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73065.3, 
    farPlane=118680, width=762.331, height=502.19, viewOffsetX=-5394.52, 
    viewOffsetY=-1889.57)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-2-1-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v1 = a.instances['zbeam-1-2-3-lin-2-1-1'].vertices
e1 = a.instances['col-2-2-4-lin-2-1-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[17], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72983.4, 
    farPlane=118762, width=1613.13, height=1062.66, viewOffsetX=-5208.89, 
    viewOffsetY=-2051.93)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72972.2, 
    farPlane=118773, width=1612.88, height=1062.49, viewOffsetX=-5124.94, 
    viewOffsetY=-1758.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73080.6, 
    farPlane=118665, width=638.505, height=420.619, viewOffsetX=-5332.12, 
    viewOffsetY=-1594.18)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-2-1-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['zbeam-2-1-3'].vertices
e11 = a.instances['col-2-2-4-lin-2-1-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[19], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72981.2, 
    farPlane=118764, width=1632.96, height=1075.72, viewOffsetX=-5169.32, 
    viewOffsetY=-1649.24)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72969.9, 
    farPlane=118775, width=1632.71, height=1075.55, viewOffsetX=-5231.66, 
    viewOffsetY=-1745.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72704.5, 
    farPlane=119041, width=4166.09, height=2744.43, viewOffsetX=-4876.65, 
    viewOffsetY=-1720.11)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    'beam-4-1', 'col-2-2-4-lin-2-1', 'zbeam-1-2-3-lin-2-1', 
    'zbeam-1-2-3-rebar-3-2-lin-2-1', 'zbeam-1-2-3-rebar-3-4-lin-2-1', 
    'zbeam-1-2-3-rebar-3-6-lin-2-1', 'xbeam-1-2-4-lin-2-1', 
    'xbeam-1-2-4-rebar-5-2-lin-2-1', 'xbeam-1-2-4-rebar-5-4-lin-2-1', 
    'xbeam-1-2-4-rebar-5-6-lin-2-1', 'xbeam-2-1-4-lin-2-1', 
    'xbeam-2-1-4-rebar-5-2-lin-2-1', 'xbeam-2-1-4-rebar-5-4-lin-2-1', 
    'zbeam-1-2-3-rebar-3-1-lin-2-1', 'xbeam-1-2-4-rebar-5-1-lin-2-1', 
    'xbeam-1-2-4-rebar-5-3-lin-2-1', 'xbeam-1-2-4-rebar-5-5-lin-2-1', 
    'xbeam-2-1-4-rebar-5-1-lin-2-1', 'xbeam-2-1-4-rebar-5-3-lin-2-1', 
    'xbeam-2-1-4-rebar-5-5-lin-2-1', 'col-2-2-4-rebar-2-1-lin-2-1', 
    'col-2-2-4-rebar-2-2-lin-2-1', 'col-2-2-4-rebar-2-4-lin-2-1', 
    'col-2-2-4-rebar-2-3-lin-2-1', 'col-2-2-4-lin-2-1-1', 'col-2-2-4-lin-3-1', 
    'col-2-2-4-lin-4-1', 'col-2-2-4-lin-5-1', 'zbeam-1-2-3-lin-2-1-1', 
    'zbeam-1-2-3-lin-3-1', 'zbeam-1-2-3-lin-4-1', 'zbeam-1-2-3-lin-5-1', 
    'zbeam-1-2-3-rebar-3-2-lin-2-1-1', 'zbeam-1-2-3-rebar-3-2-lin-3-1', 
    'zbeam-1-2-3-rebar-3-2-lin-4-1', 'zbeam-1-2-3-rebar-3-2-lin-5-1', 
    'zbeam-1-2-3-rebar-3-4-lin-2-1-1', 'zbeam-1-2-3-rebar-3-4-lin-3-1', 
    'zbeam-1-2-3-rebar-3-4-lin-4-1', 'zbeam-1-2-3-rebar-3-4-lin-5-1', 
    'zbeam-1-2-3-rebar-3-6-lin-2-1-1', 'zbeam-1-2-3-rebar-3-6-lin-3-1', 
    'zbeam-1-2-3-rebar-3-6-lin-4-1', 'zbeam-1-2-3-rebar-3-6-lin-5-1', 
    'xbeam-1-2-4-lin-2-1-1', 'xbeam-1-2-4-lin-3-1', 'xbeam-1-2-4-lin-4-1', 
    'xbeam-1-2-4-lin-5-1', 'xbeam-1-2-4-rebar-5-2-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-2-lin-3-1', 'xbeam-1-2-4-rebar-5-2-lin-4-1', 
    'xbeam-1-2-4-rebar-5-2-lin-5-1', 'xbeam-1-2-4-rebar-5-4-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-4-lin-3-1', 'xbeam-1-2-4-rebar-5-4-lin-4-1', 
    'xbeam-1-2-4-rebar-5-4-lin-5-1', 'xbeam-1-2-4-rebar-5-6-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-6-lin-3-1', 'xbeam-1-2-4-rebar-5-6-lin-4-1', 
    'xbeam-1-2-4-rebar-5-6-lin-5-1', 'xbeam-2-1-4-lin-2-1-1', 
    'xbeam-2-1-4-lin-3-1', 'xbeam-2-1-4-lin-4-1', 'xbeam-2-1-4-lin-5-1', 
    'xbeam-2-1-4-rebar-5-2-lin-2-1-1', 'xbeam-2-1-4-rebar-5-2-lin-3-1', 
    'xbeam-2-1-4-rebar-5-2-lin-4-1', 'xbeam-2-1-4-rebar-5-2-lin-5-1', 
    'xbeam-2-1-4-rebar-5-4-lin-2-1-1', 'xbeam-2-1-4-rebar-5-4-lin-3-1', 
    'xbeam-2-1-4-rebar-5-4-lin-4-1', 'xbeam-2-1-4-rebar-5-4-lin-5-1', 
    'xbeam-2-1-4-rebar-5-6-lin-2-1', 'xbeam-2-1-4-rebar-5-6-lin-3-1', 
    'xbeam-2-1-4-rebar-5-6-lin-4-1', 'xbeam-2-1-4-rebar-5-6-lin-5-1', 
    'zbeam-1-2-3-rebar-3-1-lin-2-1-1', 'zbeam-1-2-3-rebar-3-1-lin-3-1', 
    'zbeam-1-2-3-rebar-3-1-lin-4-1', 'zbeam-1-2-3-rebar-3-1-lin-5-1', 
    'zbeam-1-2-3-rebar-3-3-lin-2-1', 'zbeam-1-2-3-rebar-3-3-lin-3-1', 
    'zbeam-1-2-3-rebar-3-3-lin-4-1', 'zbeam-1-2-3-rebar-3-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-1-lin-2-1-1', 'xbeam-1-2-4-rebar-5-1-lin-3-1', 
    'xbeam-1-2-4-rebar-5-1-lin-4-1', 'xbeam-1-2-4-rebar-5-1-lin-5-1', 
    'xbeam-1-2-4-rebar-5-3-lin-2-1-1', 'xbeam-1-2-4-rebar-5-3-lin-3-1', 
    'xbeam-1-2-4-rebar-5-3-lin-4-1', 'xbeam-1-2-4-rebar-5-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-5-lin-2-1-1', 'xbeam-1-2-4-rebar-5-5-lin-3-1', 
    'xbeam-1-2-4-rebar-5-5-lin-4-1', 'xbeam-1-2-4-rebar-5-5-lin-5-1', 
    'xbeam-2-1-4-rebar-5-1-lin-2-1-1', 'xbeam-2-1-4-rebar-5-1-lin-3-1', 
    'xbeam-2-1-4-rebar-5-1-lin-4-1', 'xbeam-2-1-4-rebar-5-1-lin-5-1', 
    'xbeam-2-1-4-rebar-5-3-lin-2-1-1', 'xbeam-2-1-4-rebar-5-3-lin-3-1', 
    'xbeam-2-1-4-rebar-5-3-lin-4-1', 'xbeam-2-1-4-rebar-5-3-lin-5-1', 
    'xbeam-2-1-4-rebar-5-5-lin-2-1-1', 'xbeam-2-1-4-rebar-5-5-lin-3-1', 
    'xbeam-2-1-4-rebar-5-5-lin-4-1', 'xbeam-2-1-4-rebar-5-5-lin-5-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=76928.6, 
    farPlane=114216, width=16297.3, height=10736, viewOffsetX=-1092.33, 
    viewOffsetY=-2337.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=76820.2, 
    farPlane=114325, width=16274.3, height=10720.8, viewOffsetX=-2716.48, 
    viewOffsetY=-1862)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'col-2-2-4-rebar-2-1-lin-2-1', 'col-2-2-4-rebar-2-2-lin-2-1', 
    'col-2-2-4-rebar-2-4-lin-2-1', 'col-2-2-4-rebar-2-3-lin-2-1', 
    'col-2-2-4-lin-2-1-1', 'col-2-2-4-lin-3-1', 'col-2-2-4-lin-4-1', 
    'col-2-2-4-lin-5-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=78116.5, 
    farPlane=113655, width=4800.95, height=3162.66, viewOffsetX=-4930.44, 
    viewOffsetY=-1781.93)
session.viewports['Viewport: 1'].view.setValues(nearPlane=78151.5, 
    farPlane=113620, width=4803.1, height=3164.07, viewOffsetX=-4803.67, 
    viewOffsetY=-2175.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=76396.8, 
    farPlane=115374, width=21157.1, height=13937.4, viewOffsetX=-1581.28, 
    viewOffsetY=-2752.93)
session.viewports['Viewport: 1'].view.setValues(nearPlane=74445.7, 
    farPlane=111235, width=20616.8, height=13581.4, cameraPosition=(76284.1, 
    60860.2, -31089), cameraUpVector=(-0.791365, 0.599914, 0.117665), 
    cameraTarget=(4450.83, 11572.4, 10234.8), viewOffsetX=-1540.9, 
    viewOffsetY=-2682.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73885.5, 
    farPlane=106961, width=20461.7, height=13479.2, cameraPosition=(22980.2, 
    48667.9, -73453.6), cameraUpVector=(-0.621719, 0.601862, 0.501226), 
    cameraTarget=(5548.05, 11430.1, 13761.2), viewOffsetX=-1529.3, 
    viewOffsetY=-2662.43)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70211.1, 
    farPlane=108048, width=19444.1, height=12808.9, cameraPosition=(-7161.11, 
    74346.7, -55121.6), cameraUpVector=(-0.205476, 0.413198, 0.887157), 
    cameraTarget=(8331.97, 9761.51, 14775.9), viewOffsetX=-1453.25, 
    viewOffsetY=-2530.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=68563.2, 
    farPlane=106015, width=18987.7, height=12508.3, cameraPosition=(-52024.8, 
    73978.9, -13157.7), cameraUpVector=(0.644478, 0.429658, 0.632488), 
    cameraTarget=(15233.3, 9894.29, 12658.2), viewOffsetX=-1419.14, 
    viewOffsetY=-2470.64)
session.viewports['Viewport: 1'].view.setValues(nearPlane=68618.2, 
    farPlane=105960, width=19003, height=12518.3, viewOffsetX=6968.79, 
    viewOffsetY=-3452.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=70312.1, 
    farPlane=104266, width=4145.81, height=2731.08, viewOffsetX=6783.99, 
    viewOffsetY=-1533.48)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-4-lin-2-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#221040 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-8')
#: ???? 'Surf-8' ?????? (4 ??).
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'col-2-2-4-rebar-2-3-lin-5-1', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 
    'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 
    'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 
    'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 
    'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 
    'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 
    'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 
    'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 
    'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 
    'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 
    'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 
    'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 
    'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 
    'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 
    'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 
    'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 
    'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 
    'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 
    'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 
    'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 
    'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 
    'zbeam-2-4-2-rebar-4-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 
    'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 
    'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 
    'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 
    'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 
    'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 
    'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 
    'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    'xbeam-2-3-4-rebar-5-6', 'beam-4-1', 'col-2-2-4-lin-2-1', 
    'zbeam-1-2-3-lin-2-1', 'zbeam-1-2-3-rebar-3-2-lin-2-1', 
    'zbeam-1-2-3-rebar-3-4-lin-2-1', 'zbeam-1-2-3-rebar-3-6-lin-2-1', 
    'xbeam-1-2-4-lin-2-1', 'xbeam-1-2-4-rebar-5-2-lin-2-1', 
    'xbeam-1-2-4-rebar-5-4-lin-2-1', 'xbeam-1-2-4-rebar-5-6-lin-2-1', 
    'xbeam-2-1-4-lin-2-1', 'xbeam-2-1-4-rebar-5-2-lin-2-1', 
    'xbeam-2-1-4-rebar-5-4-lin-2-1', 'zbeam-1-2-3-rebar-3-1-lin-2-1', 
    'xbeam-1-2-4-rebar-5-1-lin-2-1', 'xbeam-1-2-4-rebar-5-3-lin-2-1', 
    'xbeam-1-2-4-rebar-5-5-lin-2-1', 'xbeam-2-1-4-rebar-5-1-lin-2-1', 
    'xbeam-2-1-4-rebar-5-3-lin-2-1', 'xbeam-2-1-4-rebar-5-5-lin-2-1', 
    'col-2-2-4-rebar-2-1-lin-2-1', 'col-2-2-4-rebar-2-2-lin-2-1', 
    'col-2-2-4-rebar-2-4-lin-2-1', 'col-2-2-4-rebar-2-3-lin-2-1', 
    'col-2-2-4-lin-2-1-1', 'col-2-2-4-lin-3-1', 'col-2-2-4-lin-4-1', 
    'col-2-2-4-lin-5-1', 'zbeam-1-2-3-lin-2-1-1', 'zbeam-1-2-3-lin-3-1', 
    'zbeam-1-2-3-lin-4-1', 'zbeam-1-2-3-lin-5-1', 
    'zbeam-1-2-3-rebar-3-2-lin-2-1-1', 'zbeam-1-2-3-rebar-3-2-lin-3-1', 
    'zbeam-1-2-3-rebar-3-2-lin-4-1', 'zbeam-1-2-3-rebar-3-2-lin-5-1', 
    'zbeam-1-2-3-rebar-3-4-lin-2-1-1', 'zbeam-1-2-3-rebar-3-4-lin-3-1', 
    'zbeam-1-2-3-rebar-3-4-lin-4-1', 'zbeam-1-2-3-rebar-3-4-lin-5-1', 
    'zbeam-1-2-3-rebar-3-6-lin-2-1-1', 'zbeam-1-2-3-rebar-3-6-lin-3-1', 
    'zbeam-1-2-3-rebar-3-6-lin-4-1', 'zbeam-1-2-3-rebar-3-6-lin-5-1', 
    'xbeam-1-2-4-lin-2-1-1', 'xbeam-1-2-4-lin-3-1', 'xbeam-1-2-4-lin-4-1', 
    'xbeam-1-2-4-lin-5-1', 'xbeam-1-2-4-rebar-5-2-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-2-lin-3-1', 'xbeam-1-2-4-rebar-5-2-lin-4-1', 
    'xbeam-1-2-4-rebar-5-2-lin-5-1', 'xbeam-1-2-4-rebar-5-4-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-4-lin-3-1', 'xbeam-1-2-4-rebar-5-4-lin-4-1', 
    'xbeam-1-2-4-rebar-5-4-lin-5-1', 'xbeam-1-2-4-rebar-5-6-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-6-lin-3-1', 'xbeam-1-2-4-rebar-5-6-lin-4-1', 
    'xbeam-1-2-4-rebar-5-6-lin-5-1', 'xbeam-2-1-4-lin-2-1-1', 
    'xbeam-2-1-4-lin-3-1', 'xbeam-2-1-4-lin-4-1', 'xbeam-2-1-4-lin-5-1', 
    'xbeam-2-1-4-rebar-5-2-lin-2-1-1', 'xbeam-2-1-4-rebar-5-2-lin-3-1', 
    'xbeam-2-1-4-rebar-5-2-lin-4-1', 'xbeam-2-1-4-rebar-5-2-lin-5-1', 
    'xbeam-2-1-4-rebar-5-4-lin-2-1-1', 'xbeam-2-1-4-rebar-5-4-lin-3-1', 
    'xbeam-2-1-4-rebar-5-4-lin-4-1', 'xbeam-2-1-4-rebar-5-4-lin-5-1', 
    'xbeam-2-1-4-rebar-5-6-lin-2-1', 'xbeam-2-1-4-rebar-5-6-lin-3-1', 
    'xbeam-2-1-4-rebar-5-6-lin-4-1', 'xbeam-2-1-4-rebar-5-6-lin-5-1', 
    'zbeam-1-2-3-rebar-3-1-lin-2-1-1', 'zbeam-1-2-3-rebar-3-1-lin-3-1', 
    'zbeam-1-2-3-rebar-3-1-lin-4-1', 'zbeam-1-2-3-rebar-3-1-lin-5-1', 
    'zbeam-1-2-3-rebar-3-3-lin-2-1', 'zbeam-1-2-3-rebar-3-3-lin-3-1', 
    'zbeam-1-2-3-rebar-3-3-lin-4-1', 'zbeam-1-2-3-rebar-3-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-1-lin-2-1-1', 'xbeam-1-2-4-rebar-5-1-lin-3-1', 
    'xbeam-1-2-4-rebar-5-1-lin-4-1', 'xbeam-1-2-4-rebar-5-1-lin-5-1', 
    'xbeam-1-2-4-rebar-5-3-lin-2-1-1', 'xbeam-1-2-4-rebar-5-3-lin-3-1', 
    'xbeam-1-2-4-rebar-5-3-lin-4-1', 'xbeam-1-2-4-rebar-5-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-5-lin-2-1-1', 'xbeam-1-2-4-rebar-5-5-lin-3-1', 
    'xbeam-1-2-4-rebar-5-5-lin-4-1', 'xbeam-1-2-4-rebar-5-5-lin-5-1', 
    'xbeam-2-1-4-rebar-5-1-lin-2-1-1', 'xbeam-2-1-4-rebar-5-1-lin-3-1', 
    'xbeam-2-1-4-rebar-5-1-lin-4-1', 'xbeam-2-1-4-rebar-5-1-lin-5-1', 
    'xbeam-2-1-4-rebar-5-3-lin-2-1-1', 'xbeam-2-1-4-rebar-5-3-lin-3-1', 
    'xbeam-2-1-4-rebar-5-3-lin-4-1', 'xbeam-2-1-4-rebar-5-3-lin-5-1', 
    'xbeam-2-1-4-rebar-5-5-lin-2-1-1', 'xbeam-2-1-4-rebar-5-5-lin-3-1', 
    'xbeam-2-1-4-rebar-5-5-lin-4-1', 'xbeam-2-1-4-rebar-5-5-lin-5-1', 
    'col-2-2-4-rebar-2-1-lin-2-1-1', 'col-2-2-4-rebar-2-1-lin-3-1', 
    'col-2-2-4-rebar-2-1-lin-4-1', 'col-2-2-4-rebar-2-1-lin-5-1', 
    'col-2-2-4-rebar-2-2-lin-2-1-1', 'col-2-2-4-rebar-2-2-lin-3-1', 
    'col-2-2-4-rebar-2-2-lin-4-1', 'col-2-2-4-rebar-2-2-lin-5-1', 
    'col-2-2-4-rebar-2-4-lin-2-1-1', 'col-2-2-4-rebar-2-4-lin-3-1', 
    'col-2-2-4-rebar-2-4-lin-4-1', 'col-2-2-4-rebar-2-4-lin-5-1', 
    'col-2-2-4-rebar-2-3-lin-2-1-1', 'col-2-2-4-rebar-2-3-lin-3-1', 
    'col-2-2-4-rebar-2-3-lin-4-1', ))
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=67623.5, 
    farPlane=125218, width=49014.1, height=32288.4, viewOffsetX=894.997, 
    viewOffsetY=316.037)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72136.9, 
    farPlane=120705, width=13536.4, height=8917.16, viewOffsetX=-2945.78, 
    viewOffsetY=-1330.43)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72046.4, 
    farPlane=120795, width=13519.4, height=8905.98, viewOffsetX=-2622.61, 
    viewOffsetY=1388.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72149.5, 
    farPlane=120319, width=13538.7, height=8918.73, cameraPosition=(68184.6, 
    60782.6, 65148.5), cameraUpVector=(-0.634856, 0.642782, -0.428706), 
    cameraTarget=(7014.68, 12499.3, 8368.76), viewOffsetX=-2626.36, 
    viewOffsetY=1390.06)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73556.3, 
    farPlane=118912, width=1314.69, height=866.06, viewOffsetX=-5198.09, 
    viewOffsetY=2540.41)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 
    'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 
    'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6'), vector=(-100.0, 5000.0, 
    0.0))
#: The instances were translated by -100., 5.E+03, 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73332.1, 
    farPlane=119136, width=3541.81, height=2333.19, viewOffsetX=-4882.96, 
    viewOffsetY=2535.37)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73807.6, 
    farPlane=120419, width=3564.78, height=2348.32, cameraPosition=(58550.2, 
    66551.9, 70797.4), cameraUpVector=(-0.568419, 0.589734, -0.573684), 
    cameraTarget=(7636.85, 12308.7, 9458.36), viewOffsetX=-4914.63, 
    viewOffsetY=2551.81)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73804.8, 
    farPlane=120422, width=3564.65, height=2348.23, viewOffsetX=-4765.12, 
    viewOffsetY=1980.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73879.5, 
    farPlane=120604, width=3568.26, height=2350.61, cameraPosition=(55897.9, 
    70220.9, 69884.8), cameraUpVector=(-0.570603, 0.552353, -0.607716), 
    cameraTarget=(7728.29, 12365.1, 9640.5), viewOffsetX=-4769.94, 
    viewOffsetY=1982.94)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=71755.5, 
    farPlane=121086, width=15088.2, height=9939.41, viewOffsetX=-3309.4, 
    viewOffsetY=-56.8386)
session.viewports['Viewport: 1'].view.setValues(nearPlane=71861.6, 
    farPlane=120980, width=15110.5, height=9954.11, viewOffsetX=-2697.54, 
    viewOffsetY=-1615.81)
session.viewports['Viewport: 1'].view.setValues(nearPlane=71861.7, 
    farPlane=120980, width=15110.5, viewOffsetX=-3395.45, viewOffsetY=1469.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72868.1, 
    farPlane=119973, width=6056.71, height=3989.89, viewOffsetX=-4667.33, 
    viewOffsetY=1897.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72912.1, 
    farPlane=119929, width=6060.36, height=3992.3, viewOffsetX=-4442.32, 
    viewOffsetY=1696.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73482.1, 
    farPlane=119359, width=1080.09, height=711.517, viewOffsetX=-5316.48, 
    viewOffsetY=1379.14)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-1-2-4-lin-3-1'].vertices
e1 = a.instances['xbeam-1-2-4-lin-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[6], normal=e1[7], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73533.8, 
    farPlane=119308, width=661.549, height=435.799, viewOffsetX=-5437.28, 
    viewOffsetY=1607.68)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['xbeam-1-2-4-lin-3-1'].vertices
e11 = a.instances['col-2-2-4-lin-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[4], normal=e11[18], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73528.6, 
    farPlane=119313, width=703.726, height=463.584, viewOffsetX=-5365.34, 
    viewOffsetY=1625.78)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-1-2-4-lin-3-1'].vertices
e1 = a.instances['col-2-2-4-lin-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[9], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73471.1, 
    farPlane=119370, width=1322.38, height=871.124, viewOffsetX=-5320.3, 
    viewOffsetY=1525.55)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v11 = a.instances['zbeam-1-2-3-lin-3-1'].vertices
e11 = a.instances['col-2-2-4-lin-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[5], normal=e11[17], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['zbeam-2-1-3'].vertices
e1 = a.instances['col-2-2-4-lin-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[19], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73048.7, 
    farPlane=119793, width=5192.28, height=3420.44, viewOffsetX=-4343.63, 
    viewOffsetY=1162.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73013.1, 
    farPlane=119828, width=5189.75, height=3418.78, viewOffsetX=-4151.98, 
    viewOffsetY=1825.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72796.6, 
    farPlane=120045, width=7500.49, height=4941, viewOffsetX=-3594.68, 
    viewOffsetY=1760.16)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72745.5, 
    farPlane=120096, width=7495.23, height=4937.53, viewOffsetX=-3890.04, 
    viewOffsetY=2475.79)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72503.9, 
    farPlane=120338, width=10178.9, height=6705.42, viewOffsetX=-3597.16, 
    viewOffsetY=2534.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72435.2, 
    farPlane=120406, width=10169.3, height=6699.06, viewOffsetX=-3451.75, 
    viewOffsetY=3439.51)
a1 = mdb.models['structure'].rootAssembly
p = mdb.models['structure'].parts['beam-4']
a1.Instance(name='beam-4-2', part=p, dependent=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73239.9, 
    farPlane=119602, width=3042.69, height=2004.39, viewOffsetX=-4787.32, 
    viewOffsetY=4784.69)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('beam-4-2', ), vector=(4500.0, 21700.0, 11850.0))
#: The instance beam-4-2 was translated by 4.5E+03, 21.7E+03, 11.85E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73401.1, 
    farPlane=119440, width=1736.12, height=1143.68, viewOffsetX=-5276.94, 
    viewOffsetY=4725.93)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-1-2-4-lin-4-1'].vertices
e11 = a.instances['xbeam-1-2-4-lin-4-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73506.8, 
    farPlane=119335, width=880.258, height=579.875, viewOffsetX=-5508.75, 
    viewOffsetY=4981.27)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['xbeam-1-2-4-lin-4-1'].vertices
e1 = a.instances['xbeam-1-2-4-lin-4-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[4], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73476.3, 
    farPlane=119365, width=1275.45, height=840.209, viewOffsetX=-5440.12, 
    viewOffsetY=4892.5)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-1-2-4-lin-4-1'].vertices
e11 = a.instances['xbeam-1-2-4-lin-4-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73524.8, 
    farPlane=119317, width=734.299, height=483.724, viewOffsetX=-5608.51, 
    viewOffsetY=5030.21)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v1 = a.instances['zbeam-1-2-3-lin-4-1'].vertices
e1 = a.instances['col-2-2-4-lin-4-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[17], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72368.5, 
    farPlane=120473, width=11417.5, height=7521.35, viewOffsetX=-4548.12, 
    viewOffsetY=5206.28)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72291.7, 
    farPlane=120550, width=11405.4, height=7513.37, viewOffsetX=-2313.67, 
    viewOffsetY=3129.36)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    'beam-4-1', 'col-2-2-4-lin-2-1', 'zbeam-1-2-3-lin-2-1', 
    'zbeam-1-2-3-rebar-3-2-lin-2-1', 'zbeam-1-2-3-rebar-3-4-lin-2-1', 
    'zbeam-1-2-3-rebar-3-6-lin-2-1', 'xbeam-1-2-4-lin-2-1', 
    'xbeam-1-2-4-rebar-5-2-lin-2-1', 'xbeam-1-2-4-rebar-5-4-lin-2-1', 
    'xbeam-1-2-4-rebar-5-6-lin-2-1', 'xbeam-2-1-4-lin-2-1', 
    'xbeam-2-1-4-rebar-5-2-lin-2-1', 'xbeam-2-1-4-rebar-5-4-lin-2-1', 
    'zbeam-1-2-3-rebar-3-1-lin-2-1', 'xbeam-1-2-4-rebar-5-1-lin-2-1', 
    'xbeam-1-2-4-rebar-5-3-lin-2-1', 'xbeam-1-2-4-rebar-5-5-lin-2-1', 
    'xbeam-2-1-4-rebar-5-1-lin-2-1', 'xbeam-2-1-4-rebar-5-3-lin-2-1', 
    'xbeam-2-1-4-rebar-5-5-lin-2-1', 'col-2-2-4-rebar-2-1-lin-2-1', 
    'col-2-2-4-rebar-2-2-lin-2-1', 'col-2-2-4-rebar-2-4-lin-2-1', 
    'col-2-2-4-rebar-2-3-lin-2-1', 'col-2-2-4-lin-2-1-1', 'col-2-2-4-lin-3-1', 
    'col-2-2-4-lin-4-1', 'col-2-2-4-lin-5-1', 'zbeam-1-2-3-lin-2-1-1', 
    'zbeam-1-2-3-lin-3-1', 'zbeam-1-2-3-lin-4-1', 'zbeam-1-2-3-lin-5-1', 
    'zbeam-1-2-3-rebar-3-2-lin-2-1-1', 'zbeam-1-2-3-rebar-3-2-lin-3-1', 
    'zbeam-1-2-3-rebar-3-2-lin-4-1', 'zbeam-1-2-3-rebar-3-2-lin-5-1', 
    'zbeam-1-2-3-rebar-3-4-lin-2-1-1', 'zbeam-1-2-3-rebar-3-4-lin-3-1', 
    'zbeam-1-2-3-rebar-3-4-lin-4-1', 'zbeam-1-2-3-rebar-3-4-lin-5-1', 
    'zbeam-1-2-3-rebar-3-6-lin-2-1-1', 'zbeam-1-2-3-rebar-3-6-lin-3-1', 
    'zbeam-1-2-3-rebar-3-6-lin-4-1', 'zbeam-1-2-3-rebar-3-6-lin-5-1', 
    'xbeam-1-2-4-lin-2-1-1', 'xbeam-1-2-4-lin-3-1', 'xbeam-1-2-4-lin-4-1', 
    'xbeam-1-2-4-lin-5-1', 'xbeam-1-2-4-rebar-5-2-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-2-lin-3-1', 'xbeam-1-2-4-rebar-5-2-lin-4-1', 
    'xbeam-1-2-4-rebar-5-2-lin-5-1', 'xbeam-1-2-4-rebar-5-4-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-4-lin-3-1', 'xbeam-1-2-4-rebar-5-4-lin-4-1', 
    'xbeam-1-2-4-rebar-5-4-lin-5-1', 'xbeam-1-2-4-rebar-5-6-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-6-lin-3-1', 'xbeam-1-2-4-rebar-5-6-lin-4-1', 
    'xbeam-1-2-4-rebar-5-6-lin-5-1', 'xbeam-2-1-4-lin-2-1-1', 
    'xbeam-2-1-4-lin-3-1', 'xbeam-2-1-4-lin-4-1', 'xbeam-2-1-4-lin-5-1', 
    'xbeam-2-1-4-rebar-5-2-lin-2-1-1', 'xbeam-2-1-4-rebar-5-2-lin-3-1', 
    'xbeam-2-1-4-rebar-5-2-lin-4-1', 'xbeam-2-1-4-rebar-5-2-lin-5-1', 
    'xbeam-2-1-4-rebar-5-4-lin-2-1-1', 'xbeam-2-1-4-rebar-5-4-lin-3-1', 
    'xbeam-2-1-4-rebar-5-4-lin-4-1', 'xbeam-2-1-4-rebar-5-4-lin-5-1', 
    'xbeam-2-1-4-rebar-5-6-lin-2-1', 'xbeam-2-1-4-rebar-5-6-lin-3-1', 
    'xbeam-2-1-4-rebar-5-6-lin-4-1', 'xbeam-2-1-4-rebar-5-6-lin-5-1', 
    'zbeam-1-2-3-rebar-3-1-lin-2-1-1', 'zbeam-1-2-3-rebar-3-1-lin-3-1', 
    'zbeam-1-2-3-rebar-3-1-lin-4-1', 'zbeam-1-2-3-rebar-3-1-lin-5-1', 
    'zbeam-1-2-3-rebar-3-3-lin-2-1', 'zbeam-1-2-3-rebar-3-3-lin-3-1', 
    'zbeam-1-2-3-rebar-3-3-lin-4-1', 'zbeam-1-2-3-rebar-3-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-1-lin-2-1-1', 'xbeam-1-2-4-rebar-5-1-lin-3-1', 
    'xbeam-1-2-4-rebar-5-1-lin-4-1', 'xbeam-1-2-4-rebar-5-1-lin-5-1', 
    'xbeam-1-2-4-rebar-5-3-lin-2-1-1', 'xbeam-1-2-4-rebar-5-3-lin-3-1', 
    'xbeam-1-2-4-rebar-5-3-lin-4-1', 'xbeam-1-2-4-rebar-5-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-5-lin-2-1-1', 'xbeam-1-2-4-rebar-5-5-lin-3-1', 
    'xbeam-1-2-4-rebar-5-5-lin-4-1', 'xbeam-1-2-4-rebar-5-5-lin-5-1', 
    'xbeam-2-1-4-rebar-5-1-lin-2-1-1', 'xbeam-2-1-4-rebar-5-1-lin-3-1', 
    'xbeam-2-1-4-rebar-5-1-lin-4-1', 'xbeam-2-1-4-rebar-5-1-lin-5-1', 
    'xbeam-2-1-4-rebar-5-3-lin-2-1-1', 'xbeam-2-1-4-rebar-5-3-lin-3-1', 
    'xbeam-2-1-4-rebar-5-3-lin-4-1', 'xbeam-2-1-4-rebar-5-3-lin-5-1', 
    'xbeam-2-1-4-rebar-5-5-lin-2-1-1', 'xbeam-2-1-4-rebar-5-5-lin-3-1', 
    'xbeam-2-1-4-rebar-5-5-lin-4-1', 'xbeam-2-1-4-rebar-5-5-lin-5-1', 
    'col-2-2-4-rebar-2-1-lin-2-1-1', 'col-2-2-4-rebar-2-1-lin-3-1', 
    'col-2-2-4-rebar-2-1-lin-4-1', 'col-2-2-4-rebar-2-1-lin-5-1', 
    'col-2-2-4-rebar-2-2-lin-2-1-1', 'col-2-2-4-rebar-2-2-lin-3-1', 
    'col-2-2-4-rebar-2-2-lin-4-1', 'col-2-2-4-rebar-2-2-lin-5-1', 
    'col-2-2-4-rebar-2-4-lin-2-1-1', 'col-2-2-4-rebar-2-4-lin-3-1', 
    'col-2-2-4-rebar-2-4-lin-4-1', 'col-2-2-4-rebar-2-4-lin-5-1', 
    'col-2-2-4-rebar-2-3-lin-2-1-1', 'col-2-2-4-rebar-2-3-lin-3-1', 
    'col-2-2-4-rebar-2-3-lin-4-1', 'col-2-2-4-rebar-2-3-lin-5-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'col-2-2-4-rebar-2-1-lin-2-1', 'col-2-2-4-rebar-2-2-lin-2-1', 
    'col-2-2-4-rebar-2-4-lin-2-1', 'col-2-2-4-rebar-2-3-lin-2-1', 
    'col-2-2-4-lin-2-1-1', 'col-2-2-4-lin-3-1', 'col-2-2-4-lin-4-1', 
    'col-2-2-4-lin-5-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'beam-4-2', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=77952.8, 
    farPlane=114918, width=14205.7, height=9358.11, viewOffsetX=-2331.04, 
    viewOffsetY=3336.09)
session.viewports['Viewport: 1'].view.setValues(nearPlane=77857.7, 
    farPlane=115013, width=14188.4, height=9346.7, viewOffsetX=-3074.96, 
    viewOffsetY=1121.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=77012.4, 
    farPlane=112425, width=14034.4, height=9245.22, cameraPosition=(59234.9, 
    91910.1, 1877.31), cameraUpVector=(-0.967402, 0.251208, -0.0320687), 
    cameraTarget=(5151.67, 12268.8, 7283.64), viewOffsetX=-3041.57, 
    viewOffsetY=1108.97)
session.viewports['Viewport: 1'].view.setValues(nearPlane=76123.1, 
    farPlane=113491, width=13872.3, height=9138.48, cameraPosition=(-9297.35, 
    91514.2, -42897.9), cameraUpVector=(-0.36872, 0.146234, 0.917966), 
    cameraTarget=(2386.46, 11460.6, 9560.31), viewOffsetX=-3006.45, 
    viewOffsetY=1096.16)
session.viewports['Viewport: 1'].view.setValues(nearPlane=79176.1, 
    farPlane=114568, width=14428.7, height=9504.98, cameraPosition=(-36018.8, 
    100104, 5952.95), cameraUpVector=(0.209658, -0.229428, 0.950477), 
    cameraTarget=(2038.92, 11604.5, 10010.8), viewOffsetX=-3127.03, 
    viewOffsetY=1140.12)
session.viewports['Viewport: 1'].view.setValues(nearPlane=79982.3, 
    farPlane=113763, width=6520.62, height=4295.5, viewOffsetX=-3208.29, 
    viewOffsetY=3021.48)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-4-lin-3-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20040 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-9')
#: ???? 'Surf-9' ?????? (2 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=80029.6, 
    farPlane=113715, width=6524.48, height=4298.04, viewOffsetX=-2516.4, 
    viewOffsetY=5750.74)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-2929.87, 
    viewOffsetY=7608.78)
session.viewports['Viewport: 1'].view.setValues(nearPlane=79098.1, 
    farPlane=114647, width=16514.4, height=10879, viewOffsetX=-1686.88, 
    viewOffsetY=8571.73)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=51759.4, 
    farPlane=91589.6, width=27264.4, height=17960.6, viewOffsetX=-2145.74, 
    viewOffsetY=-1106)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51590.3, 
    farPlane=91758.6, width=27175.4, height=17902, viewOffsetX=-1905.22, 
    viewOffsetY=-1715.67)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47579.8, 
    farPlane=89327.9, width=25062.9, height=16510.3, cameraPosition=(30831.1, 
    73044.2, -15346.5), cameraUpVector=(-0.164595, 0.133903, 0.97723), 
    cameraTarget=(3509.3, 13021, 12724.4), viewOffsetX=-1757.11, 
    viewOffsetY=-1582.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50360.4, 
    farPlane=85525.7, width=26527.6, height=17475.2, cameraPosition=(-49208.3, 
    44822.8, -13808.7), cameraUpVector=(0.761446, 0.639877, -0.103717), 
    cameraTarget=(10489.4, 15440.2, 12838.9), viewOffsetX=-1859.8, 
    viewOffsetY=-1674.77)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52780.3, 
    farPlane=83105.8, width=4083.61, height=2690.1, viewOffsetX=2919.76, 
    viewOffsetY=-2255.92)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-4-lin-3-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#21042 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-10')
#: ???? 'Surf-10' ?????? (4 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=52159.9, 
    farPlane=83726.2, width=10292.9, height=6780.5, viewOffsetX=3023.22, 
    viewOffsetY=-2044.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52091.2, 
    farPlane=83794.9, width=10279.3, height=6771.58, viewOffsetX=5470.39, 
    viewOffsetY=753)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=52390.2, 
    farPlane=90958.8, width=21458.3, height=14135.8, viewOffsetX=-3353.03, 
    viewOffsetY=2992.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52259.7, 
    farPlane=91089.3, width=21404.9, height=14100.6, viewOffsetX=-4333.3, 
    viewOffsetY=1995.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=64577.1, 
    farPlane=88435.6, width=26449.9, height=17424.1, cameraPosition=(-69769.5, 
    15860.8, 2289.26), cameraUpVector=(0.314577, 0.810923, 0.493402), 
    cameraTarget=(490.693, 10172, 15265.3), viewOffsetX=-5354.64, 
    viewOffsetY=2466.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65487.5, 
    farPlane=87525.1, width=12765.6, height=8409.39, viewOffsetX=-4127.29, 
    viewOffsetY=4682.06)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65577.7, 
    farPlane=87435, width=12783.1, height=8420.97, viewOffsetX=-1922.35, 
    viewOffsetY=9208.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60433.9, 
    farPlane=87622.7, width=11780.5, height=7760.44, cameraPosition=(-61745.6, 
    22470.5, -18863.1), cameraUpVector=(0.203739, 0.758057, 0.619548), 
    cameraTarget=(1252.41, 10797.6, 13265.3), viewOffsetX=-1771.56, 
    viewOffsetY=8485.81)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61334.3, 
    farPlane=86722.3, width=4726.12, height=3113.36, viewOffsetX=-2907.57, 
    viewOffsetY=8750.36)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-4-lin-4-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#11082 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-11')
#: ???? 'Surf-11' ?????? (4 ??).
session.viewports['Viewport: 1'].view.setValues(session.views['User-1'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    'beam-4-1', 'col-2-2-4-lin-2-1', 'zbeam-1-2-3-lin-2-1', 
    'zbeam-1-2-3-rebar-3-2-lin-2-1', 'zbeam-1-2-3-rebar-3-4-lin-2-1', 
    'zbeam-1-2-3-rebar-3-6-lin-2-1', 'xbeam-1-2-4-lin-2-1', 
    'xbeam-1-2-4-rebar-5-2-lin-2-1', 'xbeam-1-2-4-rebar-5-4-lin-2-1', 
    'xbeam-1-2-4-rebar-5-6-lin-2-1', 'xbeam-2-1-4-lin-2-1', 
    'xbeam-2-1-4-rebar-5-2-lin-2-1', 'xbeam-2-1-4-rebar-5-4-lin-2-1', 
    'zbeam-1-2-3-rebar-3-1-lin-2-1', 'xbeam-1-2-4-rebar-5-1-lin-2-1', 
    'xbeam-1-2-4-rebar-5-3-lin-2-1', 'xbeam-1-2-4-rebar-5-5-lin-2-1', 
    'xbeam-2-1-4-rebar-5-1-lin-2-1', 'xbeam-2-1-4-rebar-5-3-lin-2-1', 
    'xbeam-2-1-4-rebar-5-5-lin-2-1', 'col-2-2-4-rebar-2-1-lin-2-1', 
    'col-2-2-4-rebar-2-2-lin-2-1', 'col-2-2-4-rebar-2-4-lin-2-1', 
    'col-2-2-4-rebar-2-3-lin-2-1', 'col-2-2-4-lin-2-1-1', 'col-2-2-4-lin-3-1', 
    'col-2-2-4-lin-4-1', 'col-2-2-4-lin-5-1', 'zbeam-1-2-3-lin-2-1-1', 
    'zbeam-1-2-3-lin-3-1', 'zbeam-1-2-3-lin-4-1', 'zbeam-1-2-3-lin-5-1', 
    'zbeam-1-2-3-rebar-3-2-lin-2-1-1', 'zbeam-1-2-3-rebar-3-2-lin-3-1', 
    'zbeam-1-2-3-rebar-3-2-lin-4-1', 'zbeam-1-2-3-rebar-3-2-lin-5-1', 
    'zbeam-1-2-3-rebar-3-4-lin-2-1-1', 'zbeam-1-2-3-rebar-3-4-lin-3-1', 
    'zbeam-1-2-3-rebar-3-4-lin-4-1', 'zbeam-1-2-3-rebar-3-4-lin-5-1', 
    'zbeam-1-2-3-rebar-3-6-lin-2-1-1', 'zbeam-1-2-3-rebar-3-6-lin-3-1', 
    'zbeam-1-2-3-rebar-3-6-lin-4-1', 'zbeam-1-2-3-rebar-3-6-lin-5-1', 
    'xbeam-1-2-4-lin-2-1-1', 'xbeam-1-2-4-lin-3-1', 'xbeam-1-2-4-lin-4-1', 
    'xbeam-1-2-4-lin-5-1', 'xbeam-1-2-4-rebar-5-2-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-2-lin-3-1', 'xbeam-1-2-4-rebar-5-2-lin-4-1', 
    'xbeam-1-2-4-rebar-5-2-lin-5-1', 'xbeam-1-2-4-rebar-5-4-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-4-lin-3-1', 'xbeam-1-2-4-rebar-5-4-lin-4-1', 
    'xbeam-1-2-4-rebar-5-4-lin-5-1', 'xbeam-1-2-4-rebar-5-6-lin-2-1-1', 
    'xbeam-1-2-4-rebar-5-6-lin-3-1', 'xbeam-1-2-4-rebar-5-6-lin-4-1', 
    'xbeam-1-2-4-rebar-5-6-lin-5-1', 'xbeam-2-1-4-lin-2-1-1', 
    'xbeam-2-1-4-lin-3-1', 'xbeam-2-1-4-lin-4-1', 'xbeam-2-1-4-lin-5-1', 
    'xbeam-2-1-4-rebar-5-2-lin-2-1-1', 'xbeam-2-1-4-rebar-5-2-lin-3-1', 
    'xbeam-2-1-4-rebar-5-2-lin-4-1', 'xbeam-2-1-4-rebar-5-2-lin-5-1', 
    'xbeam-2-1-4-rebar-5-4-lin-2-1-1', 'xbeam-2-1-4-rebar-5-4-lin-3-1', 
    'xbeam-2-1-4-rebar-5-4-lin-4-1', 'xbeam-2-1-4-rebar-5-4-lin-5-1', 
    'xbeam-2-1-4-rebar-5-6-lin-2-1', 'xbeam-2-1-4-rebar-5-6-lin-3-1', 
    'xbeam-2-1-4-rebar-5-6-lin-4-1', 'xbeam-2-1-4-rebar-5-6-lin-5-1', 
    'zbeam-1-2-3-rebar-3-1-lin-2-1-1', 'zbeam-1-2-3-rebar-3-1-lin-3-1', 
    'zbeam-1-2-3-rebar-3-1-lin-4-1', 'zbeam-1-2-3-rebar-3-1-lin-5-1', 
    'zbeam-1-2-3-rebar-3-3-lin-2-1', 'zbeam-1-2-3-rebar-3-3-lin-3-1', 
    'zbeam-1-2-3-rebar-3-3-lin-4-1', 'zbeam-1-2-3-rebar-3-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-1-lin-2-1-1', 'xbeam-1-2-4-rebar-5-1-lin-3-1', 
    'xbeam-1-2-4-rebar-5-1-lin-4-1', 'xbeam-1-2-4-rebar-5-1-lin-5-1', 
    'xbeam-1-2-4-rebar-5-3-lin-2-1-1', 'xbeam-1-2-4-rebar-5-3-lin-3-1', 
    'xbeam-1-2-4-rebar-5-3-lin-4-1', 'xbeam-1-2-4-rebar-5-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-5-lin-2-1-1', 'xbeam-1-2-4-rebar-5-5-lin-3-1', 
    'xbeam-1-2-4-rebar-5-5-lin-4-1', 'xbeam-1-2-4-rebar-5-5-lin-5-1', 
    'xbeam-2-1-4-rebar-5-1-lin-2-1-1', 'xbeam-2-1-4-rebar-5-1-lin-3-1', 
    'xbeam-2-1-4-rebar-5-1-lin-4-1', 'xbeam-2-1-4-rebar-5-1-lin-5-1', 
    'xbeam-2-1-4-rebar-5-3-lin-2-1-1', 'xbeam-2-1-4-rebar-5-3-lin-3-1', 
    'xbeam-2-1-4-rebar-5-3-lin-4-1', 'xbeam-2-1-4-rebar-5-3-lin-5-1', 
    'xbeam-2-1-4-rebar-5-5-lin-2-1-1', 'xbeam-2-1-4-rebar-5-5-lin-3-1', 
    'xbeam-2-1-4-rebar-5-5-lin-4-1', 'xbeam-2-1-4-rebar-5-5-lin-5-1', 
    'col-2-2-4-rebar-2-1-lin-2-1-1', 'col-2-2-4-rebar-2-1-lin-3-1', 
    'col-2-2-4-rebar-2-1-lin-4-1', 'col-2-2-4-rebar-2-1-lin-5-1', 
    'col-2-2-4-rebar-2-2-lin-2-1-1', 'col-2-2-4-rebar-2-2-lin-3-1', 
    'col-2-2-4-rebar-2-2-lin-4-1', 'col-2-2-4-rebar-2-2-lin-5-1', 
    'col-2-2-4-rebar-2-4-lin-2-1-1', 'col-2-2-4-rebar-2-4-lin-3-1', 
    'col-2-2-4-rebar-2-4-lin-4-1', 'col-2-2-4-rebar-2-4-lin-5-1', 
    'col-2-2-4-rebar-2-3-lin-2-1-1', 'col-2-2-4-rebar-2-3-lin-3-1', 
    'col-2-2-4-rebar-2-3-lin-4-1', 'col-2-2-4-rebar-2-3-lin-5-1', 'beam-4-2', 
    ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=44513.9, 
    farPlane=98806.2, width=35139.6, height=23148.4, viewOffsetX=1622.99, 
    viewOffsetY=2114.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47150.9, 
    farPlane=96169.2, width=13830.5, height=9110.89, viewOffsetX=-3133.33, 
    viewOffsetY=5014.97)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47246.2, 
    farPlane=96073.9, width=13858.4, height=9129.31, viewOffsetX=-3854.17, 
    viewOffsetY=5888.89)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47662.1, 
    farPlane=95658, width=10915.2, height=7190.45, viewOffsetX=-4041.37, 
    viewOffsetY=5748.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50826, 
    farPlane=98373.1, width=11639.8, height=7667.76, cameraPosition=(33493.3, 
    68580.5, 50493.4), cameraUpVector=(-0.54159, 0.369013, -0.755321), 
    cameraTarget=(7984.41, 14630.3, 10795.8), viewOffsetX=-4309.64, 
    viewOffsetY=6130.22)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50742.1, 
    farPlane=98456.8, width=11620.6, height=7655.14, viewOffsetX=-2779.75, 
    viewOffsetY=4122.03)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50580.3, 
    farPlane=98296.5, width=11583.6, height=7630.73, cameraPosition=(35702.8, 
    68875.7, 48328.3), cameraUpVector=(-0.539903, 0.361279, -0.760252), 
    cameraTarget=(7968.39, 14501.2, 10759.2), viewOffsetX=-2770.89, 
    viewOffsetY=4108.89)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51747.6, 
    farPlane=97129.2, width=1469.58, height=968.092, viewOffsetX=-4585.61, 
    viewOffsetY=5107.03)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('beam-4-2', ), vector=(0.0, 5000.0, 0.0))
#: The instance beam-4-2 was translated by 0., 5.E+03, 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51541, 
    farPlane=97335.8, width=3554.52, height=2341.56, viewOffsetX=-4242.8, 
    viewOffsetY=4865.33)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51516.7, 
    farPlane=97360.2, width=3552.84, height=2340.45, viewOffsetX=-4473.57, 
    viewOffsetY=4931.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50515.8, 
    farPlane=98361.1, width=12932.7, height=8519.49, viewOffsetX=-2872.69, 
    viewOffsetY=4941.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50430.6, 
    farPlane=98446.2, width=12910.9, height=8505.13, viewOffsetX=-2035.78, 
    viewOffsetY=4545.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51407.8, 
    farPlane=97469, width=4224.13, height=2782.67, viewOffsetX=-2252.67, 
    viewOffsetY=4473.82)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('beam-4-2', ), vector=(-9000.0, -20000.0, -15800.0))
#: The instance beam-4-2 was translated by -9.E+03, -20.E+03, -15.8E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50830.7, 
    farPlane=98220.3, width=10054.6, height=6623.51, viewOffsetX=-1086.27, 
    viewOffsetY=4801.63)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50763.6, 
    farPlane=98287.3, width=10041.3, height=6614.78, viewOffsetX=-1591.76, 
    viewOffsetY=3727)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50763.6, 
    width=10041.3, height=6614.78, viewOffsetX=-2659.53, viewOffsetY=1450.13)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50857.4, 
    farPlane=98193.5, width=9810.21, height=6462.54, viewOffsetX=-2460.61, 
    viewOffsetY=1246.78)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50791.9, 
    farPlane=98259, width=9797.58, height=6454.22, viewOffsetX=-2415.34, 
    viewOffsetY=3730)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51614, 
    farPlane=97436.9, width=2552.15, height=1681.24, viewOffsetX=-4274.97, 
    viewOffsetY=5138.09)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 
    'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 
    'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6'), vector=(50.0, 10000.0, 
    0.0))
#: The instances were translated by 50., 10.E+03, 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51307.3, 
    farPlane=97743.6, width=5694.14, height=3751.05, viewOffsetX=-3544.84, 
    viewOffsetY=4938.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51268.6, 
    farPlane=97782.3, width=5689.85, height=3748.22, viewOffsetX=-3707.18, 
    viewOffsetY=4629.28)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53947.9, 
    farPlane=98401.7, width=5987.2, height=3944.1, cameraPosition=(19802.4, 
    71719.5, 55136.5), cameraUpVector=(-0.425231, 0.313949, -0.84889), 
    cameraTarget=(7543.58, 15535.7, 12354.2), viewOffsetX=-3900.92, 
    viewOffsetY=4871.21)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53913.8, 
    farPlane=98435.8, width=5983.42, height=3941.61, viewOffsetX=-2098.93, 
    viewOffsetY=4790.97)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53513.8, 
    farPlane=98470.9, width=5939.03, height=3912.37, cameraPosition=(21481.9, 
    70408.4, 55952), cameraUpVector=(-0.435939, 0.337777, -0.834185), 
    cameraTarget=(7648.95, 15320.7, 12234.5), viewOffsetX=-2083.36, 
    viewOffsetY=4755.42)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53834.9, 
    farPlane=98149.8, width=3024.96, height=1992.71, viewOffsetX=-2297.31, 
    viewOffsetY=4791.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53857, 
    farPlane=98127.7, width=3026.21, height=1993.53, viewOffsetX=-2246.25, 
    viewOffsetY=4916.56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53441.5, 
    farPlane=98184, width=3002.87, height=1978.16, cameraPosition=(24546.3, 
    70541.9, 54438.1), cameraUpVector=(-0.453949, 0.337544, -0.824618), 
    cameraTarget=(7819.42, 15231.5, 12033), viewOffsetX=-2228.92, 
    viewOffsetY=4878.63)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53444.2, 
    farPlane=98181.3, width=3003.02, height=1978.26, viewOffsetX=-2812.87, 
    viewOffsetY=5114.46)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52594.3, 
    farPlane=99031.3, width=10970.6, height=7226.96, viewOffsetX=-2471.73, 
    viewOffsetY=4534.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52521.3, 
    farPlane=99104.3, width=10955.4, height=7216.93, viewOffsetX=-1903.47, 
    viewOffsetY=5058.48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51538.5, 
    farPlane=98971.7, width=10750.4, height=7081.89, cameraPosition=(27974.6, 
    65463.6, 57963.6), cameraUpVector=(-0.473257, 0.420415, -0.774131), 
    cameraTarget=(7997.69, 14534.9, 11655.7), viewOffsetX=-1867.85, 
    viewOffsetY=4963.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50980.3, 
    farPlane=99530, width=16736.5, height=11025.3, viewOffsetX=-308.438, 
    viewOffsetY=8047.52)
a1 = mdb.models['structure'].rootAssembly
a1.rotate(instanceList=('zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 
    'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 
    'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 'col-2-2-4-lin-5-1', 
    'zbeam-1-2-3-lin-5-1', 'zbeam-1-2-3-rebar-3-2-lin-5-1', 
    'zbeam-1-2-3-rebar-3-4-lin-5-1', 'zbeam-1-2-3-rebar-3-6-lin-5-1', 
    'xbeam-1-2-4-lin-5-1', 'xbeam-1-2-4-rebar-5-2-lin-5-1', 
    'xbeam-1-2-4-rebar-5-4-lin-5-1', 'xbeam-1-2-4-rebar-5-6-lin-5-1', 
    'xbeam-2-1-4-lin-5-1', 'xbeam-2-1-4-rebar-5-2-lin-5-1', 
    'xbeam-2-1-4-rebar-5-4-lin-5-1', 'xbeam-2-1-4-rebar-5-6-lin-5-1', 
    'zbeam-1-2-3-rebar-3-1-lin-5-1', 'zbeam-1-2-3-rebar-3-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-1-lin-5-1', 'xbeam-1-2-4-rebar-5-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-5-lin-5-1', 'xbeam-2-1-4-rebar-5-1-lin-5-1', 
    'xbeam-2-1-4-rebar-5-3-lin-5-1', 'xbeam-2-1-4-rebar-5-5-lin-5-1', 
    'col-2-2-4-rebar-2-1-lin-5-1', 'col-2-2-4-rebar-2-2-lin-5-1', 
    'col-2-2-4-rebar-2-4-lin-5-1', 'col-2-2-4-rebar-2-3-lin-5-1'), axisPoint=(
    4500.0, 27300.0, 15950.0), axisDirection=(0.0, -600.0, 0.0), angle=90.0)
#: The instances were rotated by 90. ??(???????? 4.5E+03, 27.3E+03, 15.95E+03 ?????? 0., -600., 0. ??????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52593.2, 
    farPlane=97917.1, width=1756.7, height=1157.23, viewOffsetX=-3152.94, 
    viewOffsetY=6422.42)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-5-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-1-3'].vertices
e11 = a.instances['zbeam-2-1-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52677.6, 
    farPlane=97832.6, width=1072.55, height=706.547, viewOffsetX=-3293.19, 
    viewOffsetY=6522.46)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-5-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['zbeam-2-1-3'].vertices
e1 = a.instances['zbeam-2-1-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e1[4], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-4-lin-5-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-1-3'].vertices
e11 = a.instances['col-2-2-4-lin-5-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e11[9], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49926.5, 
    farPlane=100584, width=26344, height=17354.3, viewOffsetX=-2826.17, 
    viewOffsetY=6839.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49763.1, 
    farPlane=100747, width=26257.8, height=17297.5, viewOffsetX=426.526, 
    viewOffsetY=3374.11)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51404.1, 
    farPlane=99106.2, width=11406.1, height=7513.87, viewOffsetX=-1527.94, 
    viewOffsetY=4937.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51484.1, 
    farPlane=99026.2, width=11423.9, height=7525.56, viewOffsetX=-2021.14, 
    viewOffsetY=5694.05)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-2610.13, 
    viewOffsetY=5890.48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51759.5, 
    farPlane=98750.7, width=9617.48, height=6335.57, viewOffsetX=-2782.79, 
    viewOffsetY=6105.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51695.2, 
    farPlane=98815, width=9605.53, height=6327.7, viewOffsetX=-2799.96, 
    viewOffsetY=6294.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52461, 
    farPlane=98049.2, width=2827.9, height=1862.9, viewOffsetX=-3431.59, 
    viewOffsetY=6423.86)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-4-lin-5-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#840 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-12')
#: ???? 'Surf-12' ?????? (2 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=52679.2, 
    farPlane=97831.1, width=1199.03, height=789.869, viewOffsetX=-3480.4, 
    viewOffsetY=6918.48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52670.9, 
    farPlane=97839.4, width=1198.84, height=789.744, viewOffsetX=-3481.13, 
    viewOffsetY=6581.13)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52739.5, 
    farPlane=97770.8, width=571.296, height=376.345, viewOffsetX=-3607.79, 
    viewOffsetY=6511.77)
a1 = mdb.models['structure'].rootAssembly
a1.rotate(instanceList=('zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 
    'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 
    'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 'col-2-2-4-lin-5-1', 
    'zbeam-1-2-3-lin-5-1', 'zbeam-1-2-3-rebar-3-2-lin-5-1', 
    'zbeam-1-2-3-rebar-3-4-lin-5-1', 'zbeam-1-2-3-rebar-3-6-lin-5-1', 
    'xbeam-1-2-4-lin-5-1', 'xbeam-1-2-4-rebar-5-2-lin-5-1', 
    'xbeam-1-2-4-rebar-5-4-lin-5-1', 'xbeam-1-2-4-rebar-5-6-lin-5-1', 
    'xbeam-2-1-4-lin-5-1', 'xbeam-2-1-4-rebar-5-2-lin-5-1', 
    'xbeam-2-1-4-rebar-5-4-lin-5-1', 'xbeam-2-1-4-rebar-5-6-lin-5-1', 
    'zbeam-1-2-3-rebar-3-1-lin-5-1', 'zbeam-1-2-3-rebar-3-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-1-lin-5-1', 'xbeam-1-2-4-rebar-5-3-lin-5-1', 
    'xbeam-1-2-4-rebar-5-5-lin-5-1', 'xbeam-2-1-4-rebar-5-1-lin-5-1', 
    'xbeam-2-1-4-rebar-5-3-lin-5-1', 'xbeam-2-1-4-rebar-5-5-lin-5-1', 
    'col-2-2-4-rebar-2-1-lin-5-1', 'col-2-2-4-rebar-2-2-lin-5-1', 
    'col-2-2-4-rebar-2-4-lin-5-1', 'col-2-2-4-rebar-2-3-lin-5-1'), axisPoint=(
    4100.0, 27300.0, 16000.0), axisDirection=(0.0, -600.0, 0.0), angle=90.0)
#: The instances were rotated by 90. ??(???????? 4.1E+03, 27.3E+03, 16.E+03 ?????? 0., -600., 0. ??????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51341.3, 
    farPlane=99104.4, width=11391.5, height=7504.25, viewOffsetX=-1409.39, 
    viewOffsetY=5622.45)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51421.2, 
    farPlane=99024.5, width=11409.3, height=7515.92, viewOffsetX=-492.469, 
    viewOffsetY=3461.02)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=70903.3, 
    farPlane=123229, width=25979.6, height=17114.2, viewOffsetX=-3137.82, 
    viewOffsetY=1507.28)
session.viewports['Viewport: 1'].view.setValues(nearPlane=71079.2, 
    farPlane=123054, width=26044.1, height=17156.7, viewOffsetX=-3229.53, 
    viewOffsetY=7388.51)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72219.6, 
    farPlane=121913, width=17230.2, height=11350.5, viewOffsetX=-3688.29, 
    viewOffsetY=8780.98)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72105.7, 
    farPlane=122027, width=17203, height=11332.6, viewOffsetX=-2370.53, 
    viewOffsetY=5328.54)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72105.6, 
    farPlane=122027, width=17203, height=11332.6, viewOffsetX=715.297, 
    viewOffsetY=577.352)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72105.6, 
    farPlane=122027, height=11332.6, viewOffsetX=4484.81, viewOffsetY=-2066.31)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=7570.64, 
    viewOffsetY=-4451.15)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=3025.05, 
    viewOffsetY=-6540.19)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-161831.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x000000001235A2A8>materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35461.4, 
    farPlane=62271.6, width=21267.2, height=14009.9, viewOffsetX=3129.54, 
    viewOffsetY=2102.63)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35538.3, 
    farPlane=62194.8, width=21313.3, height=14040.3, viewOffsetX=-572.329, 
    viewOffsetY=870.361)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37346.7, 
    farPlane=60386.3, width=5396.95, height=3555.27, viewOffsetX=-6321.8, 
    viewOffsetY=2300.61)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37385.3, 
    farPlane=60347.7, width=5402.52, height=3558.94, viewOffsetX=-6914.43, 
    viewOffsetY=1844.33)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-6891.22, 
    viewOffsetY=2076.56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37761.9, 
    farPlane=59971.1, width=2294.77, height=1511.69, viewOffsetX=-7819.84, 
    viewOffsetY=2573.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37746.1, 
    farPlane=59986.9, width=2293.81, height=1511.06, viewOffsetX=-7737.73, 
    viewOffsetY=2259.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37337.2, 
    farPlane=60395.8, width=6181.6, height=4072.17, viewOffsetX=-6779.56, 
    viewOffsetY=1903.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37295.7, 
    farPlane=60437.3, width=6174.72, height=4067.64, viewOffsetX=-6619.48, 
    viewOffsetY=1543.41)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37847.6, 
    farPlane=59885.4, width=1334.12, height=878.859, viewOffsetX=-7765.7, 
    viewOffsetY=962.166)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['col-2-1-4'].vertices
v2 = a.instances['xbeam-2-1-4'].vertices
v3 = a.instances['zbeam-1-1-3'].vertices
a.PartitionCellByPlaneThreePoints(point1=v1[3], point2=v2[4], point3=v3[1], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37445.4, 
    farPlane=60287.6, width=5191.44, height=3419.89, viewOffsetX=-6876.32, 
    viewOffsetY=1264.42)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37410.4, 
    farPlane=60322.6, width=5186.58, height=3416.69, viewOffsetX=-6853.17, 
    viewOffsetY=1915.37)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37662, 
    farPlane=60071, width=3208.94, height=2113.91, viewOffsetX=-7716.45, 
    viewOffsetY=2326.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37640.1, 
    farPlane=60092.9, width=3207.07, height=2112.68, viewOffsetX=-7384.71, 
    viewOffsetY=1304.72)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#3 ]', ), )
v11 = a.instances['col-2-1-4'].vertices
a.PartitionCellByPlaneThreePoints(point1=v11[6], point2=v11[5], point3=v11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37283.3, 
    farPlane=60449.7, width=6674.8, height=4397.06, viewOffsetX=-6590.97, 
    viewOffsetY=1528.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37238.6, 
    farPlane=60494.4, width=6666.8, height=4391.79, viewOffsetX=-6382.56, 
    viewOffsetY=2687.17)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40702.8, 
    farPlane=63202.4, width=7287, height=4800.35, cameraPosition=(22576.9, 
    29312.5, 50591.2), cameraUpVector=(-0.429067, 0.620342, -0.656565), 
    cameraTarget=(8650.78, 4134.3, 11093.6), viewOffsetX=-6976.32, 
    viewOffsetY=2937.15)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41138.9, 
    farPlane=62766.4, width=2736.67, height=1802.8, viewOffsetX=-7613.97, 
    viewOffsetY=3130.75)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41158.9, 
    farPlane=62746.5, width=2738, height=1803.67, viewOffsetX=-7705.89, 
    viewOffsetY=3038.11)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-1-4'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#8224 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-2')
#: ???? 'Surf-2' ?????? (4 ??).
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v1 = a.instances['xbeam-2-1-4'].vertices
e1 = a.instances['xbeam-2-1-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[4], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v11 = a.instances['xbeam-2-1-4'].vertices
e11 = a.instances['xbeam-2-1-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38902.4, 
    farPlane=65002.9, width=23507.3, height=15485.6, viewOffsetX=-2489.47, 
    viewOffsetY=4276.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38759.2, 
    farPlane=65146.2, width=23420.7, height=15428.5, viewOffsetX=3205.06, 
    viewOffsetY=2851.56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38558.6, 
    farPlane=65582.9, width=23299.5, height=15348.7, cameraPosition=(26122.3, 
    27230.7, 50488.5), cameraUpVector=(-0.417568, 0.664201, -0.620059), 
    cameraTarget=(8774.17, 4081.68, 11104.5), viewOffsetX=3188.48, 
    viewOffsetY=2836.81)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38903.6, 
    farPlane=66349.9, width=23508, height=15486, cameraPosition=(30956.5, 
    28855.8, 47674.2), cameraUpVector=(-0.406572, 0.653337, -0.638631), 
    cameraTarget=(9024.81, 4626.89, 11343.9), viewOffsetX=3217.01, 
    viewOffsetY=2862.19)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41031, 
    farPlane=64222.5, width=4683.42, height=3085.23, viewOffsetX=4250.99, 
    viewOffsetY=4301.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41064.8, 
    farPlane=64188.7, width=4687.27, height=3087.77, viewOffsetX=4350.14, 
    viewOffsetY=4531.43)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43280.8, 
    farPlane=64988.8, width=4940.21, height=3254.39, cameraPosition=(30527.1, 
    39989.6, 40676.3), cameraUpVector=(-0.470576, 0.4573, -0.754609), 
    cameraTarget=(9487.19, 6533.93, 11936.5), viewOffsetX=4584.89, 
    viewOffsetY=4775.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43251.8, 
    farPlane=65017.8, width=4936.9, height=3252.22, viewOffsetX=5165.13, 
    viewOffsetY=5557.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45233.2, 
    farPlane=65515.6, width=5163.08, height=3401.21, cameraPosition=(30280.6, 
    46401.4, 34563.3), cameraUpVector=(-0.490785, 0.318616, -0.810934), 
    cameraTarget=(9652.89, 8287.23, 11985.7), viewOffsetX=5401.75, 
    viewOffsetY=5812.58)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45207.3, 
    farPlane=65541.6, width=5160.13, height=3399.27, viewOffsetX=5415.29, 
    viewOffsetY=6064.34)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45536.5, 
    farPlane=65212.5, width=2185.76, height=1439.88, viewOffsetX=5280.58, 
    viewOffsetY=6187.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45552.5, 
    farPlane=65196.5, width=2186.52, height=1440.39, viewOffsetX=5277.74, 
    viewOffsetY=6187.55)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44662.5, 
    farPlane=66086.5, width=10452, height=6885.29, viewOffsetX=6934.51, 
    viewOffsetY=5993.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44595, 
    farPlane=66153.9, width=10436.2, height=6874.9, viewOffsetX=5657.35, 
    viewOffsetY=4997.08)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=5489.21, 
    viewOffsetY=4570.9)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=5444.37, 
    viewOffsetY=3415.74)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44949.2, 
    farPlane=65799.8, width=7847.11, height=5169.33, viewOffsetX=5608.45, 
    viewOffsetY=2807.58)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44896.6, 
    farPlane=65852.4, width=7837.93, height=5163.28, viewOffsetX=6241.72, 
    viewOffsetY=7066.32)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45442.5, 
    farPlane=65306.5, width=2947.78, height=1941.87, viewOffsetX=5586.51, 
    viewOffsetY=6670.67)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 
    'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 
    'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6'), vector=(-4550.0, 0.0, 
    -6600.0))
#: The instances were translated by -4.55E+03, 0., -6.6E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45340.8, 
    farPlane=68249.6, width=4263.4, height=2808.54, viewOffsetX=5702.54, 
    viewOffsetY=6785.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45311.7, 
    farPlane=68278.7, width=4260.67, height=2806.74, viewOffsetX=5680.58, 
    viewOffsetY=6140.39)


session.viewports['Viewport: 1'].view.setValues(nearPlane=45359.3, 
    farPlane=68231.1, width=4094.28, height=2697.13, viewOffsetX=5640.68, 
    viewOffsetY=6205.57)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45331.3, 
    farPlane=68259.1, width=4091.76, height=2695.47, viewOffsetX=5694.34, 
    viewOffsetY=5251.96)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-2-1'].vertices
v2 = a.instances['col-2-3-1'].vertices
v3 = a.instances['col-1-3-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v1[2], point2=v2[5], point3=v3[3], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44532.4, 
    farPlane=69058, width=11656.9, height=7679.07, viewOffsetX=6772.67, 
    viewOffsetY=5686.24)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44455.7, 
    farPlane=69134.7, width=11636.9, height=7665.85, viewOffsetX=7073.5, 
    viewOffsetY=4776.06)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45139.5, 
    farPlane=68450.9, width=6105.74, height=4022.2, viewOffsetX=8601.45, 
    viewOffsetY=5231.54)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45098.3, 
    farPlane=68492.2, width=6100.16, height=4018.52, viewOffsetX=6470.65, 
    viewOffsetY=4584.32)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44224.6, 
    farPlane=69365.8, width=14467.6, height=9530.65, viewOffsetX=8149.71, 
    viewOffsetY=4463.58)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44130.8, 
    farPlane=69459.6, width=14437, height=9510.44, viewOffsetX=8349.53, 
    viewOffsetY=7510.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45129.5, 
    farPlane=68460.9, width=5485.82, height=3613.82, viewOffsetX=7787.66, 
    viewOffsetY=8667.65)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 
    'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 
    'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6'), vector=(-4450.0, 0.0, 
    -6150.0))
#: The instances were translated by -4.45E+03, 0., -6.15E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44379.7, 
    farPlane=69210.7, width=13051.6, height=8597.82, viewOffsetX=8377.91, 
    viewOffsetY=9033.11)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44294.5, 
    farPlane=69295.9, width=13026.5, height=8581.3, viewOffsetX=8487.74, 
    viewOffsetY=5782.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45158.6, 
    farPlane=68431.8, width=5249.74, height=3458.29, viewOffsetX=8583.86, 
    viewOffsetY=4861.22)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('col-2-4-1', 'col-2-4-1-rebar-2-1', 
    'col-2-4-1-rebar-2-2', 'col-2-4-1-rebar-2-3', 'col-2-4-1-rebar-2-4'), 
    vector=(0.0, 1650.0, 0.0))
#: The instances were translated by 0., 1.65E+03, 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42803.4, 
    farPlane=69500.1, width=13931.6, height=9177.53, viewOffsetX=8097.59, 
    viewOffsetY=5718.33)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42898.6, 
    farPlane=69404.8, width=13962.6, height=9197.95, viewOffsetX=7320.75, 
    viewOffsetY=5445.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42898.8, 
    farPlane=69404.7, width=13962.7, height=9197.99, viewOffsetX=5401.1, 
    viewOffsetY=1469.69)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43156.5, 
    farPlane=69147, width=12468.8, height=8213.89, viewOffsetX=4674.47, 
    viewOffsetY=1658.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43075, 
    farPlane=69228.5, width=12445.2, height=8198.38, viewOffsetX=7512.94, 
    viewOffsetY=3929.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44314.2, 
    farPlane=67989.3, width=1661.65, height=1094.62, viewOffsetX=8168.92, 
    viewOffsetY=5924.02)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 
    'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 
    'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6'), vector=(4500.0, 1650.0, 
    -6600.0))
#: The instances were translated by 4.5E+03, 1.65E+03, -6.6E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42125.7, 
    farPlane=68468.2, width=6690.67, height=4407.52, viewOffsetX=8125.83, 
    viewOffsetY=5747.22)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42034.9, 
    farPlane=68559, width=6676.24, height=4398.01, viewOffsetX=8832.58, 
    viewOffsetY=5397.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41689.4, 
    farPlane=68904.4, width=10252.4, height=6753.84, viewOffsetX=9249.45, 
    viewOffsetY=5456.66)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41621.8, 
    farPlane=68972.1, width=10235.8, height=6742.88, viewOffsetX=9245.44, 
    viewOffsetY=5711.81)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41984, 
    farPlane=68609.8, width=6695.46, height=4410.67, viewOffsetX=8834.77, 
    viewOffsetY=5568.45)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42031.7, 
    farPlane=68562.2, width=6703.06, height=4415.68, viewOffsetX=8844.81, 
    viewOffsetY=5452.32)


    
session.viewports['Viewport: 1'].view.setValues(nearPlane=42429.6, 
    farPlane=68164.3, width=3482.28, height=2293.97, viewOffsetX=8122.03, 
    viewOffsetY=6291.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42405.8, 
    farPlane=68188.1, width=3480.33, height=2292.69, viewOffsetX=8274.47, 
    viewOffsetY=5210.55)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=8330.54, 
    viewOffsetY=4570.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42649.1, 
    farPlane=67944.7, width=1300.62, height=856.794, viewOffsetX=8136.17, 
    viewOffsetY=4074.52)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['col-2-4-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v11[3], point2=v11[5], point3=v11[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42632.5, 
    farPlane=67961.4, width=1435.69, height=945.772, viewOffsetX=8066.12, 
    viewOffsetY=4328.62)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#3 ]', ), )
v1 = a.instances['col-2-4-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v1[5], point2=v1[6], point3=v1[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42331.8, 
    farPlane=68262.1, width=4377.57, height=2883.75, viewOffsetX=8549.66, 
    viewOffsetY=4701.24)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-163101.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x000000001206FCE8>materials created
#* TypeError:  ??????????: side1Faces
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 1044, in 
#* <module>
#*     mymodel.startBuilding()
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 272, in 
#* startBuilding
#*     assembly.Surface(side1Faces=totalSurfs, name='col-beam-surf')
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-163235.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36857.4, 
    farPlane=60875.6, width=9371.64, height=6173.62, viewOffsetX=874.907, 
    viewOffsetY=2392.56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36922.7, 
    farPlane=60810.4, width=9388.22, height=6184.54, viewOffsetX=2832.75, 
    viewOffsetY=2427.06)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37291.2, 
    farPlane=60441.8, width=6594.92, height=4344.44, viewOffsetX=2923.86, 
    viewOffsetY=2642.89)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37247.8, 
    farPlane=60485.2, width=6587.25, height=4339.39, viewOffsetX=2460.56, 
    viewOffsetY=1981.48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37433.1, 
    farPlane=60323.3, width=6620.03, height=4360.98, cameraPosition=(33572.4, 
    33195.3, 36631.8), cameraUpVector=(-0.587086, 0.532157, -0.610032), 
    cameraTarget=(7313.2, 2858.64, 8737.78), viewOffsetX=2472.8, 
    viewOffsetY=1991.34)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37828.4, 
    farPlane=59928, width=2992.84, height=1971.55, viewOffsetX=2469.3, 
    viewOffsetY=2494.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37850.1, 
    farPlane=59906.3, width=2994.56, height=1972.69, viewOffsetX=2528.62, 
    viewOffsetY=2521.58)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=2544.7, 
    viewOffsetY=2470.09)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37828.4, 
    farPlane=59928, width=2992.85, height=1971.56, viewOffsetX=2442.93, 
    viewOffsetY=2390.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39034.3, 
    farPlane=56977.4, width=3088.26, height=2034.41, cameraPosition=(3484.13, 
    38609.3, 40901), cameraUpVector=(-0.357324, 0.315142, -0.879207), 
    cameraTarget=(6611.4, 2475.75, 8151.66), viewOffsetX=2520.8, 
    viewOffsetY=2466.46)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39023.5, 
    farPlane=56988.2, width=3087.4, height=2033.85, viewOffsetX=3458.59, 
    viewOffsetY=2100.81)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36779.7, 
    farPlane=57791.9, width=2909.89, height=1916.91, cameraPosition=(-10761.1, 
    35820.3, 37963.4), cameraUpVector=(-0.205425, 0.259496, -0.943643), 
    cameraTarget=(6927.62, 1925.35, 7530.17), viewOffsetX=3259.72, 
    viewOffsetY=1980.01)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36986.2, 
    farPlane=57585.5, width=1230.55, height=810.631, viewOffsetX=3317.49, 
    viewOffsetY=1827.24)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['xbeam-2-2-2'].vertices
e1 = a.instances['xbeam-2-2-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[7], normal=e1[9], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36678.8, 
    farPlane=57892.9, width=4206.47, height=2771.04, viewOffsetX=3169.38, 
    viewOffsetY=1959.83)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38400.6, 
    farPlane=58656.4, width=4403.92, height=2901.11, cameraPosition=(17826.1, 
    38106.8, 40600.2), cameraUpVector=(-0.460619, 0.40755, -0.7885), 
    cameraTarget=(6049.96, 3023.03, 8687.92), viewOffsetX=3318.15, 
    viewOffsetY=2051.83)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38377.6, 
    farPlane=58679.4, width=4401.28, height=2899.37, viewOffsetX=3982.74, 
    viewOffsetY=1809.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38764.1, 
    farPlane=58292.9, width=1006.93, height=663.322, viewOffsetX=3663.11, 
    viewOffsetY=1832.98)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v1 = a.instances['xbeam-2-3-2'].vertices
e11 = a.instances['xbeam-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[6], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38707.8, 
    farPlane=58349.2, width=1463.44, height=964.048, viewOffsetX=3695.67, 
    viewOffsetY=1815.26)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v11 = a.instances['zbeam-2-3-2'].vertices
e1 = a.instances['zbeam-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[7], normal=e1[9], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38642.5, 
    farPlane=58414.4, width=2252.92, height=1484.13, viewOffsetX=3820.87, 
    viewOffsetY=1761.56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41675.3, 
    farPlane=62634, width=2429.74, height=1600.61, cameraPosition=(54538, 
    10778.4, -12578.6), cameraUpVector=(-0.645005, 0.647646, -0.405615), 
    cameraTarget=(11366.6, 7084.73, 10016.2), viewOffsetX=4120.74, 
    viewOffsetY=1899.81)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41654.8, 
    farPlane=62654.4, width=2428.55, height=1599.82, viewOffsetX=3244.85, 
    viewOffsetY=2065.91)
session.viewports['Viewport: 1'].view.setValues(farPlane=62654.4, 
    cameraPosition=(54552.1, 10690.2, -12566.1), cameraUpVector=(-0.639909, 
    0.659825, -0.393887), cameraTarget=(11380.7, 6996.51, 10028.7))
session.viewports['Viewport: 1'].view.setValues(nearPlane=42417.2, 
    farPlane=63122.4, width=2473, height=1629.1, cameraPosition=(52604, 27183, 
    -4845.49), cameraUpVector=(-0.768291, 0.554091, -0.320486), cameraTarget=(
    10695.4, 7533.01, 10822.4), viewOffsetX=3304.24, viewOffsetY=2103.72)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41737.4, 
    farPlane=64042.5, width=2433.36, height=1602.99, cameraPosition=(50102, 
    24851.8, -14321.2), cameraUpVector=(-0.784099, 0.604738, -0.139575), 
    cameraTarget=(11407.4, 7164, 9716.54), viewOffsetX=3251.28, 
    viewOffsetY=2070)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41742, 
    farPlane=64038, width=2433.63, height=1603.17, viewOffsetX=2927.5, 
    viewOffsetY=1507.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41931.3, 
    farPlane=63848.7, width=754.482, height=497.02, viewOffsetX=2859.76, 
    viewOffsetY=1485.88)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v1 = a.instances['zbeam-2-3-1'].vertices
e11 = a.instances['zbeam-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[6], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41577.4, 
    farPlane=64202.5, width=4094.29, height=2697.14, viewOffsetX=3577.35, 
    viewOffsetY=1518.72)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41549.5, 
    farPlane=64230.4, width=4091.54, height=2695.33, viewOffsetX=3684.82, 
    viewOffsetY=1610.04)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41777.5, 
    farPlane=63872.7, width=4114, height=2710.12, cameraPosition=(51296.3, 
    26033.7, -10339.4), cameraUpVector=(-0.774129, 0.616459, -0.143885), 
    cameraTarget=(11256.7, 6966.95, 10184.4), viewOffsetX=3705.04, 
    viewOffsetY=1618.88)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41310.9, 
    farPlane=64339.2, width=8617.85, height=5677.06, viewOffsetX=4181.62, 
    viewOffsetY=1729.91)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-164402.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x000000000F510528>materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)


session.viewports['Viewport: 1'].view.setValues(nearPlane=37813.4, 
    farPlane=59919.6, width=1611.35, height=1061.49, viewOffsetX=825.175, 
    viewOffsetY=2199.12)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#20 ]', ), )
v11 = a.instances['xbeam-2-2-3'].vertices
e1 = a.instances['col-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e1[19], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-2-3'].vertices
e11 = a.instances['col-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e11[7], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v11 = a.instances['xbeam-2-3-3'].vertices
e1 = a.instances['xbeam-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[4], normal=e1[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-3-3'].vertices
e11 = a.instances['xbeam-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[1], normal=e11[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v11 = a.instances['zbeam-2-3-2'].vertices
e1 = a.instances['col-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[4], normal=e1[64], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#20 ]', ), )
v1 = a.instances['zbeam-2-3-2'].vertices
e11 = a.instances['col-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[1], normal=e11[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1000 ]', ), )
v11 = a.instances['zbeam-2-3-3'].vertices
e1 = a.instances['col-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[5], normal=e1[67], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['zbeam-2-3-3'].vertices
e11 = a.instances['col-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[2], normal=e11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37314.8, 
    farPlane=60418.2, width=6386.67, height=4207.26, viewOffsetX=2043.6, 
    viewOffsetY=1771.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36942.4, 
    farPlane=59769.8, width=6322.94, height=4165.28, cameraPosition=(26135, 
    31499.2, 42763.2), cameraUpVector=(-0.445644, 0.564578, -0.694732), 
    cameraTarget=(6730.29, 2713.63, 8371.6), viewOffsetX=2023.21, 
    viewOffsetY=1754.28)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36874.3, 
    farPlane=60180.6, width=6311.29, height=4157.6, cameraPosition=(30841.8, 
    30168.4, 41082.4), cameraUpVector=(-0.494246, 0.592936, -0.635726), 
    cameraTarget=(6878.25, 2737.48, 8505.95), viewOffsetX=2019.48, 
    viewOffsetY=1751.05)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=36615.6, 
    farPlane=60439.2, width=9084.34, height=5984.36, viewOffsetX=2310.6, 
    viewOffsetY=1745.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39877.9, 
    farPlane=62779.2, width=9893.73, height=6517.55, cameraPosition=(50836.6, 
    23700.3, -9575.73), cameraUpVector=(-0.736267, 0.676687, 0.00243059), 
    cameraTarget=(10367.8, 3672.72, 9108.69), viewOffsetX=2516.47, 
    viewOffsetY=1900.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39995, 
    farPlane=64162.1, width=9922.78, height=6536.69, cameraPosition=(33205.3, 
    31327, -27399.4), cameraUpVector=(-0.822151, 0.480011, 0.306033), 
    cameraTarget=(10839.2, 4944.57, 7121.13), viewOffsetX=2523.86, 
    viewOffsetY=1906.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43157.4, 
    farPlane=60896.9, width=10707.4, height=7053.54, cameraPosition=(18892.4, 
    49605.2, -13356.3), cameraUpVector=(-0.531638, 0.0991244, 0.841151), 
    cameraTarget=(10435.5, 5480.1, 5863.51), viewOffsetX=2723.42, 
    viewOffsetY=2056.78)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42993, 
    farPlane=62008.3, width=10666.6, height=7026.69, cameraPosition=(-956.935, 
    46529.5, -21428.8), cameraUpVector=(0.466738, 0.191686, 0.863373), 
    cameraTarget=(7158.02, 4620.08, 2355.54), viewOffsetX=2713.04, 
    viewOffsetY=2048.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41065.2, 
    farPlane=65187.1, width=10188.3, height=6711.62, cameraPosition=(-20831.8, 
    32239.8, -27232), cameraUpVector=(0.508838, 0.562169, 0.651959), 
    cameraTarget=(5620.19, 3368.21, 2002.64), viewOffsetX=2591.39, 
    viewOffsetY=1957.07)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41119.1, 
    farPlane=65133, width=10201.7, height=6720.44, viewOffsetX=3055.02, 
    viewOffsetY=4568.88)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41855.7, 
    farPlane=64396.5, width=3627.08, height=2389.36, viewOffsetX=2078.52, 
    viewOffsetY=5648.71)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#42000402 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-1')
#: ???? 'Surf-1' ?????? (4 ??).
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-170813.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x000000001045B368>materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35461.4, 
    farPlane=62271.6, width=21267.2, height=14009.9, viewOffsetX=3198.07, 
    viewOffsetY=891.33)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37421.8, 
    farPlane=60311.2, width=5407.8, height=3562.42, viewOffsetX=1251.29, 
    viewOffsetY=1418.43)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37385.3, 
    farPlane=60347.7, width=5402.52, height=3558.95, viewOffsetX=1371.93, 
    viewOffsetY=1701.53)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37417, 
    farPlane=60316, width=5451.45, height=3591.17, viewOffsetX=1161.09, 
    viewOffsetY=1694.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37380.3, 
    farPlane=60352.8, width=5446.09, height=3587.64, viewOffsetX=2394.24, 
    viewOffsetY=2441.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37374.5, 
    farPlane=60358.5, width=5840.31, height=3847.34, viewOffsetX=2369.68, 
    viewOffsetY=2442.72)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37335.2, 
    farPlane=60397.8, width=5834.17, height=3843.29, viewOffsetX=1345.73, 
    viewOffsetY=1430.74)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1395.86, 
    viewOffsetY=822.584)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=549.874, 
    viewOffsetY=659.573)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37037.1, 
    farPlane=60695.9, width=8924.89, height=5879.33, viewOffsetX=725.769, 
    viewOffsetY=598.678)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36978.2, 
    farPlane=60754.8, width=8910.69, height=5869.97, viewOffsetX=1097.89, 
    viewOffsetY=2589.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36978.1, 
    farPlane=60754.9, width=8910.68, height=5869.96, viewOffsetX=877.753, 
    viewOffsetY=2292.64)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37813.4, 
    farPlane=59919.6, width=1611.36, height=1061.49, viewOffsetX=-1451.53, 
    viewOffsetY=2909.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37825.3, 
    farPlane=59907.8, width=1611.86, height=1061.82, viewOffsetX=-1559.32, 
    viewOffsetY=3317.17)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37866.1, 
    farPlane=59866.9, width=1184.23, height=780.117, viewOffsetX=-1662.08, 
    viewOffsetY=3333.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37874.8, 
    farPlane=59858.2, width=1184.5, height=780.297, viewOffsetX=-1665.01, 
    viewOffsetY=3325.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35951.7, 
    farPlane=61781.3, width=18829.4, height=12404, viewOffsetX=20.2893, 
    viewOffsetY=4319.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39821.7, 
    farPlane=62313.3, width=20856.3, height=13739.2, cameraPosition=(38966.1, 
    40492.6, -7184.56), cameraUpVector=(-0.895323, 0.366557, 0.253048), 
    cameraTarget=(9247.78, 3751.63, 5259.75), viewOffsetX=22.4733, 
    viewOffsetY=4784.64)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41937.4, 
    farPlane=68034.7, width=21964.4, height=14469.2, cameraPosition=(-17799.1, 
    33569.2, -31092.9), cameraUpVector=(0.00135061, 0.423472, 0.905908), 
    cameraTarget=(3396.14, 3386.7, 965.17), viewOffsetX=23.6673, 
    viewOffsetY=5038.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46390.7, 
    farPlane=67217.1, width=24296.8, height=16005.7, cameraPosition=(-43200.4, 
    31060.5, 6647.74), cameraUpVector=(0.731535, 0.455256, 0.507541), 
    cameraTarget=(-3195.13, 3000.59, 6249.75), viewOffsetX=26.1805, 
    viewOffsetY=5573.93)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48181.2, 
    farPlane=65426.5, width=6080.47, height=4005.55, viewOffsetX=-1170.25, 
    viewOffsetY=6932.11)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46543.7, 
    farPlane=66840.5, width=5873.82, height=3869.41, cameraPosition=(-33455.3, 
    39350.2, -10516.6), cameraUpVector=(0.687012, 0.397312, 0.608406), 
    cameraTarget=(-2280.3, 4542.85, 3783.99), viewOffsetX=-1130.47, 
    viewOffsetY=6696.5)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#82004004 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-2')
#: ???? 'Surf-2' ?????? (4 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=44963.9, 
    farPlane=68420.2, width=20893.5, height=13763.7, viewOffsetX=991.757, 
    viewOffsetY=8374.57)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44832.6, 
    farPlane=68551.5, width=20832.5, height=13723.5, viewOffsetX=3181.75, 
    viewOffsetY=5909.87)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38868.2, 
    farPlane=64549.4, width=18061, height=11897.8, cameraPosition=(28744.8, 
    31719.6, -29911.9), cameraUpVector=(-0.595186, 0.525345, 0.608084), 
    cameraTarget=(13644.5, 3170.06, 6760.23), viewOffsetX=2758.46, 
    viewOffsetY=5123.64)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40085.3, 
    farPlane=64106.8, width=18626.6, height=12270.4, cameraPosition=(47971.7, 
    33301.5, -5835.05), cameraUpVector=(-0.790015, 0.518011, 0.327935), 
    cameraTarget=(13780.2, 2361.75, 10339.4), viewOffsetX=2844.84, 
    viewOffsetY=5284.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40039.6, 
    farPlane=64152.5, width=18605.4, height=12256.4, viewOffsetX=6798.49, 
    viewOffsetY=6177.79)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38590.3, 
    farPlane=61988.1, width=17932, height=11812.8, cameraPosition=(44472.9, 
    32145, 27154.5), cameraUpVector=(-0.885681, 0.463892, -0.0193222), 
    cameraTarget=(9747.71, 408.789, 13929.2), viewOffsetX=6552.41, 
    viewOffsetY=5954.18)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=37164.2, 
    farPlane=60568.8, width=6878.73, height=4531.4, viewOffsetX=-126.608, 
    viewOffsetY=2497.74)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37212.9, 
    farPlane=60520.1, width=6887.74, height=4537.34, viewOffsetX=198.748, 
    viewOffsetY=2530.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37971.4, 
    farPlane=61839.8, width=7028.12, height=4629.82, cameraPosition=(30748.9, 
    18182.2, -33248.3), cameraUpVector=(-0.748987, 0.624888, 0.220301), 
    cameraTarget=(8397.27, 3091.96, 7502.48), viewOffsetX=202.799, 
    viewOffsetY=2582.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39136.2, 
    farPlane=63379.4, width=7243.72, height=4771.84, cameraPosition=(-19849.1, 
    18540.6, -32939.1), cameraUpVector=(-0.400124, 0.350429, 0.846818), 
    cameraTarget=(7285.33, 4155.06, 5070.32), viewOffsetX=209.02, 
    viewOffsetY=2661.41)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#82008010 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-3')
#: ???? 'Surf-3' ?????? (4 ??).
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=35461.4, 
    farPlane=62271.6, width=21267.2, height=14009.9, viewOffsetX=2078.75, 
    viewOffsetY=2422.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37490.5, 
    farPlane=60242.5, width=4229.88, height=2786.46, viewOffsetX=-459.747, 
    viewOffsetY=3268.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37521, 
    farPlane=60212, width=4233.32, height=2788.73, viewOffsetX=-723.851, 
    viewOffsetY=3762.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37859.4, 
    farPlane=59873.7, width=1239.19, height=816.324, viewOffsetX=-1485.17, 
    viewOffsetY=3591.91)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37868.5, 
    farPlane=59864.6, width=1239.49, height=816.52, viewOffsetX=-1597.36, 
    viewOffsetY=3562.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37479, 
    farPlane=60254, width=4884.33, height=3217.58, viewOffsetX=-918.571, 
    viewOffsetY=3904.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37445.9, 
    farPlane=60287.1, width=4880.03, height=3214.75, viewOffsetX=-89.5722, 
    viewOffsetY=3481.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37331.8, 
    farPlane=60401.3, width=6231.4, height=4104.97, viewOffsetX=-28.7996, 
    viewOffsetY=3451.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37289.9, 
    farPlane=60443.1, width=6224.42, height=4100.37, viewOffsetX=1094.44, 
    viewOffsetY=3815.42)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36679.4, 
    farPlane=61053.6, width=12191.9, height=8031.46, viewOffsetX=2123.23, 
    viewOffsetY=3736.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36600.5, 
    farPlane=61132.5, width=12165.6, height=8014.18, viewOffsetX=2732.82, 
    viewOffsetY=747.773)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2000004 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-4')
#: ???? 'Surf-4' ?????? (2 ??).
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2000010 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-5')
#: ???? 'Surf-5' ?????? (2 ??).
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2000004 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-6')
#: ???? 'Surf-6' ?????? (2 ??).
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2000010 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-7')
#: ???? 'Surf-7' ?????? (2 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=36834.4, 
    farPlane=60898.6, width=9559.01, height=6297.05, viewOffsetX=2333.76, 
    viewOffsetY=43.5415)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-1-3-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2000004 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-8')
#: ???? 'Surf-8' ?????? (2 ??).
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-1-3-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2000010 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-9')
#: ???? 'Surf-9' ?????? (2 ??).
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-1-2-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2000004 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-10')
#: ???? 'Surf-10' ?????? (2 ??).
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-1-2-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2000010 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-11')
#: ???? 'Surf-11' ?????? (2 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=35596.7, 
    farPlane=62136.3, width=22057.3, height=14530.4, viewOffsetX=3549.85, 
    viewOffsetY=-116.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35462.7, 
    farPlane=62270.3, width=21974.3, height=14475.7, viewOffsetX=4338.99, 
    viewOffsetY=1749.63)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37505.3, 
    farPlane=60227.7, width=4109.76, height=2707.33, viewOffsetX=2255.11, 
    viewOffsetY=1713.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37535, 
    farPlane=60198.1, width=4113.01, height=2709.47, viewOffsetX=2075.76, 
    viewOffsetY=2422.45)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36881.2, 
    farPlane=60851.9, width=10349.7, height=6817.96, viewOffsetX=2210.05, 
    viewOffsetY=3010.35)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 #8400008 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-12')
#: ???? 'Surf-12' ?????? (4 ??).
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 #8400008 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-13')
#: ???? 'Surf-13' ?????? (4 ??).
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-14')
#: ???? 'Surf-14' ?????? (1 ??).
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-15')
#: ???? 'Surf-15' ?????? (1 ??).
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#0 #8000000 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-16')
#: ???? 'Surf-16' ?????? (1 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=35961.6, 
    farPlane=61771.4, width=18736.3, height=12342.7, viewOffsetX=2620.66, 
    viewOffsetY=3816.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35845.2, 
    farPlane=61887.8, width=18675.7, height=12302.8, viewOffsetX=2231.04, 
    viewOffsetY=1796.91)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35844.8, 
    farPlane=61888.2, width=18675.6, height=12302.7, viewOffsetX=3213.94, 
    viewOffsetY=2499.33)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35844.8, 
    farPlane=61888.2, width=18675.7, height=12302.7, viewOffsetX=2190.89, 
    viewOffsetY=1997.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36493.8, 
    farPlane=61239.2, width=12330.1, height=8122.5, viewOffsetX=1622.92, 
    viewOffsetY=2069.17)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-17')
#: ???? 'Surf-17' ?????? (1 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=36938.7, 
    farPlane=60794.3, width=9823.94, height=6471.58, viewOffsetX=1620.51, 
    viewOffsetY=1777.38)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-18')
#: ???? 'Surf-18' ?????? (1 ??).
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-19')
#: ???? 'Surf-19' ?????? (1 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=36653.3, 
    farPlane=61079.8, width=11032.2, height=7267.5, viewOffsetX=1593.5, 
    viewOffsetY=1774)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2000000 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-20')
#: ???? 'Surf-20' ?????? (1 ??).
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2000000 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-21')
#: ???? 'Surf-21' ?????? (1 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=37388.8, 
    farPlane=60344.2, width=5055.04, height=3330.04, viewOffsetX=-847.183, 
    viewOffsetY=3244.89)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#0 #8 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-22')
#: ???? 'Surf-22' ?????? (1 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=37248.8, 
    farPlane=60484.2, width=6191.95, height=4078.99, viewOffsetX=1205.78, 
    viewOffsetY=3035.06)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#0 #8 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-23')
#: ???? 'Surf-23' ?????? (1 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=37543, 
    farPlane=60190, width=3804.23, height=2506.06, viewOffsetX=-888.216, 
    viewOffsetY=1432.54)
mdb.models['structure'].rootAssembly.features.changeKey(
    fromName='Partition cell-37', toName='Partition cell-371')
session.viewports['Viewport: 1'].view.setValues(nearPlane=37718.6, 
    farPlane=60014.4, width=2691.08, height=1772.76, viewOffsetX=-1005.42, 
    viewOffsetY=1003.53)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37700.1, 
    farPlane=60032.9, width=2689.76, height=1771.9, viewOffsetX=-1227.39, 
    viewOffsetY=1268.97)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37311.6, 
    farPlane=60421.4, width=6408.34, height=4221.53, viewOffsetX=-699.815, 
    viewOffsetY=1245.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37269.4, 
    farPlane=60463.6, width=6401.09, height=4216.76, viewOffsetX=-582.14, 
    viewOffsetY=2482.44)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36192.7, 
    farPlane=61540.3, width=14782, height=9737.74, viewOffsetX=545.064, 
    viewOffsetY=2197.51)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 
    'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 
    'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 
    'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 
    'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 
    'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 
    'xbeam-2-3-2-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 
    'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 
    'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 
    'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 
    'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 
    'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 
    'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 
    'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 
    'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 
    'xbeam-1-3-1-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 
    'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 
    'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 
    'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 
    'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 
    'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 
    'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 
    'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 
    'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 
    'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 
    'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 
    'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 
    'xbeam-2-1-4-rebar-5-6', 'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 
    'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 
    'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 'xbeam-2-3-4', 
    'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 
    'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 
    ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=36291.8, 
    farPlane=61441.2, width=14822.5, height=9764.38, viewOffsetX=3826.28, 
    viewOffsetY=4640.64)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37174.8, 
    farPlane=60558.2, width=6792.42, height=4474.54, viewOffsetX=2800.22, 
    viewOffsetY=4839.43)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37222.9, 
    farPlane=60510.1, width=6801.21, height=4480.33, viewOffsetX=3030.31, 
    viewOffsetY=5130.74)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1452.37, 
    viewOffsetY=4290.23)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1803.02, 
    viewOffsetY=5686.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37309.6, 
    farPlane=60423.4, width=6434.24, height=4238.59, viewOffsetX=1767.16, 
    viewOffsetY=5840.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37266.4, 
    farPlane=60466.6, width=6426.8, height=4233.69, viewOffsetX=-899.484, 
    viewOffsetY=4888.01)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37708.9, 
    farPlane=60024.1, width=2779.74, height=1831.17, viewOffsetX=-1967.83, 
    viewOffsetY=5226.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37689.9, 
    farPlane=60043.2, width=2778.33, height=1830.24, viewOffsetX=-203.148, 
    viewOffsetY=5402.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37189.3, 
    farPlane=60543.7, width=7533.91, height=4963.01, viewOffsetX=533.365, 
    viewOffsetY=5359.43)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37139.1, 
    farPlane=60593.9, width=7523.75, height=4956.31, viewOffsetX=3110.6, 
    viewOffsetY=6120.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37770.3, 
    farPlane=59962.8, width=1961.4, height=1292.08, viewOffsetX=3132.08, 
    viewOffsetY=6008.41)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-6'), vector=(4550.0, 0.0, -6600.0))
#: The instances were translated by 4.55E+03, 0., -6.6E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37784.6, 
    farPlane=63499.1, width=1962.14, height=1292.57, viewOffsetX=2694.89, 
    viewOffsetY=5316.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37591.4, 
    farPlane=63692.3, width=3855.65, height=2539.93, viewOffsetX=2555.87, 
    viewOffsetY=5192.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37565.1, 
    farPlane=63718.6, width=3852.96, height=2538.16, viewOffsetX=3054.84, 
    viewOffsetY=5458.33)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37889.4, 
    farPlane=63394.4, width=996.185, height=656.243, viewOffsetX=3129.31, 
    viewOffsetY=5777.27)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 
    'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 
    'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6'), 
    vector=(0.0, 0.0, 50.0))
#: The instances were translated by 0., 0., 50. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37700, 
    farPlane=63583.7, width=3056.21, height=2013.29, viewOffsetX=3211.9, 
    viewOffsetY=5751.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37658, 
    farPlane=63625.7, width=3052.8, height=2011.05, viewOffsetX=3162.42, 
    viewOffsetY=5384.45)
session.viewports['Viewport: 1'].view.setValues(width=3083.64, height=2031.36, 
    viewOffsetX=3163.17, viewOffsetY=5382.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38386.9, 
    farPlane=63617.5, width=3143.32, height=2070.68, cameraPosition=(34678.6, 
    34147.8, 35342.7), cameraUpVector=(-0.593122, 0.520368, -0.614348), 
    cameraTarget=(7432.73, 3297.12, 9001.94), viewOffsetX=3224.39, 
    viewOffsetY=5486.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38380, 
    farPlane=63624.4, width=3142.76, height=2070.31, viewOffsetX=3379.1, 
    viewOffsetY=5816.36)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=3487.13, 
    viewOffsetY=5127.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38217.9, 
    farPlane=63786.6, width=4825.89, height=3179.09, viewOffsetX=3606.32, 
    viewOffsetY=5088.41)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38185.2, 
    farPlane=63819.3, width=4821.77, height=3176.37, viewOffsetX=3592.88, 
    viewOffsetY=5172.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38332.8, 
    farPlane=63671.7, width=3339.25, height=2199.75, viewOffsetX=3367.32, 
    viewOffsetY=5130.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38357, 
    farPlane=63647.5, width=3341.36, height=2201.14, viewOffsetX=3279.72, 
    viewOffsetY=4490.51)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38378.4, 
    farPlane=63626.1, width=3356.9, height=2211.38, viewOffsetX=3286.41, 
    viewOffsetY=4458.4)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('col-2-2-1', 'col-2-2-1-rebar-2-1', 
    'col-2-2-1-rebar-2-2', 'col-2-2-1-rebar-2-3', 'col-2-2-1-rebar-2-4', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6'), 
    vector=(0.0, 1650.0, 0.0))
#: The instances were translated by 0., 1.65E+03, 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37037.4, 
    farPlane=63925.4, width=6088.82, height=4011.05, viewOffsetX=3564.84, 
    viewOffsetY=3967.34)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36997.2, 
    farPlane=63965.6, width=6082.21, height=4006.69, viewOffsetX=3809.22, 
    viewOffsetY=5806.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37182.9, 
    farPlane=63779.9, width=4216.99, height=2777.97, viewOffsetX=3599.09, 
    viewOffsetY=5859.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37213.3, 
    farPlane=63749.5, width=4220.44, height=2780.24, viewOffsetX=3606.57, 
    viewOffsetY=6118.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37451.6, 
    farPlane=63511.2, width=2038.03, height=1342.56, viewOffsetX=3240.76, 
    viewOffsetY=5451.55)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['col-2-2-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v11[3], point2=v11[5], point3=v11[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37316.2, 
    farPlane=63646.5, width=3543.95, height=2334.6, viewOffsetX=3418.79, 
    viewOffsetY=5473.67)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37292.1, 
    farPlane=63670.7, width=3541.65, height=2333.08, viewOffsetX=3625.8, 
    viewOffsetY=6162.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37072.3, 
    farPlane=63890.4, width=5775.85, height=3804.88, viewOffsetX=3829.86, 
    viewOffsetY=5994.44)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37033.5, 
    farPlane=63929.3, width=5769.8, height=3800.89, viewOffsetX=4885.6, 
    viewOffsetY=4667.45)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37033.5, 
    farPlane=63929.3, width=5769.79, height=3800.89, viewOffsetX=6118.88, 
    viewOffsetY=3576.16)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37504, 
    farPlane=63458.8, width=1613.05, height=1062.61, viewOffsetX=5620.4, 
    viewOffsetY=3022.31)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['col-2-3-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v1[3], point2=v1[5], point3=v1[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37600.4, 
    farPlane=63362.4, width=832.264, height=548.259, viewOffsetX=5580.62, 
    viewOffsetY=3006.48)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#3 ]', ), )
v11 = a.instances['col-2-3-1'].vertices
v12 = a.instances['xbeam-2-3-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v11[6], point2=v12[1], point3=v11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37324.2, 
    farPlane=63638.6, width=3470.87, height=2286.46, viewOffsetX=5972.45, 
    viewOffsetY=3001.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37300.5, 
    farPlane=63662.2, width=3468.67, height=2285.01, viewOffsetX=6330.05, 
    viewOffsetY=3969.11)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37155, 
    farPlane=63807.8, width=4443.53, height=2927.2, viewOffsetX=6549.04, 
    viewOffsetY=3816.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37186.9, 
    farPlane=63775.8, width=4447.35, height=2929.72, viewOffsetX=7920.88, 
    viewOffsetY=3016.98)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37564.4, 
    farPlane=63398.4, width=1123.67, height=740.221, viewOffsetX=8009.98, 
    viewOffsetY=1581.18)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['xbeam-2-3-1'].vertices
v2 = a.instances['col-2-4-1'].vertices
v3 = a.instances['zbeam-1-4-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v1[2], point2=v2[5], point3=v3[5], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37188.2, 
    farPlane=63774.6, width=4711.84, height=3103.95, viewOffsetX=8064.51, 
    viewOffsetY=1628.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37156.7, 
    farPlane=63806.1, width=4707.85, height=3101.32, viewOffsetX=8715.06, 
    viewOffsetY=2613.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36176.3, 
    farPlane=64786.5, width=13960.7, height=9196.72, viewOffsetX=9175.05, 
    viewOffsetY=2126.64)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36087, 
    farPlane=64875.8, width=13926.3, height=9174.01, viewOffsetX=8673.73, 
    viewOffsetY=2405.74)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36746.4, 
    farPlane=64216.4, width=8755.74, height=5767.89, viewOffsetX=9374.11, 
    viewOffsetY=1361.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36688.6, 
    farPlane=64274.2, width=8741.95, height=5758.81, viewOffsetX=8157.45, 
    viewOffsetY=2655.65)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('col-1-4-1', 'col-1-4-1-rebar-1-1', 
    'col-1-4-1-rebar-1-2', 'col-1-4-1-rebar-1-3', 'col-1-4-1-rebar-1-4'), 
    vector=(2075.0, 0.0, -3175.0))
#: The instances were translated by 2.075E+03, 0., -3.175E+03 (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35563.6, 
    farPlane=64242.3, width=8473.88, height=5582.22, viewOffsetX=10537.8, 
    viewOffsetY=989.703)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36174.7, 
    farPlane=63631.2, width=3010.62, height=1983.26, viewOffsetX=10304, 
    viewOffsetY=360.891)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-1-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['col-1-4-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v11[3], point2=v11[5], point3=v11[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36005, 
    farPlane=63800.8, width=4956.06, height=3264.84, viewOffsetX=10727.4, 
    viewOffsetY=267.229)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-1-4-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#3 ]', ), )
v1 = a.instances['col-1-4-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v1[6], point2=v1[5], point3=v1[7], 
    cells=pickedCells)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-173700.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x0000000017DF4448>materials created
#* ????????????.
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 1119, in 
#* <module>
#*     mymodel.startBuilding()
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 261, in 
#* startBuilding
#*     surfs.append(self.getColSurfToBeam(colName))
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 644, in 
#* getColSurfToBeam
#*     a.PartitionCellByPlanePointNormal(point=v1[1], normal=e1[4], 
#* cells=pickedCells)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=37711.2, 
    farPlane=60021.9, width=2759.12, height=1817.59, viewOffsetX=103.435, 
    viewOffsetY=3727.02)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-173842.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37890.3, 
    farPlane=59842.7, width=988.253, height=651.017, viewOffsetX=-32.8339, 
    viewOffsetY=4039.91)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v11 = a.instances['zbeam-2-2-1'].vertices
e1 = a.instances['col-2-2-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[4], normal=e1[64], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37799.8, 
    farPlane=59933.2, width=1947.26, height=1282.77, viewOffsetX=123.713, 
    viewOffsetY=3842.87)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['zbeam-2-2-1'].vertices
e11 = a.instances['zbeam-2-2-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[1], normal=e11[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37853, 
    farPlane=59880, width=1290.61, height=850.196, viewOffsetX=-1243.63, 
    viewOffsetY=3602.39)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v11 = a.instances['zbeam-2-2-2'].vertices
e1 = a.instances['zbeam-2-2-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[4], normal=e1[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37899.3, 
    farPlane=59833.7, width=915.777, height=603.274, viewOffsetX=-1467.87, 
    viewOffsetY=3633.46)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['zbeam-2-2-2'].vertices
e11 = a.instances['zbeam-2-2-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[1], normal=e11[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37897.4, 
    farPlane=59835.7, width=931.345, height=613.529, viewOffsetX=-1624.67, 
    viewOffsetY=3539.18)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1000 ]', ), )
v11 = a.instances['zbeam-2-2-3'].vertices
e1 = a.instances['zbeam-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[5], normal=e1[6], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37798.4, 
    farPlane=59934.6, width=1959.81, height=1291.04, viewOffsetX=-1210.71, 
    viewOffsetY=3654.43)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['zbeam-2-2-3'].vertices
e11 = a.instances['zbeam-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[2], normal=e11[6], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37888, 
    farPlane=59845, width=1006.86, height=663.274, viewOffsetX=-528.329, 
    viewOffsetY=4139.78)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1000 ]', ), )
v11 = a.instances['zbeam-2-2-2'].vertices
e1 = a.instances['col-2-2-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[5], normal=e1[62], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['zbeam-2-2-2'].vertices
e11 = a.instances['col-2-2-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[2], normal=e11[4], 
    cells=pickedCells)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-174149.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x0000000009214CE8>materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36914.6, 
    farPlane=60818.4, width=10026.1, height=6604.78, viewOffsetX=1198.8, 
    viewOffsetY=1112.67)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36945.4, 
    farPlane=59704, width=10034.5, height=6610.28, cameraPosition=(19032.3, 
    29985.9, 46871.5), cameraUpVector=(-0.473851, 0.563335, -0.676845), 
    cameraTarget=(7047.4, 2478.3, 8301.72), viewOffsetX=1199.8, 
    viewOffsetY=1113.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37577.5, 
    farPlane=59071.9, width=4291.94, height=2827.34, viewOffsetX=-365.794, 
    viewOffsetY=1357.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=37608.4, 
    farPlane=59041, width=4295.47, height=2829.66, viewOffsetX=-509.123, 
    viewOffsetY=2276.95)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-426.074, 
    viewOffsetY=2092.31)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36620.3, 
    farPlane=60029.1, width=12073.1, height=7953.26, viewOffsetX=1682.47, 
    viewOffsetY=2881)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36702.5, 
    farPlane=59946.9, width=12100.2, height=7971.1, viewOffsetX=2946.96, 
    viewOffsetY=2029.24)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36702.6, 
    farPlane=59946.8, width=12100.3, height=7971.12, viewOffsetX=2700.02, 
    viewOffsetY=1470.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36863.2, 
    farPlane=59786.2, width=10094.3, height=6649.67, viewOffsetX=2586.88, 
    viewOffsetY=1229.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36933.1, 
    farPlane=59716.3, width=10113.4, height=6662.28, viewOffsetX=2200.72, 
    viewOffsetY=1514.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35685.9, 
    farPlane=60963.5, width=22112.4, height=14566.7, viewOffsetX=3035.05, 
    viewOffsetY=527.962)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-175014.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x000000000DC33BC8>materials created
#* KeyError: ('zbeam-2-2-4',)
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 1121, in 
#* <module>
#*     mymodel.startBuilding()
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 263, in 
#* startBuilding
#*     surfs.append(self.getColSurfToBeam(colName))
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 570, in 
#* getColSurfToBeam
#*     downSize = self.partSize[self.zBeamsPart['zbeam-%d-%d-%d' % (floor, 
#* xcount, zcount)]][:2]
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-175723.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: materials created
#* KeyError: ('xbeam-2-5-4',)
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 1122, in 
#* <module>
#*     mymodel.startBuilding()
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 264, in 
#* startBuilding
#*     surfs.append(self.getColSurfToBeam(colName))
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 569, in 
#* getColSurfToBeam
#*     rightSize = self.partSize[self.xBeamsPart['xbeam-%d-%d-%d' % (floor, 
#* xcount, zcount)]][:2]
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-180112.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49363.2, 
    farPlane=79789.3, width=11756, height=7744.31, viewOffsetX=-1590.37, 
    viewOffsetY=725.275)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49285.5, 
    farPlane=79867, width=11737.5, height=7732.12, viewOffsetX=580.603, 
    viewOffsetY=1581.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48805.5, 
    farPlane=80347, width=16848.4, height=11099, viewOffsetX=951.277, 
    viewOffsetY=1627.91)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48696.8, 
    farPlane=80455.7, width=16810.8, height=11074.2, viewOffsetX=606.079, 
    viewOffsetY=1985.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48168.5, 
    farPlane=80984, width=22657.5, height=14925.8, viewOffsetX=686.928, 
    viewOffsetY=1708.12)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47442, 
    farPlane=81535.7, width=22315.8, height=14700.6, cameraPosition=(49902.2, 
    33540.5, 51411.4), cameraUpVector=(-0.545538, 0.663998, -0.511365), 
    cameraTarget=(9547.73, 2319.09, 11828.2), viewOffsetX=676.568, 
    viewOffsetY=1682.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47791.2, 
    farPlane=81177.4, width=22480.1, height=14808.9, cameraPosition=(42160.4, 
    38438.6, 54440.2), cameraUpVector=(-0.536907, 0.5944, -0.598682), 
    cameraTarget=(9564.83, 2385.29, 11922.3), viewOffsetX=681.548, 
    viewOffsetY=1694.74)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50656.6, 
    farPlane=79052.6, width=23827.9, height=15696.8, cameraPosition=(39439.7, 
    54486.6, 37913.5), cameraUpVector=(-0.478445, 0.271785, -0.834999), 
    cameraTarget=(9416.1, 3201.49, 12644.8), viewOffsetX=722.412, 
    viewOffsetY=1796.35)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49917.1, 
    farPlane=79792.2, width=30569, height=20137.5, viewOffsetX=1513.16, 
    viewOffsetY=-2372.31)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49731.1, 
    farPlane=79978.2, width=30455.1, height=20062.5, viewOffsetX=3143.13, 
    viewOffsetY=2283.95)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-180415.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x000000001888C688>materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44301.5, 
    farPlane=74098.3, width=17924.7, height=11808, viewOffsetX=-1538.41, 
    viewOffsetY=-71.2754)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43738.5, 
    farPlane=74741.8, width=17697, height=11658, cameraPosition=(50453.5, 
    28789.7, 43870.6), cameraUpVector=(-0.49399, 0.691518, -0.527046), 
    cameraTarget=(9673.17, 2401.51, 10029), viewOffsetX=-1518.86, 
    viewOffsetY=-70.3697)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43758.6, 
    farPlane=74721.8, width=17705.1, height=11663.4, viewOffsetX=1485.18, 
    viewOffsetY=2441.12)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43758.7, 
    farPlane=74721.8, width=17705.2, height=11663.4, viewOffsetX=1675.36, 
    viewOffsetY=500.392)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46228.1, 
    farPlane=71295, width=18704.3, height=12321.6, cameraPosition=(35114, 
    51538.3, 31669.3), cameraUpVector=(-0.587949, 0.245801, -0.770648), 
    cameraTarget=(9563.16, 2734.49, 9990.52), viewOffsetX=1769.9, 
    viewOffsetY=528.63)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47885.5, 
    farPlane=69637.6, width=3220.69, height=2121.65, viewOffsetX=-74.901, 
    viewOffsetY=1961.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47909, 
    farPlane=69614.1, width=3222.27, height=2122.69, viewOffsetX=-50.7101, 
    viewOffsetY=1913.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46971.8, 
    farPlane=70551.4, width=11998.9, height=7904.34, viewOffsetX=2203.74, 
    viewOffsetY=1998.37)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46892.8, 
    farPlane=70630.4, width=11978.7, height=7891.05, viewOffsetX=1968.43, 
    viewOffsetY=244.301)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46288.7, 
    farPlane=71234.4, width=18234.1, height=12011.8, viewOffsetX=3151.35, 
    viewOffsetY=-10.2628)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46172.3, 
    farPlane=71350.9, width=18188.2, height=11981.6, viewOffsetX=3143.42, 
    viewOffsetY=-1632.54)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45571.3, 
    farPlane=70368.8, width=17951.5, height=11825.6, cameraPosition=(25369.5, 
    50630.4, 39420.9), cameraUpVector=(-0.53227, 0.263187, -0.804625), 
    cameraTarget=(9352.25, 2060.1, 9604.69), viewOffsetX=3102.5, 
    viewOffsetY=-1611.29)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46466.9, 
    farPlane=69473.2, width=9858.98, height=6494.66, viewOffsetX=917.478, 
    viewOffsetY=-1221.81)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46536.2, 
    farPlane=69403.9, width=9873.68, height=6504.35, viewOffsetX=314.336, 
    viewOffsetY=-650.657)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46536.3, 
    height=6504.36, viewOffsetX=2064.24, viewOffsetY=1906.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46536.3, 
    width=9873.69, height=6504.35, viewOffsetX=2096.05, viewOffsetY=2076.29)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1979.39, 
    viewOffsetY=1959.57)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1194.59, 
    viewOffsetY=877.281)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1671.84, 
    viewOffsetY=1842.85)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=2244.53, 
    viewOffsetY=2712.93)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=2138.48, 
    viewOffsetY=2543.16)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1427.91, 
    viewOffsetY=1322.93)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45905.3, 
    farPlane=70034.8, width=16250.6, height=10705.2, viewOffsetX=2106.94, 
    viewOffsetY=1062.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45800.6, 
    farPlane=70139.5, width=16213.6, height=10680.8, viewOffsetX=1962.81, 
    viewOffsetY=310.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46203, 
    farPlane=69737.1, width=12003.8, height=7907.56, viewOffsetX=1524.26, 
    viewOffsetY=479.479)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46286.4, 
    farPlane=69653.7, width=12025.4, height=7921.84, viewOffsetX=1372.01, 
    viewOffsetY=984.343)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45569.8, 
    farPlane=70370.3, width=19422.4, height=12794.6, viewOffsetX=1925.89, 
    viewOffsetY=1892.25)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-180739.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x00000000178124A8>materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48040.4, 
    farPlane=82578.8, width=26898.3, height=17719.4, viewOffsetX=3351.46, 
    viewOffsetY=635.933)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50181.9, 
    farPlane=80437.3, width=8671.51, height=5712.41, viewOffsetX=2113.3, 
    viewOffsetY=818.872)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50243.4, 
    farPlane=80375.8, width=8682.15, height=5719.42, viewOffsetX=3290.92, 
    viewOffsetY=1631.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49269.6, 
    farPlane=81349.6, width=18120.2, height=11936.8, viewOffsetX=4730.46, 
    viewOffsetY=2418.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49153.3, 
    farPlane=81466, width=18077.4, height=11908.6, viewOffsetX=2466.9, 
    viewOffsetY=1286.12)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48704.3, 
    farPlane=80631.6, width=17912.3, height=11799.8, cameraPosition=(35174.8, 
    40814.7, 57620.9), cameraUpVector=(-0.523436, 0.553741, -0.6476), 
    cameraTarget=(9284.75, 2105.36, 11831.8), viewOffsetX=2444.37, 
    viewOffsetY=1274.37)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50056.8, 
    farPlane=79279.1, width=6044.34, height=3981.74, viewOffsetX=2087.76, 
    viewOffsetY=814.681)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50100.3, 
    farPlane=79235.7, width=6049.59, height=3985.2, viewOffsetX=3129.24, 
    viewOffsetY=360.308)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49905.7, 
    farPlane=79430.3, width=8211, height=5409.05, viewOffsetX=3285.85, 
    viewOffsetY=377.048)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49850.5, 
    farPlane=79485.4, width=8201.92, height=5403.07, viewOffsetX=3599.37, 
    viewOffsetY=1258.04)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=3766.75, 
    viewOffsetY=1496.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49431.9, 
    farPlane=79904, width=12541.8, height=8261.97, viewOffsetX=3837.49, 
    viewOffsetY=1747.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49349.3, 
    farPlane=79986.6, width=12520.8, height=8248.16, viewOffsetX=4328.68, 
    viewOffsetY=1636.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48952.1, 
    farPlane=80383.9, width=16923.2, height=11148.3, viewOffsetX=4489.73, 
    viewOffsetY=1814.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48842.8, 
    farPlane=80493.1, width=16885.5, height=11123.4, viewOffsetX=4008.16, 
    viewOffsetY=1683.87)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49262.2, 
    farPlane=80073.8, width=12498.7, height=8233.62, viewOffsetX=3967.13, 
    viewOffsetY=1544.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49349.1, 
    farPlane=79986.8, width=12520.8, height=8248.16, viewOffsetX=4027.93, 
    viewOffsetY=2126.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50397.9, 
    farPlane=78938, width=3277.77, height=2159.25, viewOffsetX=4363.77, 
    viewOffsetY=2495.22)
a = mdb.models['structure'].rootAssembly
f1 = a.instances['col-2-4-3'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
a.Set(faces=faces1, name='Set-1')
#: ?? 'Set-1' ?????? (1 ??).
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-1-4', 'zbeam-1-1-4-rebar-3-1', 
    'zbeam-1-1-4-rebar-3-2', 'zbeam-1-1-4-rebar-3-3', 'zbeam-1-1-4-rebar-3-4', 
    'zbeam-1-1-4-rebar-3-5', 'zbeam-1-1-4-rebar-3-6', 'zbeam-1-2-4', 
    'zbeam-1-2-4-rebar-3-1', 'zbeam-1-2-4-rebar-3-2', 'zbeam-1-2-4-rebar-3-3', 
    'zbeam-1-2-4-rebar-3-4', 'zbeam-1-2-4-rebar-3-5', 'zbeam-1-2-4-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-2-1-4', 'zbeam-2-1-4-rebar-3-1', 'zbeam-2-1-4-rebar-3-2', 
    'zbeam-2-1-4-rebar-3-3', 'zbeam-2-1-4-rebar-3-4', 'zbeam-2-1-4-rebar-3-5', 
    'zbeam-2-1-4-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-2-3-4', 'zbeam-2-3-4-rebar-3-1', 'zbeam-2-3-4-rebar-3-2', 
    'zbeam-2-3-4-rebar-3-3', 'zbeam-2-3-4-rebar-3-4', 'zbeam-2-3-4-rebar-3-5', 
    'zbeam-2-3-4-rebar-3-6', 'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 
    'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 
    'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 
    'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 
    'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 
    'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 
    'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 
    'zbeam-2-3-3-rebar-3-6', 'zbeam-1-4-4', 'zbeam-1-4-4-rebar-3-1', 
    'zbeam-1-4-4-rebar-3-2', 'zbeam-1-4-4-rebar-3-3', 'zbeam-1-4-4-rebar-3-4', 
    'zbeam-1-4-4-rebar-3-5', 'zbeam-1-4-4-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-2-2-4', 'zbeam-2-2-4-rebar-3-1', 'zbeam-2-2-4-rebar-3-2', 
    'zbeam-2-2-4-rebar-3-3', 'zbeam-2-2-4-rebar-3-4', 'zbeam-2-2-4-rebar-3-5', 
    'zbeam-2-2-4-rebar-3-6', 'zbeam-1-5-4', 'zbeam-1-5-4-rebar-3-1', 
    'zbeam-1-5-4-rebar-3-2', 'zbeam-1-5-4-rebar-3-3', 'zbeam-1-5-4-rebar-3-4', 
    'zbeam-1-5-4-rebar-3-5', 'zbeam-1-5-4-rebar-3-6', 'zbeam-1-5-3', 
    'zbeam-1-5-3-rebar-3-1', 'zbeam-1-5-3-rebar-3-2', 'zbeam-1-5-3-rebar-3-3', 
    'zbeam-1-5-3-rebar-3-4', 'zbeam-1-5-3-rebar-3-5', 'zbeam-1-5-3-rebar-3-6', 
    'zbeam-1-5-2', 'zbeam-1-5-2-rebar-4-1', 'zbeam-1-5-2-rebar-4-2', 
    'zbeam-1-5-2-rebar-4-3', 'zbeam-1-5-2-rebar-4-4', 'zbeam-1-5-2-rebar-4-5', 
    'zbeam-1-5-2-rebar-4-6', 'zbeam-1-5-1', 'zbeam-1-5-1-rebar-3-1', 
    'zbeam-1-5-1-rebar-3-2', 'zbeam-1-5-1-rebar-3-3', 'zbeam-1-5-1-rebar-3-4', 
    'zbeam-1-5-1-rebar-3-5', 'zbeam-1-5-1-rebar-3-6', 'zbeam-1-3-4', 
    'zbeam-1-3-4-rebar-3-1', 'zbeam-1-3-4-rebar-3-2', 'zbeam-1-3-4-rebar-3-3', 
    'zbeam-1-3-4-rebar-3-4', 'zbeam-1-3-4-rebar-3-5', 'zbeam-1-3-4-rebar-3-6', 
    'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 
    'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 
    'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 
    'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 
    'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 
    'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 
    'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 
    'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 
    'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 
    'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 
    'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 
    'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 
    'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 
    'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 
    'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 
    'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 
    'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 
    'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 
    'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 'zbeam-2-4-4', 
    'zbeam-2-4-4-rebar-3-1', 'zbeam-2-4-4-rebar-3-2', 'zbeam-2-4-4-rebar-3-3', 
    'zbeam-2-4-4-rebar-3-4', 'zbeam-2-4-4-rebar-3-5', 'zbeam-2-4-4-rebar-3-6', 
    'zbeam-2-5-4', 'zbeam-2-5-4-rebar-3-1', 'zbeam-2-5-4-rebar-3-2', 
    'zbeam-2-5-4-rebar-3-3', 'zbeam-2-5-4-rebar-3-4', 'zbeam-2-5-4-rebar-3-5', 
    'zbeam-2-5-4-rebar-3-6', 'zbeam-2-5-1', 'zbeam-2-5-1-rebar-3-1', 
    'zbeam-2-5-1-rebar-3-2', 'zbeam-2-5-1-rebar-3-3', 'zbeam-2-5-1-rebar-3-4', 
    'zbeam-2-5-1-rebar-3-5', 'zbeam-2-5-1-rebar-3-6', 'zbeam-2-5-2', 
    'zbeam-2-5-2-rebar-4-1', 'zbeam-2-5-2-rebar-4-2', 'zbeam-2-5-2-rebar-4-3', 
    'zbeam-2-5-2-rebar-4-4', 'zbeam-2-5-2-rebar-4-5', 'zbeam-2-5-2-rebar-4-6', 
    'zbeam-2-5-3', 'zbeam-2-5-3-rebar-3-1', 'zbeam-2-5-3-rebar-3-2', 
    'zbeam-2-5-3-rebar-3-3', 'zbeam-2-5-3-rebar-3-4', 'zbeam-2-5-3-rebar-3-5', 
    'zbeam-2-5-3-rebar-3-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 
    'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 
    'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 
    'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 
    'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 
    'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 
    'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 
    'xbeam-1-1-5', 'xbeam-1-1-5-rebar-5-1', 'xbeam-1-1-5-rebar-5-2', 
    'xbeam-1-1-5-rebar-5-3', 'xbeam-1-1-5-rebar-5-4', 'xbeam-1-1-5-rebar-5-5', 
    'xbeam-1-1-5-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-2-5', 'xbeam-1-2-5-rebar-5-1', 'xbeam-1-2-5-rebar-5-2', 
    'xbeam-1-2-5-rebar-5-3', 'xbeam-1-2-5-rebar-5-4', 'xbeam-1-2-5-rebar-5-5', 
    'xbeam-1-2-5-rebar-5-6', 'xbeam-2-4-3', 'xbeam-2-4-3-rebar-5-1', 
    'xbeam-2-4-3-rebar-5-2', 'xbeam-2-4-3-rebar-5-3', 'xbeam-2-4-3-rebar-5-4', 
    'xbeam-2-4-3-rebar-5-5', 'xbeam-2-4-3-rebar-5-6', 'xbeam-2-4-2', 
    'xbeam-2-4-2-rebar-5-1', 'xbeam-2-4-2-rebar-5-2', 'xbeam-2-4-2-rebar-5-3', 
    'xbeam-2-4-2-rebar-5-4', 'xbeam-2-4-2-rebar-5-5', 'xbeam-2-4-2-rebar-5-6', 
    'xbeam-2-4-1', 'xbeam-2-4-1-rebar-5-1', 'xbeam-2-4-1-rebar-5-2', 
    'xbeam-2-4-1-rebar-5-3', 'xbeam-2-4-1-rebar-5-4', 'xbeam-2-4-1-rebar-5-5', 
    'xbeam-2-4-1-rebar-5-6', 'xbeam-2-4-5', 'xbeam-2-4-5-rebar-5-1', 
    'xbeam-2-4-5-rebar-5-2', 'xbeam-2-4-5-rebar-5-3', 'xbeam-2-4-5-rebar-5-4', 
    'xbeam-2-4-5-rebar-5-5', 'xbeam-2-4-5-rebar-5-6', 'xbeam-2-4-4', 
    'xbeam-2-4-4-rebar-5-1', 'xbeam-2-4-4-rebar-5-2', 'xbeam-2-4-4-rebar-5-3', 
    'xbeam-2-4-4-rebar-5-4', 'xbeam-2-4-4-rebar-5-5', 'xbeam-2-4-4-rebar-5-6', 
    'xbeam-1-3-5', 'xbeam-1-3-5-rebar-5-1', 'xbeam-1-3-5-rebar-5-2', 
    'xbeam-1-3-5-rebar-5-3', 'xbeam-1-3-5-rebar-5-4', 'xbeam-1-3-5-rebar-5-5', 
    'xbeam-1-3-5-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-1-4-1', 
    'xbeam-1-4-1-rebar-5-1', 'xbeam-1-4-1-rebar-5-2', 'xbeam-1-4-1-rebar-5-3', 
    'xbeam-1-4-1-rebar-5-4', 'xbeam-1-4-1-rebar-5-5', 'xbeam-1-4-1-rebar-5-6', 
    'xbeam-1-4-2', 'xbeam-1-4-2-rebar-5-1', 'xbeam-1-4-2-rebar-5-2', 
    'xbeam-1-4-2-rebar-5-3', 'xbeam-1-4-2-rebar-5-4', 'xbeam-1-4-2-rebar-5-5', 
    'xbeam-1-4-2-rebar-5-6', 'xbeam-1-4-3', 'xbeam-1-4-3-rebar-5-1', 
    'xbeam-1-4-3-rebar-5-2', 'xbeam-1-4-3-rebar-5-3', 'xbeam-1-4-3-rebar-5-4', 
    'xbeam-1-4-3-rebar-5-5', 'xbeam-1-4-3-rebar-5-6', 'xbeam-1-4-4', 
    'xbeam-1-4-4-rebar-5-1', 'xbeam-1-4-4-rebar-5-2', 'xbeam-1-4-4-rebar-5-3', 
    'xbeam-1-4-4-rebar-5-4', 'xbeam-1-4-4-rebar-5-5', 'xbeam-1-4-4-rebar-5-6', 
    'xbeam-1-4-5', 'xbeam-1-4-5-rebar-5-1', 'xbeam-1-4-5-rebar-5-2', 
    'xbeam-1-4-5-rebar-5-3', 'xbeam-1-4-5-rebar-5-4', 'xbeam-1-4-5-rebar-5-5', 
    'xbeam-1-4-5-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-5', 'xbeam-2-2-5-rebar-5-1', 
    'xbeam-2-2-5-rebar-5-2', 'xbeam-2-2-5-rebar-5-3', 'xbeam-2-2-5-rebar-5-4', 
    'xbeam-2-2-5-rebar-5-5', 'xbeam-2-2-5-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-1-5', 
    'xbeam-2-1-5-rebar-5-1', 'xbeam-2-1-5-rebar-5-2', 'xbeam-2-1-5-rebar-5-3', 
    'xbeam-2-1-5-rebar-5-4', 'xbeam-2-1-5-rebar-5-5', 'xbeam-2-1-5-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    'xbeam-2-3-4-rebar-5-6', 'xbeam-2-3-5', 'xbeam-2-3-5-rebar-5-1', 
    'xbeam-2-3-5-rebar-5-2', 'xbeam-2-3-5-rebar-5-3', 'xbeam-2-3-5-rebar-5-4', 
    'xbeam-2-3-5-rebar-5-5', 'xbeam-2-3-5-rebar-5-6', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=49845.6, 
    farPlane=79490.3, width=8760.33, height=5770.92, viewOffsetX=4657.49, 
    viewOffsetY=2553.87)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49786.9, 
    farPlane=79549, width=8750.01, height=5764.12, viewOffsetX=5714.04, 
    viewOffsetY=1601.15)
a = mdb.models['structure'].rootAssembly
f1 = a.instances['col-2-4-3'].faces
faces1 = f1.getSequenceFromMask(mask=('[#4 ]', ), )
a.Set(faces=faces1, name='Set-2')
#: ?? 'Set-2' ?????? (1 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=52350, 
    farPlane=81682.8, width=9200.48, height=6060.87, cameraPosition=(52726.5, 
    42354.1, 44680.6), cameraUpVector=(-0.575159, 0.55672, -0.599378), 
    cameraTarget=(10246.1, 3870.57, 13379.1), viewOffsetX=6008.21, 
    viewOffsetY=1683.58)
a = mdb.models['structure'].rootAssembly
f1 = a.instances['col-2-4-3'].faces
faces1 = f1.getSequenceFromMask(mask=('[#2000000 ]', ), )
a.Set(faces=faces1, name='Set-3')
#: ?? 'Set-3' ?????? (1 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=57900.3, 
    farPlane=89065.8, width=10175.9, height=6703.46, cameraPosition=(71935.8, 
    18369.3, -24314.1), cameraUpVector=(-0.642139, 0.763725, -0.0661901), 
    cameraTarget=(18925.4, 5412.72, 11565.8), viewOffsetX=6645.21, 
    viewOffsetY=1862.08)
a = mdb.models['structure'].rootAssembly
f1 = a.instances['col-2-4-3'].faces
faces1 = f1.getSequenceFromMask(mask=('[#4000 ]', ), )
a.Set(faces=faces1, name='Set-4')
#: ?? 'Set-4' ?????? (1 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=57788.3, 
    farPlane=89177.7, width=10156.3, height=6690.49, viewOffsetX=4799.65, 
    viewOffsetY=1836.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62254.5, 
    farPlane=83426.8, width=10941.2, height=7207.6, cameraPosition=(63533.9, 
    52275.2, 16361.4), cameraUpVector=(-0.852789, 0.441135, -0.279556), 
    cameraTarget=(15114.9, 8451.95, 17038.7), viewOffsetX=5170.59, 
    viewOffsetY=1978.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=62165.2, 
    farPlane=83516, width=10925.5, height=7197.27, viewOffsetX=8366.91, 
    viewOffsetY=1635.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59729.1, 
    farPlane=84524.8, width=10497.4, height=6915.23, cameraPosition=(62372.2, 
    49534.5, 28915.6), cameraUpVector=(-0.788234, 0.491008, -0.370943), 
    cameraTarget=(13598.3, 7452.4, 18166.8), viewOffsetX=8039.04, 
    viewOffsetY=1571.19)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59364.1, 
    farPlane=85156.4, width=10433.3, height=6872.97, cameraPosition=(67110.9, 
    43366.3, 29476.5), cameraUpVector=(-0.609085, 0.532135, -0.588089), 
    cameraTarget=(12861.1, 9011.21, 17558.9), viewOffsetX=7989.92, 
    viewOffsetY=1561.59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59372.4, 
    farPlane=85148.1, width=10434.8, height=6873.96, cameraPosition=(65291.6, 
    49241.8, 20820.8), cameraUpVector=(-0.0506216, -0.215441, -0.975204), 
    cameraTarget=(11041.8, 14886.7, 8903.19), viewOffsetX=7991.04, 
    viewOffsetY=1561.81)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60748.7, 
    farPlane=79760.5, width=10676.7, height=7033.33, cameraPosition=(9212.31, 
    72833.6, 27990.1), cameraUpVector=(0.597852, -0.124505, -0.791879), 
    cameraTarget=(2847.13, 11935.9, 5267.9), viewOffsetX=8176.28, 
    viewOffsetY=1598.01)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60721.2, 
    farPlane=79788, width=10671.9, height=7030.16, viewOffsetX=10831.9, 
    viewOffsetY=2572.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57141.1, 
    farPlane=79757.4, width=10042.7, height=6615.68, cameraPosition=(-19136.4, 
    65213.9, 26252.6), cameraUpVector=(0.698269, 0.143091, -0.701389), 
    cameraTarget=(1265.48, 7404.54, 3731.67), viewOffsetX=10193.3, 
    viewOffsetY=2420.45)
a = mdb.models['structure'].rootAssembly
f1 = a.instances['col-2-4-3'].faces
faces1 = f1.getSequenceFromMask(mask=('[#80000000 ]', ), )
a.Set(faces=faces1, name='Set-5')
#: ?? 'Set-5' ?????? (1 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=57212.7, 
    farPlane=79685.9, width=10055.3, height=6623.98, viewOffsetX=11383.3, 
    viewOffsetY=2369.45)
session.viewports['Viewport: 1'].view.setValues(nearPlane=55857, 
    farPlane=82140.8, width=9817.03, height=6467.03, cameraPosition=(4376.49, 
    49168.8, 64274), cameraUpVector=(0.475895, 0.450358, -0.755447), 
    cameraTarget=(823.1, 11714.2, 10889.7), viewOffsetX=11113.6, 
    viewOffsetY=2313.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59152.8, 
    farPlane=81451.9, width=10396.3, height=6848.61, cameraPosition=(9192.89, 
    66988.5, 43619.8), cameraUpVector=(0.235267, 0.125786, -0.963757), 
    cameraTarget=(453.739, 10764.6, 11559.6), viewOffsetX=11769.3, 
    viewOffsetY=2449.79)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61485, 
    farPlane=86640.9, width=10806.2, height=7118.64, cameraPosition=(46209.2, 
    64651.7, -11495.1), cameraUpVector=(-0.0604933, -0.658863, -0.749827), 
    cameraTarget=(5752.31, 16210.7, 5299.8), viewOffsetX=12233.3, 
    viewOffsetY=2546.38)
a = mdb.models['structure'].rootAssembly
f1 = a.instances['col-2-4-3'].faces
faces1 = f1.getSequenceFromMask(mask=('[#82004004 ]', ), )
a.Set(faces=faces1, name='Set-6')
#: ?? 'Set-6' ?????? (4 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=60397.9, 
    farPlane=87728, width=20966.2, height=13811.6, viewOffsetX=14457.5, 
    viewOffsetY=2729.39)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=48040.4, 
    farPlane=82578.8, width=26898.3, height=17719.4, viewOffsetX=3900.4, 
    viewOffsetY=1618.74)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49890.1, 
    farPlane=80729.1, width=11042.1, height=7274.03, viewOffsetX=2364.7, 
    viewOffsetY=1871.67)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49967.5, 
    farPlane=80651.7, width=11059.2, height=7285.32, viewOffsetX=1085.45, 
    viewOffsetY=1803.27)
mdb.models['structure'].rootAssembly.deleteSets(setNames=('Set-1', 'Set-2', 
    'Set-3', 'Set-4', 'Set-5', 'Set-6', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=49967.6, 
    width=11059.2, height=7285.33, viewOffsetX=1691.27, viewOffsetY=2730.28)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49959.4, 
    farPlane=80659.9, width=10479.2, height=6903.22, viewOffsetX=1585.47, 
    viewOffsetY=2836.02)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-2-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-2')
#: ???? 'Surf-2' ?????? (1 ??).
session.viewports['Viewport: 1'].view.setValues(nearPlane=50546.7, 
    farPlane=80072.6, width=5710.6, height=3761.89, viewOffsetX=672.18, 
    viewOffsetY=4124.78)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50587.8, 
    farPlane=80031.4, width=5715.24, height=3764.95, viewOffsetX=685.004, 
    viewOffsetY=5110.83)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51040.4, 
    farPlane=79578.8, width=1707.36, height=1124.74, viewOffsetX=-694.735, 
    viewOffsetY=5482.66)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51052.9, 
    farPlane=79566.3, width=1707.78, height=1125.01, viewOffsetX=-729.758, 
    viewOffsetY=5271.12)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51114.3, 
    farPlane=79505, width=1108.79, height=730.421, viewOffsetX=-917.408, 
    viewOffsetY=5314.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51122.4, 
    farPlane=79496.8, width=1108.97, height=730.538, viewOffsetX=-950.907, 
    viewOffsetY=5291.26)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50943.5, 
    farPlane=79675.7, width=2818.55, height=1856.74, viewOffsetX=-773.185, 
    viewOffsetY=5211.44)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50924.1, 
    farPlane=79695.1, width=2817.48, height=1856.03, viewOffsetX=-827.364, 
    viewOffsetY=4367.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50746.3, 
    farPlane=79872.9, width=4624.79, height=3046.61, viewOffsetX=-750.154, 
    viewOffsetY=4294.24)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50714.7, 
    farPlane=79904.5, width=4621.91, height=3044.71, viewOffsetX=-377.352, 
    viewOffsetY=3188.91)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-218.489, 
    viewOffsetY=3362.75)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-268.134, 
    viewOffsetY=3993.55)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-153.951, 
    viewOffsetY=4018.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49549.6, 
    farPlane=81069.7, width=15565.8, height=10254, viewOffsetX=1339.14, 
    viewOffsetY=3373.88)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49448.4, 
    farPlane=81170.9, width=15534, height=10233.1, viewOffsetX=1436.52, 
    viewOffsetY=5987.87)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50477.9, 
    farPlane=80141.3, width=6268.31, height=4129.29, viewOffsetX=1498.04, 
    viewOffsetY=6945.87)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50523, 
    farPlane=80096.3, width=6273.9, height=4132.97, viewOffsetX=1775.67, 
    viewOffsetY=7349.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50715.1, 
    farPlane=79904.2, width=4344.63, height=2862.05, viewOffsetX=1733.12, 
    viewOffsetY=7443.92)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50746.6, 
    farPlane=79872.7, width=4347.33, height=2863.83, viewOffsetX=1696.84, 
    viewOffsetY=7504.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51117.6, 
    farPlane=79501.6, width=1081.35, height=712.345, viewOffsetX=1340.77, 
    viewOffsetY=6808.58)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['col-2-1-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v11[3], point2=v11[5], point3=v11[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50970.2, 
    farPlane=79649.1, width=2574.51, height=1695.97, viewOffsetX=1471.4, 
    viewOffsetY=6999.71)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50952.4, 
    farPlane=79666.8, width=2573.61, height=1695.38, viewOffsetX=1562.12, 
    viewOffsetY=7738.48)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1678.22, 
    viewOffsetY=8250.14)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['col-1-1-1'].vertices
v2 = a.instances['col-2-1-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v1[7], point2=v2[5], point3=v2[6], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1833.02, 
    viewOffsetY=7506.16)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1882.78, 
    viewOffsetY=7083.01)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-1'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v11 = a.instances['col-2-1-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v11[3], point2=v11[8], point3=v11[9], 
    cells=pickedCells)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-182347.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x0000000012ED3528>materials created
#* ????????????.
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 1126, in 
#* <module>
#*     mymodel.startBuilding()
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 264, in 
#* startBuilding
#*     surfs.append(self.getColSurfToBeam(colName))
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 592, in 
#* getColSurfToBeam
#*     cells=pickedCells)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-182625.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: materials created
#* ????????????.
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 1127, in 
#* <module>
#*     mymodel.startBuilding()
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 264, in 
#* startBuilding
#*     surfs.append(self.getColSurfToBeam(colName))
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 593, in 
#* getColSurfToBeam
#*     cells=pickedCells)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-182813.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49514.5, 
    farPlane=81104.7, width=15885.5, height=10464.7, viewOffsetX=519.095, 
    viewOffsetY=2817.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49411.4, 
    farPlane=81207.8, width=15852.5, height=10442.9, viewOffsetX=398.822, 
    viewOffsetY=3067.52)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51095.3, 
    farPlane=79524, width=1262.6, height=831.745, viewOffsetX=-3056.44, 
    viewOffsetY=4609.82)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['col-2-1-3'].vertices
v2 = a.instances['col-1-1-3'].vertices
a.PartitionCellByPlaneThreePoints(point1=v1[3], point2=v1[5], point3=v2[5], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50902.4, 
    farPlane=79716.8, width=3195.06, height=2104.76, viewOffsetX=-2590.27, 
    viewOffsetY=4841.31)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50880.5, 
    farPlane=79738.8, width=3193.68, height=2103.86, viewOffsetX=-2537.7, 
    viewOffsetY=6071.33)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['col-2-1-3'].vertices
a.PartitionCellByPlaneThreePoints(point1=v11[4], point2=v11[7], point3=v11[5], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v1 = a.instances['col-2-1-3'].vertices
e1 = a.instances['col-2-1-3'].edges
a.PartitionCellByPlaneThreePoints(point1=v1[2], point2=v1[8], 
    cells=pickedCells, point3=a.instances['col-2-1-3'].InterestingPoint(
    edge=e1[17], rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=50960.2, 
    farPlane=79659, width=2357.14, height=1552.78, viewOffsetX=-1531.35, 
    viewOffsetY=5602.39)
a1 = mdb.models['structure'].rootAssembly
a1.translate(instanceList=('col-2-1-2', 'col-2-1-2-rebar-2-1', 
    'col-2-1-2-rebar-2-2', 'col-2-1-2-rebar-2-4'), vector=(0.0, 1650.0, 0.0))
#: The instances were translated by 0., 1.65E+03, 0. (????????????????)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49572.2, 
    farPlane=80094.4, width=6645.65, height=4377.86, viewOffsetX=-1028.47, 
    viewOffsetY=4735.49)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49527.9, 
    farPlane=80138.7, width=6639.71, height=4373.95, viewOffsetX=-86.1567, 
    viewOffsetY=6543.63)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49781, 
    farPlane=79885.6, width=4740.16, height=3122.61, viewOffsetX=-797.97, 
    viewOffsetY=7736.56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49748.7, 
    farPlane=79917.9, width=4737.08, height=3120.58, viewOffsetX=-817.805, 
    viewOffsetY=6596.32)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50065.9, 
    farPlane=79600.7, width=1884.47, height=1241.4, viewOffsetX=-1515.13, 
    viewOffsetY=6188.85)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['col-2-1-2'].vertices
a.PartitionCellByPlaneThreePoints(point1=v11[3], point2=v11[5], point3=v11[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49774.7, 
    farPlane=79891.9, width=4797.97, height=3160.69, viewOffsetX=-804.505, 
    viewOffsetY=6237.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49742, 
    farPlane=79924.6, width=4794.81, height=3158.61, viewOffsetX=-850.327, 
    viewOffsetY=7521.47)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50008.1, 
    farPlane=79658.5, width=2660.76, height=1752.79, viewOffsetX=-2152.64, 
    viewOffsetY=7942.28)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49989.8, 
    farPlane=79676.8, width=2659.79, height=1752.15, viewOffsetX=-1754.74, 
    viewOffsetY=7190.49)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-1574.75, 
    viewOffsetY=6644.55)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50160, 
    farPlane=79506.6, width=1122.31, height=739.329, viewOffsetX=-1658.66, 
    viewOffsetY=6337.2)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['col-2-1-2'].vertices
a.PartitionCellByPlaneThreePoints(point1=v1[6], point2=v1[5], point3=v1[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50041.8, 
    farPlane=79624.8, width=2352.63, height=1549.81, viewOffsetX=-1470.11, 
    viewOffsetY=6377.16)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50025.5, 
    farPlane=79641.1, width=2351.87, height=1549.31, viewOffsetX=-1353.43, 
    viewOffsetY=7317.83)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-1345.85, 
    viewOffsetY=7808.16)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50150.5, 
    farPlane=79516.1, width=1356.5, height=893.606, viewOffsetX=-1549.79, 
    viewOffsetY=7971.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50141.1, 
    farPlane=79525.5, width=1356.25, height=893.438, viewOffsetX=-1747.62, 
    viewOffsetY=7970.5)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-1628.16, 
    viewOffsetY=7531.8)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50018.7, 
    farPlane=79647.9, width=2563.69, height=1688.84, viewOffsetX=-1488.92, 
    viewOffsetY=7509.29)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50001.1, 
    farPlane=79665.5, width=2562.78, height=1688.25, viewOffsetX=-1392.05, 
    viewOffsetY=6897.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50079.9, 
    farPlane=79586.7, width=1770.78, height=1166.51, viewOffsetX=-1478.79, 
    viewOffsetY=6753.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50092.9, 
    farPlane=79573.7, width=1771.24, height=1166.81, viewOffsetX=-1486.78, 
    viewOffsetY=6203)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-1-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v11 = a.instances['col-2-1-2'].vertices
a.PartitionCellByPlaneThreePoints(point1=v11[2], point2=v11[8], point3=v11[9], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-183340.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x0000000012351DE8>materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49621.8, 
    farPlane=80997.4, width=13222.9, height=8710.64, viewOffsetX=-103.233, 
    viewOffsetY=1782.95)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'col-2-4-2', 'col-2-4-2-rebar-2-1', 'col-2-4-2-rebar-2-2', 
    'col-2-4-2-rebar-2-3', 'col-2-4-2-rebar-2-4', 'col-2-2-1', 
    'col-2-2-1-rebar-2-1', 'col-2-2-1-rebar-2-2', 'col-2-2-1-rebar-2-3', 
    'col-2-2-1-rebar-2-4', 'col-2-2-2', 'col-2-2-2-rebar-2-1', 
    'col-2-2-2-rebar-2-2', 'col-2-2-2-rebar-2-3', 'col-2-2-2-rebar-2-4', 
    'col-2-2-3', 'col-2-2-3-rebar-2-1', 'col-2-2-3-rebar-2-2', 
    'col-2-2-3-rebar-2-3', 'col-2-2-3-rebar-2-4', 'col-2-2-4', 
    'col-2-2-4-rebar-2-1', 'col-2-2-4-rebar-2-2', 'col-2-2-4-rebar-2-3', 
    'col-2-2-4-rebar-2-4', 'col-2-2-5', 'col-2-2-5-rebar-2-1', 
    'col-2-2-5-rebar-2-2', 'col-2-2-5-rebar-2-3', 'col-2-2-5-rebar-2-4', 
    'col-2-4-4', 'col-2-4-4-rebar-2-1', 'col-2-4-4-rebar-2-2', 
    'col-2-4-4-rebar-2-3', 'col-2-4-4-rebar-2-4', 'col-2-4-3', 
    'col-2-4-3-rebar-2-1', 'col-2-4-3-rebar-2-2', 'col-2-4-3-rebar-2-3', 
    'col-2-4-3-rebar-2-4', 'col-2-5-5', 'col-2-5-5-rebar-2-1', 
    'col-2-5-5-rebar-2-2', 'col-2-5-5-rebar-2-3', 'col-2-5-5-rebar-2-4', 
    'col-1-2-3', 'col-1-2-3-rebar-1-1', 'col-1-2-3-rebar-1-2', 
    'col-1-2-3-rebar-1-3', 'col-1-2-3-rebar-1-4', 'col-1-2-2', 
    'col-1-2-2-rebar-1-1', 'col-1-2-2-rebar-1-2', 'col-1-2-2-rebar-1-3', 
    'col-1-2-2-rebar-1-4', 'col-1-2-1', 'col-1-2-1-rebar-1-1', 
    'col-1-2-1-rebar-1-2', 'col-1-2-1-rebar-1-3', 'col-1-2-1-rebar-1-4', 
    'col-2-4-1', 'col-2-4-1-rebar-2-1', 'col-2-4-1-rebar-2-2', 
    'col-2-4-1-rebar-2-3', 'col-2-4-1-rebar-2-4', 'col-1-2-5', 
    'col-1-2-5-rebar-1-1', 'col-1-2-5-rebar-1-2', 'col-1-2-5-rebar-1-3', 
    'col-1-2-5-rebar-1-4', 'col-1-2-4', 'col-1-2-4-rebar-1-1', 
    'col-1-2-4-rebar-1-2', 'col-1-2-4-rebar-1-3', 'col-1-2-4-rebar-1-4', 
    'col-1-1-1', 'col-1-1-1-rebar-1-1', 'col-1-1-1-rebar-1-2', 
    'col-1-1-1-rebar-1-3', 'col-1-1-1-rebar-1-4', 'col-1-3-4', 
    'col-1-3-4-rebar-1-1', 'col-1-3-4-rebar-1-2', 'col-1-3-4-rebar-1-3', 
    'col-1-3-4-rebar-1-4', 'col-1-3-5', 'col-1-3-5-rebar-1-1', 
    'col-1-3-5-rebar-1-2', 'col-1-3-5-rebar-1-3', 'col-1-3-5-rebar-1-4', 
    'col-1-3-2', 'col-1-3-2-rebar-1-1', 'col-1-3-2-rebar-1-2', 
    'col-1-3-2-rebar-1-3', 'col-1-3-2-rebar-1-4', 'col-1-3-3', 
    'col-1-3-3-rebar-1-1', 'col-1-3-3-rebar-1-2', 'col-1-3-3-rebar-1-3', 
    'col-1-3-3-rebar-1-4', 'col-2-3-3', 'col-2-3-3-rebar-2-1', 
    'col-2-3-3-rebar-2-2', 'col-2-3-3-rebar-2-3', 'col-2-3-3-rebar-2-4', 
    'col-1-3-1', 'col-1-3-1-rebar-1-1', 'col-1-3-1-rebar-1-2', 
    'col-1-3-1-rebar-1-3', 'col-1-3-1-rebar-1-4', 'col-1-1-3', 
    'col-1-1-3-rebar-1-1', 'col-1-1-3-rebar-1-2', 'col-1-1-3-rebar-1-3', 
    'col-1-1-3-rebar-1-4', 'col-2-5-1', 'col-2-5-1-rebar-2-1', 
    'col-2-5-1-rebar-2-2', 'col-2-5-1-rebar-2-3', 'col-2-5-1-rebar-2-4', 
    'col-1-1-4', 'col-1-1-4-rebar-1-1', 'col-1-1-4-rebar-1-2', 
    'col-1-1-4-rebar-1-3', 'col-1-1-4-rebar-1-4', 'col-2-4-5', 
    'col-2-4-5-rebar-2-1', 'col-2-4-5-rebar-2-2', 'col-2-4-5-rebar-2-3', 
    'col-2-4-5-rebar-2-4', 'col-1-1-5', 'col-1-1-5-rebar-1-1', 
    'col-1-1-5-rebar-1-2', 'col-1-1-5-rebar-1-3', 'col-1-1-5-rebar-1-4', 
    'col-2-5-4', 'col-2-5-4-rebar-2-1', 'col-2-5-4-rebar-2-2', 
    'col-2-5-4-rebar-2-3', 'col-2-5-4-rebar-2-4', 'col-1-1-2', 
    'col-1-1-2-rebar-1-1', 'col-1-1-2-rebar-1-2', 'col-1-1-2-rebar-1-3', 
    'col-1-1-2-rebar-1-4', 'col-2-3-5', 'col-2-3-5-rebar-2-1', 
    'col-2-3-5-rebar-2-2', 'col-2-3-5-rebar-2-3', 'col-2-3-5-rebar-2-4', 
    'col-2-3-4', 'col-2-3-4-rebar-2-1', 'col-2-3-4-rebar-2-2', 
    'col-2-3-4-rebar-2-3', 'col-2-3-4-rebar-2-4', 'col-2-5-3', 
    'col-2-5-3-rebar-2-1', 'col-2-5-3-rebar-2-2', 'col-2-5-3-rebar-2-3', 
    'col-2-5-3-rebar-2-4', 'col-2-5-2', 'col-2-5-2-rebar-2-1', 
    'col-2-5-2-rebar-2-2', 'col-2-5-2-rebar-2-3', 'col-2-5-2-rebar-2-4', 
    'col-1-5-4', 'col-1-5-4-rebar-1-1', 'col-1-5-4-rebar-1-2', 
    'col-1-5-4-rebar-1-3', 'col-1-5-4-rebar-1-4', 'col-1-5-5', 
    'col-1-5-5-rebar-1-1', 'col-1-5-5-rebar-1-2', 'col-1-5-5-rebar-1-3', 
    'col-1-5-5-rebar-1-4', 'col-1-5-1', 'col-1-5-1-rebar-1-1', 
    'col-1-5-1-rebar-1-2', 'col-1-5-1-rebar-1-3', 'col-1-5-1-rebar-1-4', 
    'col-1-5-2', 'col-1-5-2-rebar-1-1', 'col-1-5-2-rebar-1-2', 
    'col-1-5-2-rebar-1-3', 'col-1-5-2-rebar-1-4', 'col-1-5-3', 
    'col-1-5-3-rebar-1-1', 'col-1-5-3-rebar-1-2', 'col-1-5-3-rebar-1-3', 
    'col-1-5-3-rebar-1-4', 'col-1-4-1', 'col-1-4-1-rebar-1-1', 
    'col-1-4-1-rebar-1-2', 'col-1-4-1-rebar-1-3', 'col-1-4-1-rebar-1-4', 
    'col-1-4-3', 'col-1-4-3-rebar-1-1', 'col-1-4-3-rebar-1-2', 
    'col-1-4-3-rebar-1-3', 'col-1-4-3-rebar-1-4', 'col-1-4-2', 
    'col-1-4-2-rebar-1-1', 'col-1-4-2-rebar-1-2', 'col-1-4-2-rebar-1-3', 
    'col-1-4-2-rebar-1-4', 'col-1-4-5', 'col-1-4-5-rebar-1-1', 
    'col-1-4-5-rebar-1-2', 'col-1-4-5-rebar-1-3', 'col-1-4-5-rebar-1-4', 
    'col-1-4-4', 'col-1-4-4-rebar-1-1', 'col-1-4-4-rebar-1-2', 
    'col-1-4-4-rebar-1-3', 'col-1-4-4-rebar-1-4', 'col-2-1-3', 
    'col-2-1-3-rebar-2-1', 'col-2-1-3-rebar-2-2', 'col-2-1-3-rebar-2-3', 
    'col-2-1-3-rebar-2-4', 'col-2-1-2', 'col-2-1-2-rebar-2-1', 
    'col-2-1-2-rebar-2-2', 'col-2-1-2-rebar-2-3', 'col-2-1-2-rebar-2-4', 
    'col-2-1-1', 'col-2-1-1-rebar-2-1', 'col-2-1-1-rebar-2-2', 
    'col-2-1-1-rebar-2-3', 'col-2-1-1-rebar-2-4', 'col-2-3-2', 
    'col-2-3-2-rebar-2-1', 'col-2-3-2-rebar-2-2', 'col-2-3-2-rebar-2-3', 
    'col-2-3-2-rebar-2-4', 'col-2-3-1', 'col-2-3-1-rebar-2-1', 
    'col-2-3-1-rebar-2-2', 'col-2-3-1-rebar-2-3', 'col-2-3-1-rebar-2-4', 
    'col-2-1-5', 'col-2-1-5-rebar-2-1', 'col-2-1-5-rebar-2-2', 
    'col-2-1-5-rebar-2-3', 'col-2-1-5-rebar-2-4', 'col-2-1-4', 
    'col-2-1-4-rebar-2-1', 'col-2-1-4-rebar-2-2', 'col-2-1-4-rebar-2-3', 
    'col-2-1-4-rebar-2-4', 'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 
    'zbeam-1-1-3-rebar-3-2', 'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 
    'zbeam-1-1-3-rebar-3-5', 'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 
    'zbeam-1-1-2-rebar-4-1', 'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 
    'zbeam-1-1-2-rebar-4-4', 'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 
    'zbeam-1-1-1', 'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 
    'zbeam-1-1-1-rebar-3-3', 'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 
    'zbeam-1-1-1-rebar-3-6', 'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 
    'zbeam-1-2-1-rebar-3-2', 'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 
    'zbeam-1-2-1-rebar-3-5', 'zbeam-1-2-1-rebar-3-6', 'zbeam-1-1-4', 
    'zbeam-1-1-4-rebar-3-1', 'zbeam-1-1-4-rebar-3-2', 'zbeam-1-1-4-rebar-3-3', 
    'zbeam-1-1-4-rebar-3-4', 'zbeam-1-1-4-rebar-3-5', 'zbeam-1-1-4-rebar-3-6', 
    'zbeam-1-2-4', 'zbeam-1-2-4-rebar-3-1', 'zbeam-1-2-4-rebar-3-2', 
    'zbeam-1-2-4-rebar-3-3', 'zbeam-1-2-4-rebar-3-4', 'zbeam-1-2-4-rebar-3-5', 
    'zbeam-1-2-4-rebar-3-6', 'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 
    'zbeam-2-1-1-rebar-3-2', 'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 
    'zbeam-2-1-1-rebar-3-5', 'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 
    'zbeam-2-1-2-rebar-4-1', 'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 
    'zbeam-2-1-2-rebar-4-4', 'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 
    'zbeam-2-1-3', 'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 
    'zbeam-2-1-3-rebar-3-3', 'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 
    'zbeam-2-1-3-rebar-3-6', 'zbeam-2-1-4', 'zbeam-2-1-4-rebar-3-1', 
    'zbeam-2-1-4-rebar-3-2', 'zbeam-2-1-4-rebar-3-3', 'zbeam-2-1-4-rebar-3-4', 
    'zbeam-2-1-4-rebar-3-5', 'zbeam-2-1-4-rebar-3-6', 'zbeam-1-4-2', 
    'zbeam-1-4-2-rebar-4-1', 'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 
    'zbeam-1-4-2-rebar-4-4', 'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 
    'zbeam-1-4-3', 'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 
    'zbeam-1-4-3-rebar-3-3', 'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 
    'zbeam-1-4-3-rebar-3-6', 'zbeam-2-3-4', 'zbeam-2-3-4-rebar-3-1', 
    'zbeam-2-3-4-rebar-3-2', 'zbeam-2-3-4-rebar-3-3', 'zbeam-2-3-4-rebar-3-4', 
    'zbeam-2-3-4-rebar-3-5', 'zbeam-2-3-4-rebar-3-6', 'zbeam-1-4-1', 
    'zbeam-1-4-1-rebar-3-1', 'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 
    'zbeam-1-4-1-rebar-3-4', 'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 
    'zbeam-2-3-2', 'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 
    'zbeam-2-3-2-rebar-4-3', 'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 
    'zbeam-2-3-2-rebar-4-6', 'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 
    'zbeam-2-3-3-rebar-3-2', 'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 
    'zbeam-2-3-3-rebar-3-5', 'zbeam-2-3-3-rebar-3-6', 'zbeam-1-4-4', 
    'zbeam-1-4-4-rebar-3-1', 'zbeam-1-4-4-rebar-3-2', 'zbeam-1-4-4-rebar-3-3', 
    'zbeam-1-4-4-rebar-3-4', 'zbeam-1-4-4-rebar-3-5', 'zbeam-1-4-4-rebar-3-6', 
    'zbeam-2-3-1', 'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 
    'zbeam-2-3-1-rebar-3-3', 'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 
    'zbeam-2-3-1-rebar-3-6', 'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 
    'zbeam-2-2-3-rebar-3-2', 'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 
    'zbeam-2-2-3-rebar-3-5', 'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 
    'zbeam-2-2-2-rebar-4-1', 'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 
    'zbeam-2-2-2-rebar-4-4', 'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 
    'zbeam-2-2-1', 'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 
    'zbeam-2-2-1-rebar-3-3', 'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 
    'zbeam-2-2-1-rebar-3-6', 'zbeam-2-2-4', 'zbeam-2-2-4-rebar-3-1', 
    'zbeam-2-2-4-rebar-3-2', 'zbeam-2-2-4-rebar-3-3', 'zbeam-2-2-4-rebar-3-4', 
    'zbeam-2-2-4-rebar-3-5', 'zbeam-2-2-4-rebar-3-6', 'zbeam-1-5-4', 
    'zbeam-1-5-4-rebar-3-1', 'zbeam-1-5-4-rebar-3-2', 'zbeam-1-5-4-rebar-3-3', 
    'zbeam-1-5-4-rebar-3-4', 'zbeam-1-5-4-rebar-3-5', 'zbeam-1-5-4-rebar-3-6', 
    'zbeam-1-5-3', 'zbeam-1-5-3-rebar-3-1', 'zbeam-1-5-3-rebar-3-2', 
    'zbeam-1-5-3-rebar-3-3', 'zbeam-1-5-3-rebar-3-4', 'zbeam-1-5-3-rebar-3-5', 
    'zbeam-1-5-3-rebar-3-6', 'zbeam-1-5-2', 'zbeam-1-5-2-rebar-4-1', 
    'zbeam-1-5-2-rebar-4-2', 'zbeam-1-5-2-rebar-4-3', 'zbeam-1-5-2-rebar-4-4', 
    'zbeam-1-5-2-rebar-4-5', 'zbeam-1-5-2-rebar-4-6', 'zbeam-1-5-1', 
    'zbeam-1-5-1-rebar-3-1', 'zbeam-1-5-1-rebar-3-2', 'zbeam-1-5-1-rebar-3-3', 
    'zbeam-1-5-1-rebar-3-4', 'zbeam-1-5-1-rebar-3-5', 'zbeam-1-5-1-rebar-3-6', 
    'zbeam-1-3-4', 'zbeam-1-3-4-rebar-3-1', 'zbeam-1-3-4-rebar-3-2', 
    'zbeam-1-3-4-rebar-3-3', 'zbeam-1-3-4-rebar-3-4', 'zbeam-1-3-4-rebar-3-5', 
    'zbeam-1-3-4-rebar-3-6', 'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 
    'zbeam-1-2-2-rebar-4-2', 'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 
    'zbeam-1-2-2-rebar-4-5', 'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 
    'zbeam-1-2-3-rebar-3-1', 'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 
    'zbeam-1-2-3-rebar-3-4', 'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 
    'zbeam-1-3-1', 'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 
    'zbeam-1-3-1-rebar-3-3', 'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 
    'zbeam-1-3-1-rebar-3-6', 'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 
    'zbeam-1-3-3-rebar-3-2', 'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 
    'zbeam-1-3-3-rebar-3-5', 'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 
    'zbeam-1-3-2-rebar-4-1', 'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 
    'zbeam-1-3-2-rebar-4-4', 'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 
    'zbeam-2-4-1', 'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 
    'zbeam-2-4-1-rebar-3-3', 'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 
    'zbeam-2-4-1-rebar-3-6', 'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 
    'zbeam-2-4-3-rebar-3-2', 'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 
    'zbeam-2-4-3-rebar-3-5', 'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 
    'zbeam-2-4-2-rebar-4-1', 'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 
    'zbeam-2-4-2-rebar-4-4', 'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 
    'zbeam-2-4-4', 'zbeam-2-4-4-rebar-3-1', 'zbeam-2-4-4-rebar-3-2', 
    'zbeam-2-4-4-rebar-3-3', 'zbeam-2-4-4-rebar-3-4', 'zbeam-2-4-4-rebar-3-5', 
    'zbeam-2-4-4-rebar-3-6', 'zbeam-2-5-4', 'zbeam-2-5-4-rebar-3-1', 
    'zbeam-2-5-4-rebar-3-2', 'zbeam-2-5-4-rebar-3-3', 'zbeam-2-5-4-rebar-3-4', 
    'zbeam-2-5-4-rebar-3-5', 'zbeam-2-5-4-rebar-3-6', 'zbeam-2-5-1', 
    'zbeam-2-5-1-rebar-3-1', 'zbeam-2-5-1-rebar-3-2', 'zbeam-2-5-1-rebar-3-3', 
    'zbeam-2-5-1-rebar-3-4', 'zbeam-2-5-1-rebar-3-5', 'zbeam-2-5-1-rebar-3-6', 
    'zbeam-2-5-2', 'zbeam-2-5-2-rebar-4-1', 'zbeam-2-5-2-rebar-4-2', 
    'zbeam-2-5-2-rebar-4-3', 'zbeam-2-5-2-rebar-4-4', 'zbeam-2-5-2-rebar-4-5', 
    'zbeam-2-5-2-rebar-4-6', 'zbeam-2-5-3', 'zbeam-2-5-3-rebar-3-1', 
    'zbeam-2-5-3-rebar-3-2', 'zbeam-2-5-3-rebar-3-3', 'zbeam-2-5-3-rebar-3-4', 
    'zbeam-2-5-3-rebar-3-5', 'zbeam-2-5-3-rebar-3-6', 'xbeam-2-3-2', 
    'xbeam-2-3-2-rebar-5-1', 'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 
    'xbeam-2-3-2-rebar-5-4', 'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 
    'xbeam-2-3-3', 'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 
    'xbeam-2-3-3-rebar-5-3', 'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 
    'xbeam-2-3-3-rebar-5-6', 'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 
    'xbeam-1-1-1-rebar-5-2', 'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 
    'xbeam-1-1-1-rebar-5-5', 'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 
    'xbeam-1-1-3-rebar-5-1', 'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 
    'xbeam-1-1-3-rebar-5-4', 'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 
    'xbeam-1-1-2', 'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 
    'xbeam-1-1-2-rebar-5-3', 'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 
    'xbeam-1-1-2-rebar-5-6', 'xbeam-1-1-5', 'xbeam-1-1-5-rebar-5-1', 
    'xbeam-1-1-5-rebar-5-2', 'xbeam-1-1-5-rebar-5-3', 'xbeam-1-1-5-rebar-5-4', 
    'xbeam-1-1-5-rebar-5-5', 'xbeam-1-1-5-rebar-5-6', 'xbeam-1-1-4', 
    'xbeam-1-1-4-rebar-5-1', 'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 
    'xbeam-1-1-4-rebar-5-4', 'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 
    'xbeam-1-2-2', 'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 
    'xbeam-1-2-2-rebar-5-3', 'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 
    'xbeam-1-2-2-rebar-5-6', 'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 
    'xbeam-1-2-3-rebar-5-2', 'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 
    'xbeam-1-2-3-rebar-5-5', 'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 
    'xbeam-1-2-1-rebar-5-1', 'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 
    'xbeam-1-2-1-rebar-5-4', 'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 
    'xbeam-1-2-4', 'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 
    'xbeam-1-2-4-rebar-5-3', 'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 
    'xbeam-1-2-4-rebar-5-6', 'xbeam-1-2-5', 'xbeam-1-2-5-rebar-5-1', 
    'xbeam-1-2-5-rebar-5-2', 'xbeam-1-2-5-rebar-5-3', 'xbeam-1-2-5-rebar-5-4', 
    'xbeam-1-2-5-rebar-5-5', 'xbeam-1-2-5-rebar-5-6', 'xbeam-2-4-3', 
    'xbeam-2-4-3-rebar-5-1', 'xbeam-2-4-3-rebar-5-2', 'xbeam-2-4-3-rebar-5-3', 
    'xbeam-2-4-3-rebar-5-4', 'xbeam-2-4-3-rebar-5-5', 'xbeam-2-4-3-rebar-5-6', 
    'xbeam-2-4-2', 'xbeam-2-4-2-rebar-5-1', 'xbeam-2-4-2-rebar-5-2', 
    'xbeam-2-4-2-rebar-5-3', 'xbeam-2-4-2-rebar-5-4', 'xbeam-2-4-2-rebar-5-5', 
    'xbeam-2-4-2-rebar-5-6', 'xbeam-2-4-1', 'xbeam-2-4-1-rebar-5-1', 
    'xbeam-2-4-1-rebar-5-2', 'xbeam-2-4-1-rebar-5-3', 'xbeam-2-4-1-rebar-5-4', 
    'xbeam-2-4-1-rebar-5-5', 'xbeam-2-4-1-rebar-5-6', 'xbeam-2-4-5', 
    'xbeam-2-4-5-rebar-5-1', 'xbeam-2-4-5-rebar-5-2', 'xbeam-2-4-5-rebar-5-3', 
    'xbeam-2-4-5-rebar-5-4', 'xbeam-2-4-5-rebar-5-5', 'xbeam-2-4-5-rebar-5-6', 
    'xbeam-2-4-4', 'xbeam-2-4-4-rebar-5-1', 'xbeam-2-4-4-rebar-5-2', 
    'xbeam-2-4-4-rebar-5-3', 'xbeam-2-4-4-rebar-5-4', 'xbeam-2-4-4-rebar-5-5', 
    'xbeam-2-4-4-rebar-5-6', 'xbeam-1-3-5', 'xbeam-1-3-5-rebar-5-1', 
    'xbeam-1-3-5-rebar-5-2', 'xbeam-1-3-5-rebar-5-3', 'xbeam-1-3-5-rebar-5-4', 
    'xbeam-1-3-5-rebar-5-5', 'xbeam-1-3-5-rebar-5-6', 'xbeam-1-3-4', 
    'xbeam-1-3-4-rebar-5-1', 'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 
    'xbeam-1-3-4-rebar-5-4', 'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 
    'xbeam-1-3-3', 'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 
    'xbeam-1-3-3-rebar-5-3', 'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 
    'xbeam-1-3-3-rebar-5-6', 'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 
    'xbeam-1-3-2-rebar-5-2', 'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 
    'xbeam-1-3-2-rebar-5-5', 'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 
    'xbeam-1-3-1-rebar-5-1', 'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 
    'xbeam-1-3-1-rebar-5-4', 'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 
    'xbeam-1-4-1', 'xbeam-1-4-1-rebar-5-1', 'xbeam-1-4-1-rebar-5-2', 
    'xbeam-1-4-1-rebar-5-3', 'xbeam-1-4-1-rebar-5-4', 'xbeam-1-4-1-rebar-5-5', 
    'xbeam-1-4-1-rebar-5-6', 'xbeam-1-4-2', 'xbeam-1-4-2-rebar-5-1', 
    'xbeam-1-4-2-rebar-5-2', 'xbeam-1-4-2-rebar-5-3', 'xbeam-1-4-2-rebar-5-4', 
    'xbeam-1-4-2-rebar-5-5', 'xbeam-1-4-2-rebar-5-6', 'xbeam-1-4-3', 
    'xbeam-1-4-3-rebar-5-1', 'xbeam-1-4-3-rebar-5-2', 'xbeam-1-4-3-rebar-5-3', 
    'xbeam-1-4-3-rebar-5-4', 'xbeam-1-4-3-rebar-5-5', 'xbeam-1-4-3-rebar-5-6', 
    'xbeam-1-4-4', 'xbeam-1-4-4-rebar-5-1', 'xbeam-1-4-4-rebar-5-2', 
    'xbeam-1-4-4-rebar-5-3', 'xbeam-1-4-4-rebar-5-4', 'xbeam-1-4-4-rebar-5-5', 
    'xbeam-1-4-4-rebar-5-6', 'xbeam-1-4-5', 'xbeam-1-4-5-rebar-5-1', 
    'xbeam-1-4-5-rebar-5-2', 'xbeam-1-4-5-rebar-5-3', 'xbeam-1-4-5-rebar-5-4', 
    'xbeam-1-4-5-rebar-5-5', 'xbeam-1-4-5-rebar-5-6', 'xbeam-2-2-1', 
    'xbeam-2-2-1-rebar-5-1', 'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 
    'xbeam-2-2-1-rebar-5-4', 'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 
    'xbeam-2-2-3', 'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 
    'xbeam-2-2-3-rebar-5-3', 'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 
    'xbeam-2-2-3-rebar-5-6', 'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 
    'xbeam-2-2-2-rebar-5-2', 'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 
    'xbeam-2-2-2-rebar-5-5', 'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-5', 
    'xbeam-2-2-5-rebar-5-1', 'xbeam-2-2-5-rebar-5-2', 'xbeam-2-2-5-rebar-5-3', 
    'xbeam-2-2-5-rebar-5-4', 'xbeam-2-2-5-rebar-5-5', 'xbeam-2-2-5-rebar-5-6', 
    'xbeam-2-2-4', 'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 
    'xbeam-2-2-4-rebar-5-3', 'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 
    'xbeam-2-2-4-rebar-5-6', 'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 
    'xbeam-2-1-2-rebar-5-2', 'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 
    'xbeam-2-1-2-rebar-5-5', 'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 
    'xbeam-2-1-3-rebar-5-1', 'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 
    'xbeam-2-1-3-rebar-5-4', 'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 
    'xbeam-2-1-1', 'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 
    'xbeam-2-1-1-rebar-5-3', 'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 
    'xbeam-2-1-1-rebar-5-6', 'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 
    'xbeam-2-3-1-rebar-5-2', 'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 
    'xbeam-2-3-1-rebar-5-5', 'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 
    'xbeam-2-1-4-rebar-5-1', 'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 
    'xbeam-2-1-4-rebar-5-4', 'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 
    'xbeam-2-1-5', 'xbeam-2-1-5-rebar-5-1', 'xbeam-2-1-5-rebar-5-2', 
    'xbeam-2-1-5-rebar-5-3', 'xbeam-2-1-5-rebar-5-4', 'xbeam-2-1-5-rebar-5-5', 
    'xbeam-2-1-5-rebar-5-6', 'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 
    'xbeam-2-3-4-rebar-5-2', 'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 
    'xbeam-2-3-4-rebar-5-5', 'xbeam-2-3-4-rebar-5-6', 'xbeam-2-3-5', 
    'xbeam-2-3-5-rebar-5-1', 'xbeam-2-3-5-rebar-5-2', 'xbeam-2-3-5-rebar-5-3', 
    'xbeam-2-3-5-rebar-5-4', 'xbeam-2-3-5-rebar-5-5', 'xbeam-2-3-5-rebar-5-6', 
    ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=48598.3, 
    farPlane=82021, width=24240.5, height=15968.6, viewOffsetX=1103.72, 
    viewOffsetY=1518.3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48447, 
    farPlane=82172.2, width=24165, height=15918.9, viewOffsetX=2995.08, 
    viewOffsetY=4006.58)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50296.3, 
    farPlane=80322.9, width=7742.6, height=5100.49, viewOffsetX=1047.15, 
    viewOffsetY=4924.31)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50351.5, 
    farPlane=80267.7, width=7751.1, height=5106.08, viewOffsetX=948.39, 
    viewOffsetY=4163.38)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50819.3, 
    farPlane=79800, width=3499.78, height=2305.5, viewOffsetX=-132.023, 
    viewOffsetY=4819.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50844.7, 
    farPlane=79774.5, width=3501.54, height=2306.66, viewOffsetX=-177.222, 
    viewOffsetY=5100.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51146.4, 
    farPlane=79472.9, width=848.729, height=559.105, viewOffsetX=-1067.24, 
    viewOffsetY=5372.99)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['xbeam-2-1-3'].vertices
e11 = a.instances['col-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e11[14], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-1-3'].vertices
e1 = a.instances['col-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e1[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#20 ]', ), )
v1 = a.instances['xbeam-2-2-3'].vertices
e11 = a.instances['col-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e11[27], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-2-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-2-3'].vertices
e1 = a.instances['col-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e1[37], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50393.5, 
    farPlane=80225.7, width=7853.18, height=5173.33, viewOffsetX=-46.1534, 
    viewOffsetY=5433.11)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50340.7, 
    farPlane=80278.6, width=7844.95, height=5167.91, viewOffsetX=922.927, 
    viewOffsetY=3791.89)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1024.04, 
    viewOffsetY=3420.94)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1327.39, 
    viewOffsetY=4263.99)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50390.1, 
    farPlane=80229.2, width=7884.77, height=5194.14, viewOffsetX=1156.51, 
    viewOffsetY=4403.69)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50337, 
    farPlane=80282.2, width=7876.47, height=5188.67, viewOffsetX=3050.39, 
    viewOffsetY=3180.18)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=5486.93, 
    viewOffsetY=3290.22)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50965.6, 
    farPlane=79653.6, width=2313.55, height=1524.06, viewOffsetX=5571.27, 
    viewOffsetY=3359.42)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52856.2, 
    farPlane=73664, width=2399.37, height=1580.6, cameraPosition=(7136.81, 
    52461.3, 51708), cameraUpVector=(-0.264315, 0.31759, -0.910645), 
    cameraTarget=(7289.56, 2056.5, 10178.8), viewOffsetX=5777.94, 
    viewOffsetY=3484.04)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52846.3, 
    farPlane=73673.8, width=2398.92, height=1580.3, viewOffsetX=6735.4, 
    viewOffsetY=3027.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46563.6, 
    farPlane=74504.8, width=2113.72, height=1392.43, cameraPosition=(-25999.1, 
    41323.8, 43423.2), cameraUpVector=(0.106858, 0.385188, -0.91663), 
    cameraTarget=(8536.44, 93.377, 6373.32), viewOffsetX=5934.66, 
    viewOffsetY=2667.2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46732, 
    farPlane=74336.5, width=892.085, height=587.666, viewOffsetX=5667.25, 
    viewOffsetY=2556.16)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v1 = a.instances['xbeam-2-3-2'].vertices
e11 = a.instances['xbeam-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[7], normal=e11[9], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46609.3, 
    farPlane=74459.2, width=2133.15, height=1405.22, viewOffsetX=5930.54, 
    viewOffsetY=2585.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51677.4, 
    farPlane=73596.8, width=2365.1, height=1558.02, cameraPosition=(9081.84, 
    50434.6, 53231.8), cameraUpVector=(-0.363108, 0.338813, -0.867962), 
    cameraTarget=(6153.21, 1372.7, 10223.7), viewOffsetX=6575.4, 
    viewOffsetY=2867.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51650.5, 
    farPlane=73623.6, width=2363.87, height=1557.21, viewOffsetX=7417.49, 
    viewOffsetY=2276.3)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=7864.37, 
    viewOffsetY=2101.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51589.4, 
    farPlane=78667.7, width=2361.07, height=1555.37, cameraPosition=(40421.9, 
    46669.4, 49254.4), cameraUpVector=(-0.693507, 0.458898, -0.555393), 
    cameraTarget=(7960.16, 2332.88, 13957.7), viewOffsetX=7855.07, 
    viewOffsetY=2098.54)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51733.1, 
    farPlane=78524.1, width=1059.2, height=697.756, viewOffsetX=7885.04, 
    viewOffsetY=2112.5)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v11 = a.instances['xbeam-2-4-2'].vertices
e1 = a.instances['xbeam-2-4-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e1[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51797.3, 
    farPlane=78459.9, width=539.134, height=355.158, viewOffsetX=7860.3, 
    viewOffsetY=2156.99)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v1 = a.instances['zbeam-2-4-2'].vertices
e11 = a.instances['zbeam-2-4-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[7], normal=e11[9], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51659.1, 
    farPlane=78598.1, width=1876.29, height=1236.01, viewOffsetX=7980.62, 
    viewOffsetY=2162.28)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51646.1, 
    farPlane=78611.1, width=1875.82, height=1235.7, viewOffsetX=8290.92, 
    viewOffsetY=2532.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59375.8, 
    farPlane=81577.7, width=2156.57, height=1420.65, cameraPosition=(64010.7, 
    48047.5, 5351.62), cameraUpVector=(-0.877914, 0.471003, 0.086154), 
    cameraTarget=(16652.3, 4181.81, 15267.7), viewOffsetX=9531.8, 
    viewOffsetY=2911.71)
session.viewports['Viewport: 1'].view.setValues(width=2177.16, height=1434.22, 
    viewOffsetX=9531.22, viewOffsetY=2909.28)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59340.9, 
    farPlane=81612.6, width=2177.07, height=1434.16, viewOffsetX=8649.25, 
    viewOffsetY=3152.48)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58664.9, 
    farPlane=83926.7, width=2152.27, height=1417.82, cameraPosition=(66472.7, 
    43292.1, -5445.14), cameraUpVector=(-0.804115, 0.542335, 0.243459), 
    cameraTarget=(18339.3, 3494.23, 13650.7), viewOffsetX=8550.72, 
    viewOffsetY=3116.57)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58667.8, 
    farPlane=83923.8, width=2152.38, height=1417.89, viewOffsetX=7952.36, 
    viewOffsetY=3701.92)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=7637.94, 
    viewOffsetY=3671.85)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58329.7, 
    farPlane=85190.1, width=2139.98, height=1409.72, cameraPosition=(65191.5, 
    41877.5, -13240.9), cameraUpVector=(-0.763249, 0.563188, 0.316654), 
    cameraTarget=(19004.6, 3501.11, 12437.3), viewOffsetX=7593.93, 
    viewOffsetY=3650.69)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58331.2, 
    farPlane=85188.7, width=2140.03, height=1409.76, viewOffsetX=6971.19, 
    viewOffsetY=4129.13)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58474.8, 
    farPlane=85045, width=848.021, height=558.639, viewOffsetX=6705.21, 
    viewOffsetY=3965.9)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#8 ]', ), )
v11 = a.instances['zbeam-2-4-1'].vertices
e1 = a.instances['zbeam-2-4-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[6], normal=e1[7], 
    cells=pickedCells)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-183831.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x000000000EC06968>materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48040.4, 
    farPlane=82578.8, width=26898.3, height=17719.4, viewOffsetX=6327.32, 
    viewOffsetY=1647.65)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50026.5, 
    farPlane=80592.7, width=11208.7, height=7383.81, viewOffsetX=4200.22, 
    viewOffsetY=2022.21)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49952.2, 
    farPlane=80667, width=11192.1, height=7372.85, viewOffsetX=2318.62, 
    viewOffsetY=2079.34)

    
session.viewports['Viewport: 1'].view.setValues(nearPlane=51098.8, 
    farPlane=79520.4, width=1234.16, height=813.009, viewOffsetX=1458.83, 
    viewOffsetY=4026.46)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#20 ]', ), )
v1 = a.instances['xbeam-2-2-3'].vertices
e11 = a.instances['xbeam-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[2], normal=e11[6], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-2-3'].vertices
e1 = a.instances['xbeam-2-2-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[5], normal=e1[6], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51001.6, 
    farPlane=79617.7, width=2286.99, height=1506.57, viewOffsetX=1709.37, 
    viewOffsetY=3902.57)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v1 = a.instances['xbeam-2-3-3'].vertices
e11 = a.instances['xbeam-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e11[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-3-3'].vertices
e1 = a.instances['xbeam-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e1[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#400 ]', ), )
v1 = a.instances['zbeam-2-3-3'].vertices
e11 = a.instances['col-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e11[51], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-3-3'].vertices
e1 = a.instances['col-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e1[7], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#40 ]', ), )
v1 = a.instances['zbeam-2-3-2'].vertices
e11 = a.instances['col-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e11[74], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-3-2'].vertices
e1 = a.instances['col-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e1[82], 
    cells=pickedCells)


session.viewports['Viewport: 1'].view.setValues(nearPlane=50393.5, 
    farPlane=80225.7, width=7853.17, height=5173.33, viewOffsetX=1651.77, 
    viewOffsetY=4013.9)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50340.7, 
    farPlane=80278.6, width=7844.94, height=5167.9, viewOffsetX=4034.7, 
    viewOffsetY=4701)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51145.1, 
    farPlane=79474.2, width=859.166, height=565.981, viewOffsetX=2744.38, 
    viewOffsetY=4938.44)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#20 ]', ), )
v1 = a.instances['xbeam-2-2-2'].vertices
e11 = a.instances['xbeam-2-2-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e11[6], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#40 ]', ), )
v11 = a.instances['xbeam-2-2-2'].vertices
e1 = a.instances['xbeam-2-2-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e1[6], 
    cells=pickedCells)
#: ????: ????????--??????????????????????????.
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v1 = a.instances['xbeam-2-3-2'].vertices
e11 = a.instances['col-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e11[33], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(width=914.12, height=602.182, 
    viewOffsetX=2737.74, viewOffsetY=4942.44)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-3-2'].vertices
e1 = a.instances['xbeam-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e1[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#400 ]', ), )
v1 = a.instances['zbeam-2-3-2'].vertices
e11 = a.instances['col-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e11[51], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-3-2'].vertices
e1 = a.instances['col-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e1[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#40 ]', ), )
v1 = a.instances['zbeam-2-3-1'].vertices
e11 = a.instances['zbeam-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e11[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-3-1'].vertices
e1 = a.instances['zbeam-2-3-1'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e1[4], 
    cells=pickedCells)


session.viewports['Viewport: 1'].view.setValues(nearPlane=50947.3, 
    farPlane=79672, width=2784.44, height=1834.27, viewOffsetX=2813.77, 
    viewOffsetY=4679.79)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50928.1, 
    farPlane=79691.1, width=2783.39, height=1833.58, viewOffsetX=2872.51, 
    viewOffsetY=4767.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50528.2, 
    farPlane=80091, width=6620.76, height=4361.47, viewOffsetX=3227.93, 
    viewOffsetY=4640.94)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50483.4, 
    farPlane=80135.8, width=6614.89, height=4357.6, viewOffsetX=5896.6, 
    viewOffsetY=3961.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50963.3, 
    farPlane=79656, width=2332.41, height=1536.49, viewOffsetX=5685.75, 
    viewOffsetY=3859.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50980.3, 
    farPlane=79638.9, width=2333.19, height=1537, viewOffsetX=5700.18, 
    viewOffsetY=3595.21)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#20 ]', ), )
v1 = a.instances['xbeam-2-3-2'].vertices
e11 = a.instances['xbeam-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e11[6], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#40 ]', ), )
v11 = a.instances['xbeam-2-3-2'].vertices
e1 = a.instances['xbeam-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e1[6], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v1 = a.instances['xbeam-2-4-2'].vertices
e11 = a.instances['col-2-4-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e11[33], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-4-2'].vertices
e1 = a.instances['col-2-4-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e1[8], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#400 ]', ), )
v1 = a.instances['zbeam-2-4-2'].vertices
e11 = a.instances['col-2-4-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e11[51], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-4-2'].vertices
e1 = a.instances['col-2-4-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e1[4], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#40 ]', ), )
v1 = a.instances['zbeam-2-4-1'].vertices
e11 = a.instances['col-2-4-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e11[80], 
    cells=pickedCells)
#: ????: ????????--??????????????????????????.
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-4-1'].vertices
e1 = a.instances['col-2-4-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e1[85], 
    cells=pickedCells)


session.viewports['Viewport: 1'].view.setValues(nearPlane=50977.1, 
    farPlane=79642.1, width=2220.09, height=1462.5, viewOffsetX=4456.04, 
    viewOffsetY=2782.74)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#20 ]', ), )
v1 = a.instances['xbeam-2-3-3'].vertices
e11 = a.instances['xbeam-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e11[6], 
    cells=pickedCells)
#: ????: ????????--??????????????????????????.
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#40 ]', ), )
v11 = a.instances['xbeam-2-3-3'].vertices
e1 = a.instances['xbeam-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e1[6], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#10 ]', ), )
v1 = a.instances['xbeam-2-4-3'].vertices
e11 = a.instances['col-2-4-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e11[33], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-4-3'].vertices
e1 = a.instances['col-2-4-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e1[8], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#400 ]', ), )
v1 = a.instances['zbeam-2-4-3'].vertices
e11 = a.instances['zbeam-2-4-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[5], normal=e11[6], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-4-3'].vertices
e1 = a.instances['zbeam-2-4-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e1[6], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#40 ]', ), )
v1 = a.instances['zbeam-2-4-2'].vertices
e11 = a.instances['col-2-4-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[4], normal=e11[74], 
    cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['zbeam-2-4-2'].vertices
e1 = a.instances['col-2-4-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[1], normal=e1[82], 
    cells=pickedCells)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-184932.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x000000000EEC0B68>materials created
#* ????????????.
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 1128, in 
#* <module>
#*     mymodel.startBuilding()
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 264, in 
#* startBuilding
#*     surfs.append(self.getColSurfToBeam(colName))
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 629, in 
#* getColSurfToBeam
#*     a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[6], 
#* cells=pickedCells)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=49716.5, 
    farPlane=80902.8, width=12453.2, height=8203.62, viewOffsetX=1326.45, 
    viewOffsetY=2096.47)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49803.2, 
    farPlane=80816, width=12474.9, height=8217.93, viewOffsetX=2534.72, 
    viewOffsetY=5156.72)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49803.3, 
    farPlane=80816, width=12474.9, height=8217.94, viewOffsetX=4263.26, 
    viewOffsetY=3521.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49803.3, 
    farPlane=80816, width=12474.9, height=8217.94, viewOffsetX=4370.45, 
    viewOffsetY=3521.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49803.3, 
    farPlane=80816, width=12474.9, height=8217.94, viewOffsetX=4678.64, 
    viewOffsetY=3413.93)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50217.8, 
    farPlane=80401.5, width=9460.54, height=6232.19, viewOffsetX=6166.33, 
    viewOffsetY=2842.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50154.5, 
    farPlane=80464.7, width=9448.63, height=6224.34, viewOffsetX=4555.04, 
    viewOffsetY=3722.21)
#: ????: ????????--??????????????????????????.
session.viewports['Viewport: 1'].view.setValues(nearPlane=51141.3, 
    farPlane=79477.9, width=889.693, height=586.091, viewOffsetX=2808.93, 
    viewOffsetY=2821.47)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v1 = a.instances['col-2-3-2'].vertices
a.PartitionCellByPlaneThreePoints(point1=v1[3], point2=v1[5], point3=v1[4], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50988.5, 
    farPlane=79630.8, width=2406.81, height=1585.5, viewOffsetX=3020.68, 
    viewOffsetY=2712.72)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50971.9, 
    farPlane=79647.3, width=2406.02, height=1584.98, viewOffsetX=3167, 
    viewOffsetY=3619.39)
session.viewports['Viewport: 1'].view.setValues(farPlane=79647.3, 
    viewOffsetX=3309.14, viewOffsetY=4436.44)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50757.6, 
    farPlane=79861.7, width=4521.51, height=2978.57, viewOffsetX=2731, 
    viewOffsetY=4348.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50726.7, 
    farPlane=79892.5, width=4518.76, height=2976.76, viewOffsetX=3476.8, 
    viewOffsetY=3311.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51157.6, 
    farPlane=79461.6, width=757.531, height=499.028, viewOffsetX=3005.56, 
    viewOffsetY=2836.67)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['col-2-3-2'].vertices
a.PartitionCellByPlaneThreePoints(point1=v11[6], point2=v11[5], point3=v11[7], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50811, 
    farPlane=79808.2, width=4032.2, height=2656.24, viewOffsetX=3536.18, 
    viewOffsetY=2854.95)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50783.4, 
    farPlane=79835.8, width=4030.01, height=2654.79, viewOffsetX=3659.79, 
    viewOffsetY=4048.7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50915.8, 
    farPlane=79703.4, width=3071.29, height=2023.23, viewOffsetX=2777.36, 
    viewOffsetY=4561.69)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50894.8, 
    farPlane=79724.4, width=3070.02, height=2022.39, viewOffsetX=3007.05, 
    viewOffsetY=3791.11)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=3119.17, 
    viewOffsetY=2949.82)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51147.3, 
    farPlane=79472, width=841.347, height=554.243, viewOffsetX=2970.15, 
    viewOffsetY=2798.98)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#4 ]', ), )
v1 = a.instances['col-2-3-2'].vertices
a.PartitionCellByPlaneThreePoints(point1=v1[2], point2=v1[8], point3=v1[9], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50789.8, 
    farPlane=79829.4, width=4225.95, height=2783.87, viewOffsetX=3082.31, 
    viewOffsetY=2463.67)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50760.9, 
    farPlane=79858.3, width=4223.55, height=2782.29, viewOffsetX=3702.07, 
    viewOffsetY=3946.45)
session.viewports['Viewport: 1'].view.setValues(farPlane=79858.3, 
    viewOffsetY=4622.74)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51030.7, 
    farPlane=79588.5, width=1785.54, height=1176.24, viewOffsetX=3131.61, 
    viewOffsetY=4803.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51043.9, 
    farPlane=79575.4, width=1786, height=1176.54, viewOffsetX=2998.13, 
    viewOffsetY=4739.15)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-3-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
v11 = a.instances['xbeam-2-2-2'].vertices
e11 = a.instances['xbeam-2-2-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[2], normal=e11[6], 
    cells=pickedCells)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-185621.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: materials created
#* ????????????.
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 1142, in 
#* <module>
#*     mymodel.startBuilding()
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 264, in 
#* startBuilding
#*     surfs.append(self.getColSurfToBeam(colName))
#* File "F:/documents/Abaqus/abaqus-model/abaqus_structure.py", line 637, in 
#* getColSurfToBeam
#*     a.PartitionCellByPlanePointNormal(point=v1[5], normal=e1[6], 
#* cells=pickedCells)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=50703.1, 
    farPlane=79916.2, width=5020.34, height=3307.18, viewOffsetX=4271.29, 
    viewOffsetY=3161.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50668.9, 
    farPlane=79950.4, width=5016.95, height=3304.95, viewOffsetX=5567.11, 
    viewOffsetY=3822.26)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50703.1, 
    farPlane=79916.2, width=5020.34, height=3307.18, viewOffsetX=5548.49, 
    viewOffsetY=3832.31)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50668.9, 
    farPlane=79950.4, width=5016.96, height=3304.95, viewOffsetX=4154.44, 
    viewOffsetY=4034.6)
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: ?????????????????? "c:\Abaqus_TempSave\abaqus_model_20170721-185859.cae".
#: ????????????????????.
#: ???? "Model-1" ??????.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: ?????????????????? "D:\pymodel.cae".
#: materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49434.7, 
    farPlane=81184.6, width=16614.5, height=10944.9, viewOffsetX=1432.41, 
    viewOffsetY=2762.96)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49327.2, 
    farPlane=81292, width=16578.4, height=10921.1, viewOffsetX=4403.08, 
    viewOffsetY=3166.72)


    
session.viewports['Viewport: 1'].view.setValues(nearPlane=50711.4, 
    farPlane=79907.9, width=4944.46, height=3257.19, viewOffsetX=4215.27, 
    viewOffsetY=2954.66)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50677.7, 
    farPlane=79941.6, width=4941.17, height=3255.03, viewOffsetX=5518.09, 
    viewOffsetY=3080.14)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51120.1, 
    farPlane=79499.1, width=1061.21, height=699.079, viewOffsetX=5432.48, 
    viewOffsetY=3621.06)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#20 ]', ), )
v1 = a.instances['xbeam-2-3-2'].vertices
e1 = a.instances['xbeam-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v1[2], normal=e1[6], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-2'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-3-2'].vertices
e11 = a.instances['xbeam-2-3-2'].edges
a.PartitionCellByPlanePointNormal(point=v11[5], normal=e11[6], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51081.4, 
    farPlane=79537.8, width=1374.93, height=905.744, viewOffsetX=4423.47, 
    viewOffsetY=3034.09)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#20 ]', ), )
v1 = a.instances['xbeam-2-3-3'].vertices
e1 = a.instances['xbeam-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v1[2], normal=e1[6], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-3'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-3-3'].vertices
e11 = a.instances['xbeam-2-3-3'].edges
a.PartitionCellByPlanePointNormal(point=v11[5], normal=e11[6], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50541.6, 
    farPlane=80077.7, width=6498.5, height=4280.93, viewOffsetX=4721.42, 
    viewOffsetY=2704.75)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50497.6, 
    farPlane=80121.7, width=6492.84, height=4277.2, viewOffsetX=3364.34, 
    viewOffsetY=3532.72)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=2109.01, 
    viewOffsetY=2423.3)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1767.28, 
    viewOffsetY=1530.18)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51001.3, 
    farPlane=79617.9, width=2023.83, height=1333.21, viewOffsetX=651.581, 
    viewOffsetY=893.776)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#20 ]', ), )
v1 = a.instances['xbeam-2-3-4'].vertices
e1 = a.instances['xbeam-2-3-4'].edges
a.PartitionCellByPlanePointNormal(point=v1[2], normal=e1[6], cells=pickedCells)
a = mdb.models['structure'].rootAssembly
c1 = a.instances['col-2-4-4'].cells
pickedCells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
v11 = a.instances['xbeam-2-3-4'].vertices
e11 = a.instances['xbeam-2-3-4'].edges
a.PartitionCellByPlanePointNormal(point=v11[5], normal=e11[6], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
execfile('F:/documents/Abaqus/abaqus-model/abaqus_structure.py', 
    __main__.__dict__)
#: 模型数据库已保存到 "c:\Abaqus_TempSave\abaqus_model_20170721-190307.cae".
#: 新的模型数据库已创建.
#: 模型 "Model-1" 已创建.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 模型数据库已保存到 "D:\pymodel.cae".
#: Exception <ExceptionValue object at 0x0000000009D42F48>materials created
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['structure'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50179.2, 
    farPlane=80440.1, width=9813.33, height=6464.59, viewOffsetX=2149.51, 
    viewOffsetY=3628.36)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50113.7, 
    farPlane=80505.5, width=9800.52, height=6456.15, viewOffsetX=809.789, 
    viewOffsetY=3465.64)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=388.714, 
    viewOffsetY=3865.86)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50359.7, 
    farPlane=80259.5, width=7227.95, height=4761.45, viewOffsetX=130.243, 
    viewOffsetY=3582.09)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'zbeam-1-1-3', 'zbeam-1-1-3-rebar-3-1', 'zbeam-1-1-3-rebar-3-2', 
    'zbeam-1-1-3-rebar-3-3', 'zbeam-1-1-3-rebar-3-4', 'zbeam-1-1-3-rebar-3-5', 
    'zbeam-1-1-3-rebar-3-6', 'zbeam-1-1-2', 'zbeam-1-1-2-rebar-4-1', 
    'zbeam-1-1-2-rebar-4-2', 'zbeam-1-1-2-rebar-4-3', 'zbeam-1-1-2-rebar-4-4', 
    'zbeam-1-1-2-rebar-4-5', 'zbeam-1-1-2-rebar-4-6', 'zbeam-1-1-1', 
    'zbeam-1-1-1-rebar-3-1', 'zbeam-1-1-1-rebar-3-2', 'zbeam-1-1-1-rebar-3-3', 
    'zbeam-1-1-1-rebar-3-4', 'zbeam-1-1-1-rebar-3-5', 'zbeam-1-1-1-rebar-3-6', 
    'zbeam-1-2-1', 'zbeam-1-2-1-rebar-3-1', 'zbeam-1-2-1-rebar-3-2', 
    'zbeam-1-2-1-rebar-3-3', 'zbeam-1-2-1-rebar-3-4', 'zbeam-1-2-1-rebar-3-5', 
    'zbeam-1-2-1-rebar-3-6', 'zbeam-1-1-4', 'zbeam-1-1-4-rebar-3-1', 
    'zbeam-1-1-4-rebar-3-2', 'zbeam-1-1-4-rebar-3-3', 'zbeam-1-1-4-rebar-3-4', 
    'zbeam-1-1-4-rebar-3-5', 'zbeam-1-1-4-rebar-3-6', 'zbeam-1-2-4', 
    'zbeam-1-2-4-rebar-3-1', 'zbeam-1-2-4-rebar-3-2', 'zbeam-1-2-4-rebar-3-3', 
    'zbeam-1-2-4-rebar-3-4', 'zbeam-1-2-4-rebar-3-5', 'zbeam-1-2-4-rebar-3-6', 
    'zbeam-2-1-1', 'zbeam-2-1-1-rebar-3-1', 'zbeam-2-1-1-rebar-3-2', 
    'zbeam-2-1-1-rebar-3-3', 'zbeam-2-1-1-rebar-3-4', 'zbeam-2-1-1-rebar-3-5', 
    'zbeam-2-1-1-rebar-3-6', 'zbeam-2-1-2', 'zbeam-2-1-2-rebar-4-1', 
    'zbeam-2-1-2-rebar-4-2', 'zbeam-2-1-2-rebar-4-3', 'zbeam-2-1-2-rebar-4-4', 
    'zbeam-2-1-2-rebar-4-5', 'zbeam-2-1-2-rebar-4-6', 'zbeam-2-1-3', 
    'zbeam-2-1-3-rebar-3-1', 'zbeam-2-1-3-rebar-3-2', 'zbeam-2-1-3-rebar-3-3', 
    'zbeam-2-1-3-rebar-3-4', 'zbeam-2-1-3-rebar-3-5', 'zbeam-2-1-3-rebar-3-6', 
    'zbeam-2-1-4', 'zbeam-2-1-4-rebar-3-1', 'zbeam-2-1-4-rebar-3-2', 
    'zbeam-2-1-4-rebar-3-3', 'zbeam-2-1-4-rebar-3-4', 'zbeam-2-1-4-rebar-3-5', 
    'zbeam-2-1-4-rebar-3-6', 'zbeam-1-4-2', 'zbeam-1-4-2-rebar-4-1', 
    'zbeam-1-4-2-rebar-4-2', 'zbeam-1-4-2-rebar-4-3', 'zbeam-1-4-2-rebar-4-4', 
    'zbeam-1-4-2-rebar-4-5', 'zbeam-1-4-2-rebar-4-6', 'zbeam-1-4-3', 
    'zbeam-1-4-3-rebar-3-1', 'zbeam-1-4-3-rebar-3-2', 'zbeam-1-4-3-rebar-3-3', 
    'zbeam-1-4-3-rebar-3-4', 'zbeam-1-4-3-rebar-3-5', 'zbeam-1-4-3-rebar-3-6', 
    'zbeam-2-3-4', 'zbeam-2-3-4-rebar-3-1', 'zbeam-2-3-4-rebar-3-2', 
    'zbeam-2-3-4-rebar-3-3', 'zbeam-2-3-4-rebar-3-4', 'zbeam-2-3-4-rebar-3-5', 
    'zbeam-2-3-4-rebar-3-6', 'zbeam-1-4-1', 'zbeam-1-4-1-rebar-3-1', 
    'zbeam-1-4-1-rebar-3-2', 'zbeam-1-4-1-rebar-3-3', 'zbeam-1-4-1-rebar-3-4', 
    'zbeam-1-4-1-rebar-3-5', 'zbeam-1-4-1-rebar-3-6', 'zbeam-2-3-2', 
    'zbeam-2-3-2-rebar-4-1', 'zbeam-2-3-2-rebar-4-2', 'zbeam-2-3-2-rebar-4-3', 
    'zbeam-2-3-2-rebar-4-4', 'zbeam-2-3-2-rebar-4-5', 'zbeam-2-3-2-rebar-4-6', 
    'zbeam-2-3-3', 'zbeam-2-3-3-rebar-3-1', 'zbeam-2-3-3-rebar-3-2', 
    'zbeam-2-3-3-rebar-3-3', 'zbeam-2-3-3-rebar-3-4', 'zbeam-2-3-3-rebar-3-5', 
    'zbeam-2-3-3-rebar-3-6', 'zbeam-1-4-4', 'zbeam-1-4-4-rebar-3-1', 
    'zbeam-1-4-4-rebar-3-2', 'zbeam-1-4-4-rebar-3-3', 'zbeam-1-4-4-rebar-3-4', 
    'zbeam-1-4-4-rebar-3-5', 'zbeam-1-4-4-rebar-3-6', 'zbeam-2-3-1', 
    'zbeam-2-3-1-rebar-3-1', 'zbeam-2-3-1-rebar-3-2', 'zbeam-2-3-1-rebar-3-3', 
    'zbeam-2-3-1-rebar-3-4', 'zbeam-2-3-1-rebar-3-5', 'zbeam-2-3-1-rebar-3-6', 
    'zbeam-2-2-3', 'zbeam-2-2-3-rebar-3-1', 'zbeam-2-2-3-rebar-3-2', 
    'zbeam-2-2-3-rebar-3-3', 'zbeam-2-2-3-rebar-3-4', 'zbeam-2-2-3-rebar-3-5', 
    'zbeam-2-2-3-rebar-3-6', 'zbeam-2-2-2', 'zbeam-2-2-2-rebar-4-1', 
    'zbeam-2-2-2-rebar-4-2', 'zbeam-2-2-2-rebar-4-3', 'zbeam-2-2-2-rebar-4-4', 
    'zbeam-2-2-2-rebar-4-5', 'zbeam-2-2-2-rebar-4-6', 'zbeam-2-2-1', 
    'zbeam-2-2-1-rebar-3-1', 'zbeam-2-2-1-rebar-3-2', 'zbeam-2-2-1-rebar-3-3', 
    'zbeam-2-2-1-rebar-3-4', 'zbeam-2-2-1-rebar-3-5', 'zbeam-2-2-1-rebar-3-6', 
    'zbeam-2-2-4', 'zbeam-2-2-4-rebar-3-1', 'zbeam-2-2-4-rebar-3-2', 
    'zbeam-2-2-4-rebar-3-3', 'zbeam-2-2-4-rebar-3-4', 'zbeam-2-2-4-rebar-3-5', 
    'zbeam-2-2-4-rebar-3-6', 'zbeam-1-5-4', 'zbeam-1-5-4-rebar-3-1', 
    'zbeam-1-5-4-rebar-3-2', 'zbeam-1-5-4-rebar-3-3', 'zbeam-1-5-4-rebar-3-4', 
    'zbeam-1-5-4-rebar-3-5', 'zbeam-1-5-4-rebar-3-6', 'zbeam-1-5-3', 
    'zbeam-1-5-3-rebar-3-1', 'zbeam-1-5-3-rebar-3-2', 'zbeam-1-5-3-rebar-3-3', 
    'zbeam-1-5-3-rebar-3-4', 'zbeam-1-5-3-rebar-3-5', 'zbeam-1-5-3-rebar-3-6', 
    'zbeam-1-5-2', 'zbeam-1-5-2-rebar-4-1', 'zbeam-1-5-2-rebar-4-2', 
    'zbeam-1-5-2-rebar-4-3', 'zbeam-1-5-2-rebar-4-4', 'zbeam-1-5-2-rebar-4-5', 
    'zbeam-1-5-2-rebar-4-6', 'zbeam-1-5-1', 'zbeam-1-5-1-rebar-3-1', 
    'zbeam-1-5-1-rebar-3-2', 'zbeam-1-5-1-rebar-3-3', 'zbeam-1-5-1-rebar-3-4', 
    'zbeam-1-5-1-rebar-3-5', 'zbeam-1-5-1-rebar-3-6', 'zbeam-1-3-4', 
    'zbeam-1-3-4-rebar-3-1', 'zbeam-1-3-4-rebar-3-2', 'zbeam-1-3-4-rebar-3-3', 
    'zbeam-1-3-4-rebar-3-4', 'zbeam-1-3-4-rebar-3-5', 'zbeam-1-3-4-rebar-3-6', 
    'zbeam-1-2-2', 'zbeam-1-2-2-rebar-4-1', 'zbeam-1-2-2-rebar-4-2', 
    'zbeam-1-2-2-rebar-4-3', 'zbeam-1-2-2-rebar-4-4', 'zbeam-1-2-2-rebar-4-5', 
    'zbeam-1-2-2-rebar-4-6', 'zbeam-1-2-3', 'zbeam-1-2-3-rebar-3-1', 
    'zbeam-1-2-3-rebar-3-2', 'zbeam-1-2-3-rebar-3-3', 'zbeam-1-2-3-rebar-3-4', 
    'zbeam-1-2-3-rebar-3-5', 'zbeam-1-2-3-rebar-3-6', 'zbeam-1-3-1', 
    'zbeam-1-3-1-rebar-3-1', 'zbeam-1-3-1-rebar-3-2', 'zbeam-1-3-1-rebar-3-3', 
    'zbeam-1-3-1-rebar-3-4', 'zbeam-1-3-1-rebar-3-5', 'zbeam-1-3-1-rebar-3-6', 
    'zbeam-1-3-3', 'zbeam-1-3-3-rebar-3-1', 'zbeam-1-3-3-rebar-3-2', 
    'zbeam-1-3-3-rebar-3-3', 'zbeam-1-3-3-rebar-3-4', 'zbeam-1-3-3-rebar-3-5', 
    'zbeam-1-3-3-rebar-3-6', 'zbeam-1-3-2', 'zbeam-1-3-2-rebar-4-1', 
    'zbeam-1-3-2-rebar-4-2', 'zbeam-1-3-2-rebar-4-3', 'zbeam-1-3-2-rebar-4-4', 
    'zbeam-1-3-2-rebar-4-5', 'zbeam-1-3-2-rebar-4-6', 'zbeam-2-4-1', 
    'zbeam-2-4-1-rebar-3-1', 'zbeam-2-4-1-rebar-3-2', 'zbeam-2-4-1-rebar-3-3', 
    'zbeam-2-4-1-rebar-3-4', 'zbeam-2-4-1-rebar-3-5', 'zbeam-2-4-1-rebar-3-6', 
    'zbeam-2-4-3', 'zbeam-2-4-3-rebar-3-1', 'zbeam-2-4-3-rebar-3-2', 
    'zbeam-2-4-3-rebar-3-3', 'zbeam-2-4-3-rebar-3-4', 'zbeam-2-4-3-rebar-3-5', 
    'zbeam-2-4-3-rebar-3-6', 'zbeam-2-4-2', 'zbeam-2-4-2-rebar-4-1', 
    'zbeam-2-4-2-rebar-4-2', 'zbeam-2-4-2-rebar-4-3', 'zbeam-2-4-2-rebar-4-4', 
    'zbeam-2-4-2-rebar-4-5', 'zbeam-2-4-2-rebar-4-6', 'zbeam-2-4-4', 
    'zbeam-2-4-4-rebar-3-1', 'zbeam-2-4-4-rebar-3-2', 'zbeam-2-4-4-rebar-3-3', 
    'zbeam-2-4-4-rebar-3-4', 'zbeam-2-4-4-rebar-3-5', 'zbeam-2-4-4-rebar-3-6', 
    'zbeam-2-5-4', 'zbeam-2-5-4-rebar-3-1', 'zbeam-2-5-4-rebar-3-2', 
    'zbeam-2-5-4-rebar-3-3', 'zbeam-2-5-4-rebar-3-4', 'zbeam-2-5-4-rebar-3-5', 
    'zbeam-2-5-4-rebar-3-6', 'zbeam-2-5-1', 'zbeam-2-5-1-rebar-3-1', 
    'zbeam-2-5-1-rebar-3-2', 'zbeam-2-5-1-rebar-3-3', 'zbeam-2-5-1-rebar-3-4', 
    'zbeam-2-5-1-rebar-3-5', 'zbeam-2-5-1-rebar-3-6', 'zbeam-2-5-2', 
    'zbeam-2-5-2-rebar-4-1', 'zbeam-2-5-2-rebar-4-2', 'zbeam-2-5-2-rebar-4-3', 
    'zbeam-2-5-2-rebar-4-4', 'zbeam-2-5-2-rebar-4-5', 'zbeam-2-5-2-rebar-4-6', 
    'zbeam-2-5-3', 'zbeam-2-5-3-rebar-3-1', 'zbeam-2-5-3-rebar-3-2', 
    'zbeam-2-5-3-rebar-3-3', 'zbeam-2-5-3-rebar-3-4', 'zbeam-2-5-3-rebar-3-5', 
    'zbeam-2-5-3-rebar-3-6', 'xbeam-2-3-2', 'xbeam-2-3-2-rebar-5-1', 
    'xbeam-2-3-2-rebar-5-2', 'xbeam-2-3-2-rebar-5-3', 'xbeam-2-3-2-rebar-5-4', 
    'xbeam-2-3-2-rebar-5-5', 'xbeam-2-3-2-rebar-5-6', 'xbeam-2-3-3', 
    'xbeam-2-3-3-rebar-5-1', 'xbeam-2-3-3-rebar-5-2', 'xbeam-2-3-3-rebar-5-3', 
    'xbeam-2-3-3-rebar-5-4', 'xbeam-2-3-3-rebar-5-5', 'xbeam-2-3-3-rebar-5-6', 
    'xbeam-1-1-1', 'xbeam-1-1-1-rebar-5-1', 'xbeam-1-1-1-rebar-5-2', 
    'xbeam-1-1-1-rebar-5-3', 'xbeam-1-1-1-rebar-5-4', 'xbeam-1-1-1-rebar-5-5', 
    'xbeam-1-1-1-rebar-5-6', 'xbeam-1-1-3', 'xbeam-1-1-3-rebar-5-1', 
    'xbeam-1-1-3-rebar-5-2', 'xbeam-1-1-3-rebar-5-3', 'xbeam-1-1-3-rebar-5-4', 
    'xbeam-1-1-3-rebar-5-5', 'xbeam-1-1-3-rebar-5-6', 'xbeam-1-1-2', 
    'xbeam-1-1-2-rebar-5-1', 'xbeam-1-1-2-rebar-5-2', 'xbeam-1-1-2-rebar-5-3', 
    'xbeam-1-1-2-rebar-5-4', 'xbeam-1-1-2-rebar-5-5', 'xbeam-1-1-2-rebar-5-6', 
    'xbeam-1-1-5', 'xbeam-1-1-5-rebar-5-1', 'xbeam-1-1-5-rebar-5-2', 
    'xbeam-1-1-5-rebar-5-3', 'xbeam-1-1-5-rebar-5-4', 'xbeam-1-1-5-rebar-5-5', 
    'xbeam-1-1-5-rebar-5-6', 'xbeam-1-1-4', 'xbeam-1-1-4-rebar-5-1', 
    'xbeam-1-1-4-rebar-5-2', 'xbeam-1-1-4-rebar-5-3', 'xbeam-1-1-4-rebar-5-4', 
    'xbeam-1-1-4-rebar-5-5', 'xbeam-1-1-4-rebar-5-6', 'xbeam-1-2-2', 
    'xbeam-1-2-2-rebar-5-1', 'xbeam-1-2-2-rebar-5-2', 'xbeam-1-2-2-rebar-5-3', 
    'xbeam-1-2-2-rebar-5-4', 'xbeam-1-2-2-rebar-5-5', 'xbeam-1-2-2-rebar-5-6', 
    'xbeam-1-2-3', 'xbeam-1-2-3-rebar-5-1', 'xbeam-1-2-3-rebar-5-2', 
    'xbeam-1-2-3-rebar-5-3', 'xbeam-1-2-3-rebar-5-4', 'xbeam-1-2-3-rebar-5-5', 
    'xbeam-1-2-3-rebar-5-6', 'xbeam-1-2-1', 'xbeam-1-2-1-rebar-5-1', 
    'xbeam-1-2-1-rebar-5-2', 'xbeam-1-2-1-rebar-5-3', 'xbeam-1-2-1-rebar-5-4', 
    'xbeam-1-2-1-rebar-5-5', 'xbeam-1-2-1-rebar-5-6', 'xbeam-1-2-4', 
    'xbeam-1-2-4-rebar-5-1', 'xbeam-1-2-4-rebar-5-2', 'xbeam-1-2-4-rebar-5-3', 
    'xbeam-1-2-4-rebar-5-4', 'xbeam-1-2-4-rebar-5-5', 'xbeam-1-2-4-rebar-5-6', 
    'xbeam-1-2-5', 'xbeam-1-2-5-rebar-5-1', 'xbeam-1-2-5-rebar-5-2', 
    'xbeam-1-2-5-rebar-5-3', 'xbeam-1-2-5-rebar-5-4', 'xbeam-1-2-5-rebar-5-5', 
    'xbeam-1-2-5-rebar-5-6', 'xbeam-2-4-3', 'xbeam-2-4-3-rebar-5-1', 
    'xbeam-2-4-3-rebar-5-2', 'xbeam-2-4-3-rebar-5-3', 'xbeam-2-4-3-rebar-5-4', 
    'xbeam-2-4-3-rebar-5-5', 'xbeam-2-4-3-rebar-5-6', 'xbeam-2-4-2', 
    'xbeam-2-4-2-rebar-5-1', 'xbeam-2-4-2-rebar-5-2', 'xbeam-2-4-2-rebar-5-3', 
    'xbeam-2-4-2-rebar-5-4', 'xbeam-2-4-2-rebar-5-5', 'xbeam-2-4-2-rebar-5-6', 
    'xbeam-2-4-1', 'xbeam-2-4-1-rebar-5-1', 'xbeam-2-4-1-rebar-5-2', 
    'xbeam-2-4-1-rebar-5-3', 'xbeam-2-4-1-rebar-5-4', 'xbeam-2-4-1-rebar-5-5', 
    'xbeam-2-4-1-rebar-5-6', 'xbeam-2-4-5', 'xbeam-2-4-5-rebar-5-1', 
    'xbeam-2-4-5-rebar-5-2', 'xbeam-2-4-5-rebar-5-3', 'xbeam-2-4-5-rebar-5-4', 
    'xbeam-2-4-5-rebar-5-5', 'xbeam-2-4-5-rebar-5-6', 'xbeam-2-4-4', 
    'xbeam-2-4-4-rebar-5-1', 'xbeam-2-4-4-rebar-5-2', 'xbeam-2-4-4-rebar-5-3', 
    'xbeam-2-4-4-rebar-5-4', 'xbeam-2-4-4-rebar-5-5', 'xbeam-2-4-4-rebar-5-6', 
    'xbeam-1-3-5', 'xbeam-1-3-5-rebar-5-1', 'xbeam-1-3-5-rebar-5-2', 
    'xbeam-1-3-5-rebar-5-3', 'xbeam-1-3-5-rebar-5-4', 'xbeam-1-3-5-rebar-5-5', 
    'xbeam-1-3-5-rebar-5-6', 'xbeam-1-3-4', 'xbeam-1-3-4-rebar-5-1', 
    'xbeam-1-3-4-rebar-5-2', 'xbeam-1-3-4-rebar-5-3', 'xbeam-1-3-4-rebar-5-4', 
    'xbeam-1-3-4-rebar-5-5', 'xbeam-1-3-4-rebar-5-6', 'xbeam-1-3-3', 
    'xbeam-1-3-3-rebar-5-1', 'xbeam-1-3-3-rebar-5-2', 'xbeam-1-3-3-rebar-5-3', 
    'xbeam-1-3-3-rebar-5-4', 'xbeam-1-3-3-rebar-5-5', 'xbeam-1-3-3-rebar-5-6', 
    'xbeam-1-3-2', 'xbeam-1-3-2-rebar-5-1', 'xbeam-1-3-2-rebar-5-2', 
    'xbeam-1-3-2-rebar-5-3', 'xbeam-1-3-2-rebar-5-4', 'xbeam-1-3-2-rebar-5-5', 
    'xbeam-1-3-2-rebar-5-6', 'xbeam-1-3-1', 'xbeam-1-3-1-rebar-5-1', 
    'xbeam-1-3-1-rebar-5-2', 'xbeam-1-3-1-rebar-5-3', 'xbeam-1-3-1-rebar-5-4', 
    'xbeam-1-3-1-rebar-5-5', 'xbeam-1-3-1-rebar-5-6', 'xbeam-1-4-1', 
    'xbeam-1-4-1-rebar-5-1', 'xbeam-1-4-1-rebar-5-2', 'xbeam-1-4-1-rebar-5-3', 
    'xbeam-1-4-1-rebar-5-4', 'xbeam-1-4-1-rebar-5-5', 'xbeam-1-4-1-rebar-5-6', 
    'xbeam-1-4-2', 'xbeam-1-4-2-rebar-5-1', 'xbeam-1-4-2-rebar-5-2', 
    'xbeam-1-4-2-rebar-5-3', 'xbeam-1-4-2-rebar-5-4', 'xbeam-1-4-2-rebar-5-5', 
    'xbeam-1-4-2-rebar-5-6', 'xbeam-1-4-3', 'xbeam-1-4-3-rebar-5-1', 
    'xbeam-1-4-3-rebar-5-2', 'xbeam-1-4-3-rebar-5-3', 'xbeam-1-4-3-rebar-5-4', 
    'xbeam-1-4-3-rebar-5-5', 'xbeam-1-4-3-rebar-5-6', 'xbeam-1-4-4', 
    'xbeam-1-4-4-rebar-5-1', 'xbeam-1-4-4-rebar-5-2', 'xbeam-1-4-4-rebar-5-3', 
    'xbeam-1-4-4-rebar-5-4', 'xbeam-1-4-4-rebar-5-5', 'xbeam-1-4-4-rebar-5-6', 
    'xbeam-1-4-5', 'xbeam-1-4-5-rebar-5-1', 'xbeam-1-4-5-rebar-5-2', 
    'xbeam-1-4-5-rebar-5-3', 'xbeam-1-4-5-rebar-5-4', 'xbeam-1-4-5-rebar-5-5', 
    'xbeam-1-4-5-rebar-5-6', 'xbeam-2-2-1', 'xbeam-2-2-1-rebar-5-1', 
    'xbeam-2-2-1-rebar-5-2', 'xbeam-2-2-1-rebar-5-3', 'xbeam-2-2-1-rebar-5-4', 
    'xbeam-2-2-1-rebar-5-5', 'xbeam-2-2-1-rebar-5-6', 'xbeam-2-2-3', 
    'xbeam-2-2-3-rebar-5-1', 'xbeam-2-2-3-rebar-5-2', 'xbeam-2-2-3-rebar-5-3', 
    'xbeam-2-2-3-rebar-5-4', 'xbeam-2-2-3-rebar-5-5', 'xbeam-2-2-3-rebar-5-6', 
    'xbeam-2-2-2', 'xbeam-2-2-2-rebar-5-1', 'xbeam-2-2-2-rebar-5-2', 
    'xbeam-2-2-2-rebar-5-3', 'xbeam-2-2-2-rebar-5-4', 'xbeam-2-2-2-rebar-5-5', 
    'xbeam-2-2-2-rebar-5-6', 'xbeam-2-2-5', 'xbeam-2-2-5-rebar-5-1', 
    'xbeam-2-2-5-rebar-5-2', 'xbeam-2-2-5-rebar-5-3', 'xbeam-2-2-5-rebar-5-4', 
    'xbeam-2-2-5-rebar-5-5', 'xbeam-2-2-5-rebar-5-6', 'xbeam-2-2-4', 
    'xbeam-2-2-4-rebar-5-1', 'xbeam-2-2-4-rebar-5-2', 'xbeam-2-2-4-rebar-5-3', 
    'xbeam-2-2-4-rebar-5-4', 'xbeam-2-2-4-rebar-5-5', 'xbeam-2-2-4-rebar-5-6', 
    'xbeam-2-1-2', 'xbeam-2-1-2-rebar-5-1', 'xbeam-2-1-2-rebar-5-2', 
    'xbeam-2-1-2-rebar-5-3', 'xbeam-2-1-2-rebar-5-4', 'xbeam-2-1-2-rebar-5-5', 
    'xbeam-2-1-2-rebar-5-6', 'xbeam-2-1-3', 'xbeam-2-1-3-rebar-5-1', 
    'xbeam-2-1-3-rebar-5-2', 'xbeam-2-1-3-rebar-5-3', 'xbeam-2-1-3-rebar-5-4', 
    'xbeam-2-1-3-rebar-5-5', 'xbeam-2-1-3-rebar-5-6', 'xbeam-2-1-1', 
    'xbeam-2-1-1-rebar-5-1', 'xbeam-2-1-1-rebar-5-2', 'xbeam-2-1-1-rebar-5-3', 
    'xbeam-2-1-1-rebar-5-4', 'xbeam-2-1-1-rebar-5-5', 'xbeam-2-1-1-rebar-5-6', 
    'xbeam-2-3-1', 'xbeam-2-3-1-rebar-5-1', 'xbeam-2-3-1-rebar-5-2', 
    'xbeam-2-3-1-rebar-5-3', 'xbeam-2-3-1-rebar-5-4', 'xbeam-2-3-1-rebar-5-5', 
    'xbeam-2-3-1-rebar-5-6', 'xbeam-2-1-4', 'xbeam-2-1-4-rebar-5-1', 
    'xbeam-2-1-4-rebar-5-2', 'xbeam-2-1-4-rebar-5-3', 'xbeam-2-1-4-rebar-5-4', 
    'xbeam-2-1-4-rebar-5-5', 'xbeam-2-1-4-rebar-5-6', 'xbeam-2-1-5', 
    'xbeam-2-1-5-rebar-5-1', 'xbeam-2-1-5-rebar-5-2', 'xbeam-2-1-5-rebar-5-3', 
    'xbeam-2-1-5-rebar-5-4', 'xbeam-2-1-5-rebar-5-5', 'xbeam-2-1-5-rebar-5-6', 
    'xbeam-2-3-4', 'xbeam-2-3-4-rebar-5-1', 'xbeam-2-3-4-rebar-5-2', 
    'xbeam-2-3-4-rebar-5-3', 'xbeam-2-3-4-rebar-5-4', 'xbeam-2-3-4-rebar-5-5', 
    'xbeam-2-3-4-rebar-5-6', 'xbeam-2-3-5', 'xbeam-2-3-5-rebar-5-1', 
    'xbeam-2-3-5-rebar-5-2', 'xbeam-2-3-5-rebar-5-3', 'xbeam-2-3-5-rebar-5-4', 
    'xbeam-2-3-5-rebar-5-5', 'xbeam-2-3-5-rebar-5-6', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=49165.7, 
    farPlane=81453.5, width=19068.7, height=12561.6, viewOffsetX=809.755, 
    viewOffsetY=3805.63)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49043.7, 
    farPlane=81575.5, width=19021.4, height=12530.5, viewOffsetX=1216.37, 
    viewOffsetY=750.443)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50845.5, 
    farPlane=80550.5, width=19720.3, height=12990.8, cameraPosition=(58541.1, 
    41257.5, 33201.3), cameraUpVector=(-0.655695, 0.543745, -0.523837), 
    cameraTarget=(9983.26, 2798.85, 12503.1), viewOffsetX=1261.06, 
    viewOffsetY=778.013)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48137.7, 
    farPlane=82576.3, width=18670.1, height=12299, cameraPosition=(49100, 
    28365.3, 57012.2), cameraUpVector=(-0.534517, 0.723247, -0.43727), 
    cameraTarget=(9518.74, 2111.27, 12185.9), viewOffsetX=1193.9, 
    viewOffsetY=736.58)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52051.8, 
    farPlane=79684.1, width=20188.2, height=13299.1, cameraPosition=(64139.5, 
    37658, 24475.5), cameraUpVector=(-0.667068, 0.571815, -0.477545), 
    cameraTarget=(10132.7, 2878.95, 12684.2), viewOffsetX=1290.98, 
    viewOffsetY=796.471)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52593.9, 
    farPlane=79142, width=13227.9, height=8713.99, viewOffsetX=784.544, 
    viewOffsetY=1471.31)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52803.2, 
    farPlane=78561.7, width=13280.6, height=8748.66, cameraPosition=(27651.9, 
    56356.9, 46103.5), cameraUpVector=(-0.649513, 0.25564, -0.716087), 
    cameraTarget=(9777.84, 3044.35, 12882.3), viewOffsetX=787.665, 
    viewOffsetY=1477.17)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52864.4, 
    farPlane=78500.6, width=13514.9, height=8903.03, viewOffsetX=205.83, 
    viewOffsetY=1549.28)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52775.4, 
    farPlane=78589.5, width=13492.2, height=8888.04, viewOffsetX=1988.01, 
    viewOffsetY=952.201)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52224.9, 
    farPlane=79140.1, width=19353.6, height=12749.3, viewOffsetX=2376.65, 
    viewOffsetY=655.236)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52100.6, 
    farPlane=79264.3, width=19307.5, height=12719, viewOffsetX=4361.9, 
    viewOffsetY=2023.09)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52100.4, 
    width=19307.5, height=12718.9, viewOffsetX=3179.79, viewOffsetY=1857.09)
session.viewports['Viewport: 1'].view.setValues(farPlane=79264.5, 
    width=19307.5, height=12718.9, viewOffsetX=3594.56, viewOffsetY=4886.39)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=5315.85, 
    viewOffsetY=5571.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53629.9, 
    farPlane=77735, width=5765.67, height=3798.17, viewOffsetX=4200.45, 
    viewOffsetY=5238.69)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58377.1, 
    farPlane=81746.1, width=6276.03, height=4134.37, cameraPosition=(53781.3, 
    55336.2, -5034.55), cameraUpVector=(-0.954219, 0.297628, 0.0297353), 
    cameraTarget=(15686.5, 4750.07, 10940.1), viewOffsetX=4572.26, 
    viewOffsetY=5702.4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57029.5, 
    farPlane=87851.9, width=6131.15, height=4038.93, cameraPosition=(51256.7, 
    32874.2, -40172.2), cameraUpVector=(-0.663304, 0.631791, 0.401084), 
    cameraTarget=(16584.3, 1838.28, 5653.15), viewOffsetX=4466.71, 
    viewOffsetY=5570.76)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61366.3, 
    farPlane=90986.1, width=6597.39, height=4346.07, cameraPosition=(-12260.2, 
    31329.7, -56887.7), cameraUpVector=(0.114936, 0.666755, 0.736361), 
    cameraTarget=(8389.61, 847.054, -2945.49), viewOffsetX=4806.38, 
    viewOffsetY=5994.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61313.1, 
    farPlane=91039.3, width=6591.67, height=4342.3, viewOffsetX=3329.53, 
    viewOffsetY=8085.96)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=2394.94, 
    viewOffsetY=9042.25)
session.viewports['Viewport: 1'].view.setValues(nearPlane=60804.7, 
    farPlane=91408.2, width=6537.01, height=4306.3, cameraPosition=(-19035.3, 
    26591.9, -56090), cameraUpVector=(0.24522, 0.719075, 0.650229), 
    cameraTarget=(6244.64, -421.255, -2270.16), viewOffsetX=2375.08, 
    viewOffsetY=8967.28)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61333.6, 
    farPlane=90879.2, width=1912.92, height=1260.15, viewOffsetX=1040.3, 
    viewOffsetY=9199.98)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#82001000 #80000000 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-2')
#: 表面 'Surf-2' 已创建 (4 面).
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=49278.5, 
    farPlane=81340.7, width=18039.2, height=11883.4, viewOffsetX=1021.08, 
    viewOffsetY=2321.89)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53150.7, 
    farPlane=78318.5, width=19456.7, height=12817.2, cameraPosition=(74236.4, 
    12509.2, 7168.66), cameraUpVector=(-0.486734, 0.861118, -0.146852), 
    cameraTarget=(9914.29, 2244.65, 11927.7), viewOffsetX=1101.32, 
    viewOffsetY=2504.34)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50150.9, 
    farPlane=84287.9, width=18358.6, height=12093.8, cameraPosition=(40446.4, 
    26741.4, -43438.9), cameraUpVector=(-0.446071, 0.740156, 0.50318), 
    cameraTarget=(11223.6, 2436.58, 9670.84), viewOffsetX=1039.16, 
    viewOffsetY=2363)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51203.1, 
    farPlane=85415.6, width=18743.8, height=12347.6, cameraPosition=(-36482.2, 
    24829.2, -34742.9), cameraUpVector=(0.197726, 0.710803, 0.675028), 
    cameraTarget=(8021.61, 2794.28, 7674.27), viewOffsetX=1060.96, 
    viewOffsetY=2412.58)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52037.1, 
    farPlane=84867.5, width=19049.1, height=12548.7, cameraPosition=(-41753.2, 
    31483.9, -24856.9), cameraUpVector=(0.396271, 0.655974, 0.642392), 
    cameraTarget=(7098.04, 3088.07, 7893.3), viewOffsetX=1078.24, 
    viewOffsetY=2451.87)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53853.4, 
    farPlane=83051.2, width=2895.6, height=1907.49, viewOffsetX=-875.558, 
    viewOffsetY=3430.17)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-3'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#82001040 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-3')
#: 表面 'Surf-3' 已创建 (4 面).
session.viewports['Viewport: 1'].view.setValues(nearPlane=53057.2, 
    farPlane=83847.4, width=10547, height=6947.93, viewOffsetX=823.802, 
    viewOffsetY=4475.6)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=50632.6, 
    farPlane=79986.6, width=5013.36, height=3302.58, viewOffsetX=-2122.46, 
    viewOffsetY=1579.27)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48327.5, 
    farPlane=77711.7, width=4785.12, height=3152.23, cameraPosition=(49779.8, 
    36660.8, -23747.4), cameraUpVector=(-0.833637, 0.533623, 0.142464), 
    cameraTarget=(7153.52, 1555.86, 11123.7), viewOffsetX=-2025.84, 
    viewOffsetY=1507.37)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47090, 
    farPlane=78949.2, width=16605.6, height=10939.1, viewOffsetX=524.846, 
    viewOffsetY=1692.23)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46986.9, 
    farPlane=79052.3, width=16569.3, height=10915.1, viewOffsetX=-2110.3, 
    viewOffsetY=1688.53)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47217.7, 
    farPlane=78989.3, width=16650.7, height=10968.8, cameraPosition=(25941.7, 
    36156.6, -40094.1), cameraUpVector=(-0.20238, 0.634979, 0.74555), 
    cameraTarget=(5086.05, 2676.91, 11958.8), viewOffsetX=-2120.67, 
    viewOffsetY=1696.83)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47354.2, 
    farPlane=80536.3, width=16698.9, height=11000.5, cameraPosition=(-27029.2, 
    33175.1, -32299.2), cameraUpVector=(0.231057, 0.63906, 0.733631), 
    cameraTarget=(6815.48, 1886.44, 13970.8), viewOffsetX=-2126.8, 
    viewOffsetY=1701.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49069.9, 
    farPlane=78820.6, width=1753.38, height=1155.05, viewOffsetX=-1623.5, 
    viewOffsetY=3940.04)
a = mdb.models['structure'].rootAssembly
s1 = a.instances['col-2-3-4'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20800400 #20000000 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Surf-4')
#: 表面 'Surf-4' 已创建 (4 面).
session.viewports['Viewport: 1'].view.setValues(nearPlane=47478.1, 
    farPlane=80412.4, width=16537.8, height=10894.4, viewOffsetX=-1262.73, 
    viewOffsetY=570.094)
mdb.save()
#: 模型数据库已保存到 "D:\pymodel.cae".
