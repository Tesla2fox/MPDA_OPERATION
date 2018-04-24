h# -*- coding: utf-8 -*-
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



#__import__ ('classDefine')

#py.sign_in('tesla_fox', 'HOTRQ3nIOdYUUszDIfgN') 

robotNum = 2
taskNum = 5

fileDir = 'D://VScode//MPDA_orgDecode//data//'
f = open(fileDir+'MPDA_cfg_sp.txt','w')
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
    taskpnt.displayTaskPnt()
    taskpnt.initState = 0.5
    taskpnt.increaseRatio = 0.2
    taskPntList.append(copy.deepcopy(taskpnt))
#    increaseRatioList.append(taskpnt.increaseRatio)
#    initStateList.append(taskpnt.initState)
    taskPntTrace = taskpnt.getTrace()
    drawData.append(copy.deepcopy(taskPntTrace))


taskPntList[0].pnt.x=15
taskPntList[0].pnt.y=15


taskPntList[1].pnt.x=15
taskPntList[1].pnt.y=15

taskPntList[2].pnt.x=15
taskPntList[2].pnt.y=15

taskPntList[3].pnt.x=15
taskPntList[3].pnt.y=15


taskPntList[4].pnt.x= 15
taskPntList[4].pnt.y= 0


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
for i in range(0,robotNum):
    rob = cd.Robot()
    rob.random()
    rob.displayRobot()
    rob.ability = 10000000
    robotList.append(copy.deepcopy(rob))
#end create

#robotList[0].ability = 100000000
robotList[0].pnt.x = 15
robotList[0].pnt.y = 5

robotList[1].pnt.x = 15
robotList[1].pnt.y = 0


#write the robots 
f.write('AgentAbility ')
for i in range(0,robotNum):
    f.write(' '+str(robotList[i].ability))
f.write('\n')
#end writing 
        

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
#    random.shuffle(permutationList)
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
        
#plotly.offline.plot(drawData, filename='MPDASketchFig')




    