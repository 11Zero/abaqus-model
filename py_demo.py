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

GV = tuple(['GV'])#广义速度
GA = tuple(['GA'])#广义加速度
IRA = 'IRA1', 'IRA2', 'IRA3', 'IRAR1', 'IRAR2', 'IRAR3'#惯性释放等同于刚体加速度,
IRF = 'IRF1', 'IRF2', 'IRF3', 'IRM1', 'IRM2', 'IRM3'#作用力反作用力-惯性释放荷载相应于同等的刚体加速度
ALLEN = 'ALLAE', 'ALLCD', 'ALLDMD','ALLEE', 'ALLFD', 'ALLIE',\
        'ALLJD', 'ALLKE', 'ALLKL', 'ALLPD', 'ALLQB','ALLSE', \
        'ALLSD', 'ALLVD', 'ALLWK', 'ETOTAL'#总能量
BROKEN = 'DBS11', 'DBS12', 'DBT', 'DBSF', 'OPENBC', 'CRSTS11', 'CRSTS12', 'CRSTS13', 'ENRRT11', 'ENRRT12', 'ENRRT13', 'EFENRRTR', 'BDSTAT', 'CSDMG',  'CSMAXSCRT', 'CSMAXUCRT','CSQUADSCRT', 'CSQUADUCRT'#破坏断裂
variables = GA+GV+ALLEN+BROKEN
mdb.models['structure'].historyOutputRequests['H-Output-1'].setValues(variables=variables)
print r'完成'