import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE="finance_data.csv"
    COLUMNS=["date", "amount", "category", "description"]

    @classmethod
    def initalize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.COLUMNS)
            #dataframe is an object in 'pandas' that allows us to access different rows/columns from a csv file
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        #dictionary for all different data that we wanted to add into the csv file
        new_entry={
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        # 'with' syntax is known as context manager so it is storing the open file in this variable
        # inshort when we are done with the code inside of csv writer this will automatically handle closing of file
        # and deal with any memory leaks
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer=csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            #'csvwriter' will take a dictionary amd write it into the csv file
            writer.writerow(new_entry)
        print("Entry added successfully")
            

CSV.initalize_csv()    
CSV.add_entry("20-01-2025", 326.65, "Income", "Salary")                        