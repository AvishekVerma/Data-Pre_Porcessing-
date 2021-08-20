################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


#------------------------------------- 8.DISCRETIZATION ---------------------------------------#

#Everything will revolve around the data in Analytics world. Proper data will help you to make
#useful predictions which improve your business. Sometimes the usage of original data as it is
#does not help to have accurate solutions. It is needed to convert the data from one form to 
#another form to have better predictions. Explore on various techniques to transform the data 
#for better model performance. you can go through this link:

library(readr)

iris <-read.csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/iris.csv")

str(iris)

attach(iris)

#Discretizing sepal length
min(iris$Sepal.Length)
max(iris$Sepal.Length)

iris$Sepal_l <- cut(iris$Sepal.Length ,breaks = c(4,6,8))

#Discretizing sepal width
min(iris$Sepal.Width)
max(iris$Sepal.Width)


iris$Sepal_W <- cut(iris$Sepal.Width ,breaks = c(1,3,5))

#Discretizing petal length
min(iris$Petal.Length)
max(iris$Petal.Length)

iris$petal_L <- cut(iris$Petal.Length ,breaks = c(1,3,5,7))

#Discretizing petal width
min(iris$Petal.Width)
max(iris$Petal.Width)

iris$petal_W <- cut(iris$Petal.Width ,breaks = c(0,1,2,3))



