import os
import pandas as pd
from datetime import datetime


def create_data_folder_if_not_exists():
    # Check if the data folder exists, if not, create it
    data_folder = "fakedatafolder"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)


def read_data_file(new_data_file):
    # Read the new data file, handling both CSV and Excel formats
    try:
        if new_data_file.lower().endswith('.csv'):
            return pd.read_csv(new_data_file)
        elif new_data_file.lower().endswith(('.xls', '.xlsx')):
            return pd.read_excel(new_data_file)
        else:
            print("Unsupported file format. Please provide a CSV or Excel file.")
            return None
    except pd.errors.EmptyDataError:
        print(f"Warning: The file {new_data_file} is empty. ")
        return None
    except Exception as e:
        print(f"Error: An error occurred while reading the file {new_data_file}.")
        print(e)
        return None


def update_data_file(new_data, data_path):
    # Read the old data file
    old_data = pd.read_csv(data_path)

    # Update the data
    all_data = pd.concat([new_data, old_data])

    # Sort the data by 'Downloaded' column in descending order
    all_data_sorted = all_data.sort_values(by='Downloaded', ascending=False)

    # Drop duplicates based on 'Uni ID', keeping the first occurrence (which has the latest 'Downloaded' timestamp)
    updated_data = all_data_sorted.drop_duplicates(subset=['Uni ID'], keep='first')

    updated_data = updated_data.sort_values(by='Uni ID', ascending=True)

    # Write the updated data to the old data file
    updated_data.to_csv(data_path, index=False)
    print('successfully updated')

def delete_file(file_path):
    # Delete the file if it exists
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} deleted.")


def update_student_data(new_data_file, file):
    create_data_folder_if_not_exists()
    file_name, _ = os.path.splitext(file)
    data_path = os.path.join("fakedatafolder", file_name + '.csv')

    # Create an empty CSV file if it doesn't exist
    if not os.path.exists(data_path):
        new_data = read_data_file(new_data_file)
        if new_data is not None:
            new_data.to_csv(data_path, index=False)
    else:
        # Read the new data file
        new_data = read_data_file(new_data_file)
        if new_data is not None:
            # Update the data file
            update_data_file(new_data, data_path)
            # Delete the input file

    delete_file(new_data_file)


# Example usage
#update_student_data("newfiles/COMP2400.xlsx", "COMP2400.xlsx")
