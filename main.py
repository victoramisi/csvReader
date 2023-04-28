import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
imported_data = pd.read_csv("Company_data.csv")
temporary_container = dict()

def top_paid():
    while True:
        try:
            user_choice = int(input("Please select a number: "))
            user_key_name = input("Pick the title of this data: ")
        except:
            print("Please select a whole number!")
        else:
            if user_key_name in temporary_container.keys():
                print("Please pick a unique key name each time")
            else:
                headcount = imported_data.head(user_choice)
                inner_container = dict()
                df = pd.DataFrame(headcount)
                for index, row in df.iterrows():
                    employee_full_Name = row["first_name"] + ' ' + row["last_name"]
                    employee_salary = row["salary"]
                    inner_container[employee_full_Name] = employee_salary
                temporary_container[user_key_name] = inner_container
                print("Added successfully")
                break

def low_paid():
    while True:
        try:
            user_choice = int(input("Please select a number: "))
            user_key_name = input("Pick the title of this data: ")
        except:
            print("Please select a whole number!")
        else:
            if user_key_name.strip() in temporary_container.keys():
                print("Please pick a unique key name each time")
            else:

                headcount = imported_data.tail(user_choice)
                inner_container = dict()
                df = pd.DataFrame(headcount)
                for index, row in df.iterrows():
                    employee_full_Name = row["first_name"] + ' ' + row["last_name"]
                    employee_salary = row["salary"]
                    inner_container[employee_full_Name] = employee_salary
                temporary_container[user_key_name] = inner_container
                print("Added successfully")
                break

def max_paid():
    temporary_container["Max_Salary"] = np.max(imported_data["salary"])
    print("Added successfully")

def min_paid():
    temporary_container["Min_Salary"] = np.min(imported_data["salary"])
    print("Added successfully")

def avg_paid():
    temporary_container["AVG_Salary"] = round(np.average(imported_data["salary"]), 2)
    print("Added successfully")
def yearly_monthly_labour():
    temporary_container["Yearly_Labour"] = np.sum(imported_data["salary"])
    temporary_container["Monthly_Labour"] = round(np.sum(imported_data["salary"])/12, 2)
    print("Added successfully")

def show_case():
    if len(temporary_container) < 1:
        print("No data added!")

    else:
        search_option = input("Select the data name you want to visualize: ")
        helper_xlist = list()
        helper_ylist = list()
        if search_option in temporary_container.keys():
            if isinstance(temporary_container[search_option], dict):
                for innerChildItem in temporary_container.keys():
                    if innerChildItem == search_option:
                        for keyItem2 in temporary_container[innerChildItem].keys():
                            helper_xlist.append(keyItem2)
                            helper_ylist.append(temporary_container[innerChildItem][keyItem2])
                    y = helper_ylist
                    myLabels = helper_xlist
                    plt.figure(figsize=(10, 10),
                               facecolor='white')

                plt.title(search_option)

                plt.pie(y, labels=myLabels,
                        startangle=90,
                        shadow=True,
                        autopct='%1.2f%%')

                sumValues = np.round(np.sum(helper_ylist))
                plt.legend(title=f"Total rounded salary: {sumValues}$",
                           loc="best")

                plt.show()

            else:
                helper_xlist = list()
                helper_ylist = list()
                for element in temporary_container:
                    if element == search_option:
                        helper_xlist.append(element)
                        helper_ylist.append(temporary_container[element])

                        y = helper_ylist
                        myLabels = helper_xlist

                        plt.figure(figsize=(10, 10),
                                facecolor='white')
                        plt.title(search_option)

                        plt.pie(y,
                            labels=myLabels,
                            startangle=90,
                            shadow=True,
                            autopct='%1.2f%%')

                        sumValues = np.round(np.sum(helper_ylist))

                        plt.legend(title=f"Total rounded salary: {sumValues}$",
                                   loc="best")
                plt.show()
                print(temporary_container)

        else:
            print("Data name not found!")
print("Please try to use pycharm. I noticed vscode was stopping the program" + "\n" + "when you tried to visualize the data")
print("1: Add the top N highest paid employees. N = number of employees")
print("2: Add the top N lowest paid employees. N = number of employees")
print("3: Add the Minimum salary")
print("4: Add the Maximum salary")
print("5: Add the Average salary")
print("6: Add the Yearly and Monthly salary burn")
print("7: Show me a visual representation of the data")
print("8: Quit")
def user_options():
    user_choices = [1, 2, 3, 4, 5, 6, 7, 8]
    condition_Helper = {
        "1": top_paid,
        "2": low_paid,
        "3": min_paid,
        "4": max_paid,
        "5": avg_paid,
        "6": yearly_monthly_labour,
        "7": show_case,
    }
    while True:
        try:
            user_selection = int(input("What do you need?: "))
        except:
            print("Please select a whole number!")
        else:
            if user_selection not in user_choices:
                print("Invalid option!")
            elif user_selection == 8:
                print("Bye!")
                break
            else:
                condition_Helper[str(user_selection)]()
user_options()




