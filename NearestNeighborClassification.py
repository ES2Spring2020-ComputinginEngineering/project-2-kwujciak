# Kate Wujciak
# References: Jenn's helper code.
# File name: NearestNeighborClassification.py
# This file contains code for steps 2 and 3.
##############################################

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats


# Step 2

def openckdfile():
#This function doesn't take any parameters.
#The purpose of this function is to load the array of values of glucose, hemoglobin, and 
#classification from the csv file. It returns those values.
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
#This function takes three parameters: the values of glucose, hemoglobin, and
#the classification. The purpose of this function is to normalize three NumPy arrays (glucose, hemoglobin, and classification). 
#This was done by converting the original units to a unitless scale of 0-1.
#The function returns the three normalized arrays.
    glucose_L = []
    hemoglobin_L = []
    
    for g in glucose:
        gluc_orig = (g-70)/(420)
        glucose_L.append(gluc_orig)
        
    for h in hemoglobin:
        hemo_orig = (h-3.1)/(17.8-3.1)
        hemoglobin_L.append(hemo_orig)
        
    glucose_scaled = np.array(glucose_L)
    hemoglobin_scaled = np.array(hemoglobin_L)
    classification_scaled = np.array(classification)
    
    return glucose_scaled, hemoglobin_scaled, classification_scaled

def graphData(glucose, hemoglobin, classification): 
#This function takes three parameters: glucose, hemoglobin, classification (explained above).
#The purpose of this function is to plot the glucose values vs. the hemoglobin values.
#It is a void function.    
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Glucose vs. Hemoglobin")
    plt.legend()
    plt.show()

def createTestCase():
#This function doesn't take any parameters.
#The purpose of this function is to create a random test case within the 
#given range of the training hemoglobin and glucose data. It returns 
#random floats within each range.
    newhemoglobin = random.uniform(3.1,17.8)
    newglucose = random.uniform(70,490)
    return newhemoglobin, newglucose

def calculateDistanceArray(newhemoglobin, newglucose, glucose, hemoglobin):
#This function takes four parameters: newhemoglobin, newglucose, glucose, hemoglobin.
#These values are the original values for glucose and hemoglobin, and the random
#values found above.
#The purpose of this function is to create an array of the distances between the points
#derived from the test case and the orginial points from the data set.
#It returns an array of all the distances.
    newhemoglobin = (newhemoglobin-3.1)/(17.8-3.1)
    newglucose = (newglucose-70)/(420)
    distance = np.sqrt(((glucose-newglucose)**2)+(hemoglobin-newhemoglobin)**2)
    distance = np.array(distance)
    return distance

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classificiation):
#This function takes 5 parameters: newglucose, newhemoglobin, glucose, hemoglobin, classificiation.
#These parameters are explained in above functions. The purpose of this function
#is to call the distance function and find the index of the shortest distance in that array.
#The class of the closest point is returned.
    distance = calculateDistanceArray(newhemoglobin, newglucose, glucose, hemoglobin)
    min_index = np.argmin(distance)
    nearest_class = classification[min_index]
    return nearest_class

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classificiation):
#This function taks 5 paramters: newglucose, newhemoglobin, glucose, hemoglobin, classificiation.
#This function graphs the test case as well as the training data in order to compare.
#It is a void function.
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1: CKD")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0: Normal")
    plt.plot((newhemoglobin-3.1)/(17.8-3.1),(newglucose-70)/(420),"x", markersize = 10)
    plt.xlabel("Normalized Hemoglobin")
    plt.ylabel("Normalizeed Glucose")
    plt.title("Normalized Glucose vs. Hemoglobin + Test Case Data")
    plt.legend()
    plt.show()

#------------------------------------------------------------------------------
#Step 3  
    
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classificiation):
#This function takes 6 parameters: k (number of nearest neighbors), newglucose, newhemoglobin, glucose, 
#hemoglobin, classificiation. The purpose of this function is to more accurate classify points. 
#It returns the classification for the point (newglucose, newhemoglobin) either a 1 or 0 based on the 
#k nearest neighbors. K is an odd integer to avoid ties. The classification of the new point is based on 
#the majority of classifications of k nearest points.
    distance = calculateDistanceArray(newhemoglobin, newglucose, glucose, hemoglobin)
    sorted_indices = np.argsort(distance)
    k_indices = sorted_indices[:k]
    k_classification = classification[k_indices]
    classMode = float(stats.mode(k_classification)[0])
    return classMode
    
            
    
# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
graphData(glucose, hemoglobin, classification)
newhemoglobin, newglucose = createTestCase()
calculateDistanceArray(newhemoglobin, newglucose, glucose, hemoglobin)
nearest_class = nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)
classMode = kNearestNeighborClassifier(21, newglucose, newhemoglobin, glucose, hemoglobin, classification)
print("Classification: " + str(classMode))