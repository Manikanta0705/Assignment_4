import numpy as np
from numpy import linalg as LA
from numpy import random as RN 

a=[]
#n=int(input("Enter number of elements:"))
for j in range(36):
    a.append(RN.randint(1,6,2))
print('SAMPLE SPACE is: ',a)
