import os
import pandas as pd
import numpy as np
import re
from IPython.display import display

# Define the file path
file_path = '../fakedata/g24002.csv'

def get_course_weights(course):
    # Load the course data
    df = pd.read_csv('../fakedata/compcourse.csv')

    # Filter the data for the specified course
    df = df[df['CourseID'] == course]
    as_names = df['Assessment']

    assessment_keywords = {
        'final_exam': ['final exam','oral exam'],
        'midsem_exam': ['midsem exam'],
        'assignment': ['assignment: assignment','assignment: assessment','assignment'],
        'quiz': ['quiz: quiz'],
        'attendance': ['attendance'],
        'lab': ['lab'],
    }

    # Initialize a dictionary to store the headers for each category
    assessment_weights = {assessment_keyword: [] for assessment_keyword in assessment_keywords}

    # Classify headers
    for as_name in as_names:
        for assessment, keywords in assessment_keywords.items():
            if any(keyword in as_name.lower() for keyword in keywords):
                percentage = df[df['Assessment'] == as_name]['Percentage'].values[0]
                assessment_weights[assessment].append(percentage)
                break
        else:
            assessment_weights.setdefault('other', []).append(as_name)

    return assessment_weights

def filter_headers(file_path):  
    # File path
    file_path = '../fakedata/g24002.csv'

    # Extract the numerical part (courseID) using a regular expression
    course = re.search(r'\d+', file_path)
    if course:
        course = int(course.group()[:4])

    # Check if the directory exists
    if os.path.exists(os.path.dirname(file_path)):
        # Load the data
        df = pd.read_csv(file_path)

        # Replace '-' with NaN
        df = df.replace('-', np.nan)

        # Drop columns where all values are NaN
        df = df.dropna(axis=1, how='all')

        # Get the column headers
        headers = df.columns.tolist()

    else:
        print(f"The directory does not exist: {os.path.dirname(file_path)}")
    # Define categories and their keywords
    categories_keywords = {
        'uni_id': ['uni', 'id'],
        'total': ['total'],
        'px_exam': ['da/px exam'],
        'final_exam': ['final exam','oral exam'],
        'midsem_exam': ['midsem exam'],
        'assignment': ['assignment: assignment','assignment: assessment','assignment'],
        'quiz': ['quiz: quiz'],
        'attendance': ['attendance'],
        'lab': ['lab'],
    }

    # Initialize a dictionary to store the headers for each category
    category_headers = {category_keyword: [] for category_keyword in categories_keywords}

    # Classify headers
    for header in headers:
        for category, keywords in categories_keywords.items():
            if any(keyword in header.lower() for keyword in keywords):
                category_headers[category].append(header)
                break
        else:
            category_headers.setdefault('other', []).append(header)

    # If there are multiple attendance columns, keep only the first one
    if len(category_headers['attendance']) > 1:
        category_headers['attendance'] = [category_headers['attendance'][0]]

    # Keep only the columns that fall under the categories 'uni_id', 'exam', 'assignment', 'quiz', 'attendance', and 'lab'
    keep_categories = ['uni_id', 'px_exam', 'final_exam', 'midsem_exam', 'assignment', 'quiz', 'attendance', 'lab']
    keep_headers = [header for category in keep_categories for header in category_headers[category]]
    df = df[keep_headers]

    # Replace NaN values with 0
    df = df.fillna(0)
    # Combine the 'px_exam' and 'final_exam' columns
    if len(category_headers['px_exam']) > 0 and len(category_headers['final_exam']) > 0:
        df[category_headers['final_exam'][0]] = df[category_headers['px_exam'][0]].combine(df[category_headers['final_exam'][0]],
                                                lambda px_exam, final_exam: final_exam if px_exam == 0 else px_exam)
        # Drop the original 'px_exam' and 'final_exam' columns
        df = df.drop(columns=[category_headers['px_exam'][0]])

    return df, category_headers, get_course_weights(course)