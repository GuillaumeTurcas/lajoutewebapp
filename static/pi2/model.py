from vpython import *
import sys

def lect():
    file = open("static/pi2/point.txt")
    lines = file.readlines()
    l = 0
    lframe = []
    frame=[]
    for line in lines:
        point = []
        if l%26 != 0:
            i = line.rstrip()
            i = i.replace('[', '')
            i = i.replace(']', '')
            line = i.replace(' ','')
            ll = len(line)
            point = [round(float(line[0:int(ll/3)]),2), 
                     round(float(line[int(ll/3):int(2*ll/3)]),2),
                     round(float(line[int(2*ll/3):]),2)]
            frame.append(point)
        else :
            lframe.append(frame)
            frame = []
        l += 1
    return lframe

def model(lframe):
    model = []
    for i in range(len(lframe)): 
        newmodel = []
        for j in range(len(lframe[i])):
            newmodel.append(rvect(lframe[i][j], lframe[i][1]))
        model.append(newmodel)
    return model

def main():
    lframe = lect()
    return lframe
