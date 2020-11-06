

# SF Salaries 





import pandas as pd





sal = pd.read_csv("Salaries.csv")





sal.head()


#  .info() method to find out how many entries there are



sal.info()


# The average BasePay 




sal['BasePay'].mean()


# The highest amount of OvertimePay 



sal['OvertimePay'].max()


# job title of  JOSEPH DRISCOLL ? 


sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']






sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**


s=sal['TotalPayBenefits'].max()
s
sal[sal['TotalPayBenefits']==s]['EmployeeName']


#  name of lowest paid person (including benefits)?


s=sal['TotalPayBenefits'].min()
sal[sal['TotalPayBenefits']==s]['EmployeeName']


# average (mean) BasePay of all employees per year


sal.groupby('Year').mean()['BasePay']


# No. of unique job titles 


sal['JobTitle'].nunique()


#  top 5 most common jobs


sal['JobTitle'].value_counts().head()


# No. of Job Titles were represented by only one person in 2013? 


sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)


# No. of people have the word Chief in their job title? 


def find(s):
    if("chief" in s.lower().split()):
        return True
    else:
        return False
sum(sal['JobTitle'].apply(lambda x: find(xsal['title_len']=sal['JobTitle'].apply(len)
sal[['TotalPayBenefits','title_len']].corr()





sal[['TotalPayBenefits','BasePay','OvertimePay']].corr()



