from matplotlib import pyplot as plt
import numpy as np
import joblib
import os.path


def equilibrium(r, x):
    templist = []
    for i in range(1000):
        x = r*x*(1-x)
        if i>500:
            if x not in templist:
                templist.append(x)
    return templist


def bifurcation(initx):
    ax = plt.subplot(111)
    listx = []
    for i in np.linspace(0, 4, 10000):
        listx.append(equilibrium(i, initx))
    max = 0
    for i in listx:
        count = 0
        for _ in i:
            count += 1
        if count > max:
            max = count
    newlist = []
    for i in listx:
        templist = []
        for j in range(max):
            try:
                templist.append(i[j])
            except IndexError:
                templist.append(i[0])
        newlist.append(templist)
    for i in range(max):
        plt.scatter(np.linspace(0, 4, 10000), [item[i] for item in newlist], 0.01)
    return ax


if os.path.isfile('bifgram'):
    plot = joblib.load('bifgram')
else:
    plot = bifurcation(0.4)
    joblib.dump(plot, 'bifgram')
plt.show()