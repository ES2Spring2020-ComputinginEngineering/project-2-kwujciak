# Kate Wujciak
# Reference: Jenn's starter code
# File name: KMeansClustering_functions.py
# This file contains Step 4 and part of Step 5. It is the fnc file.
#-------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import random


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

def amount_k(k):
# This function takes one parameter: k (number of centroids).
# This function creates an array of k centroids and returns
# that array.
      cent_array = np.random.rand(k,2) #rows are cent,  column col 0 = g, col 1 = h
      return cent_array

def assign_data(cent_array, k):
# This function takes 2 parameters: cent_array (array with centroid points) 
# and k (number of clusters).
# This function assigns each data point to the closest centroid. 
# It returns an array of the indices of assignments (minimum distance).
      glucose, hemoglobin, classification = openckdfile()
      glucose_scaled, hemoglobin_scaled, classification = normalizeData(glucose, hemoglobin, classification)
      distance = np.zeros((len(glucose),k))
      for i in range(k):
          cent_point_dist = np.array(np.sqrt(((glucose_scaled-cent_array[i,0])**2)+(hemoglobin_scaled-cent_array[i,1])**2))
          distance[:,i] = cent_point_dist
      assign_array = np.argmin(distance, axis = 1)
      return assign_array
  
def update_data(assign_array, k):
    # This function takes two parameters: k (number of clusters) 
    # and assign_array (array of classifications).
    # The purpose of this function is to update the clusters by 
    # taking the average of the assignments. It returns the new
    # array that has the new centroid locations. 
      glucose, hemoglobin, classification = openckdfile()
      glucose_scaled, hemoglobin_scaled, classification = normalizeData(glucose, hemoglobin, classification)
      avg_array = np.zeros((k,2))
      for i in range(k):
          glucose_assign = glucose_scaled[assign_array==i]
          hemoglobin_assign = hemoglobin_scaled[assign_array==i]
          glucose_avg = np.average(glucose_assign)
          hemoglobin_avg = np.average(hemoglobin_assign)
          avg_array[i,0] = glucose_avg
          avg_array[i,1] = hemoglobin_avg
          new_cent = avg_array
      return new_cent

def iterate_data(k, max_it):
    # This function takes two parameters: k and max_it. K is amount
    # of centroid points and max_it is the amount of iterations the
    # user wants to do. The purpose of this function is to iterate
    # through the assignment and update functions until the end condition
    # is met. Each cycle, the centroid is more accurately relocated.
    # It returns new_cent, which is the final centroid array, and assign_array
    # which is an array of the assignments.
    iteration = 0
    new_cent = amount_k(k)
    while max_it != iteration:
        assign_array = assign_data(new_cent, k)
        new_cent = update_data(assign_array, k)
        max_it = max_it -1
    return assign_array, new_cent

def calc_percent(assign_array, classification):
    # This function has two parameters: assign_array and classification.
    # The purpose of this function is to determine the accuracy of the 
    # above functions. It prints the percentage of the True/False and 
    # Positive/Negative rates. It is a void function.
    true_pos = 0
    false_pos = 0
    true_neg = 0
    false_neg = 0
    CKD_patient = 0
    non_CKD = 0
    for i in range(len(classification)):
        if (classification[i] + assign_array[i]) == 2:
            true_neg +=1
            non_CKD +=1
        elif (classification[i] + assign_array[i]) == 0:
            true_pos +=1
            CKD_patient +=1
        elif (classification[i] + assign_array[i]) == 1:
            if classification[i] == 0:
                false_neg +=1
                CKD_patient +=1
            elif classification[i] == 1:
                false_pos +=1
                non_CKD +=1
    
    if true_pos/CKD_patient >= .5:
        if CKD_patient != 0:
            print("Percentage of CKD Patients incorrectly labeled by K-means as being in non-CKD cluster: " + str((false_neg/CKD_patient)*100)+ "%")
            print("Percentage of CKD Patients correctly labeled by K-means: " + str(round((true_pos/CKD_patient),3)*100)+ "%")
        if non_CKD != 0:
            print("Percentage of non-CKD Patients incorrectly labeled by K-means as being in non-CKD cluster: " + str(round((false_pos/non_CKD),3)*100)+ "%")
            print("Percentage of non-CKD Patients correctly labeled by K-means: " + str(round((true_neg/non_CKD),3)*100)+ "%")
        else:
            print("Run file again")
    else:
        if CKD_patient != 0:
            print("Percentage of CKD Patients incorrectly labeled by K-means as being in non-CKD cluster: " + str((true_pos/CKD_patient)*100)+ "%")
            print("Percentage of CKD Patients correctly labeled by K-means: " + str(round((false_neg/CKD_patient),3)*100)+ "%")
        if non_CKD != 0:
            print("Percentage of non-CKD Patients incorrectly labeled by K-means as being in non-CKD cluster: " + str(round((true_neg/non_CKD),3)*100)+ "%")
            print("Percentage of non-CKD Patients correctly labeled by K-means: " + str(round((false_pos/non_CKD),3)*100)+ "%")
        else:
            print("Run file again")
            
            
def graphingKMeans(glucose, hemoglobin, assign_array, new_cent, k):
    # This function takes 5 parameters: glucose, hemoglobin, assign_array, new_cent, k.
    # The purpose of this function is to graph the training data based on the determined
    # clusters. It is a void function.
    plt.figure()
    for i in range(assign_array.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assign_array==i], glucose[assign_array==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot((14.7*new_cent[i, 1])+3.1, (420*new_cent[i, 0])+70, "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title('K Means Clustering K= ' + str(k))
    plt.legend()
    plt.show() 
    
    
        
          