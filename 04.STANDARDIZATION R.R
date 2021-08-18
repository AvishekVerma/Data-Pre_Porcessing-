################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


#------------------------------------- 4.STANDARDIZATION & NORMALIZATION ------------------------#

#Data is one of the most important assets. It is often common that data is stored in distinct systems
#with different formats and scales. These seemingly small differences in how the data is stored can 
#result in misinterpretations and inconsistencies in your analytics. Inconsistency can make it 
#impossible to deliver reliable information to management for good decision making. We have the
#pre processing techniques to make the data uniform. Explore the various techniques to have reliable
#uniform standard data, you can go through this link:

library(readr)

seed <- read.csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/Seeds_data.csv")

summary(seed)
str(seed)

#Standardization

std_seed <-scale(seed)

#Normalization

#function

normalize <-function(x){
  return((x-min(x))/max(x)-min(x))
}

norm_seed <-as.data.frame(lapply(seed, normalize))

summary(norm_seed)


