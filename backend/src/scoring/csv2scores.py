from student import Student
from csv_parser import filter_headers
import csv

def calculate_engagement(csv_file):
    df, headers, weights = filter_headers(csv_file)
    df['Engagement'] = 0
    df.to_csv(csv_file, index=False)
