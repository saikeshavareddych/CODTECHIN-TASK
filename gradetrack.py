import streamlit as st
import pandas as pd

# Define a function to calculate letter grade
def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# Define a function to calculate GPA
def get_gpa(average):
    if average >= 90:
        return 10.0
    elif average >= 80:
        return 9.0
    elif average >= 70:
        return 8.0
    elif average >= 60:
        return 7.0
    else:
        return 0.0

st.title("Student Grade Tracker")

# Input student name
student_name = st.text_input("Enter the student's name:")

# Input grades
st.write("Enter the grades for different subjects or assignments:")
grades = []
subjects = []
num_subjects = st.number_input("Number of subjects/assignments:", min_value=1, max_value=20, step=1, value=5, key="num_subjects")
for i in range(num_subjects):
    subject = st.text_input(f"Subject/Assignment {i+1} name:", key=f"subject_{i}")
    grade = st.number_input(f"Grade for {subject}:", min_value=0.0, max_value=100.0, step=0.1, key=f"grade_{i}")
    grades.append(grade)
    subjects.append(subject)

# Calculate average grade
if len(grades) > 0:
    average_grade = sum(grades) / len(grades)
else:
    average_grade = 0

# Get letter grade and GPA
letter_grade = get_letter_grade(average_grade)
gpa = get_gpa(average_grade)

# Display results
if student_name:
    st.write(f"### Results for {student_name}:")
    data = {
        "Subject/Assignment": subjects,
        "Grade": grades
    }
    df = pd.DataFrame(data)
    st.table(df)
    
    st.write(f"**Average Grade:** {average_grade:.2f}")
    st.write(f"**Letter Grade:** {letter_grade}")
    st.write(f"**GPA:** {gpa:.2f}")
else:
    st.write("Please enter the student's name to display the results.")
