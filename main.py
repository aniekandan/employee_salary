#%% Import pandas for dataframe manipulation

import pandas as pd

#%% Print the list of tuples as a HTML table

def print_table(lst: list):
    '''
    Print out a list of tuples as a well formatted table

    Parameters
    ----------
    lst : list
        The list to format as a table

    Returns
    -------
    None.

    '''
    
    # print out the sorted filtered_list in a tabular form
    headers = ['name', 'job', 'salary']    # the table headers
    df = pd.DataFrame(lst, columns=headers)   # convert the table to a dataframe
    print(df)

def filter_list_and_display(list_of_employees: list, salary: int = None):
    '''
    Filter the list of employees and display it

    Parameters
    ----------
    list_of_employees : list
        The list of employees to filter
        
    salary : int, optional
        The threshold salary. The default is None. If salary is None,
        all employeees should be displayed

    Returns
    -------
    None.

    '''
    
    # get the filtered list
    if salary == None:
        filtered_list = list_of_employees

    else:
        filtered_list = [(name, job, emp_salary) for (name, job, emp_salary) in list_of_employees if emp_salary >= salary]


    # sort filtered_list by salary, from largest to smallest salary
    sorted_list = sorted(filtered_list, key=(lambda emp: emp[2]), reverse=True)

    if len(sorted_list) > 0:
        if salary != None:
            print(f"showing staff having salaries >= {salary}\n")

        else:
            print("showing all staff:\n")
            
        print_table(sorted_list)

    else:
        print("No matches found")
    
    
#%% The main program

filename = input("Enter name of data file: ")

employee_list = []

try:
    employee_file = open(filename)

except:
    print("File not found")

else:
    # load each line into the employee list
    # convert to tuple
     _ = [line.rstrip().split(",") for line in employee_file]
     employee_list = [(split_data[0], split_data[1], int(split_data[2])) for split_data in _]

     # close the file
     employee_file.close()
    
     # print out the tuples, no formatting
     print("contents of employee file:\n")
     print(employee_list)
         

     # view filtered employees
     
     while True:
         # The loop should repeat indefinitely to give user 
         # opportunities to filter the employee list
         try:
             # try to get a valid input
             input_salary = int(input("Enter a salary: "))

         except:
             # user entered a non integer
             print("Invalid input, enter a whole number")
 
         else:
             if input_salary < 0:
                 # user entered a negative number
                 print("Invalid input, enter a whole number")
 
             else:
                 # filter and print, no formatting
                 filter_list_and_display(employee_list, input_salary)

                 # ask user if they want to continue
                 print("Would you like to continue, or exit")

                 # Get user response
                 resp = input("Enter x to exit, or any other thing to continue: ")

                 if str.lower(resp) == "x":
                     break




