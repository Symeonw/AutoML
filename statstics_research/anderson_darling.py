import pandas as pd

df = pd.read_csv("test_data/IBM_Data.csv")

from scipy.stats import anderson
from scipy.stats import shapiro
from statsmodels.stats.diagnostic import lilliefors
from math import sqrt


anderson_statistic_30 = []
anderson_critical_30 = []
anderson_critical_30.append(anderson(df.Age.sample(30))[1][4])
for i in range(1,1000):
    anderson_statistic_30.append(anderson(df.Age.sample(30))[0])



anderson_statistic_50 = []
anderson_critical_50 = []
anderson_critical_50.append(anderson(df.Age.sample(50))[1][4])
for i in range(1,1000):
    anderson_statistic_50.append(anderson(df.Age.sample(50))[0])





anderson_statistic_100 = []
anderson_critical_100 = []
anderson_critical_100.append(anderson(df.Age.sample(100))[1][4])
for i in range(1,1000):
    anderson_statistic_100.append(anderson(df.Age.sample(100))[0])


anderson_statistic_150 = []
anderson_critical_150 = []
anderson_critical_150.append(anderson(df.Age.sample(150))[1][4])
for i in range(1,1000):
    anderson_statistic_150.append(anderson(df.Age.sample(150))[0])




anderson_statistic_200 = []
anderson_critical_200 = []
anderson_critical_200.append(anderson(df.Age.sample(200))[1][4])
for i in range(1,1000):
    anderson_statistic_200.append(anderson(df.Age.sample(200))[0])





anderson_statistic_500 = []
anderson_critical_500 = []
anderson_critical_500.append(anderson(df.Age.sample(500))[1][4])
for i in range(1,1000):
    anderson_statistic_500.append(anderson(df.Age.sample(500))[0])
    


sns.distplot(anderson_statistic_30)
plt.axvline(anderson_critical_30)
sns.distplot(anderson_statistic_50)
plt.axvline(anderson_critical_50)
sns.distplot(anderson_statistic_100)
plt.axvline(anderson_critical_100)
sns.distplot(anderson_statistic_150)
plt.axvline(anderson_critical_150)
sns.distplot(anderson_statistic_200)
plt.axvline(anderson_critical_200)
sns.distplot(anderson_statistic_500)
plt.axvline(anderson_critical_500)
plt.title("Normal Distribution")