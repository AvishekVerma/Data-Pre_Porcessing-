################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


#------------------------------------- 6.Zero - Variance Features ---------------------------------------#

#Find which columns of the given dataset with zero variance, explore various techniques used to remove the
#zero variance from the dataset to perform certain analysis.

library(readr)

data <-read.csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/Z_dataset.csv")

data <- data[-c(1,6)]

attach(data)

summary(data)
str(data)

apply(data, 2, var)

which(apply(data, 2, var)==0)


