import pandas as pd
ecom=pd.read_csv("Ecommerce Purchases")


ecom.head()


ecom.info()


# average Purchase Price



ecom['Purchase Price'].mean()


#  highest and lowest purchase prices




ecom['Purchase Price'].max()
ecom['Purchase Price'].min()


# No. of people who have English 'en' as their language of choice on the website

ecom[ecom['Language']=='en'].count()


# No. of people have the job title of "Lawyer" 



ecom[ecom['Job']=='Lawyer'].count()


# No. of people made the purchase during the AM and how many people made the purchase during PM 

ecom['AM or PM'].value_counts()


# 5 most common Job Titles

ecom['Job'].value_counts().head()



#  email of the person with the following Credit Card Number: 4926535242672853




ecom[ecom['Credit Card']==4926535242672853]['Email']


# No. of people have American Express as their Credit Card Provider *and* made a purchase above $95 



sum(ecom[ecom['CC Provider']=='American Express']['Purchase Price']>95)


# No. of people have a credit card that expires in 2025

def find(x):
    if str(x).split('/')[1]=='25':
        return True
    else:
        return False
sum(ecom['CC Exp Date'].apply(lambda x: find(x)))


# top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)



def find(x):
    return x.split('@')[1]
ecom['Email'].apply(lambda x: find(x)).value_counts().head()


