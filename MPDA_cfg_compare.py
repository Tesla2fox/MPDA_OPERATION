# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 09:01:23 2018
比较原始和新的静态排序方法
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


robotNum = 100
taskNum = 50

#
endBool = False
infNum = 0
for pc in range(0,100):
    print('circle index = ',pc)    
    #若智能体的数量小于5，则MPDA编码的全排列
    if(robotNum<5 and taskNum < 5):
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
    
    #设置可执行文件的位置
    fileDir = 'D://VScode//MPDA_orgDecode//data//'
    fileCfg = fileDir + 'MPDA_cfg.txt'
    f = open(fileCfg,'w')
    #write time 
    f.write('time  ' +datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
    f.write('AgentNum ' + str(robotNum)+'\n')
    f.write('TaskNum '+ str(taskNum)+'\n')
    
    robotList = []
    taskPntList = []
    
    #create the taskPnt
    for i in range(0,taskNum):
        taskpnt =  cd.TaskPnt()
        taskpnt.random()
        taskPntList.append(copy.deepcopy(taskpnt))
        taskPntTrace = taskpnt.getTrace()
    #    drawData.append(copy.deepcopy(taskPntTrace))
    print('task init success')
    
    
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
    print('write task successfully')
    #end write txt 
    
    
    #create the robots
    f.write('AgentAbility ')
    for i in range(0,robotNum):
        rob = cd.Robot()
        rob.random()
        robotList.append(copy.deepcopy(rob))
        f.write(' '+str(rob.ability))
    f.write('\n')        
    #end create
    print('robots init success')
    
    
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
    
                    
    org_exe_name = "D:\VScode\\MPDA_StaticConstrn\\bin\\MPDA\\Release\\mpda_OrgStaticConstrn.exe"
    
    proc = subprocess.Popen([org_exe_name,fileCfg],stdin =subprocess.PIPE,stdout =  subprocess.PIPE)
    for line in proc.stdout:
        print(line)
        linesp = line.split()
#        print(len(linesp))
        print(linesp)
        if(len(linesp)>1):        
            if (linesp[1]==b'fitNess'):
                print(float(linesp[3]))
                if(float(linesp[3])>100002000000000000):
                    infNum = infNum +1
                    #print('w0-00-0-0-')                    
                    #endBool = True
                    #break
    o = proc.communicate()
    print('infNum = ',infNum)
#    if(endBool):
#        break
#    print(runTimes,'<<<<<<<<<<<<<<<<')
            