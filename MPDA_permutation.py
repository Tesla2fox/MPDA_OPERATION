# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:11:04 2018

@author: stef_leonA
"""

#COUNT = 0
#def perm(n,begin,end):
#    global COUNT
#    if begin>=end:
#        print(n)
#        COUNT+=1
#    else:
#        i=begin
#        for num in range(begin,end):
#            n[num],n[i]=n[i],n[num]
#            perm(n,begin+1,end)
#            n[num],n[i]=n[i],n[num]
#
#
#
#n=[1,2,3]
#perm(n,0,len(n))
#print(COUNT)
#
#
#
#
#生成所有MPDA排列
import itertools
import copy

#函数

#def loop(maxloopTimes=10,
#         loopTimes=0,
#         ListIndex = [],
#         PerList =[],
#         All_list = []):
#    if loopTimes==maxloopTimes:
#        ListUnit.
#    else:
#        for i in range(0,len(PerList)):
#            ListIndex.append(copy.copy(i))
#            

robotNum = 3
taskNum = 4
s = []
for i in range(0,taskNum):
    s.append(copy.copy(i))
    
PerList = list(itertools.permutations(s,taskNum))
#print(PerList)
PerListMap = tuple(PerList)
index = 0

fileDir = 'D://VScode//MPDA_orgDecode//data//'
f = open(fileDir+'Permu.txt','w')

for encodeUnit in  itertools.product(PerListMap, repeat = robotNum):
    f.write('\n')
    f.write('Encode')
    f.write(str(index))
    index += 1
    for perm in encodeUnit:
        for x in perm:
            f.write(' '+ str(x))
f.close()

print(w11)

#All_List = []


#for i in range(0,robotNum):
    
#
#for x in range(0,len(PerList)):
#    for y in range(0,len(PerList)):
#        for z in range(0,len(PerList)):
#            ListUnit = []
#            ListUnit.append(PerList[x])
#            ListUnit.append(PerList[y])
#            ListUnit.append(PerList[z])
#            All_List.append(ListUnit)			
#print(All_List)
#            
#for i in range(0,len(All_List)):
#    for j in range (0,len(All_List[i])):    
#        for p in range (0,len(All_List[i][j])):
#            f.write('  ')
#            f.write(str(All_List[i][j][p]))   
f.close()

#print(All_List)            
    

    