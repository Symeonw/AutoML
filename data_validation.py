import pandas as pd
import os

def data_validation(file_path, sheet_name=None):
    """Check for file size within limits, checks file extention, labels columns."""
    if os.stat(file_path).st_size/1000000000 > 5:
        raise ValueError("File sizes of over 4 Gigabytes are not currently supported.")
    
    if file_path.endswith(".csv"):
        try:
            df = pd.read_csv(file_path)
        except:
            df = pd.read_csv(file_path, encoding="unicode_escape")

    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path, sheet_name=sheet_name)

    else: 
        raise ValueError(f"{file_path[file_path.rindex('.'):]} file extentioon is not currently supported.")
#TODO: Create a label for Unique ID
    labels = [] 
    for col in df.columns:
        dfi = pd.DataFrame(df[col].unique(), columns=[col])
        if len(dfi[col]) == len(df[col]):
            labels.append(1)
            continue
        try:
            if all(dfi[col].astype(str).str.isnumeric()) == False:
                labels.append(1)
                continue
            #Captures all data with letters
        except:
            pass
        try:
            if all(x.isdigit() for x in dfi[col]) == False:
                labels.append(1)
            #Captures all strings with only numbers
        except:
            if dfi[col].dtype == float:
                labels.append(0)
                continue
            #Captures all  floats
            values = df[col]
            unique_range = [i for i in range(min(values), max(values)+1)]
            if (sorted(dfi[col]) == unique_range):
                if (min(unique_range) == 1) | (min(unique_range) == 0):
                    labels.append(1)
            #Captures all columns who's min value begins with 1 or 0 and all values are present from min() to max() in their unique values.
                else:
                    labels.append(0)
            else:
                    labels.append(0)
    return df, labels

def data_validation_post_user_input(df, user_input): 
    
    for col, ui in zip(df.columns, user_input):
        """"Turns all continuous columns into number only columns (replaces all non-numerical data with NAN"""
        if ui == 0:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df



# df = pd.read_csv("test_data/IBM_Data.csv")
# user_column_input = [0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0]

# labels = [] 

# for col in df.columns:
#     try:
#         if df[col].str.isnumeric().all() == False:
#             labels.append(1)
#             continue
#         else:
#             labels.append(0)
#         #Captures all data with letters
#     except:
#         if df[col].dtype == float:
#             labels.append(0)
#             continue
#         #Captures all  floats
#         #HERE!
#         values = df[col].unique()
#         unique_range = [i for i in range(min(values), max(values)+1)]
#         if (sorted(df[col].unique()) == unique_range):
#             if (min(unique_range) == 1) | (min(unique_range) == 0):
#                 labels.append(1)
#         #Captures all columns who's min value begins with 1 or 0 and all values are present from min() to max() in their unique values.
#             else:
#                 labels.append(0)
#         else:
#                 labels.append(0)

# count = 0
# for x,y,z in zip(labels, user_column_input, df.columns):
#     if x == y:
#         print("Matched")
#     else:
#         print("Mislabeled", z, f"Labled {x} while column was {y}")
#         count += 1
# count


# sorted(df.DistanceFromHome.unique())






# import seaborn as strings
# from scipy.stats import norm
# import matplotlib.pyplot as plt

# sns.distplot(df.Parch, fit=norm
# sns.distplot(df.Age)
# sns.distplot(df.DistanceFromHome)
# sns.distplot(df.YearsSinceLastPromotion)
# sns.distplot(df.YearsWithCurrManager)
# sns.distplot(df.Education.astype("category").cat.codes, fit=norm)

# sns.distplot(df.Education, fit=norm)

# df.DistanceFromHome.value_counts().idxmax() 
# df.DistanceFromHome.median()
# df.Age.max()

# df.Age.describe()
# df.DistanceFromHome.describe()

# mislabeled.remove("PerformanceRating")
# mislabeled.remove("EmployeeCount")
# for col in mislabeled:
#     sns.distplot(df[col], fit=norm)
#     plt.show()



# # Mean > Median > Mode = Right Skewed
# # Mode > Median > Mean = Left Skewed

# mean = df.YearsInCurrentRole.mean()
# mode = df.YearsInCurrentRole.mode()
# median = df.YearsInCurrentRole.median()

# mean > median > mode

# # If meets right skewed:

# x = df.YearsSinceLastPromotion.value_counts().idxmax()
# y = df.YearsSinceLastPromotion.max()
# x
# y

# # If meets left skewed:

# x = df.YearsSinceLastPromotion.value_counts().idxmax()
# y = df.YearsSinceLastPromotion.min()





# x = df.Education.value_counts().idxmax()
# y = df.Education.max()

# df.Education.unique()

