################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


#------------------------------------- 5.Dummy Variables ---------------------------------------#

#Data is one of the most important assets. It is often common that data is stored in distinct 
#systems with different formats and forms. Non-numeric form of data makes it tricky while developing
#mathematical equations for prediction models. We have the preprocessing techniques to make the data
#convert to numeric form. Explore the various techniques to have reliable uniform standard data, 
#you can go through this link:

import pandas as pd

#loading data set
ani = pd.read_csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/animal_category.csv")
 
#column Index has nothing important 
#removing Index 
# Remove three columns as index base 
ani.drop(ani.columns[0], axis = 1, inplace = True) #now shape is 30*4
 
ani.info()   #For data types and non or null values
# data has no na or nall values 

ani.describe() # for mean ,min, max, IQR 

#creating Dummy variables using dummies 
# Create dummy variables on categorcal columns

# 1 method
df_new = pd.get_dummies(ani)

#2 method
from sklearn.preprocessing import OneHotEncoder
# creating instance of one-hot-encoder
enc = OneHotEncoder(handle_unknown='ignore')

enc_ani = pd.DataFrame(enc.fit_transform(ani).toarray())

#we have created dummies for all categorical columns

#lets us see using one hot encoding works

#3 method

from sklearn.preprocessing import LabelEncoder
# creating instance of labelencoder
labelencoder = LabelEncoder()

ani.columns

ani['Animals']= labelencoder.fit_transform(ani['Animals'])
ani['Gender'] = labelencoder.fit_transform(ani['Gender'])
ani['Homly'] = labelencoder.fit_transform(ani['Homly'])
ani['Types'] = labelencoder.fit_transform(ani['Types'])

