# TSP-24
Tracking Student Progress and Identification of Students at Risks






# Data Upload and Update

The only data we need to write repeatedly is the student data from a specific course.
This can be done manually by clicking the upload data button in the application.
In the local database, we should have different CSV files with the names of the
different courses.

When reading files, the program should first locate the folder with the same name
in the database. Then compare the uid of the new file with the uid of the old file
one by one. When the uid of the new file does not appear in the old file of the
database, the new data is directly written in. When the uid of the new file also
appears in the old file, compare the download date of the new file and the database
file change entry, such as the new If the date of the file is updated, the entry in the
database file will be overwritten, otherwise, it will not be processed.

This script provides a utility to upload and update student data stored in CSV or Excel files.

## Usage

1. **Function**: `update_student_data(new_data_file)`

   This function updates the student data based on the new data provided in the specified file.
   
   - `new_data_file`: Path to the file containing new student data. Supported formats are CSV and Excel (XLS/XLSX).

2. **Example Usage**:

   ```python
   update_student_data("COMP2400.xlsx")
   ```

   This will update the existing student data with the contents of the "COMP2400.xlsx" file.

## Requirements

- Python 3
- pandas
- xlrd (if using Excel files)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your_username/your_repository.git
   ```

2. Navigate to the project directory:

   ```
   cd your_repository
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```
## Demo
<video id="video" controls="" preload="none" poster="封面">
      <source id="mp4" src="demo/writefirsttime.mp4" type="video/mp4">
</video>

<video id="video" controls="" preload="none" poster="封面">
      <source id="mp4" src="demo/update.mp4" type="video/mp4">
</video>

## License

This project is licensed under the MIT License 
