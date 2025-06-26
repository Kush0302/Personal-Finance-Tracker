from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES={"I": "Income", "E": "Expense"}


#the prompt is what we are going to ask user to input beforethey give us the date
def get_date(prompt, allow_default=False):
    while True:
        date_str=input(prompt)
        if allow_default and not date_str:
            return datetime.today().strftime(date_format)
        
        try:
            valid_date=datetime.strptime(date_str, date_format)
            return valid_date.strftime(date_format) #makes sure to clean up the date that user typed in and gives us in the format we need in
        except ValueError:
            print("Invalid date format, please enter the date in dd-mm-yy format")

def get_amount():
    try:
        amount=float(input("Enter the amount: "))
        if amount<=0:
            raise ValueError("Ammount must be a non -negative non- zero value")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category=input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category, please enter 'I' for Income or 'E' for Expense: ")
    return get_category()

def get_description():
    return input("Enter a description (optional): ")

