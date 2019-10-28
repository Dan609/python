#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as nu, matplotlib as mat,math as m
import pylab
t1=int(input("Введите временной слой для построения:"))
filename=input("Введите имя файла для сохранения:")
c,dt,N,xm,A,s=(0.00005,0.0004,200,0.5,0.5,0.08)
dj=pylab.array([-2,-1,0,1,2])
jn=pylab.array([0,0,0,0,0])
dx=1./N
xmin = 0.0
xmax = 1.0
xlist = pylab.mlab.frange (xmin, xmax, dx)
pylab.ion()
dtdx1=dt/(2*dx)
dtdx2=c*dt/(2*dx**3)
N1=N-1
v=pylab.array([A*m.exp(-(j*dx-xm)**2/(2*s**2)) for j in range(0,N+1)])
for i in range(0,100000):
    t=i*dt
    if t>t1: break
    for j in range(0,N+1):
        if(j==0):
            for it in range(2,5):
                jn[it]=j+dj[it]
            jn[0],jn[1]=(N1,N)
        elif(j==1):
            for it in range(1,5):
                jn[it]=j+dj[it]
            jn[0]=N
        elif(j==N-1):
            for it in range(0,4):
                jn[it]=j+dj[it]
            jn[4]=0
        elif(j==N):
            for it in range(0,3):
                jn[it]=j+dj[it]
            jn[3],jn[4]=(0,1)
        else:
            for it in range(0,5):
                jn[it]=j+dj[it]
        vn1=-dtdx1*v[jn[2]]*(v[jn[3]]-v[jn[1]])
        vd=-dtdx2*(v[jn[4]]-2.0*v[jn[3]]+2.*v[jn[1]]-v[jn[0]])
        v[j]=v[jn[2]]+vn1+vd
ylist=[v[j] for j in range(0,N+1)]
pylab.clf()
pylab.plot (xlist, ylist)
pylab.draw()
pylab.savefig(filename)
