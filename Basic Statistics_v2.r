2 + 2 # control + enter  or control + R
# works as calculator

#Packages
install.packages("readr")
library(readr)

install.packages()

# Read data into R
education <- read_csv("C:/Data/education.csv")
education <- read.csv(file.choose()) # load csv file into R

# C:\Users\\education.csv - this is windows default file path with a '\'
# C:\\Users\\Desktop\\education.csv - change it to '\\' to make it work in R

View(education)

#Exploratory Data Analysis
#Measures of Central Tendency / First moment business decision

mean(education$workex) # '$' is used to refer to the variables within object
attach(education) # When used we can directly refer to the variable name

mean(gmat)
mean(workex)

rm(xyz) #Remove specific object to free RAM (memory)
rm(list=ls()) # Remove all to free RAM (memory)

median(workex) #Median

mode(workex)

#Mode
y <- c(19, 4, 5, 7, 29, 19,19,19,19, 29, 13, 25,29,5,5,5,5,4,4,4,4)
# uni mode function
Mode <- function(x){
     a = unique(x) # x is a vector
     return(a[which.max(tabulate(match(x, a)))])
}

Mode(y)

# Bi mode function 
Modes <- function(x) {
  ux <- unique(x)
  tab <- tabulate(match(x, ux))
  ux[tab == max(tab)]
}
Modes(y)

# Measures of Dispersion / Second moment business decision
var(workex) # variance
sd(workex) #standard deviation
range <- max(workex) - min(workex) # range

install.packages("moments")
library(moments)

#Third moment business decision
skewness(workex)

#Fourth moment business decision
kurtosis(workex)

#Graphical Representation
barplot(gmat)
dotchart(gmat)

hist(gmat) #histogram

boxplot(gmat) #boxplot
y <- boxplot(gmat)
y$out # to see outliers

# Probability Distribution
install.packages("UsingR")
library("UsingR")
densityplot(gmat)

# Normal Quantile-Quantile Plot
qqnorm(gmat)
qqline(gmat)
qqnorm(workex)
qqline(workex)

# Transformation to make workex variable normal
qqnorm(log(workex))
qqline(log(workex))



#### Data Pre-processing ##############################

## Dummy variables creation 
# use ethnic diversity dataset
# packages such as 'dummyvars', 'fastdummies' can be used 
# loading the dataset
data <- read.csv(file.choose())

# checking str and summary of the data
str(data)
summary(data)
attach(data)

install.packages("fastDummies")
library(fastDummies)

data_dummy <- dummy_cols(data, select_columns = c("Position","State","Sex","MaritalDesc","CitizenDesc","EmploymentStatus","Department","Race"),
                      remove_first_dummy = TRUE,remove_most_frequent_dummy = FALSE,remove_selected_columns = TRUE)
??fastDummies
# you can choose between remove_first_dummy and remove_most_frequent_dummy
# as both will remove multicollinearity issue 
#################################################
### Label encoding in R
library(CatEncoders)
View(data)

# character column: 'Position'
lb_new <- LabelEncoder.fit(data$Position)
# new values are transformed to NA
position_new<- transform(lb_new,data$Position)
position_new

# Using cbind to combine with original dataset
newdata <- cbind(data, position_new)

################################################
###### Normalization ###################################
# we will ethnic diversity dataset
df <- data_dummy[, -c(1,2,3)]

# to normalize the data we use custom function 
norm <- function(x){
  return ((x-min(x))/(max(x)-min(x)))
}

df_norm <- as.data.frame(lapply(df, norm))
# Normalized data have values ranging between 0 to 1

# To apply standardization we have inbuilt function scale
# we use mtcars dataset 
df_mt <- read.csv(file.choose())
View(df_mt)
# remove first column 
df_mt <- df_mt[,-1]
# use scale function 
df_scale <- as.data.frame(scale(df_mt))
# hypothetically you have values ranging between -3 to +3 or in general the range is -inf to +inf

###########//\\\\//////\\\\\\\\/////\\\\\\////\\\\\\///\\\\\//\\\\##############

# Handling duplicates###############################################
# Duplicate entries are removed using 'duplicated' function
# it stores the duplicate values into another variable

