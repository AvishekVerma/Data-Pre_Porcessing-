################################## Data Pre-Processing ###############################


#Name: Avishek kumar verma
#Batch Id: 05012021_10A.M


#-------------------------------- 1.Outlier Treatments ------------------------------#

#Most of the datasets have extreme values or exceptions in their observations. These 
#values affect the predictions (Accuracy) of the model in one way or the other, removing
#these values is not a very good option. For these types of scenarios, we have the
#techniques for treating such values. Explore on various other techniques to treat 
#these values, you can go through this link:

import pandas as pd

#loding the data frame
boston=pd.read_csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/boston_data.csv")

boston.info()   #For data types and non or null values
# data has no na or nall values 

boston.describe() # for mean ,min, max, IQR 

EDA=pd.DataFrame({"columns_name ":boston.columns,
                  "mean":boston.mean(),
                  "median":boston.median(),
                  "mode":boston.mode(),
                  "standard_deviation":boston.std(),
                  "variance":boston.var(),
                  "skewness":boston.skew(),
                  "kurtosis":boston.kurt()})

EDA            

# Scatter plot between the variables along with histograms
import seaborn as sns
sns.pairplot(boston.iloc[:, :])

import matplotlib.pyplot as plt # for data visualization 
import numpy as np

# let's find outliers in boston
#boxplot for every column
for column in boston:
    plt.figure()
    boston.boxplot([column])

boxplot = boston.boxplot(column=[ 'crim','zn', 'indus',  'chas', 'nox',
                'rm', 'age', 'dis','rad', 'tax' ,'ptratio', 'black',
            'lstat','medv'])

# from all thies boxplot we can see that column 'crim','zn','rm', 'dis','black','lstat','medv' has some outlier 

#For "rm" column HVO and LVO finding and replacing

# Detection of outliers for rad column(find limits for RM based on IQR)

rm_IQR = boston['rm'].quantile(0.75) - boston['rm'].quantile(0.25)
rm_lower_limit = boston['rm'].quantile(0.25) - (rm_IQR * 1.5)
rm_upper_limit = boston['rm'].quantile(0.75) + (rm_IQR * 1.5)

####################### Replace ############################

# Now let's replace the outliers by the maximum and minimum limit
boston['rm_replaced'] = pd.DataFrame(np.where(boston['rm'] > rm_upper_limit, rm_upper_limit, 
                                         np.where(boston['rm'] < rm_lower_limit, rm_lower_limit, boston['rm'])))
sns.boxplot(boston.boston_replaced)
plt.title('Boxplot')
plt.show()

#For "crim" column HVO  finding and replacing 

# Detection of outliers (find limits for RM based on IQR)
crim_IQR = boston['crim'].quantile(0.75) - boston['crim'].quantile(0.25)
crim_upper_limit = boston['crim'].quantile(0.75) + (crim_IQR * 1.5)

# Now let's replace the outliers by the maximum and minimum limit
boston['crim_replaced']= pd.DataFrame(np.where(boston['crim'] > crim_upper_limit, crim_upper_limit ,  boston['crim']))
sns.boxplot(boston.crim_replaced)
plt.title('Boxplot')
plt.show()

#For "zn" column HVO  finding and replacing 
zn_IQR = boston['zn'].quantile(0.75)-boston['zn'].quantile(0.25)
zn_up_lm = boston['zn'].quantile(0.75)+(zn_IQR*1.5)
#replacling with upper limit 
boston['zn_replaced'] = pd.DataFrame(np.where(boston['zn'] > zn_up_lm,zn_up_lm, boston['zn']))
sns.boxplot(boston.zn_replaced)
plt.title('Boxplot')
plt.show()

#for "dis" column HVO  finding and replacing 
dis_IQR = boston['dis'].quantile(0.75)-boston['dis'].quantile(0.25)
dis_up_lm = boston['dis'].quantile(0.75)+(dis_IQR*1.5)
#replacling with upper limit 
boston['dis_replaced'] = pd.DataFrame(np.where(boston['dis'] > dis_up_lm,dis_up_lm,boston['dis']))
sns.boxplot(boston.dis_replaced)
plt.title('Boxplot')
plt.show()

