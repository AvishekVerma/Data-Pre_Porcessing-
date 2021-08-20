################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


#------------------------------------- 8.DISCRETIZATION ---------------------------------------#

#Everything will revolve around the data in Analytics world. Proper data will help you to make
#useful predictions which improve your business. Sometimes the usage of original data as it is
#does not help to have accurate solutions. It is needed to convert the data from one form to 
#another form to have better predictions. Explore on various techniques to transform the data 
#for better model performance. you can go through this link:

import pandas as pd 


#loading data set
iris = pd.read_csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/iris.csv")

iris.info()   #For data types and non or null values
# data has no na or nall values 

# droping Unnamed column # it is nothing but index
iris.drop(iris.columns[0], axis = 1 , inplace = True)


iris.describe() # for mean ,min, max, IQR 

# check for count of NA'sin each column
iris.isna().sum()


#boxplot for every column
iris.columns
iris.boxplot(column= ['Sepal.Length', 'Sepal.Width', 'Petal.Length','Petal.Width'])
  # sepal have some outlier     


#Graphical Representation
import matplotlib.pyplot as plt

#discretization for iris['Sepal.Length']

plt.hist(iris['Sepal.Length']) #histogram
iris['Sepal.Length'].unique() 
iris['Sepal.Length']= pd.cut(iris['Sepal.Length'],bins=[0, 5.5 ,6.7 ,7.9],labels=['small','medium','large'])
# size under 5.5 = small , 5.5 between 6.7 = medium ,grater 6.7 5 = large 
iris['Sepal.Length'].value_counts()  

#discretization for iris['Sepal.Width']

plt.hist(iris['Sepal.Width']) #histogram
iris['Sepal.Width'].unique() 
iris['Sepal.Width']= pd.cut(iris['Sepal.Width'],bins=[0, 2.7 ,3.5 ,4.5],labels=['small','medium','large'])
# size under 2.7 = small , 2.7 between 3.5 = medium ,grater than 3.5 = large 
iris['Sepal.Width'].value_counts()  


#discretization for iris Petal.Length column

#check for distribution 
plt.hist(iris["Petal.Length"])
iris['Petal.Length'].unique()
iris['Petal.Length']= pd.cut(iris['Petal.Length'],bins=[0,2.5,5,7],labels=['small','medium','large'])
# size under 2.5 = small , 2.5 between 5 = medium ,grater than 5 = large 
iris['Petal.Length'].value_counts()

#disretization for iris Petal.Width 

#check for distribution 
plt.hist(iris['Petal.Width'])
iris['Petal.Width'].unique()
iris['Petal.Width'].value_counts()
iris['Petal.Width']=pd.cut(iris['Petal.Width'],bins=[0,0.9,1.8,2.5],labels=('small','medium','large'))
# size under 0.9 = small , 0.9 between 1.8 = medium ,grater than 1.8 = large 
iris['Petal.Width'].value_counts()


