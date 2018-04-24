# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 09:01:23 2018

@author: robot
"""


#import classDefine
import classDefine as cd
import plotly.plotly as py
import plotly.graph_objs as go
import math
import plotly
import copy 
import random
import time 
import datetime
from numpy import *
import numpy as np
from copy import deepcopy

#__import__ ('classDefine')

#py.sign_in('tesla_fox', 'HOTRQ3nIOdYUUszDIfgN') 


RobInfoMat=[1,2,1,0.2,3,1,1,0.3,5,2,1,0.4]
             
TaskInfoMat= [7,8,0.15,5,5,9,0.25,6,10,12,0.12,4]

 
robotNum = int(len(RobInfoMat)/4)
taskNum = int(len(TaskInfoMat)/4)

fileDir = 'D://VScode//MPDA_DirectConstrn//data//'
f = open(fileDir+'MPDA_cfg_matlab.txt','w')
#write time 
f.write('time  ' +datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
f.write('AgentNum ' + str(robotNum)+'\n')
f.write('TaskNum '+ str(taskNum)+'\n')

robotList = []
taskPntList = []
#increaseRatioList  = []
#initStateList = []
drawData = []

#create the taskPnt
for i in range(0,taskNum):
    taskpnt =  cd.TaskPnt()
    taskpnt.random()
    taskpnt.pnt.x = TaskInfoMat[i*4]
    taskpnt.pnt.y = TaskInfoMat[i*4 + 1]
    taskpnt.increaseRatio = TaskInfoMat[i*4 + 2]
    taskpnt.initState = TaskInfoMat[i*4 + 3]
    taskpnt.displayTaskPnt()
#    //copy.deepcopy()
    taskPntList.append(deepcopy(taskpnt))
#    increaseRatioList.append(taskpnt.increaseRatio)
#    initStateList.append(taskpnt.initState)
    taskPntTrace = taskpnt.getTrace()
    drawData.append(deepcopy(taskPntTrace))

print('<<<<<<<<<<<<<<<<')


#write txt 
f.write('TaskIncreaseRatio ')
for j in range(0,taskNum):
    f.write(' ')
    f.write(str(taskPntList[j].increaseRatio))    
f.write('\n')

f.write('TaskInitState ')
for j in range (0,taskNum):
    f.write(' ')
    f.write(str(taskPntList[j].initState))
f.write('\n')
#end write txt 


#create the robots

f.write('AgentAbility ')
for i in range(0,robotNum):
    rob = cd.Robot()
    rob.random()
    rob.pnt.x = RobInfoMat[i*4]
    rob.pnt.y = RobInfoMat[i*4 + 1]
    rob.ability = RobInfoMat[i*4 + 3]
    rob.vel  = 1
    rob.ability
    rob.displayRobot()
    robotList.append(deepcopy(rob))
    f.write(' '+str(rob.ability))
f.write('\n')
        
#end create

f.write('TaskDisMat  ') 
for i in range (0,taskNum):
    for j in range(i+1,taskNum):
         dis = cd.distance_point(taskPntList[i].pnt,taskPntList[j].pnt)
         f.write(' '+str(dis))
f.write('\n')


f.write('Ag2TaskDisMat  ')
for i in range (0,robotNum):
    for j in range (0,taskNum):
        dis = cd.distance_point(robotList[i].pnt,taskPntList[j].pnt)
        f.write('  ' +str(dis))
f.write('\n')          
         


f.write('Encode ')
for i in range(0,robotNum):
    permutationList =[]
    for j in range (0,taskNum):
        permutationList.append(j)
    random.shuffle(permutationList)
    for j in range (0,taskNum):
        f.write('  '+ str(permutationList[j]))
#    print(disOrderPermutation)     
f.write('\n')



#write something that C++ don't need to use  
f.write('robotPosstion\n')
f.write('<<<<<<<<<\n')
for i in range(0,robotNum):
    f.write('index '+ str(i))
    f.write(' pntx = ' +str(robotList[i].pnt.x) + '  pnty = ' + 
            str(robotList[i].pnt.y) + '\n')


f.write('taskPosition\n')
f.write('<<<<<<<<<\n')
for i in range (0,taskNum):
    f.write('index '+ str(i))
    f.write(' pntx = ' +str(taskPntList[i].pnt.x) + '  pnty = ' + 
            str(taskPntList[i].pnt.y) + '\n')


# end writing the data to the configure txt        
f.close()
        



    