#GDP spending data to be used here.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("GDP_data.csv", sep=',')
df_USA = df[df['LOCATION'] == "USA"]

df_USA = df_USA[['TIME','Value','SUBJECT','MEASURE']][df_USA['TIME'].isin(['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990',
       '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001',
       '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
       '2013', '2014', '2015', '2016', '2017', '2018'])]

df_USA_MLN_USD = df_USA[['TIME','Value','SUBJECT','MEASURE']][df_USA['MEASURE'].isin(['MLN_USD'])]

#GDP PER CAPITA
#df_USA_USD_CAP = df_USA[['TIME','Value','SUBJECT','MEASURE']][df_USA['MEASURE'].isin(['USD_CAP'])]

plt.plot(df_USA_MLN_USD['TIME'],df_USA_MLN_USD['Value'],'b.-')
plt.xticks(df_USA_MLN_USD['TIME'],df_USA_MLN_USD['TIME'],rotation=45,fontsize=7)
plt.yticks(fontsize=8)
plt.title("GDP in Million USD, pattern sice 1980")
plt.xlabel("YEARS")
plt.ylabel("GDP")
plt.legend(['GDP'],loc='lower right')

df = pd.read_csv("net_national_income.csv", sep=',')
df_USA = df[df['LOCATION'] == "USA"]
df_USA = df_USA[['TIME','Value','SUBJECT','MEASURE']][df_USA['TIME'].isin(['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990',
       '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001',
       '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
       '2013', '2014', '2015', '2016', '2017', '2018'])]

unique_Subject = [df_USA['SUBJECT'].unique()]
#print(unique_Subject)

df_USA_TOT = df_USA[['TIME','Value','SUBJECT','MEASURE']][df_USA['SUBJECT'].isin(['TOT'])]
df_USA_TOT = df_USA_TOT[['TIME','Value','SUBJECT','MEASURE']][df_USA['MEASURE'].isin(['MLN_USD'])]
print(df_USA_TOT)

plt.plot(df_USA_TOT['TIME'],df_USA_TOT['Value'],'g.-')
plt.xticks(df_USA_TOT['TIME'],df_USA_TOT['TIME'],rotation=45,fontsize=7)
plt.yticks(fontsize=8)
plt.title("National income and GDP pattern since 1980")
plt.xlabel("YEARS")
plt.ylabel("National income and GDP")
plt.legend(['National income','GDP in MLN_USD'],loc='best')
plt.show()

#GDP PER CAPITA plot
#plt.plot(df_USA_USD_CAP['TIME'],df_USA_USD_CAP['Value'],'r.:')
#plt.xticks(df_USA_USD_CAP['TIME'],df_USA_USD_CAP['TIME'],rotation=45,fontsize=7)
#plt.yticks(fontsize=8)
#plt.title("GDP per capita, pattern sice 1980")
#plt.xlabel("YEARS")
#plt.ylabel("GDP per capita")
#plt.legend(['GDP per capita'],loc='lower right')
#plt.show()