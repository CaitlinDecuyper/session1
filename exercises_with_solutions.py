from faker import Faker  # Before running this script, run `pip install faker`
from numpy.random import normal
import numpy as np

# First, let me generate some fake data...
fake = Faker()
students = []
for i in range(100):
    students.append({
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'address': fake.address(),
        'maths': np.clip(normal(3, .5), 0, 4),
        'linguistics': np.clip(normal(3, .5), 0, 4),
        'psychology': np.clip(normal(3, .5), 0, 4)
    })

# Now, let's try out some things!
first_names = []
last_names = []
addresses = []
maths_grades = []
linguistics_grades = []
psychology_grades = []

# Can you write a loop that fills the above separate lists from the students list of dictionaries?
for student in students:
    first_names.append(student['first_name'])
    last_names.append(student['last_name'])
    addresses.append(student['address'])
    maths_grades.append(student['maths'])
    linguistics_grades.append(student['linguistics'])
    psychology_grades.append(student['psychology'])

# Now, can you turn it into a pandas dataframe?
import pandas as pd  # noqa: E402

students_df = pd.DataFrame(students)
print(students_df)

# What if you wanted to create a 3x100 numpy array of all the grades? (excluding other information)
import numpy as np  # noqa: E402

grades = np.array([maths_grades, linguistics_grades, psychology_grades])
print(grades)

# Now, try to do the following for all four data structures:
#   (list of dictionaries, separate lists, dataframe, array)
# Don't spend more than 20 minutes on any of these!
# Thinking about the solution is more important than programming it.
# 1. Get all the information belonging to the 20th student
print(students[19])  # List of dictionaries
print(first_names[19], last_names[19], addresses[19], maths_grades[19], linguistics_grades[19], psychology_grades[19])  # Separate lists
print(students_df.iloc[19])  # Dataframe
print(grades[:, 19])  # Array

# 2. Find the student with the highest linguistics grade
# List of dictionaries
highest = 0
highest_student = None
for student in students:
    if student['linguistics'] > highest:
        highest = student['linguistics']
        highest_student = student
print(highest_student)

# Separate lists
highest = max(linguistics_grades)
highest_index = linguistics_grades.index(highest)
print(first_names[highest_index], last_names[highest_index], linguistics_grades[highest_index])

# Dataframe
highest_index = students_df['linguistics'].argmax()
print(students_df.iloc[highest_index])

# Array
highest_index = grades[1, :].argmax()
print(grades[:, highest_index])  # This will only print the grades of the student with the highest linguistics grade

# 3. Calculate the average grade per student; (maths + linguistics + psychology) / 3
# List of dictionaries
for student in students:
    student['average'] = (student['maths'] + student['linguistics'] + student['psychology']) / 3
print(students[0])  # We only print the first student to check, to not clutter up the output too much

# Separate lists
average_grades = []
for i in range(len(linguistics_grades)):
    average_grades.append((maths_grades[i] + linguistics_grades[i] + psychology_grades[i]) / 3)
print(average_grades[0])

# Dataframe
students_df['average'] = (students_df['maths'] + students_df['linguistics'] + students_df['psychology']) / 3
print(students_df.iloc[0])

# Array
averages = grades.mean(axis=0)
print(averages[0])
