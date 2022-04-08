# employee salary

Write a function that takes 2 arguments, a list of tuples and a integer denoting a salary.
Each tuple in the list will contain the name, job and salary of an employee. The function
should output the names and jobs of all employees in the list whose salary is greater than
or equal to the integer argument. The output should be displayed one employee per line,
sorted by salary (largest first), in a neatly formatted table. If there are no matches an
appropriate message should be output.

Write a program that asks the user to supply a file name and attempts to open the file.
Each line of the file should contain the name, job title and salary of a single employee
(separated by commas). A typical line may be

Gareth Southgate,manager,2500000

The program should convert the contents of each line into a tuple with 3 elements and
add the tuples to a list. (You may assume that the contents of the file are in the correct
format so there is no need to perform validation). If the file cannot be opened the program
should output an appropriate message and terminate.

After the input of the file contents has been completed the program should output the list
of tuples (no formatting required) then enter a loop in which the user is asked to supply a
salary. The user input and list of tuples should be passed as arguments in a call to the
function described above. After returning from the function the user should be asked if
he/she wishes to quit or to supply the name of another department.

Hint: the elements of the tuple do not have to be stored in the order described above. A
different order may make the sorting easier.
