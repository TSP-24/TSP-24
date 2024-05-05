import numpy as np
import pandas as pd
from datetime import datetime

# Generate student names
def generate_student_names(num_students):
    names = []
    for i in range(num_students):
        first_name = chr(np.random.randint(97, 123))  # Generate a random lowercase letter as the first name initial
        last_name = chr(np.random.randint(97, 123)) + chr(np.random.randint(97, 123))  # Generate random lowercase letters as the last name
        names.append((first_name, last_name))
    return names

# Generate student IDs
def generate_student_ids(num_students):
    student_ids = []
    for i in range(num_students):
        student_id = "u" + str(np.random.randint(1000000, 10000000))  # Generate a random 7-digit number as the student ID
        student_ids.append(student_id)
    return student_ids

# Generate student scores based on normal distribution
def generate_scores(num_students, mean, std):
    scores = np.random.normal(mean, std, num_students)
    scores = np.round(np.clip(scores, 0, 100), 2)  # Limit scores between 0 and 100, and round to two decimal places
    return scores

# Generate student data
def generate_student_data(num_students):#, mean, std):
    student_names = generate_student_names(num_students)
    student_ids = generate_student_ids(num_students)
    #scores = generate_scores(num_students, mean, std)
    data = {"First name": [], "Last name": [], "Uni ID": [], "Email address": [], "Groups": []}
    for i in range(num_students):
        first_name, last_name = student_names[i]
        uni_id = student_ids[i]
        email = uni_id + "@anu.edu.au"
        groups = "[MyTT] LecA/01 (Classes 5811/5817);[MyTT] LecB/01 (Classes 5811/5817);[MyTT] TutA/01 (Classes 5811/5817)"
        data["First name"].append(first_name)
        data["Last name"].append(last_name)
        data["Uni ID"].append(uni_id)
        data["Email address"].append(email)
        data["Groups"].append(groups)
    return pd.DataFrame(data)#, scores



# Generate grades data
def generate_grades_data(num_students, scores, course_data):
    grades_data = {"Course total (Real)": [], "Last downloaded from this course": []}
    for i in range(num_students):
        total_score = 0
        for _, row in course_data.iterrows():
            assessment = row["Assessment"]
            weight = row["Percentage"]

            grade = np.random.choice(scores, p=np.ones(len(scores)) / len(scores))
            if assessment not in grades_data:
                grades_data[assessment] = []
            grades_data[assessment].append(grade)
            total_score += grade * weight / 100
        grades_data["Course total (Real)"].append(total_score)
        grades_data["Last downloaded from this course"].append(0)
    return pd.DataFrame(grades_data)





# Filter course data based on CourseID
def filter_course_data(course_data, course_id):
    return course_data[course_data["CourseID"] == course_id]

#Main function
def main():
    num_students = 50
    mean = 70  # Mean total score
    std = 15  # Standard deviation


    # Load course data
    course_data = pd.read_csv("compcourse.csv")

    # Choose a course ID (e.g., 3610)
    course_id = 3620

    # Filter course data based on course ID
    filtered_course_data = filter_course_data(course_data, course_id)

    # Generate student scores
    scores = generate_scores(int(num_students), mean, std)

    # Generate grades data for the selected course
    grades_data = generate_grades_data(int(num_students), scores, filtered_course_data)

    student_data = generate_student_data(num_students)

    result = pd.concat([grades_data, student_data], axis=1)
    # Save grades data to a CSV file
    result.to_csv("generated_grades_data3620.csv", index=False)

# Main function

# if __name__ == "__main__":
#
#     main()