################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


#------------------------------------- 3.TRANSFORMATIONS ---------------------------------------#


#Everything will revolve around the data in Analytics world. Proper data will help you to make 
#useful predictions which improve your business. Sometimes the usage of original data as it is
#does not help to have accurate solutions. It is needed to convert the data from one form to 
#another form to have better predictions. Explore on various techniques to transform the data 
#for better model performance. you can go through this link:

import pandas as pd

#loding the data frame
con=pd.read_csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/calories_consumed.csv")

con.info()   #For data types and non or null values
# data has no na or nall values 

con.describe() # for mean ,min, max, IQR 

con.shape

con.dtypes

EDA=pd.DataFrame({"columns_name ":con.columns,
                  "mean":con.mean(),
                  "median":con.median(),
                  "mode":con.mode(),
                  "standard_deviation":con.std(),
                  "variance":con.var(),
                  "skewness":con.skew(),
                  "kurtosis":con.kurt()})
EDA

#transforming the columns

# pass a list of functions 
result = con.transform(func = ['sqrt', 'exp','log']) 
  
# Print the result 
print(result) 



