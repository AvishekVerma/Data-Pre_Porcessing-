2 + 2 # Function F9
# works as calculator

# Python Libraries (Packages)
# pip install <package name> - To install library (package), execute the code in Command prompt
# pip install pandas

import pandas as pd

# Read data into Python
education = pd.read_csv("C:/Data/education.csv")

# C:\Users\education.csv - this is windows default file path with a '\'
# C:\\Users\\education.csv - change it to '\\' to make it work in Python

#Exploratory Data Analysis
#Measures of Central Tendency / First moment business decision
education.workex.mean() # '.' is used to refer to the variables within object
education.workex.median()
education.workex.mode()

from scipy import stats
stats.mode(education.workex)

# Measures of Dispersion / Second moment business decision
education.workex.var() # variance
education.workex.std() #standard deviation
range = max(education.workex) - min(education.workex) # range
range

# Third moment business decision
education.workex.skew()

#Fourth moment business decision
education.workex.kurt()

#Graphical Representation
import matplotlib.pyplot as plt # mostly used for visualization purposes 
import numpy as np

plt.bar(height = education.gmat, x = np.arange(1,774,1)) # initializing the parameter

plt.hist(education.gmat) #histogram

plt.boxplot(education.gmat) #boxplot


#Normal Quantile-Quantile Plot
import scipy.stats as stats
import pylab

# Checking Whether data is normally distributed
stats.probplot(education.gmat, dist="norm",plot=pylab)

stats.probplot(education.workex,dist="norm",plot=pylab)

#transformation to make workex variable normal
import numpy as np
stats.probplot(np.log(education.workex),dist="norm",plot=pylab)

# z-distribution
# cdf => cumulative distributive function; # similar to pnorm in R
stats.norm.cdf(740,711,29)  # given a value, find the probability

# ppf => Percent point function; # similar to qnorm in R
stats.norm.ppf(0.975,0,1) # given probability, find the Z value

#t-distribution
stats.t.cdf(1.98,139) # given a value, find the probability; # similar to pt in R
stats.t.ppf(0.975, 139) # given probability, find the t value; # similar to qt in R


##############################################################
###### Data Preprocessing########################################

## import packages
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns

##################  creating Dummy variables using dummies ###############
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# we use ethinc diversity dataset  for this
df = pd.read_csv("C:/Users/abdul/Downloads/ethnic diversity.csv")


df.columns
# drop emp_name column
df.drop(['Employee_Name','EmpID','Zip'],axis =1,inplace =True)
df.dtypes


######################################
# Create dummy variables on categorcal columns

df_new = pd.get_dummies(df)



### we have created dummies for all categorical columns

#######lets us see using one hot encoding works

df1 = pd.read_csv("C:/Users/abdul/Downloads/ethnic diversity.csv")
df1.drop(['Employee_Name', 'EmpID','Zip'], axis =1, inplace =True)
from sklearn.preprocessing import OneHotEncoder
# creating instance of one-hot-encoder
enc = OneHotEncoder(handle_unknown='ignore')

enc_df = pd.DataFrame(enc.fit_transform(df1).toarray())

############################################################
########/\/\/\/\/\/\\\/\/\/\//\/\\/\\\/\/\/\/\\\####################

df2 = pd.read_csv('C:/Users/abdul/Downloads/ethnic diversity.csv')
df2.drop(['Employee_Name', 'EmpID','Zip'], axis =1, inplace =True)


from sklearn.preprocessing import LabelEncoder
# creating instance of labelencoder
labelencoder = LabelEncoder()
X = df2.iloc[:, 0:9]
y = df2['Race']

df2.columns

X['Sex']= labelencoder.fit_transform(X['Sex'])
X['MaritalDesc'] = labelencoder.fit_transform(X['MaritalDesc'])
X['CitizenDesc'] = labelencoder.fit_transform(X['CitizenDesc'])


########## label encode y

y = labelencoder.fit_transform(y)
y = pd.DataFrame(y)

### we have to convert y to data frame so that we can use concatenate function

# concatenate X and y

df_new = pd.concat([X, y], axis =1)
## rename column name
df_new.columns
df_new = df_new.rename(columns={0:'Type'})
#################################################################################


import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns

## load data set

ethnic= pd.read_csv("C:/Users/abdul/Downloads/ethnic diversity.csv")

ethnic.columns


ethnic.isna().sum()
ethnic.isnull().sum()


# Normalization function using z std. all are continuous data.
def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(ethnic.iloc[:,10:12])
df_norm.describe()

##################################################################################
###################### Outlier Treatment ###################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/abdul/Downloads/ethnic diversity.csv") # for doing modifications
df.dtypes
df.isna().sum()

# let's find outliers in RM
sns.boxplot(df.Salaries);plt.title('Boxplot');plt.show() #

sns.boxplot(df.age);plt.title('Boxplot');plt.show() #


