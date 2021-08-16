################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


#------------------------------------- 3.TRANSFORMATIONS ---------------------------------------#

#Everything will revolve around the data in Analytics world. Proper data will help you to make 
#useful predictions which improve your business. Sometimes the usage of original data as it is
#does not help to have accurate solutions. It is needed to convert the data from one form to 
#another form to have better predictions. Explore on various techniques to transform the data 
#for better model performance. you can go through this link:

library(readr)
calories <- read.csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/calories_consumed.csv")

str(calories)
attach(calories)
boxplot(calories)
qqnorm(calories$Weight.gained..grams.)
qqnorm(calories$Calories.Consumed)

#transformation to make Weight.gained..grams. variable normal
qqnorm(log(Weight.gained..grams.))
qqline(log(Weight.gained..grams.))

#transformation to make workex variable normal
qqnorm(log(Calories.Consumed))
qqline(log(Calories.Consumed))


