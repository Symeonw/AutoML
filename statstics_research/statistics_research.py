import pandas as pd


df = pd.read_csv("../test_data/IBM_Data.csv")


from scipy.stats import anderson
from scipy.stats import shapiro
from statsmodels.stats.diagnostic import lilliefors
from math import sqrt

a = anderson(df.Age, dist="norm")
a[1]
a[2]/100
t = df.Age.sample(150)
x = anderson(t)

print(x[0])
print(x[1])
print(x[2]/100)

y[1]

df40 = df[df.Age > 35]
df40.PercentSalaryHike.sample(50).hist()
y = anderson(df40.PercentSalaryHike.sample(30))

print(y[0])
print(y[1])
print(y[2]/100)

shapiro(df.Age)
shapiro(df.Age.sample(50))
shapiro(df40.PercentSalaryHike)

lilliefors(df.Age)
lilliefors(df.Age.sample(50))
lilliefors(df40.PercentSalaryHike)
lilliefors(df40.PercentSalaryHike.sample(50))



#Min/Max value testing on skewed dist - sampled
import seaborn as sns
from scipy.stats import probplot
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
anderson_statistic_30 = []
for i in range(1,1000):
    anderson_statistic_30.append(anderson(df40.PercentSalaryHike.sample(30))[0])

sns.distplot(anderson_statistic_30)


anderson_statistic_50 = []
for i in range(1,1000):
    anderson_statistic_50.append(anderson(df40.PercentSalaryHike.sample(50))[0])

sns.distplot(anderson_statistic_50)


anderson_statistic_100 = []
for i in range(1,1000):
    anderson_statistic_100.append(anderson(df40.PercentSalaryHike.sample(100))[0])

sns.distplot(anderson_statistic_100)

anderson_statistic_200 = []
for i in range(1,1000):
    anderson_statistic_200.append(anderson(df40.PercentSalaryHike.sample(200))[0])

sns.distplot(anderson_statistic_200)


anderson_statistic_500 = []
for i in range(1,1000):
    anderson_statistic_500.append(anderson(df40.PercentSalaryHike.sample(500))[0])

sns.distplot(anderson_statistic_500)

#Min/Max testing on normal dist - sampled

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


print(kurtosis(anderson_statistic_30))
print(kurtosis(anderson_statistic_50))
print(kurtosis(anderson_statistic_100))
print(kurtosis(anderson_statistic_200))
print(kurtosis(anderson_statistic_500))


sum(anderson_statistic_500)/1000
sum(anderson_statistic_100)/1000
sum(anderson_statistic_50)/1000




sns.distplot(df.Age)


# CDF TESTING
df.Age.hist(cumulative=True)
df.Age.describe()[1]

import numpy as np
from scipy.stats import norm
x = np.linespace(-5,5,5000)
cdf_graph = norm.cdf(x,df.Age.describe()[1], df.Age.describe()[2])

sns.lineplot(x, cdf_graph, label="cdf")

df2 = pd.DataFrame(df.Age.value_counts())
df2.reset_index(inplace=True)
df2.rename(columns={"index":"value", "Age":"frequency"}, inplace=True)
df2["pdf"] = df2.frequency / sum(df2.frequency)
df2["cdf"] = df2.pdf.cumsum()
 
norm_dist_cdf = norm.cdf(x,df.Age.describe()[1], df.Age.describe()[2])
len(norm_dist_cdf)
len(df2.cdf)
solution = np.abs(norm_dist_cdf - df2.cdf)


#----------------------------------------------------------------------------
# ANDERSON-DARLING TESTING

#Min/Max testing on normal dist - sampled

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