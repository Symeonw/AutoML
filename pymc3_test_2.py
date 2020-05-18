import pandas as pd
import pymc3 as pm

df = pd.read_csv("test_data/IBM_Data.csv")

X = df[df.Attrition == "Yes"].Age
Y = df[df.Attrition == "No"].Age
y1 = np.array(X)
y2 = np.array(Y)
y = pd.DataFrame(dict(value=np.r_[y1, y2], group=np.r_[['X']*len(X), ['Y']*len(Y)]))
y.hist('value', by='group', figsize=(12, 4))

mean_prior_mean = y.value.mean()
mean_prior_std = y.value.std() * 2

std_prior_mean = y.value.std()


with pm.Model() as model:
    group1_mean = pm.Normal('group1_mean', mean_prior_mean, sd=mean_prior_std)
    group2_mean = pm.Normal('group2_mean', mean_prior_mean, sd=mean_prior_std)

with pm.Model() as model:
    group1_std = pm.Normal('group1_std', std_prior_mean, sd=std_prior_std)
    group2_std = pm.Normal('group2_std', std_prior_mean, sd=std_prior_std)