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
import subprocess
import itertools
#__import__ ('classDefine')

#py.sign_in('tesla_fox', 'HOTRQ3nIOdYUUszDIfgN') 


#RobInfoMat=[1 2 1 0.2 3 1 1 0.3 5 2 1 0.4]
             
#TaskInfoMat= [7 8 0.15 5;5 9 0.25 6;10 12 0.12 4];

robotNum = 100
taskNum = 50
fileDir = 'D://VScode//MPDA_orgDecode//data//'


if(robotNum<5):
    s = []
    for i in range(0,taskNum):
        s.append(copy.copy(i))
         
    PerList = list(itertools.permutations(s,taskNum))
    #print(PerList)
    PerListMap = tuple(PerList)
    
    index = 0
    
    fperm = open(fileDir+'Permu.txt','w')
    for encodeUnit in  itertools.product(PerListMap, repeat = robotNum):
        fperm.write('\n')
        fperm.write('Encode')
        fperm.write(str(index))
        index += 1
        for perm in encodeUnit:
            for x in perm:
                fperm.write(' '+ str(x))
    fperm.close()




fileDir = 'D://VScode//MPDA_orgDecode//data//'
f = open(fileDir+'MPDA_cfg.txt','w')
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
#        taskpnt.displayTaskPnt()
    taskPntList.append(copy.deepcopy(taskpnt))
#    increaseRatioList.append(taskpnt.increaseRatio)
#    initStateList.append(taskpnt.initState)
    taskPntTrace = taskpnt.getTrace()
    drawData.append(copy.deepcopy(taskPntTrace))

#    print('<<<<<<<<<<<<<<<<')


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
#        rob.displayRobot()
    robotList.append(copy.deepcopy(rob))
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

            
    
#    pname = "D:\\VScode\\MPDA_StaticConstrn\\bin\\mpda_StaticConstrn\\Debug\\mpda_StaticConstrn.exe"
#    
#    p = subprocess.Popen(pname,stdin =subprocess.PIPE,stdout =  subprocess.PIPE)
#    o = p.communicate()
#    print(runTimes,'<<<<<<<<<<<<<<<<')
        