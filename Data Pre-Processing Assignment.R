################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


#-------------------------------- 1.Outlier Treatments ------------------------------#

#Most of the datasets have extreme values or exceptions in their observations. These 
#values affect the predictions (Accuracy) of the model in one way or the other, removing
#these values is not a very good option. For these types of scenarios, we have the
#techniques for treating such values. Explore on various other techniques to treat 
#these values, you can go through this link:

library(readr)

boston <-read.csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/boston_data.csv")

str(boston)
attach(boston)

#Outlier detection through box plot

boxplot(boston$crim)
boxplot(boston$zn)
boxplot(boston$indus)
boxplot(boston$chas)
boxplot(boston$nox)
boxplot(boston$rm)
boxplot(boston$age)
boxplot(boston$dis)
boxplot(boston$rad)
boxplot(boston$tax)
boxplot(boston$ptratio)
boxplot(boston$black)
boxplot(boston$lstat)
boxplot(boston$medv)

#Except indus,nox,age,rad and tax all inputs have outliers

#Outlier treatment for crim column

qunt_crim <- quantile(boston$crim,probs = c(.25,.75))
qunt_crim 
caps_crim <- quantile(boston$crim, probs = c(.01,.99), na.rm = T)
caps_crim 
H <- 1.5*IQR( boston$crim,na.rm = T)
H 
boston$crim[boston$crim<(qunt_crim[1]-H)] <- caps_crim[1]
boston$crim[boston$crim>(qunt_crim[2]+H)] <- caps_crim[2]
boxplot(boston$crim)

#Outlier treatment for zn column

qunt_zn <- quantile(boston$zn,probs = c(.25,.75))
qunt_zn 
caps_zn <- quantile(boston$zn, probs = c(.01,.99), na.rm = T)
caps_zn 
H <- 1.5*IQR( boston$zn,na.rm = T)
H 
boston$zn[boston$zn<(qunt_zn[1]-H)] <- qunt_zn[1]
boston$zn[boston$zn>(qunt_zn[2]+H)] <- qunt_zn[2]
boxplot(boston$zn)

#Outlier treatment for chas column

qunt_chas <- quantile(boston$chas,probs = c(.25,.75))
qunt_chas 
caps_zn <- quantile(boston$chas, probs = c(.01,.99), na.rm = T)
caps_zn 
H <- 1.5*IQR( boston$chas,na.rm = T)
H 
boston$chas[boston$chas<(qunt_chas[1]-H)] <- qunt_zn[1]
boston$chas[boston$chas>(qunt_chas[2]+H)] <- qunt_zn[2]
boxplot(boston$chas)

#Outlier treatment for rm column
qunt1 <- quantile(boston$rm,probs = c(.25,.75))
qunt1 
caps <- quantile(boston$rm, probs = c(.01,.99), na.rm = T)
caps
H <- 1.5*IQR( boston$rm,na.rm = T)
H # 42539.92
boston$rm[boston$rm<(qunt1[1]-H)] <- caps[1]
boston$rm[boston$rm>(qunt1[2]+H)] <- caps[2]
boxplot(boston$rm)

#Outlier treatment for dis column
qunt1 <- quantile(boston$dis,probs = c(.25,.75))
qunt1 
caps <- quantile(boston$dis, probs = c(.01,.99), na.rm = T)
caps 
H <- 1.5*IQR( boston$dis,na.rm = T)
H 
boston$dis[boston$dis<(qunt1[1]-H)] <- caps[1]
boston$dis[boston$dis>(qunt1[2]+H)] <- caps[2]
boxplot(boston$dis)

#Outlier treatment for black column
qunt1 <- quantile(boston$black,probs = c(.25,.75))
qunt1 
caps <- quantile(boston$black, probs = c(.01,.99), na.rm = T)
caps 
H <- 1.5*IQR( boston$black,na.rm = T)
H 
boston$black[boston$black<(qunt1[1]-H)] <- caps[1]
boston$black[boston$black>(qunt1[2]+H)] <- caps[2]
boxplot(boston$black)

