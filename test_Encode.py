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
import itertools
s = [1,2,3]
PerList = list(itertools.permutations(s,3))
print(PerList)

All_List = []

for x in range(0,len(PerList)):
    for y in range(0,len(PerList)):
        for z in range(0,len(PerList)):
            ListUnit = []
            ListUnit.append(PerList[x])
            ListUnit.append(PerList[y])
            ListUnit.append(PerList[z])
            All_List.append(ListUnit)
			
print(All_List)
            
f = open('Permu.txt','w')
for i in range(0,len(All_List)):
    f.write('\n')
    f.write('Encode ')
    f.write(str(i))
    for j in range (0,len(All_List[i])):    
        for p in range (0,len(All_List[i][j])):
            f.write('  ')
            f.write(str(All_List[i][j][p]))   
f.close()

print(All_List)            
    
    