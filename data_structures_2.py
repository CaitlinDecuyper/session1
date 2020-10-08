# Let's look at another example of data using lists
first_names = ['Marcus', 'Kristin', 'Adam', 'Kimberly', 'Judith']
last_names = ['Mcguire', 'Cantu', 'Mendez', 'Wolf', 'Johnson']
grades = [3.3, 2.7, 3.7, 2.7, 3.0]

# What if you wanted to get Judith's grade?
name = 'Judith'
index = first_names.index(name)
grade = grades[index]
print(grade)

# Or the name of the person with the highest grade?
max_grade = max(grades)
index = grades.index(max_grade)
name = f'Full name: {first_names[index]} {last_names[index]}'
print(name)

# An array won't work here, because the value types differ (strings and floats)

# Dictionaries are key-based, rather than index based:
#  they allow you to retrieve a value through a key-value mapping
#  they are very efficient at performing this specific mapping
student = {
    'first_name': 'Marcus',
    'last_name': 'Mcguire',
    'grade': 3.3
}
print(student['grade'])

# Can be combined with lists!
students = [
    {'first_name': 'Marcus', 'last_name': 'Mcguire', 'grade': 3.3},
    {'first_name': 'Kristin', 'last_name': 'Cantu', 'grade': 2.7},
    {'first_name': 'Adam', 'last_name': 'Mendez', 'grade': 3.7},
    {'first_name': 'Kimberly', 'last_name': 'Wolf', 'grade': 2.7},
    {'first_name': 'Judith', 'last_name': 'Johnson', 'grade': 3.0}
]

# Getting all information from a specific student is now much easier!
print(students[3])

# ... but for the questions before, it doesn't make things that much easier
name = 'Judith'
for student in students:
    if student['first_name'] == name:
        print(student['grade'])

# I've heard pandas are pretty cool animals
import pandas as pd  # noqa: E402

students = pd.DataFrame(students)
print(students)  # That looks like... a table!

# Let's try our two questions again
mask = students['first_name'] == 'Judith'  # students[column] selects a single column
grade = students.loc[mask, 'grade']  # students.loc[row, column] selects on both row and column
print(float(grade))

# And getting the highest grade
index = students['grade'].argmax()
student = students.iloc[index]  # students.iloc[row] selects a single row
print(f'Full name: {student.first_name} {student.last_name}')
