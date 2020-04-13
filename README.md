This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Kate Wujciak
Project 2: Biomedical Data Analysis

NearestNeighborClassification.py - contains Step 2 and Step 3 code. This includes Nearest Neighbor Classification method and K-Nearest Neighbor Classification method. In Nearest Neighbor, the classification of the nearest point in the training data is the classification of the new point being tested. In K-Nearest Neighbor, multiple neighboring points are looked at to classify the new point. 
Nearest Neighbor produces a graph of the training data and new data. As explained further in the report, the training data was normalized and graphed. Then a random test case was generated. The distance between the new data and training data was determined, allowing to classify the new data. It prints the classification of the new data point based on the graph. 
 
KMeansClustering_functions.py - contains Step 4 code. This classification method assigns and updates centroid locations where data has similar features (glucose and hemoglobin levels).  
K-Means Clustering generates a graph of the data and clusters. It plots each class and the associated centroid. This is done by selecting random k cluster location. Then, the training data is assigned to a cluster based on which it is closest to. The location of the cluster is updated based on the average of the features of the data (glucose/hemoglobin levels). This process is iterated a number of times to increase precision. The accuracy of this method is also displayed by presenting percentages of true positive, true negative, false positives, and false negatives (CKD patients/non CKD patients incorrectly/correctly labeled). 
KMeansClustering_driver.py - contains the main script for the functions file. Run the driver to get results from the functions file.
As a user, all one has to do is pick a number, k, for the amount of clusters, and a number, max_it, for the amount of iterations. The rest of the data is pulled from the original csv file.
 
List of Functions:

Name: openckdfile 
Arguments: none
Purpose: Load the array of values of glucose, hemoglobin, and classification from the csv file.
Return: The glucose, hemoglobin, and classification values.
 
Name: normalizeData 
Arguments: glucose, hemoglobin, classification
Purpose: Normalize three NumPy arrays (glucose, hemoglobin, and classification). 
Return: glucose_scaled, hemoglobin_scaled, classification_scaled - Three normalized arrays of glucose, hemoglobin, and classification.
 
Name: amount_k 
Arguments: k (number of centroids)
Purpose: creates an array of k centroids. Rows are centroids, column 0 is glucose and column 1 is hemoglobin.
Return: cent_array - the centroid array.
Name: assign_data 
Arguments: cent_array (centroid array returned by amount_k) and k (number of centroids)
Purpose: assigns each data point to the closest centroid.
Return: assign_array - an array of the assignments of the shortest distances between data points and centroid. 
 
Name: assign_data 
Arguments: cent_array (centroid array returned by amount_k) and k (number of centroids).
Purpose: assigns each data point to the closest centroid.
Return: assign_array - an array of the assignments of the shortest distances between data points and centroid. 
 
Name: update_data 
Arguments: assign_array (array of classifications returned by assign_data) and k (number of centroids).
Purpose: update the cluster locations by taking the average of the assignments (glucose and hemoglobin).
Return: new_cent - an array of the updated centroid locations. 
 
Name: iterate_data 
Arguments: max_it (maximum number of iterations) and k (number of centroids).
Purpose: Iterate through the assignment and update functions until the end condition is met. Each cycle, the centroid is more accurately relocated.
Return: new_cent - the final centroid array, and assign_array - an array of the assignments.
 
Name: calc_percent 
Arguments: assign_array (updated array of assignments) and classification (original assignments)
Purpose: Determine the accuracy of the above functions (the K-Means Clustering method). It prints the percentage of correctly and incorrectly labeled patients.
Return: void function.
 
Name: graphingKMeans
Arguments: glucose, hemoglobin, assign_array, new_cent, k (explained above)
Purpose: Graph training data based on the determined clusters.
Return: void function.

