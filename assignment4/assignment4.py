#Task 1
import pandas as pd

data={
    "Name":["Alice", "Bob", "Charlie"],
    "Age": [25, 30,35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
task1_data_frame=pd.DataFrame(data)

print(task1_data_frame)

#add a column 
task1_with_salary= task1_data_frame.copy() 
task1_with_salary["Salary"] = [70000, 80000, 90000] 

print(task1_with_salary)

#modify an existing column 
task1_older= task1_with_salary.copy() 
#to select a specific column in pandas we use ["Age"]
task1_older["Age"]= task1_older["Age"] + 1

print(task1_older)

#save dataframe as CSV file 
task1_older.to_csv('employees.csv', index=False)#by putting index=false it doesnt include index number
print("DataFrame saved to employees.csv")

#Task 2
#read data from csv file 
task2_employees= pd.read_csv('employees.csv')
print(task2_employees)

#read data from json file 
#basically creating the DataFrame by loading the JSON file
json_employees=pd.read_json("additional_employees.json")
print (json_employees)

#combine data frames / since tas2 contains original employees from csv file and json contains new employees we start with original data first 
more_employees = pd.concat([task2_employees,json_employees], ignore_index=True)
print(more_employees)


#Task 3
first_three=more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)

employee_shape= more_employees.shape
print(employee_shape)

more_employees.info()

#Task 4
dirty_data= pd.read_csv("dirty_data.csv")
print (dirty_data)

clean_data= dirty_data.copy()

#remove duplicate rows 
clean_data=clean_data.drop_duplicates()
print(clean_data)

clean_data["Age"]=clean_data["Age"].replace("unknown",pd.NA) # this replaces any occurence of "unknown" in the age column with pd.NA wich represents missing data in pandas
clean_data["Age"]=pd.to_numeric(clean_data["Age"], errors="coerce") #pd.to_numer() converts the values into number , errors="coerce" converts anything that cannot be interpreted as a number into a missing value (NaN)
print("\nAfter conversion to numeric:")
print(clean_data)

clean_data["Salary"]=clean_data["Salary"].replace(["unknown","n/a"],pd.NA)
clean_data["Salary"]=pd.to_numeric(clean_data["Salary"], errors="coerce")
print(clean_data)

# 1. Fill missing numeric values
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())

print("\nAfter filling missing numeric values:")
print(clean_data)


# 2. Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format="mixed")

print("\nAfter converting Hire Date:")
print(clean_data)


# 3. Strip whitespace and convert Name and Department to uppercase
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()

print("\nAfter cleaning Name and Department:")
print(clean_data)