#for "medv" column HVO  finding and replacing 
medv_IQR = boston['medv'].quantile(0.75)-boston['medv'].quantile(0.25)
medv_up_lm = boston['medv'].quantile(0.75)+(medv_IQR*1.5)

boston['medv_replaced'] = pd.DataFrame(np.where(boston['medv'] > medv_up_lm,medv_up_lm,boston['medv']))
sns.boxplot(boston['medv_replaced'])
plt.title('Boxplot')
plt.show()

#for "ptratio" column LVO  finding and replacing
ptr_IQR = boston['ptratio'].quantile(0.75)-boston['ptratio'].quantile(0.25)
ptr_lo_lm = boston['ptratio'].quantile(0.25)  - (ptr_IQR*1.5)
#replacing with lv
boston['ptratio_replaced'] = pd.DataFrame(np.where(boston['ptratio'] < ptr_lo_lm,ptr_lo_lm,boston['ptratio']))
sns.boxplot(boston['ptratio_replaced'])
plt.title('Boxplot')
plt.show()

#for "black  " column LVO  finding and replacing

bla_IQR = boston['black'].quantile(0.75)-boston['black'].quantile(0.25)
bla_lo_lm =  boston['black'].quantile(0.25)  - (bla_IQR*1.5)
#replacing with lv
boston['black_replaced']=pd.DataFrame(np.where(boston['black'] < bla_lo_lm,bla_lo_lm,boston['black']))
sns.boxplot(boston['black_replaced'])
plt.title('Boxplot')
plt.show()



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


#------------------------------------- 6.Zero - Variance Features ---------------------------------------#


#Find which columns of the given dataset with zero variance, explore various techniques used to remove the
#zero variance from the dataset to perform certain analysis. 

import pandas as pd 

#loading data set
z = pd.read_csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/Z_dataset.csv")
 #150*6

#id column is nothing but index 
#droping id columns 
z.drop(z.columns[0], axis = 1, inplace = True) 

z.info()   #For data types and non or null values
# data has no na or nall values 

z.describe() # for mean ,min, max, IQR 

#Graphical Representation
import matplotlib.pyplot as plt
#histogram for square.length
plt.hist(z['square.length']) #histogram

#histogram for 'square.breadth'
plt.hist(z['square.breadth']) #histogram

#histogram for'rec.Length'
plt.hist(z['rec.Length']) #histogram

#histogram for 'rec.breadth'
plt.hist(z['rec.breadth']) #histogram

#histogram for 'colour'
plt.hist(z['colour']) #histogram

# let's find outliers in z
#boxplot for every column
z.columns
boxplot = z.boxplot(column= ['square.length', 'square.breadth', 'rec.Length', 'rec.breadth'])
# square.breadth have some outlier 

# get number of unique values for each column
counts = z.nunique()
counts

#variance for every column
z.var()

#'square.breadth'variance =0.1  
#indicates that all the data values are identical.
#droping square.breadth columns 
z.drop(["square.breadth"], axis = 1, inplace = True) 




#------------------------------------- 7.STRING MANIPULATIONS ---------------------------------------#


#It is obvious that as part of data analysis we encounter a lot of text data which is a
#collection of strings which in turn is a sequence of characters. Access the text data and
#manipulate as per our requirements. you can go through this link for further assistance:

###########  Q1

word ="Grow Gratitude"

# a)	How do you access the letter “G” of “Growth”?

print(word[0])


#b)	How do you find the length of the string?
 
len(word)


#c)	Count how many times “G” is in the string.

print(word.count('G')) 


###########   Q2

"""
2.	Create a string “Being aware of a single shortcoming within yourself is
 far more useful than being aware of a thousand in someone else.”
Code for the following
a)	Count the number of characters in the string.
"""

sentence_2 = 'Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.'

sentence_2

print(sentence_2.count(' '))


"""
3.	Create a string "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
Code for the following tasks:
a)	get one char of the word
b)	get the first three char
c)	get the last three char """



sentence_3 =  "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"

##  a)	get one char of the word
print (sentence_3[0])


