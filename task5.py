""""
Employee Shift Manager
You are asked to build a small program to help manage employee work shifts in a company.  
Create a dictionary `shifts` where each key is an employee's name, and the value is a list of the days they are scheduled to work.  
     shifts = {
       "Alice": ["Monday", "Wednesday"],
       "Bob": ["Tuesday", "Thursday"],
       "Charlie": ["Monday", "Friday"]
   }


fucntion signature function add_shift(employee, day):
The  function should 
1. Checks if the employee exists in the dictionary.

 - If they exist, add the new day to their list (only if it’s not already there).

-  If they don’t exist, create a new key for them with the day inside a list.

-  Return the updated dictionary.


2. Write another function get_schedule(day) that:

Returns a list of employees working on that day.
"""

shifts = {
       "Alice": ["Monday", "Wednesday"],
       "Bob": ["Tuesday", "Thursday"],
       "Charlie": ["Monday", "Friday"]
}

def add_shift(employee, day):
	if employee in shifts:
		if day not in shifts[employee]:
			shifts[employee].append(day)
	else:
		shifts[employee] = [day]
	return shifts
def get_schedule(day):
	employees = []
	for employee, days in shifts.items():
		if day in days:
			employees.append(employee)
	return employees
print(get_schedule("Monday")) 
print(add_shift("Bob", "Friday"))