#Outlier treatment for lstat column
qunt1 <- quantile(boston$lstat,probs = c(.25,.75))
qunt1 
caps <- quantile(boston$lstat, probs = c(.01,.99), na.rm = T)
caps 
H <- 1.5*IQR( boston$lstat,na.rm = T)
H 
boston$lstat[boston$lstat<(qunt1[1]-H)] <- caps[1]
boston$lstat[boston$lstat>(qunt1[2]+H)] <- caps[2]
boxplot(boston$lstat)

#Outlier treatment for medv column
qunt1 <- quantile(boston$medv,probs = c(.25,.75))
qunt1 
caps <- quantile(boston$medv, probs = c(.01,.99), na.rm = T)
caps 
H <- 1.5*IQR( boston$medv,na.rm = T)
H 
boston$medv[boston$medv<(qunt1[1]-H)] <- caps[1]
boston$medv[boston$medv>(qunt1[2]+H)] <- caps[2]
boxplot(boston$medv)




#------------------------------------- 2.Imputation ---------------------------------------#

#Majority of the datasets have missing values, that might be because the data collected were
##to build the proper model or in other words, get accurate results. The common techniques are
#either removing those records completely or substitute those missing values with the logical
#ones, there are various techniques to treat these types of problems.

library(readr)

climates<-read.csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/claimants.csv")

attach(climates)

sum(is.na(climates$CASENUM))
sum(is.na(climates$ATTORNEY))
sum(is.na(climates$CLMSEX))
sum(is.na(climates$CLMINSUR))
sum(is.na(climates$SEATBELT))
sum(is.na(climates$CLMAGE))
sum(is.na(climates$LOSS))

#we have missing values in CLMSEX,CLMINSUR,SEATBELT,CLMAGE
#Imputation will be done through mean values as all are continuous variables
#We can also omit missing values but in this case data will be loss

#Mean imputation
climates$CLMSEX[is.na(climates$CLMSEX)] <- mean(climates$CLMSEX, na.rm = TRUE)
climates$CLMINSUR[is.na(climates$CLMINSUR)] <- mean(climates$CLMINSUR, na.rm = TRUE)
climates$SEATBELT[is.na(climates$SEATBELT)] <- mean(climates$SEATBELT, na.rm = TRUE)
climates$CLMAGE[is.na(climates$CLMAGE)] <- mean(climates$CLMAGE, na.rm = TRUE)

sum(is.na(climates))



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



#------------------------------------- 7.STRING MANIPULATIONS---------------------------------------#

#It is obvious that as part of data analysis we encounter a lot of text data which is a
#collection of strings which in turn is a sequence of characters. Access the text data and
#manipulate as per our requirements. you can go through this link for further assistance:

###Q1###
library(stringr)
?stringr
st <-c('Grow Gratitude')

length()
nchar(st)
class(st)
str(st)
substring(st,6,6)
str_count(st ,pattern = "G")
str_locate(st,pattern = "G")

#Q2

st2<- "Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else"

str(st2)
length(st2)
nchar(st2)


#Q3
st3 <- "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"

str_sub(st3,1,1)

str_sub(st3,1,3)
str_sub(st3,-3)

#Q4

st4 <-"stay positive and optimistic"

str_starts(st4,pattern = "H")
str_ends(st4,pattern = "d")
str_ends(st4,pattern = "c")

#Q6

str_c("o", 1:108 ,sep = "-",collapse = "")

#Q7
st7<-"Grow Gratitude"

str_replace(st7,'Grow' ,'Growth of')






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




#------------------------------------- 9.Duplication Typecasting ---------------------------------------#

#Q1. For the given dataset perform the type casting (convert the datatypes, ex. float to int)
#Q2. Check for the duplicate values, and handle the duplicate values (ex. drop)
#Q3. Do the data analysis (EDA)?
#   Such as histogram, boxplot, scatterplot etc

retail <- read.csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/OnlineRetail.csv")

str(retail)

retail <- na.omit(retail)

#Character column to int transformation of InvoiceNo and Stock code

attach(retail)

retail$InvoiceNo <- as.integer(retail$InvoiceNo)

retail$StockCode <-as.integer(retail$StockCode)

retail <-na.omit(retail)
str(retail)

#EDA Of retail data
plot(retail)

hist(retail$InvoiceNo)
hist(retail$StockCode)
hist(retail$Quantity)
hist(retail$UnitPrice)

boxplot(retail$Quantity)
boxplot(retail$UnitPrice)





