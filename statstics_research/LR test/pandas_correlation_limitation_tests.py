import pandas as pd
import seaborn as sns

def get_data():
    df = pd.read_csv("../../test_data/internet_usage.csv")
    df.columns = ["pid", "age", "income","gender", "house_number", "favorite_color", "height_inches","occupation", "reads_books", "internet_hours"]
    df.set_index("pid", inplace=True)
    df.replace(-1, pd.NA, inplace=True)
    df.replace("-1", pd.NA, inplace=True)
    df.gender = df.gender.str[:1]
    df["target"] = df.internet_hours.apply(lambda x: 1 if x > 3 else 0)
    df.drop(columns=["reads_books", "internet_hours"], inplace=True)
    return df


df = get_data()

df = df[["income", "age", "target", "occupation"]]

inage = df[["income", "age", "target"]].dropna()

sns.regplot(inage.age, inage.income)

inage.corr()

# Correlation at .38 with lots of noise, seems significant enough to keep

# Further Linear tests
df = pd.read_csv("../../test_data/LR_data.csv")
df.columns = ["id", "trans_date", "house_age", "distance", "conv_stores", "lat", "long", "price"]
df.drop(columns=["id", "lat", "long"], inplace=True)
sns.regplot(df.house_age, df.price)
sns.regplot(df.distance, df.price)
sns.regplot(df.conv_stores, df.price)
df.corr()

# Correlation at .21 still seems significant, further research required to determine min. 
from sklearn.datasets import load_iris
df = pd.DataFrame(load_iris().data)
df.columns = ["a", "b", "c", "d"]
df.corr()
sns.regplot(df.a, df.b)
sns.regplot(df.b, df.d, robust=True)

# Futher reseach has concluded a cuttof of .20 correlation is sufficent to cut out noise. 