# Detection of outliers (find limits for RM based on IQR)
IQR = df['Salaries'].quantile(0.75) - df['Salaries'].quantile(0.25)
lower_limit = df['Salaries'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['Salaries'].quantile(0.75) + (IQR * 1.5)



############### 1. Remove (let's trimm the dataset) ################
# Trimming Technique
# let's flag the outliers in the data set
outliers_df = np.where(df['Salaries'] > upper_limit, True, np.where(df['Salaries'] < lower_limit, True, False))
df_trimmed = df.loc[~(outliers_df), ]
df.shape, df_trimmed.shape

# let's explore outliers in the trimmed dataset
sns.boxplot(df_trimmed.Salaries);plt.title('Boxplot');plt.show()

#we see no outiers


####################### 2.Replace ############################
# Now let's replace the outliers by the maximum and minimum limit
df['df_replaced']= pd.DataFrame(np.where(df['Salaries'] > upper_limit, upper_limit, 
                                         np.where(df['Salaries'] < lower_limit, lower_limit, df['Salaries'])))
sns.boxplot(df.df_replaced);plt.title('Boxplot');plt.show()

###################### 3. Winsorization #####################################
from feature_engine.outlier_removers import Winsorizer
windsoriser = Winsorizer(distribution='skewed', # choose skewed for IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['Salaries'])
df_t = windsoriser.fit_transform(df[['Salaries']])

# we can inspect the minimum caps and maximum caps 
windsoriser.left_tail_caps_, windsoriser.right_tail_caps_

# lets see boxplot
sns.boxplot(df_t.Salaries);plt.title('Boxplot');plt.show()
###################################################################################
#################### Missing Values Imputation ##################################
import numpy as np
import pandas as pd

# load the dataset
# use modified ethnic dataset
df_raw = pd.read_csv('C:/Users/abdul/Downloads/modifiedethnic diversity.csv') # raw data without doing any modifications
df = pd.read_csv('C:/Users/abdul/Downloads/modifiedethnic diversity.csv') # for doing modifications

# check for count of NA'sin each column
df.isna().sum()

# There are 3 columns that have missing data ---Create an imputer object that fills 'Nan' values of SEX,MaritalDesc,Salaries
# Mean and Median imputer are used for numeric data (Salaries)
# mode is used for discrete data (SEX,MaritalDesc) 

# for Mean,Meadian,Mode imputation we can use Simple Imputer or df.fillna()
from sklearn.impute import SimpleImputer

# Mean Imputer 
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df["Salaries"] = pd.DataFrame(mean_imputer.fit_transform(df[["Salaries"]]))
df["Salaries"].isnull().sum()  # all 2 records replaced by mean 

# Median Imputer
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
df["Salaries"] = pd.DataFrame(median_imputer.fit_transform(df[["Salaries"]]))
df["Salaries"].isnull().sum()  # all 2 records replaced by median 

# Mode Imputer
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
df["Sex"] = pd.DataFrame(mode_imputer.fit_transform(df[["Sex"]]))
df["MaritalDesc"] = pd.DataFrame(mode_imputer.fit_transform(df[["MaritalDesc"]]))
df.isnull().sum()  # all SEX,MaritalDesc,Salaries records replaced by mode

##############################################################################
################## Type casting###############################################
import pandas as pd

data = pd.read_csv("C:/Users/abdul/Downloads/ethnic diversity.csv")
data.dtypes

#type casting
# Now we will convert 'float64' into 'int64' type. 
data.Salaries = data.Salaries.astype('int64') 
data.dtypes


#Identify duplicates records in the data
duplicate = data.duplicated()
sum(duplicate)

#Removing Duplicates
data1 = data.drop_duplicates() 

##############################################################################
#################### String manipulation ######################################

word = "Keep Adapting"
print(word)

#Accessing

word = "Keep Adapting"
letter=word[0]

print(letter)

#length 
word = "Keep Adapting"

len(word)

#finding

word = "Keep Adapting"
print(word.count('p')) # count how many times p is in the string
print(word.find("t")) # find the word t in the string
print(word.index("Adapting")) # find the letters Adapting in the string

s = "The world won't care about your self-esteem. The world will expect you to accomplish something BEFORE you feel good about yourself."

print(s.count(' '))

#Slicing

word1 = "_$_the internet frees us from the responsibility of having to retain anything in our long-term memory@_."

print (word1[0]) #get one char of the word
print (word1[0:1]) #get one char of the word (same as above)
print (word1[0:3]) #get the first three char
print (word1[:3]) #get the first three char
print (word1[-3:]) #get the last three char
print (word1[3:]) #get all but the three first char
print (word1[:-3]) #get all but the three last character
print (word1[3:-3]) #get all 


# spliting

word3 = 'Good health is not something we can buy. However, it can be an extremely valuable savings account.'

word3.split(' ') # Split on whitespace
['Good','health','is','not','something','we','can','buy.','However,','it','can','be','an','extremely','valuable','savings','account.']

# Startswith / Endswith
word3 = 'Remain calm, because peace equals power.'
word3.startswith("R")
word3.endswith("d")
word3.endswith("c")

# repeat string 

print( " & "* 108 )# prints ten dots


# replacing

word4 = "Live Happily"

word4.replace("Live", "Lead Life")



# Reversing
string = "eert a tsniaga pu mih deit yehT .meht htiw noil eht koot dna tserof eht otni emac sretnuh wef a ,yad enO "

print (''.join(reversed(string)))

#Strip
#Python strings have the strip(), lstrip(), rstrip() methods for removing
#any character from both ends of a string.

#If the characters to be removed are not specified then white-space will be removed




