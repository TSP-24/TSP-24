import pandas as pd
from student import Student
from csv_parser import filter_headers

def calculate_engagement(csv_file, csv_name):
    df, headers, weights, course = filter_headers(csv_file, csv_name)
    # Singular items
    id_header, final_exam_header, midsem_exam_header, attendance_header = None, None, None, None
    # Items with multiple iterations
    asg_headers, quiz_headers, lab_headers = None, None, None
    if len(headers['uni_id']) >= 1:
        id_header = headers['uni_id'][0]
    if len(headers['final_exam']) >= 1:
        final_exam_header = headers['final_exam'][0]
    if len(headers['midsem_exam']) >= 1:
        midsem_exam_header = headers['midsem_exam'][0]
    if len(headers['assignment']) >= 1:
        asg_headers = headers['assignment']
    if len(headers['quiz']) >= 1:
        quiz_headers = headers['quiz']
    if len(headers['lab']) >= 1:
        lab_headers = headers['lab']
    if len(headers['attendance']) >= 1:
        attendance_header = headers['attendance'][0]
    
    info = []
    engagement_scores = []
    uids = []
    failed_assessments = []

    for index, row in df.iterrows():
        # Create student object
        if id_header != None:
            student = Student(row[id_header])
        else: student = Student('u' + str(10000000+index))
        # Set the weights (Not yet implemented)
        # student.set_weights(weights)

        # Quiz engagement
        if quiz_headers != None:
            for quiz in quiz_headers:
                student.add_quiz(int(row[quiz]))
        # Assignment engagement
        if asg_headers != None:
            for asg in asg_headers:
                student.add_assignment(int(row[asg]))

        # Lab engagement
        if lab_headers != None:
            for lab in lab_headers:
                student.add_lab(int(row[lab]))
        # Attendance engagement
        if attendance_header != None:
            student.add_attendance(int(row[attendance_header]))

        # Midsem exam engagement
        if midsem_exam_header != None:
            student.add_midsem_exam(int(row[midsem_exam_header]))
        # Final exam engagement
        if final_exam_header != None:
            student.add_final_exam(int(row[final_exam_header]))

        engagement_scores.append(student.engagement_score)
        uids.append(student.uni_id)
        failed_assessments.append(student.failed_assessments)
        info.append(student.disengagement_reasons())
        
    # Append the engagement scores to the dataframe and add uid column (if neccessary)
    if 'Uni ID' not in df.columns:
        df.insert(0, 'Uni ID', uids)
        
    df['Info'] = info
    df['Engagement'] = engagement_scores
    df['Failed Assessments'] = failed_assessments
    df['Fail#'] = df['Failed Assessments'].apply(len)
    df['Late#'] = 0
    df['No Submit#'] = 0
    df['Course'] = 'COMP' + str(course)

    # Sort the DataFrame by the engagement value from lowest to highest
    df = df.sort_values('Engagement')

    # Add a 'Risk' column by dividing the sorted DataFrame into 5 groups of equal size
    df['Risk'] = pd.qcut(df['Engagement'], 5, labels=['Very high', 'High', 'Average', 'Low', 'Very low'])
    
    # Create a new DataFrame with only the 'Uni ID', 'Failed Assessments', and 'Risk' columns
    new_df = df[['Uni ID', 'Course', 'Info', 'Failed Assessments', 'Fail#', 'Late#', 'No Submit#', 'Engagement', 'Risk']]

    return new_df