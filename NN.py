# using python3
#%matplotlib inline
import random
import numpy as np
import math
import time
import statistics
#data is length,  width, color (blue = 0, red = 1)
data = [[3, 1.5, 1],
        [2, 1,   0],
        [4, 1.5, 1],
        [3, 1,   0],
        [3.5,0.5,1],
        [2, 0.5, 0],
        [5.5, 1, 1],
        [1,  1,  0]]
#list of the targets to make things easier for rmse
targets = [1,0,1,0,1,0,1,0]
#list for predictions
predictions = []
#datachoice to itterate through
datachoice = 0
#mystery flower
mystery = [4.5, 1]
#training_rate
training_rate = 0.01
#network
#    0     flower type
#  /   \   w1, w2, b
# 0     0  length, width

#weights and bias
w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

#w1 = random.uniform(-1,1)
#w2 = random.uniform(-1,1)
#b = random.uniform(-1,1)

#logistic sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

#def reLU(x):
#    if x == 0:

#neural network function
def nn(length, width):
    x = sigmoid(w1*length+w2*width + b)
    return x
#rmse function
def rmse(pre, targ):
    pred_mean = statistics.mean(pre)
    targ_mean = statistics.mean(targ)
    return math.sqrt(((pred_mean - targ_mean) ** 2))

#first train
for i in range(0,7):
    Neuralresult = nn(data[datachoice][0],data[datachoice][1])
    print('network got {0}!'.format(Neuralresult))
    print('w1 is {0}'.format(w1))
    print('w2 is {0}'.format(w2))
    print('bias is {0}'.format(b))
    print('datachoice is {0}'.format(datachoice))
    predictions.append(Neuralresult)
    print(Neuralresult)
    if Neuralresult > 0.5 and data[datachoice][2] > 0.5:
        print('correct,  flower is red')
    elif Neuralresult < 0.5 and data[datachoice][2] > 0.5:
        print('incorrect, flower is red; not blue')
    elif Neuralresult < 0.5 and data[datachoice][2] < 0.5:
        print('correct, flower is blue')
    elif Neuralresult > 0.5 and data[datachoice][2] < 0.5:
        print('incorrect, flower is red; not blue')
    else:
        print('you suck at programming')
    datachoice = datachoice + 1
    time.sleep(0.1)

print(targets)
print(predictions)


print("predictions are: " + str(["%.8f" % elem for elem in predictions]))
print("targets are: " + str(["%.8f" % elem for elem in targets]))

rmse_val = rmse(predictions,targets)
print("rms error is: " + str(rmse_val))

#averages rmse and each weight/bias
w1 = (w1+rmse_val)/2
w2 = (w2+rmse_val)/2
b = (b+rmse_val)/2

datachoice = 0


#second train
accuracy = 0
RoN = 0 # right or not
print('second started ')
while accuracy < 0.9:
    accuracy = 0
    datachoice = 0

    for i in range(0,7):

        Neuralresult = nn(data[datachoice][0],data[datachoice][1])
        print('network got {0}!'.format(Neuralresult))
        print('w1 is {0}'.format(w1))
        print('w2 is {0}'.format(w2))
        print('bias is {0}'.format(b))
        print('datachoice is {0}'.format(datachoice))
        predictions.append(Neuralresult)
        print(Neuralresult)
        if Neuralresult > 0.5 and data[datachoice][2] > 0.5:
            print('correct,  flower is red')
            RoN = RoN + 1
        elif Neuralresult < 0.5 and data[datachoice][2] > 0.5:
            print('incorrect, flower is red; not blue')
        elif Neuralresult < 0.5 and data[datachoice][2] < 0.5:
            print('correct, flower is blue')
            RoN = RoN + 1
        elif Neuralresult > 0.5 and data[datachoice][2] < 0.5:
            print('incorrect, flower is red; not blue')
        else:
            print('you suck at programming')
        datachoice = datachoice + 1
        time.sleep(0)



    print(targets)
    print(predictions)


    print("predictions are: " + str(["%.8f" % elem for elem in predictions]))
    print("targets are: " + str(["%.8f" % elem for elem in targets]))

    rmse_val = rmse(predictions,targets)
    print("rms error is: " + str(rmse_val))

    w1 = (w1+rmse_val)/2
    w2 = (w2+rmse_val)/2
    b = (b+rmse_val)/2
    #calculates accuracy.
    accuracy = RoN/8

print('accuracy is {0}'.format(accuracy))
