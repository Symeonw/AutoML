import pymc3 as pm
import pandas as pd
import numpy as np

df2 = pd.read_csv("test_data/IBM_Data.csv")

X = df2[df2.Attrition == "Yes"].DistanceFromHome
Y = df2[df2.Attrition == "No"].DistanceFromHome
y1 = np.array(X)
y2 = np.array(Y)
y = pd.DataFrame(dict(value=np.r_[y1, y2], group=np.r_[['X']*len(X), ['Y']*len(Y)]))
y.hist('value', by='group', figsize=(12, 4))

μ_m = y.value.mean()
μ_s = y.value.std() * 2

with pm.Model() as model:
    group1_mean = pm.Normal('group1_mean', mu=μ_m, sd=μ_s)
    group2_mean = pm.Normal('group2_mean', mu=μ_m, sd=μ_s)


σ_low = 1
σ_high = 10

with model:
    group1_std = pm.Uniform('group1_std', lower=σ_low, upper=σ_high)
    group2_std = pm.Uniform('group2_std', lower=σ_low, upper=σ_high)

with model:
    ν = pm.Exponential('ν_minus_one', 1/29.) + 1

pm.kdeplot(np.random.exponential(30, size=10000), fill_kwargs={'alpha': 0.5})

with model:
    λ1 = group1_std**-2
    λ2 = group2_std**-2

    group1 = pm.StudentT('drug', nu=ν, mu=group1_mean, lam=λ1, observed=y1)
    group2 = pm.StudentT('placebo', nu=ν, mu=group2_mean, lam=λ2, observed=y2)


with model:
    diff_of_means = pm.Deterministic('difference of means', group1_mean - group2_mean)
    diff_of_stds = pm.Deterministic('difference of stds', group1_std - group2_std)
    effect_size = pm.Deterministic('effect size',
                                   diff_of_means / np.sqrt((group1_std**2 + group2_std**2) / 2))

with model:
    trace = pm.sample(5000,  tune=2000, cores=1)

pm.plot_posterior(trace, var_names=['group1_mean','group2_mean', 'group1_std', 'group2_std', 'ν_minus_one'],
                  color='#87ceeb')


pm.plot_posterior(trace, var_names=['difference of means','difference of stds', 'effect size'],ref_val=0,color='#87ceeb')

import seaborn as sns

sns.catplot(x="NumCompaniesWorked",y="Attrition",data=df2, kind="violin")
df2.columns
