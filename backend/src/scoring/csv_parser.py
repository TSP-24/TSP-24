import os
import pandas as pd
import re
from io import StringIO
from datetime import datetime

def get_assessments_info(course):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the CSV file
    csv_path = os.path.join(script_dir, '..', 'fakedata', 'compcourse.csv')
    
    # Load the course data
    df = pd.read_csv(csv_path)

    # Filter the data for the specified course
    df = df[df['CourseID'] == course]
    as_names = df['Assessment']

    assessment_keywords = {
        'midsem_exam': ['midsem exam'],
        'final_exam': ['final exam', 'oral exam', 'exam'],
        'assignment': ['assignment: assignment','assignment: assessment','assignment'],
        'quiz': ['quiz: quiz'],
        'attendance': ['attendance'],
        'lab': ['lab'],
    }

    # Initialize a dictionary to store the headers for each category
    assessment_weights = {assessment_keyword: [] for assessment_keyword in assessment_keywords}
    assessment_dls = {assessment_keyword: [] for assessment_keyword in assessment_keywords}

    # Classify headers
    for as_name in as_names:
        for assessment, keywords in assessment_keywords.items():
            if any(keyword in as_name.lower() for keyword in keywords):
                percentage = df[df['Assessment'] == as_name]['Percentage'].values[0]
                deadline = df[df['Assessment'] == as_name]['Due'].values[0]
                deadline = datetime.strptime(deadline, '%Y/%m/%d')
                assessment_weights[assessment].append(percentage)
                assessment_dls[assessment].append(deadline)
                break
        else:
            assessment_weights.setdefault('other', []).append(as_name)

    return assessment_weights, assessment_dls

def filter_headers(file, filename):  
    # Extract the numerical part (courseID) using a regular expression
    course = re.search(r'\d+', filename)
    if course:
        course = int(course.group()[:4])

    df = pd.read_csv(StringIO(file))
    headers = df.columns.to_list()
    # Define categories and their keywords
    categories_keywords = {
        'uni_id': ['uni', 'id'],
        'total': ['total'],
        'px_exam': ['da/px exam'],
        'midsem_exam_d': ['submit_midsem exam', 'submit_assignment: midsem exam'],
        'midsem_exam': ['midsem exam'],
        'final_exam_d': ['submit_final exam', 'submit_assignment: exam'],
        'final_exam': ['final exam','oral exam','exam'],
        'assignment_d': ['submit_assignment: assignment','submit_assignment: assessment','submit_assignment'],
        'assignment': ['assignment: assignment','assignment: assessment','assignment'],
        'quiz_d': ['submit_quiz: quiz'],
        'quiz': ['quiz: quiz'],
        'attendance': ['attendance'],
        'lab_d': ['submit_lab'],
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
    keep_categories = ['uni_id', 'px_exam', 'final_exam', 'final_exam_d', 'midsem_exam', 'midsem_exam_d', 
                       'assignment', 'assignment_d', 'quiz', 'quiz_d', 'lab', 'lab_d', 'attendance']
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

    return df, category_headers, get_assessments_info(course), course

def get_all_assessments_info(course):
    info = get_assessments_info(course)[0]
    assessments = []
    for assessment, values in info.items():
        if values:
            if   assessment == 'final_exam':
                assessments.append(f'Final Exam ({values[0]}%)')
            elif assessment == 'midsem_exam':
                assessments.append(f'Midsem Exam ({values[0]}%)')
            elif assessment == 'attendance':
                assessments.append(f'Attendance ({values[0]}%)')
            elif assessment == 'assignment':
                for asg in values:
                    assessments.append(f'Assignment ({asg}%)')
            elif assessment == 'quiz':
                for quiz in values:
                    assessments.append(f'Quiz ({quiz}%)')
            elif assessment == 'lab':
                for lab in values:
                    assessments.append(f'Lab ({lab}%)')
    
    return assessments