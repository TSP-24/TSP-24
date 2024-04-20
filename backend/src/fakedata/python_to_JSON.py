import csv
import json


def csv_to_json(csv_file, json_file):
    data = {}
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            course_id = row['CourseID']
            course_name = row['Course Name']
            convenor = row['Convenor']
            assessment = {
                'Assessment': row['Assessment'],
                'Type': row['Type'],
                'Due': row['Due'],
                'Mark': row['Mark']
            }
            key = (course_id, course_name, convenor)
            if key not in data:
                data[key] = {
                    'CourseID': course_id,
                    'Course Name': course_name,
                    'Convenor': convenor,
                    'Assessments': []
                }
            data[key]['Assessments'].append(assessment)

    with open(json_file, 'w') as jsonfile:
        jsonfile.write(json.dumps(list(data.values()), indent=4))


# Example usage
csv_to_json('data.csv', 'data.json')