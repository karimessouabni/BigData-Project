#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 02:34:46 2016

@author: karim
"""
import numpy as np
import matplotlib.pyplot as plt

# X0 = np.load("""data/trn_img.npy""")
X0 = np.load('trn_img.npy')
lbl0 = np.load('trn_lbl.npy')
#
#img = X0[2000].reshape(28,28)
#plt.imshow(img, plt.cm.gray)
#plt.show()

#10 classs associated to each number between 0 and 9


#print(len(lbl0))

w0,w1,w2,w3,w4,w5,w6,w7,w8,w9=([] for i in range(10))
for l, x in zip(lbl0, X0):

    if l==0 :
        w0.append(x)
    elif l==1:
        w1.append(x)
    elif l==2:
        w2.append(x)
    elif l==3:
        w3.append(x)
    elif l==4:
        w4.append(x)
    elif l==5:
        w5.append(x)
    elif l==6:
        w6.append(x)
    elif l==7:
        w7.append(x)
    elif l==8:
        w8.append(x)
    elif l==9:
        w9.append(x)
    else:
        print("exception")


AllW = [w0,w1,w2,w3,w4,w5,w6,w7,w8,w9] #all classes
AllwMoyen =[]


for wi in AllW :
    moyenWi={}
    i=0

    #initalize un vector de 784 a 0
    for nbr in range(784):
            moyenWi[i]=0
            i+=1


    #sommer les valeurs de tous les vecteur representnat le chiffre "0"
    for w in wi:
        i=0
        for nbr in w:
            moyenWi[i]+=nbr
            i+=1

    #calcule moyenne
    i=0
    for nbr in range(784): #initalize all the vector moyen's values to 0
            moyenWi[i]/=len(wi)
            i+=1


    AllwMoyen.append(moyenWi)






print(len(AllwMoyen)) # = 10
print(AllwMoyen[0][583]) # = 6.07492507493


#img = w2[0].reshape(28,28)
#plt.imshow(img, plt.cm.gray)
#plt.show()


#for l in X0:
