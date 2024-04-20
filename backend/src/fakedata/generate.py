import numpy as np
import pandas as pd
from datetime import datetime
import mark_generator as mg


# Main function
def main(course_id, num_students):
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
    grades_data = mg.generate_grades_data(int(num_students), scores, filtered_course_data)

    # Save grades data to a CSV file
    grades_data.to_csv('generated' + str(course_id) + '.csv', index=False)
    print(filtered_course_data)





if __name__ == "__main__":
    course_id = input("Enter course id: ")
    num_students = input("Enter student numbers: ")
    main(course_id, num_students)