dup <- duplicated(data)
dup
data_new <- data[!duplicated(data), ]
data_new

####### /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ ####################
###################### Type Casting ########################
# Type casting is used to convert one data type into another.
# ex: categorical data to numeric data

as.numeric(data$age) 

is.numeric(data$age) # it will return true or false

# Ex: Convert Numeric to Integer
data$age <- as.integer(data$age)

# Ex: Convert categorical data to factor type
str(data) # categorical data is character

# convert sex column to factors
data$Sex <- as.factor(data$Sex)
str(data) # check now for Sex column

# Alternatively we can use argument stringAsFactors=TRUE
# load ethnic diversity dataset
data1 <- read.csv(file.choose(),stringsAsFactors = TRUE)
str(data1)
summary(data1)

################################################
## Missing values - imputation

# Lets introduce NA values into the dataset using 'missForest' package

install.packages("missForest")
library(missForest)

# Generate 10% missing values at Random
# remove three unwanted columns as they are not required for analysis
data.mis <- prodNA(data[,-c(1,2,5)], noNA = 0.1)
summary(data.mis)
attach(data.mis)
sum(is.na(data.mis)) # 310

# Omitting NA values from the Data 
data_omit <- na.omit(data.mis) # na.omit => will omit the rows which has atleast 1 NA value
dim(data_omit)
sum(is.na(data_omit)) #0

# Alternatively We can apply mean/median/mode imputation
data_new <- data.mis # work with original data for imputation
summary(data_new)

# NA values are present in both continuous and categorical columns

# Mean imputation for continuous data - CLMAGE
data_new$Salaries[is.na(data_new$Salaries)] <- mean(data_new$Salaries, na.rm = TRUE)
data_new$age[is.na(data_new$age)] <- mean(data_new$age, na.rm = TRUE)


# Mode imputation for categorical data
# Custom function to calculate Mode
Mode <- function(x){
  a = table(x) # x is a vector
  names(a[which.max(a)])
}

data_new$Position[is.na(data_new$Position)] <- Mode(data_new$Position[!is.na(data_new$Position)])

# select categorical columns with NA, so we simple remove columns which 
# does not have NA and use apply function to impute all columns at once
data_cat <- data_new[,-c(1,8,9)]
sum(is.na(data_cat)) # 210
# create a new dataframe to use apply function 
# apply is inbuilt function which takes arguments as
### X ---- dataframe, matrix, list
#### MARGIN --- 2 implies to columns and 1 implies to rows
#### FUN ---- Implies to functions suchas mean, sum, average, or any custom defined function
data_tran <- as.data.frame(apply(data_cat,c(1,2),Mode))
sum(is.na(data_tran)) # 0

# now combine using cbind function
clean_data <- cbind(data_new[,c(1,8,9)],data_tran)
sum(is.na(clean_data)) 

######################################################################
##########/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\############3
# Outlier Treatment
data<- read.csv(file.choose())
sum(is.na(data))
attach(data)
View(data)
boxplot(data$Salaries)
boxplot(data$age)

# There are 2 outliers in the salary column
# Replace outliers with the maximum value - Winsorization
qunt1 <- quantile(data$Salaries,probs = c(.25,.75))
qunt1 # 25% 23092, # 75% = 51452
caps <- quantile(data$Salaries, probs = c(.01,.99), na.rm = T)
caps # 1 % = 441, 99% = 95770
H <- 1.5*IQR( data$Salaries,na.rm = T)
H # 42539.92
data$Salaries[data$Salaries<(qunt1[1]-H)] <- caps[1]
data$Salaries[data$Salaries>(qunt1[2]+H)] <- caps[2]
boxplot(data$Salaries)


####################################################
############# zero Variance
library(ggplot2)
library(ggthemes)
# Use 'apply' and 'var' functions to 
# check for variance on numerical values
apply(data, 2, var)

# Check for the columns having zero variance

which(apply(data, 2, var)==0) # ignore the warnings


###################
# z-distribution
pnorm(680,711,29) # given a value, find the probability
qnorm(0.025) # given probability, find the Z value


# t-distribution
pt(1.98, 139) # given a value, find the probability
qt(0.975, 139) # given probability, find the t value
