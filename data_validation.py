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


df.StockCode.str.isnumeric().all()

df = pd.read_csv("test_data/IBM_Data.csv")

tested = []
for col in df.columns:
    try:
        if all(x.isdigit() for x in df[col]) == False:
            tested.append(1)
    except:
        tested.append(0)



user_column_input = [0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0]

for x,y,z in zip(tested, user_column_input, df.columns):
    if x == y:
        print("Matched")
    else:
        print("Mislabeled", z, f"Labled {x} while column was {y}")

