import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description

class CSV:
    CSV_FILE="finance_data.csv"
    COLUMNS=["date", "amount", "category", "description"]
    FORMAT="%d-%m-%Y"

    @classmethod
    def initalize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.COLUMNS)
    # dataframe is an object in 'pandas' that allows us to access different rows/columns from a csv file
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

    @classmethod
    def get_transaction(cls, start_date, end_date):
        df=pd.read_csv(cls.CSV_FILE)
        df["date"]=pd.to_datetime(df["date"], format=CSV.FORMAT)# stored the object in variable in the form of datetime obj
       #start_date which is given to us is a string in function(get_transaction) so to convert it to the correct format
        start_date=datetime.strptime(start_date, CSV.FORMAT)
        end_date=datetime.strptime(end_date, CSV.FORMAT)

    # We can apply mask to different rows inside of our dataframe to see if we would select that row or not
        mask=(df["date"] >= start_date) & (df["date"] <= end_date)
    #'filtered_df' returns a new filtered dataframe which contains the rows where the mask condition was true     
        filtered_df=df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range")
        else:
            print(f"Transaction from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")

    #with the help of 'formatters we can format any specific column in this case "date",
    # so we put column name as the'key' and then put a function (lamda) we want to apply to every single element,
    # inside the column to format it differently   
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

    #by applying 'filtered_df' we are getting all rows with category income
    #then from all those rows we are looking at all of the values in the amount columns and then did summation of them
            total_income=filtered_df[filtered_df["category"]=="Income"]["amount"].sum()
            total_expense=filtered_df[filtered_df["category"]=="Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}") 
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income-total_expense):.2f}")
        
        return filtered_df

def add():
    CSV.initalize_csv()
    date=get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter today's date: "
        ,allow_default=True
        )
    amount=get_amount()
    category=get_category()
    description=get_description()
    CSV.add_entry(date, amount, category, description)

def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice=input("Enter your choice (1-3): ")

        if choice=="1":
            add()
        elif choice=="2":
            start_date=get_date("Enter the start date (dd-mm-yyyy): ")
            end_date=get_date("Enter the end date (dd-mm-yyyy): ")
            CSV.get_transaction(start_date, end_date)
        elif choice=="3":
            print("Exiting..")
            break
        else:
            print("Invalid choice, Enter 1, 2 or 3")


if __name__=="__main__":
    main()
    