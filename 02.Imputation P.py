################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


#------------------------------------- 2.Imputation ---------------------------------------#


#Majority of the datasets have missing values, that might be because the data collected were
##to build the proper model or in other words, get accurate results. The common techniques are
#either removing those records completely or substitute those missing values with the logical
#ones, there are various techniques to treat these types of problems.

import pandas as pd

#loding the data frame
claim=pd.read_csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/claimants.csv")

claim.info()   #For data types and non or null values
# data has no na or nall values 

claim.describe() # for mean ,min, max, IQR 

claim.shape
#claim.shape (1340, 7)

#checking for minnsing value
claim.isnull().sum()
claim.isna().sum()

claim.dtypes
claim.CLMAGE.unique()

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# let's find outliers in clmage
sns.boxplot(claim.CLMAGE);plt.title('Boxplot');plt.show() # we have some HVoutlier 

#missing value imputations

from sklearn.impute import SimpleImputer
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

# Mode Imputer for CLMSEX
claim["CLMSEX"] = pd.DataFrame(mode_imputer.fit_transform(claim[["CLMSEX"]]))

# Mode Imputer for  CLMINSUR
claim["CLMINSUR"] = pd.DataFrame(mode_imputer.fit_transform(claim[["CLMINSUR"]]))

# Mode Imputer for SEATBELT
claim["SEATBELT"] = pd.DataFrame(mode_imputer.fit_transform(claim[["SEATBELT"]]))

#median imputation for CLMAGE  
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
claim["CLMAGE"] = pd.DataFrame(median_imputer.fit_transform(claim[["CLMAGE"] ]))
claim["CLMAGE"] .isnull().sum()  # all 2 records replaced by median 

claim.isnull().sum() # no na value now

EDA=pd.DataFrame({"columns_name ":claim.columns,
                  "mean":claim.mean(),
                  "median":claim.median(),
                  "mode":claim.mode(),
                  "standard_deviation":claim.std(),
                  "variance":claim.var(),
                  "skewness":claim.skew(),
                  "kurtosis":claim.kurt()})


