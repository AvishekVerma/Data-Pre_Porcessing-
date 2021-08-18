################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


#----------------------------- 5.STANDARDIZATION & NORMALIZATION ------------------------------#


#Data is one of the most important assets. It is often common that data is stored in distinct systems
#with different formats and scales. These seemingly small differences in how the data is stored can 
#result in misinterpretations and inconsistencies in your analytics. Inconsistency can make it 
#impossible to deliver reliable information to management for good decision making. We have the
#pre processing techniques to make the data uniform. Explore the various techniques to have reliable
#uniform standard data, you can go through this link:

import pandas as pd

#loading data set
seed = pd.read_csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/Seeds_data.csv")

seed.info()   #For data types and non or null values
# data has no na or nall values 

seed.describe() # for mean ,min, max, IQR 

EDA=pd.DataFrame({"columns_name ":seed.columns,
                  "mean":seed.mean(),
                  "median":seed.median(),
                  "mode":seed.mode(),
                  "standard_deviation":seed.std(),
                  "variance":seed.var(),
                  "skewness":seed.skew(),
                  "kurtosis":seed.kurt()})
EDA            

import matplotlib.pyplot as plt # for data visualization 
# let's find outliers in seed
#boxplot for every column
for column in seed:
    plt.figure()
    seed.boxplot([column])

seed.columns
boxplot = seed.boxplot(column= ['Area', 'Perimeter ', 'Compactness', 'length', 'Width',
       'Assymetry_coeff', 'len_ker_grove', 'Type'])

# Standardization function using z std. all are continuous data.
def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)

# Standardization data frame (considering the numerical part of data)
seed_norm = norm_func(seed.iloc[:,0:7])
seed_norm.describe()


