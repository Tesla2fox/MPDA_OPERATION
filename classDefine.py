# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 09:01:23 2018

@author: robot
"""
import random
import random as rd

import plotly.plotly as py
import plotly.graph_objs as go
import math
import plotly
import numpy



class Point2D:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def displayPoint2D(self):
#        wtf = 1
        print("x= ",self.x,"y = ",self.y)
    def randomPosition(self):
        self.x= random.uniform(0,50)
        self.y = random.uniform(0,50)

class Robot:
    def __init__(self,pnt = Point2D(),vel=1,ability= 0):
        self.pnt = pnt
        self.vel = vel
        self.ability = ability
    def random(self):
        self.pnt.randomPosition()
        self.ability = random.uniform(0,0.5)
    def displayRobot(self):
        self.pnt.displayPoint2D()
#        print("ability  = ",self.ability)
        
class TaskPnt:
    def __init__(self,pnt = Point2D(),initState = 0,increaseRatio=0):
        self.pnt = pnt
        self.initState = initState
        self.increaseRatio = increaseRatio
    def random(self):
        self.pnt.randomPosition()
        self.initState = rd.uniform(1,20)
        self.increaseRatio = rd.uniform(0,0.5)
    def displayTaskPnt(self):
        self.pnt.displayPoint2D()
#        print("initState = ",self.initState,
#              " increaseRatio = ",self.increaseRatio)
    def getTrace(self):
        lstx = []
        lsty = []
        lstx.append(self.pnt.x)
        lsty.append(self.pnt.y)
        trace = go.Scatter(x = lstx, y = lsty)
        return trace


def distance_point(pntA = Point2D(),pntB = Point2D()):
#    print(pntA)
#    print()
#    pntA.displayPoint2D()
#    pntB.displayPoint2D()
    dis2 = numpy.square(pntA.x-pntB.x)+numpy.square(pntA.y-pntB.y)
#    print(dis2)
    dis = math.sqrt(dis2)
    return dis
        






    