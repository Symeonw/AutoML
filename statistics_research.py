import pandas as pd

df = pd.read_csv("test_data/IBM_Data.csv")

from scipy.stats import anderson
from scipy.stats import shapiro
from statsmodels.stats.diagnostic import lilliefors
from math import sqrt

a = anderson(df.Age, dist="norm")
a[1]
a[2]/100
t = df.Age.sample(100)
x = anderson(t)

print(x[0])
print(x[1])
print(x[2]/100)

y[1]

df40 = df[df.Age > 35]
df40.Age.sample(50).hist()
y = anderson(df40.Age.sample(30))

print(y[0])
print(y[1])
print(y[2]/100)

shapiro(df.Age)
shapiro(df.Age.sample(50))
shapiro(df40.Age)

lilliefors(df.Age)
lilliefors(df.Age.sample(50))
lilliefors(df40.Age)
lilliefors(df40.Age.sample(50))



#Min/Max value testing
anderson_statistic = []
anderson_statistic
for i in range(1,100):
    anderson_statistic.append(anderson(df40.Age.sample(30))[0])