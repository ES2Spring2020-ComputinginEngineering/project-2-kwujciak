# Kate Wujciak
# KMeansCLustering_driver.py
# This file contains the driver for the functions of step 4.
#-----------------------------------------------------------

import KMeansClustering_functions as kmc #Use kmc to call your functions

k = 3
max_it = 10
glucose, hemoglobin, classification = kmc.openckdfile()
glucose_scaled, hemoglobin_scaled, classification = kmc.normalizeData(glucose, hemoglobin, classification)
cent_array = kmc.amount_k(k)
assign_array = kmc.assign_data(cent_array, k)
new_cent = kmc.update_data(assign_array, k)
assign_array, new_cent = kmc.iterate_data(k, max_it)
kmc.calc_percent(assign_array, classification)
kmc.graphingKMeans(glucose, hemoglobin, assign_array, new_cent, k)