#b)	get the first three char

print (sentence_3[0:3])


#   c)	get the last three char 

print (sentence_3[-3:])


"""4.	create a string "stay positive and optimistic". Now write a code to split on whitespace.
Write a code to find if:
a)	The string starts with “H”
b)	The string ends with “d”
c)	The string ends with “c”
"""

sentence_4 ='stay positive and optimistic.' 
#Now write a code to split on whitespace.'

sentence_4.split(' ') # Split on whitespace

#a)	The string starts with “H”

sentence_4.startswith("H")


##b)	The string ends with “d”
sentence_4.endswith("d")

##c)	The string ends with “c”

sentence_4.endswith("c")



"""5.	Write a code to print " 🪐 " one hundred and eight times. (only in python)"""

print( " 🪐 "* 108 )


"""7.	Create a string “Grow Gratitude” and write a code to replace “Grow” with “Growth of”"""

sentence_7 ='Grow Gratitude'


sentence_7.replace("Grow", "Growth of " )

"""8.	A story was printed in a pdf, which isn’t making any sense. i.e.:
“.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A”
You have noticed that the story is printed in a reversed order. Rectify the same and write a code to print the same story in a correct order.
"""

story = '.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A'


print (''.join(reversed(story)))



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



#------------------------------------- 9.Duplication Typecasting ---------------------------------------#

#Q1. For the given dataset perform the type casting (convert the datatypes, ex. float to int)
#Q2. Check for the duplicate values, and handle the duplicate values (ex. drop)
#Q3. Do the data analysis (EDA)?
#   Such as histogram, boxplot, scatterplot etc

import pandas as pd 

retail = pd.read_csv("C:/Users/admin/Desktop/D.S-360/5.Data Pre-processing/DataSets/OnlineRetail.csv",header= 0, encoding= 'unicode_escape')

retail.info()   #For data types and non or null values
# data has no na or nall values 

retail.describe() # for mean ,min, max, IQR 

# check for count of NA'sin each column
retail.isna().sum()
retail.isnull().sum()

# for Mean,Meadian,Mode imputation we can use Simple Imputer or df.fillna()
from sklearn.impute import SimpleImputer
import numpy as np
# Mode Imputer
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
retail["CustomerID"] = pd.DataFrame(mode_imputer.fit_transform(retail[["CustomerID"]]))
retail["Description"] = pd.DataFrame(mode_imputer.fit_transform(retail[["Description"]]))

retail.isnull().sum() 

retail.dtypes

#type casting
# Now we will convert 'float64' into 'int64' type. 

retail.UnitPrice = retail.UnitPrice.astype('int64')

retail.CustomerID = retail.CustomerID.astype('int64')

retail.dtypes
retail.nunique()

#Identify duplicates records in the data
duplicate = retail.duplicated()
sum(duplicate)

#Removing Duplicates
retail1 = retail.drop_duplicates() 

retail1.dtypes
retail1.dtypes
retail1.nunique()
 
# EDA     

#1st moment of business decision 
#measure  of central tendency
#mean
retail1.Quantity.mean()
retail1.UnitPrice.mean()
#median
retail1.Quantity.median()
retail1.UnitPrice.median()

#2nd moment of business decision
#measure of dispersion

#variance
retail1.Quantity.var()
retail1.UnitPrice.var()
#standard deviation 
retail1.Quantity.std()
retail1.UnitPrice.std()
#Range 
range_Quantity = max(retail1.Quantity) - min(retail1.Quantity) 
range_Quantity

range_UnitPrice = max(retail1.UnitPrice)-min(retail1.UnitPrice)
range_UnitPrice


#3rd moment of business decision #skewness

retail1.Quantity.skew()
retail1.UnitPrice.skew()

#4th moment of business decision #kurtosis peakness of dataset 

retail1.Quantity.kurt()
retail1.UnitPrice.kurt() 
      
retail1.dtypes

retail.columns

boxplot = retail1.boxplot(column= [ 'Quantity','UnitPrice', 'CustomerID'])

# Scatter plot between the variables along with histograms
import seaborn as sns
sns.pairplot(retail1.iloc[:, :])
