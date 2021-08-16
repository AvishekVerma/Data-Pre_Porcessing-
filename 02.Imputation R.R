################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


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


