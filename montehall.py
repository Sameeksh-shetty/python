# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:06:11 2019

@author: Sameeksh M Shetty
"""

import random
doors=[0]*3
s=0;ns=0
j=0
while j<3:
    x=random.randint(0,2)
    doors[x]='BMW'
    gdoors=[i for i in range(3) if i!=x]
    for i in range(3):
        if i==x:
            continue
        else:
            doors[i]='goat'

    ch=int(input('enter the door of choice'))
    if ch>2:
        ch=2
    open_door=random.choice(gdoors)
    while open_door==ch:
        open_door=random.choice(gdoors)
    
    swap=input('y/n')
    
    if swap=='y':
        if doors[ch]=='goat':
            print('win')
            s=s+1
        else:
            print('lost')
    else:
        if doors[ch]=='goat':
            print('lost')
        else:
            print('win')
            ns=ns+1
    j=j+1
print("swap wins",s)
print("with swap wins",ns)
        

