################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


#------------------------------------- 5.Dummy Variables ---------------------------------------#

#Data is one of the most important assets. It is often common that data is stored in distinct 
#systems with different formats and forms. Non-numeric form of data makes it tricky while developing
#mathematical equations for prediction models. We have the preprocessing techniques to make the data
#convert to numeric form. Explore the various techniques to have reliable uniform standard data, 
#you can go through this link:

library(readr)
install.packages("fastDummies")
library(fastDummies)

animal <-read.csv(file.choose())
str(animal)
attach(animal)

Dummy_animal <-dummy_columns(animal,select_columns = c("Animals","Gender","Homly","Types"),
                             remove_first_dummy = TRUE,remove_most_frequent_dummy = FALSE)

Dummy_animal

#Other approach

library(rlang)
library(caret)

dmy <-dummyVars("~.",data=animal[c(2,3,4)],fullRank = TRUE)
Data_transformed <-data.frame(predict(dmy,newdata = animal[c(2,3,4)]))
finaldata <-cbind(animal[c(1,2,3,4,5)],Data_transformed)



