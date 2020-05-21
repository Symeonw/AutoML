import pandas as pd
import os

file_path = "test_data/EC_dataset.csv"
def data_validation(file_path):
    
    if file_path.endswith(".csv"):
        print("here!")

    elif file_path.endswith(".xlsx"):
        print("here1!")

    else: 
        raise ValueError(f"{file_path[file_path.rindex('.'):]} file extentioon is not currently supported.")

    if os.stat(file_path).st_size/1000000000 > 5:
        raise ValueError("File sizes of over 4 Gigabytes are not currently supported.")

    df = pd.read_csv(file_path, encoding="unicode_escape")





data_validation(file_path)




tested = []
for col in df.columns:
    try:
        if df[col].str.isnumeric().all() == False:
            tested.append(1)
            continue
    except:
        pass

    try:
        if all(x.isdigit() for x in df[col]) == False:
            tested.append(1)
    except:
        tested.append(0)



user_column_input = [0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0]

count = 0
for x,y,z in zip(tested, user_column_input, df.columns):
    if x == y:
        print("Matched")
    else:
        print("Mislabeled", z, f"Labled {x} while column was {y}")
        count += 1
count
df = pd.read_csv("test_data/IBM_Data.csv")
df2 = df[["Education", "EnvironmentSatisfaction", "JobInvolvement", "JobLevel", "JobSatisfaction",\
     "PerformanceRating", "RelationshipSatisfaction", "StockOptionLevel","WorkLifeBalance", "Age", "DailyRate", "MonthlyRate", "DistanceFromHome",\
         "YearsWithCurrManager",  "YearsSinceLastPromotion", "YearsInCurrentRole", "YearsAtCompany", "TrainingTimesLastYear"]]


likely_cat = {}
for var in df2.columns:
    likely_cat[var] = 1.*df[var].nunique()/df[var].count() < 0.01 #or some other threshold
likely_cat


#_------------------------------------------------------------------------------------------------------

df = pd.read_csv("test_data/winequality-red.csv")




tested = [] 
for col in df.columns:
    try:
        if df[col].str.isnumeric().all() == False:
            tested.append(1)
            continue
        #Captures all data with letters
    except:
        pass

    try:
        if all(x.isdigit() for x in df[col]) == False:
            tested.append(1)
        #Captures all strings with only numbers
    except:
        if df[col].dtype == float:
            tested.append(0)
            continue
        #Captures all  floats
        values = df[col].unique()
        unique_range = [i for i in range(min(values), max(values)+1)]
        if (sorted(df[col].unique()) == unique_range):
            if (min(unique_range) == 1) | (min(unique_range) == 0):
                tested.append(1)
        #Captures all columns who's min value begins with 1 or 0 and all values are present from min() to max() in their unique values.
        else:
            tested.append(0)
df
print(tested)

user_column_input = [0,]

count = 0
for x,y,z in zip(tested, user_column_input, df.columns):
    if x == y:
        print("Matched")
    else:
        print("Mislabeled", z, f"Labled {x} while column was {y}")
        count += 1
count

df.PoolArea.unique()


values = df["PoolArea"].unique()
unique_range = [i for i in range(min(values), max(values)+1)]
if (sorted(df["PoolArea"].unique()) == unique_range):
    if (min(unique_range) == 1) | (min(unique_range) == 0):
        print("YAY! ", "PoolArea", "IS CATEGORICAL")
else:
    print("BOO")

unique_range