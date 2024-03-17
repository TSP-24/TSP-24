# Setup the back-end environment
Pull Changes from the Remote Repository:
Your team members should pull the latest changes from the remote repository (GitHub) to ensure they have the latest code, including the back-end setup you've implemented. They can use the following command:

git pull origin backend-setup

## Activate the Virtual Environment:
Navigate to the directory "venv" and run the command below based on your OS:

### On Windows:

** venv\Scripts\activate **

### On Unix or MacOS:

** source venv/bin/activate ** 

## Install Dependencies:
If any new dependencies were added during the setup of the back-end environment, you should install them. You can do this by running:

** pip install -r requirements.txt **

## Run the Flask Application:
After successfully activating the virtual environment and installing dependencies, run the Flask application to ensure everything is set up correctly. You can do this by running the following command:

** python test_Python_Flask_app.py **

![image](https://github.com/TSP-24/TSP-24/assets/110961902/161b47ef-1f37-4bdf-aaa3-b5eb58a449f6)


## Verify Functionality:
Verify that the Flask application is running as expected and you can access any endpoints or functionality you've implemented. Do this by navigating to ** http://localhost:5000 ** in a web browser or using tools like cURL or Postman to make requests to the server. You should see the following

![image](https://github.com/TSP-24/TSP-24/assets/110961902/dfd66861-3158-40bf-a7d5-c6fdd221eed8)
