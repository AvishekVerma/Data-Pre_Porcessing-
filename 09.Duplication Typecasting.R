################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


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





