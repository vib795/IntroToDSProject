#Unemployment data to be used here. Can be merged with employment_data.py as the plots need to be part of the same figure.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('unemployment_data.csv', sep=',')
df2 = pd.read_csv('employment_data.csv', sep=',')

df_USA = df[df['LOCATION'] == 'USA']
years = [np.arange(start=1980, stop=2019, step=1)]

df_rate_and_years_USA = df_USA[['TIME','Value']][df_USA['TIME'].isin(['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990',
       '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001',
       '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
       '2013', '2014', '2015', '2016', '2017', '2018'])]
#print(df_rate_and_years_USA)

df2_USA = df2[df2['LOCATION'] == 'USA']
years2 = [np.arange(start=1980, stop=2019, step=1)]

df2_part1 = df2_USA[['TIME','Value','SUBJECT','MEASURE']][df2_USA['TIME'].isin(['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990',
       '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001',
       '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
       '2013', '2014', '2015', '2016', '2017', '2018'])]
df2_part2 = df2_part1[['TIME','Value','SUBJECT','MEASURE']][df2_part1['MEASURE'].isin(['THND_PER'])]
df2_rate_and_years_USA = df2_part2[['TIME','Value']][df2_part2["SUBJECT"].isin(['TOT'])]

df_PC_WKGPOP = df2_USA[['TIME','Value','SUBJECT','MEASURE']][df2_USA['TIME'].isin(['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990',
       '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001',
       '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
       '2013', '2014', '2015', '2016', '2017', '2018'])]
df_PC_WKGPOP = df2_part1[['TIME','Value','SUBJECT','MEASURE']][df2_part1['MEASURE'].isin(['PC_WKGPOP'])]
df_PC_WKGPOP_rate_and_years_USA = df2_part2[['TIME','Value']][df2_part2["SUBJECT"].isin(['TOT'])]

#plt.plot(df_rate_and_years_USA['TIME'],df_rate_and_years_USA['Value'],'b.-')
#plt.xticks(df_rate_and_years_USA['TIME'],df_rate_and_years_USA['TIME'],rotation=45,fontsize=7)
#plt.yticks(fontsize=8)
#plt.title("Unemployment pattern sice 1980")
#plt.xlabel("YEARS")
#plt.ylabel("UNEMPLOYMENT  RATES")
#plt.legend(['Unemployment Rate'],loc='lower left')
#plt.show()

#########################################################################################################
#EMPLOYMENT AGAINST GDP
#########################################################################################################

df = pd.read_csv("GDP_data.csv", sep=',')
df_USA = df[df['LOCATION'] == "USA"]

df_USA = df_USA[['TIME','Value','SUBJECT','MEASURE']][df_USA['TIME'].isin(['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990',
       '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001',
       '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
       '2013', '2014', '2015', '2016', '2017', '2018'])]

df_USA_MLN_USD = df_USA[['TIME','Value','SUBJECT','MEASURE']][df_USA['MEASURE'].isin(['MLN_USD'])]

#GDP PER CAPITA
#df_USA_USD_CAP = df_USA[['TIME','Value','SUBJECT','MEASURE']][df_USA['MEASURE'].isin(['USD_CAP'])]

#plt.plot(df_USA_MLN_USD['TIME'],df_USA_MLN_USD['Value'],'b.-')
#plt.xticks(df_USA_MLN_USD['TIME'],df_USA_MLN_USD['TIME'],rotation=45,fontsize=7)
#plt.yticks(fontsize=8)
#plt.title("GDP in Million USD, pattern sice 1980")
#plt.xlabel("YEARS")
#plt.ylabel("GDP")
#plt.legend(['GDP'],loc='lower right')

plt.plot(df_USA_MLN_USD['TIME'],df_USA_MLN_USD['Value'],'b.-')
plt.xticks(df_USA_MLN_USD['TIME'],df_USA_MLN_USD['TIME'],rotation=45,fontsize=7)
plt.yticks(fontsize=8)
plt.title("Employment and GDP pattern sice 1980")
plt.xlabel("YEARS")
plt.ylabel("EMPLOYMENT RATES AND GDP")
plt.legend(['GDP'],loc='lower right')
plt.show()
#########################################################################################################