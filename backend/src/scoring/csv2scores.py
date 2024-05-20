import pandas as pd
from student import Student
from csv_parser import filter_headers, get_all_assessments_info, get_weights
from datetime import datetime

def calculate_engagement(csv_file, csv_name, weights = None):
    df, headers, as_info, course = filter_headers(csv_file, csv_name)

    final_exam_header = headers['final_exam']
    midsem_exam_header = headers['midsem_exam']
    attendance_header = headers['attendance']

    asg_headers = headers['assignment']
    quiz_headers = headers['quiz']
    lab_headers = headers['lab']

    final_exam_d_header = headers['final_exam_d']
    midsem_exam_d_header = headers['midsem_exam_d']
    asg_d_headers = headers['assignment_d']
    quiz_d_headers = headers['quiz_d']
    lab_d_headers = headers['lab_d']

    info = []
    engagement_scores = []
    failed_assessments = []
    late_submissions = []

    for index, row in df.iterrows():
        # Create student object
        student = Student('u' + str(10000000+index))
        # Set weights if provided
        if weights is not None:
            student.set_weights(get_weights(weights))
        # Set deadlines
        student.set_deadlines(as_info[1])

        # Quiz engagement
        if quiz_headers != []:
            for i, quiz in enumerate(quiz_headers):
                submission_date = datetime.strptime(row[quiz_d_headers[i]], '%Y-%m-%d')
                student.add_quiz(int(row[quiz]), submission_date)
        # Assignment engagement
        if asg_headers != []:
            for i, asg in enumerate(asg_headers):
                submission_date = datetime.strptime(row[asg_d_headers[i]], '%Y-%m-%d')
                student.add_assignment(int(row[asg]), submission_date)

        # Lab engagement         (NOTE: not considered in the engagement score calculation)
        if lab_headers != []:
            for lab in lab_headers:
                student.add_lab(int(row[lab]))
        # Attendance engagement  (NOTE: not considered in the engagement score calculation)
        if attendance_header != []:
            student.add_attendance(int(row[attendance_header[0]]))

        # Midsem exam engagement (NOTE: assume no deadlines)
        if midsem_exam_header != []:
            student.add_midsem_exam(int(row[midsem_exam_header[0]]))
        # Final exam engagement  (NOTE: assume no deadlines)
        if final_exam_header != []:
            student.add_final_exam(int(row[final_exam_header[0]]))

        engagement_scores.append(student.engagement_score)
        failed_assessments.append(student.failed_assessments)
        late_submissions.append(student.late_submissions)
        info.append(student.disengagement_reasons())
        
    df['Info'] = info
    df['Engagement'] = engagement_scores
    df['Failed Assessments'] = failed_assessments
    df['Late Submissions'] = late_submissions
    df['Fail#'] = df['Failed Assessments'].apply(len)
    df['Late#'] = df['Late Submissions'].apply(len)
    df['No Submit#'] = 0
    df['Course'] = 'COMP' + str(course)

    # Sort the DataFrame by the engagement value from lowest to highest
    df = df.sort_values('Engagement')

    # Add a 'Risk' column by dividing the sorted DataFrame into 5 groups of equal size
    df['Risk'] = pd.qcut(df['Engagement'], 5, labels=['Very high', 'High', 'Average', 'Low', 'Very low'])
    
    # Create a new DataFrame with only the 'Uni ID', 'Failed Assessments', and 'Risk' columns
    new_df = df[['Uni ID', 'Course', 'Info', 'Failed Assessments', 'Late Submissions','Fail#', 'Late#', 'No Submit#', 'Engagement', 'Risk']]

    return new_df, get_all_assessments_info(course)