# using python3
import random
from sklearn import linear_model
import math
import numpy as np
#user input 
length = int(input('enter length'))
width = int(input('enter width'))
reg = linear_model.Ridge(alpha=.5)
reg.fit([[3, 1.5],
         [2, 1],
         [4, 1.5],
         [3, 1],
         [3.5, 0.5],
         [2, 0.5],
         [5.5, 1],
         [1,1]],
         [1,0,1,0,1,0,1,0])

Network_input = [length, width]
oofamos = np.array(Network_input)


oofamos = oofamos.reshape(1,-1)


print(reg.predict(oofamos))
