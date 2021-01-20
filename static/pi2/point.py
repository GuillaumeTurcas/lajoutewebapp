from vpython import *
import sys

def lect():
    file = open("point.txt")
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

def rvect(lframe, ref):
    cbutton = button({text:'<b>Red</b>', color:color.red, background:color.cyan, pos:scene.title_anchor, bind:Color})
    vect = [float(ref[0])/100-lframe[0]/100, 
                  float(ref[1])/100-lframe[1]/100, 
                  float(ref[2])/100-lframe[2]/100]
    return vect

def model(lframe):
    model = []
    for i in range(len(lframe)-1): 
        newmodel = []
        for j in range(len(lframe[i])-1):
            model.append(rvect(lframe[i][j], lframe[1][j]))
        model.append(newmodel)
    return model

def main():
    lframe = lect()
    newmodel = model(lframe)
    return newmodel
