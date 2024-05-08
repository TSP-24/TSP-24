import numpy as np
import pandas as pd
from datetime import datetime
import mark_generator as mg


# Main function
def main(course_id, num_students, threshold_percentage):
    num_students = int(num_students)
    mean = 70  # Mean total score
    std = 15  # Standard deviation


    # Load course data
    course_data = pd.read_csv("compcourse.csv")

    # Choose a course ID (e.g., 3610)
    course_id = int(course_id)

    # Filter course data based on course ID
    filtered_course_data = mg.filter_course_data(course_data, course_id)

    # Generate student scores
    scores = mg.generate_scores(int(num_students), mean, std)

    # Generate grades data for the selected course
    # grades_data = mg.generate_grades_data(int(num_students), scores, filtered_course_data)
    grades_data = mg.generate_grades_data(int(num_students), scores, filtered_course_data, int(threshold_percentage))

    student_data = mg.generate_student_data(num_students)

    result = pd.concat([student_data, grades_data], axis=1)

    # Save grades data to a CSV file
    result.to_csv('generated' + str(course_id) + '.csv', index=False)
    print(filtered_course_data)





if __name__ == "__main__":
    course_id = input("Enter course id: ")
    num_students = input("Enter student numbers: ")
    threshold_percentage = input("Enter student submit threshold: ")
    main(course_id, num_students, threshold_percentage)