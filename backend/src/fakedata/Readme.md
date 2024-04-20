# Grade Data Generator

## Overview
The Grade Data Generator is a Python script designed to generate student grades data based on course assessments. It allows for the creation of synthetic student data and their corresponding grades for a given course.

## Features
- Generates synthetic student data including names, IDs, and email addresses.
- Generates random student scores based on a normal distribution with customizable mean and standard deviation.
- Utilizes course assessment data to calculate student grades.
- Outputs grades data to CSV files for further analysis or integration with other systems.

## Prerequisites
- Python 3.x
- Required Python libraries: `numpy`, `pandas`

## Usage
1. **Clone Repository**: Clone this repository to your local machine.
    ```
    git clone https://github.com/your-username/grade-data-generator.git
    ```
2. **Install Dependencies**: Install the required Python libraries using pip.
    ```
    pip install numpy pandas
    ```
3. **Prepare Course Data**: Prepare your course data in CSV format. The course data should include columns for Assessment names and their respective Percentage weights. Refer to the provided `compcourse.csv` file as an example. You can modify this file to match your course assessment structure.

4. **Run Script**: Execute the main script `main.py`.
    ```
    python main.py
    ```
5. **Input Course ID and Student Count**: Follow the prompts to input the Course ID and the number of students enrolled in the course. Ensure you enter valid integers for both inputs.

6. **Generate Grades Data**: The script will generate grades data based on the provided course data and student count. It will then save the generated grades data to a CSV file named `generated<course_id>.csv`, where `<course_id>` is the ID of the course you provided.

## File Structure
- `main.py`: Main script file to run the Grade Data Generator.
- `mark_generator.py`: Module containing functions for generating student data, scores, and grades data.
- `compcourse.csv`: Sample course data in CSV format. Modify this file to match your course assessment structure.
- `generated<course_id>.csv`: Output CSV file containing the generated grades data for the specified course.

## Function Details
- `generate_student_names(num_students)`: Generates synthetic student names based on the number of students provided.
- `generate_student_ids(num_students)`: Generates synthetic student IDs based on the number of students provided.
- `generate_scores(num_students, mean, std)`: Generates random student scores based on a normal distribution with customizable mean and standard deviation.
- `generate_student_data(num_students, mean, std)`: Generates synthetic student data including names, IDs, email addresses, and group assignments based on the provided parameters.
- `generate_grades_data(num_students, scores, course_data)`: Generates grades data for the selected course based on student scores and course assessment data.
- `filter_course_data(course_data, course_id)`: Filters course data based on the provided course ID.

## License
This project is licensed under the MIT License 

## Acknowledgments
- This script was developed as a part of Data Scoring at TSP Project.


