#GDP spending data to be used here.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("net_national_income.csv", sep=',')
df_USA = df[df['LOCATION'] == "USA"]
print(df_USA)
df_USA = df_USA[['TIME','Value','SUBJECT','MEASURE']][df_USA['TIME'].isin(['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990',
       '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001',
       '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
       '2013', '2014', '2015', '2016', '2017', '2018'])]

unique_Subject = [df_USA['SUBJECT'].unique()]
#print(unique_Subject)

df_USA_TOT = df_USA[['TIME','Value','SUBJECT','MEASURE']][df_USA['SUBJECT'].isin(['TOT'])]
print(df_USA_TOT)

plt.plot(df_USA_TOT['TIME'],df_USA_TOT['Value'],'g.-')
plt.xticks(df_USA_TOT['TIME'],df_USA_TOT['TIME'],rotation=45,fontsize=7)
plt.yticks(fontsize=8)
plt.title("National income pattern since 1980")
plt.xlabel("YEARS")
plt.ylabel("National income")
plt.legend(['National income'],loc='best')
plt.show()