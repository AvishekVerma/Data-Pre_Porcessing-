################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


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





