from sklearn.datasets import make_blobs
import seaborn as sns
import random
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from pandas import DataFrame
from matplotlib import pyplot
from sklearn.cluster import KMeans

N = 100
clusters = 3
X, y = make_blobs(n_samples = N, n_features = 2, centers = clusters, random_state = 0)


for i in range(N):
    avr_x_center0 = 0
    avr_y_center0 = 0
    avr_x_center1 = 0
    avr_y_center1 = 0
    avr_x_center2 = 0
    avr_y_center2 = 0
    n0 = 0
    n1 = 0
    n2 = 0
    distance0 = ((X[i,0] - centers[0][0])**2 + (X[i, 1] - centers[0][1])**2)**(1/2)
    distance1 = ((X[i,0] - centers[1][0])**2 + (X[i, 1] - centers[1][1])**2)**(1/2)
    distance2 = ((X[i,0] - centers[2][0])**2 + (X[i, 1] - centers[2][1])**2)**(1/2)
    if ((distance0 < distance1) and (distance0 < distance2)):
        y[i] = 0
        n0 += 1
        avr_x_center0 += X[i, 0]
        avr_y_center0 += X[i, 1]
    elif (distance1 < distance2):
        y[i] = 1
        n1 += 1
        avr_x_center1 += X[i, 0]
        avr_y_center1 += X[i, 1]
    else:
        y[i] = 2
        n2 += 1
        avr_x_center2 += X[i, 0]
        avr_y_center2 += X[i, 1]
    center_x_prev0= centers[0][0]
    center_y_prev0= centers[0][1]
    center_x_prev1= centers[1][0]
    center_y_prev1= centers[1][1]
    center_x_prev2= centers[2][0]
    center_y_prev2= centers[2][1]

    centers[0][0] = avr_x_center0/n0
    centers[0][1] = avr_y_center0/n0
    if ( (centers[0][0] != center_x_prev0) or (centers[0][1] != center_y_prev0) ):
        change_center0 = True #центр первого изменился

    centers[1][0] = avr_x_center1/n1
    centers[1][1] = avr_y_center1/n1
    if ( (centers[1][0] != center_x_prev1) or (centers[1][1] != center_y_prev1) ):
        change_center1 = True #центр второго изменился

    centers[2][0] = avr_x_center2/n2
    centers[2][1] = avr_y_center2/n2
    if ( (centers[2][0] != center_x_prev2) or (centers[2][1] != center_y_prev2) ):
        change_center2 = True #центр третьего изменился
    if ((change_center0 == False) and (change_center1 == False) and (change_center1 == False)):
        break

sns.scatterplot(x=X[:,0], y=X[:,1], hue=y, palette = "tab10")









    
