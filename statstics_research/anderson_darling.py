from statsmodels.stats.diagnostic import lilliefors
from scipy.stats import kurtosis
from scipy.stats import probplot
from scipy.stats import anderson
from scipy.stats import shapiro
import matplotlib.pyplot as plt
from math import sqrt
import seaborn as sns
import pandas as pd
import numpy as np


df = pd.read_csv("test_data/IBM_Data.csv")
df40 = df[df.Age > 35]
df40inv = df[df.Age < 35]







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




from scipy.stats import gaussian_kde
xs = np.linspace(0,8,200)

# Anderson 30 sample size
density30 = gaussian_kde(anderson_statistic_30)
density30.covariance_factor = lambda : .35
density30._compute_covariance()


# Anderson 50 sample size
density50 = gaussian_kde(anderson_statistic_50)
density50.covariance_factor = lambda : .35
density50._compute_covariance()


# Anderson 100 sample size
density100 = gaussian_kde(anderson_statistic_100)
density100.covariance_factor = lambda : .35
density100._compute_covariance()

# Anderson 150 sample size
density150 = gaussian_kde(anderson_statistic_150)
density150.covariance_factor = lambda : .35
density150._compute_covariance()


# Anderson 200 sample size
density200 = gaussian_kde(anderson_statistic_200)
density200.covariance_factor = lambda : .35
density200._compute_covariance()

# Anderson 500 sample size
density500 = gaussian_kde(anderson_statistic_500)
density500.covariance_factor = lambda : .35
density500._compute_covariance()


plt.plot(xs,density30(xs))
plt.plot(xs,density50(xs))
plt.plot(xs,density100(xs))
plt.plot(xs,density150(xs))
plt.plot(xs,density200(xs))
plt.plot(xs,density500(xs))
plt.vlines(1,0,1.5)
plt.show()



# Testing Anderson-Darling test with non-normal distributed data

anderson_statistic_non_normal_30 = []
anderson_critical_non_normal_30 = []
anderson_critical_non_normal_30.append(anderson(df40.Age.sample(30))[1][4])
for i in range(1,1000):
    anderson_statistic_non_normal_30.append(anderson(df40.Age.sample(30))[0])



anderson_statistic_non_normal_50 = []
anderson_critical_non_normal_50 = []
anderson_critical_non_normal_50.append(anderson(df40.Age.sample(50))[1][4])
for i in range(1,1000):
    anderson_statistic_non_normal_50.append(anderson(df40.Age.sample(50))[0])

anderson_statistic_non_normal_100 = []
anderson_critical_non_normal_100 = []
anderson_critical_non_normal_100.append(anderson(df40.Age.sample(100))[1][4])
for i in range(1,1000):
    anderson_statistic_non_normal_100.append(anderson(df40.Age.sample(100))[0])


anderson_statistic_non_normal_150 = []
anderson_critical_non_normal_150 = []
anderson_critical_non_normal_150.append(anderson(df40.Age.sample(150))[1][4])
for i in range(1,1000):
    anderson_statistic_non_normal_150.append(anderson(df40.Age.sample(150))[0])




anderson_statistic_non_normal_200 = []
anderson_critical_non_normal_200 = []
anderson_critical_non_normal_200.append(anderson(df40.Age.sample(200))[1][4])
for i in range(1,1000):
    anderson_statistic_non_normal_200.append(anderson(df40.Age.sample(200))[0])





anderson_statistic_non_normal_500 = []
anderson_critical_non_normal_500 = []
anderson_critical_non_normal_500.append(anderson(df40.Age.sample(500))[1][4])
for i in range(1,1000):
    anderson_statistic_non_normal_500.append(anderson(df40.Age.sample(500))[0])
    


sns.distplot(anderson_statistic_non_normal_30)
plt.axvline(anderson_critical_non_normal_30)
sns.distplot(anderson_statistic_non_normal_50)
plt.axvline(anderson_critical_non_normal_50)
sns.distplot(anderson_statistic_non_normal_100)
plt.axvline(anderson_critical_non_normal_100)
sns.distplot(anderson_statistic_non_normal_150)
plt.axvline(anderson_critical_non_normal_150)
sns.distplot(anderson_statistic_non_normal_200)
plt.axvline(anderson_critical_non_normal_200)
sns.distplot(anderson_statistic_non_normal_500)
plt.axvline(anderson_critical_non_normal_500)
plt.title("Non-Normal Distribution")

anderson_30 = pd.DataFrame(anderson_statistic_30, columns=["test_stat"])
len(anderson_30[anderson_30.test_stat < anderson_critical_30[0]]) / len(anderson_30)

def test_anderson(dfi:pd.Series, dist_type:"1 == Normal, 0 == Non-Normal", sample_sizes = [30,50,100,150,200,500]):
    results = {}
    for ss in sample_sizes:
        anderson_statistic_list = []
        results.update({f"anderson_critical_{ss}":anderson(dfi.sample(ss))[1][4]})
        for i in range(1,1000):
            anderson_statistic_list.append(anderson(dfi.sample(ss))[0])
        results.update({f"anderson_statistic_{ss}":anderson_statistic_list})
    for ss in sample_sizes:
        sns.distplot(results[f"anderson_statistic_{ss}"])
        plt.axvline(results[f"anderson_critical_{ss}"])
        plt.title(f"Anderson-Darling Test Results")
    plt.show()
    sns.distplot(dfi)
    plt.title("Original Data Distribution")
    for ss in sample_sizes:
        data = results[f"anderson_statistic_{ss}"]
        critical = results[f"anderson_critical_{ss}"]
        data = pd.DataFrame(data, columns=["test_statistic"])
        if dist_type == 1:
            pct_critical = len(data[data.test_statistic > critical]) / len(data)
            print(f"Sample size {ss}: {pct_critical*100}% of data misclassified non-normal\r")
        if dist_type == 0:
            pct_critical = len(data[data.test_statistic < critical]) / len(data)
            print(f"Sample size {ss}: {pct_critical*100}% of data misclassified normal\r")




test_anderson(pd.Series(x),1)
test_anderson(df.Age,1)
test_anderson(df.DailyRate,0)
test_anderson(df40.Age,0)
test_anderson(df.DistanceFromHome,0)


df.columns


mu,sigma,n = 0.,1.,1000
x = np.random.normal(mu,sigma,n) 
sns.distplot(x)

