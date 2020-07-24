## Deploying ML Model using Flask
This is a simple project to elaborate on how to deploy an "Automatic Ticket Management" Machine Learning model using Flask API

### Project Structure
This project has four major parts :
1. main.py - This contains code for our Machine Learning model to predict the ticket assignment to a group.
2. app.yaml - This is useful in order to deploy the application to Google cloud app engine.
3. templates - This folder contains the HTML template (index.html) to allow user to enter ticket description and displays the group assignment.
4. static - This folder contains the css folder with style.css file which has the styling required for out index.html file.
5. models - This folder contains the pre trained Machine Learning models.

### Running the project
1. Run main.py using below command to start Flask API
```
python main.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000

You should be able to view the homepage.

Enter valid ticket description in the input boxe and hit Predict. You should  be able to see the predcited Group Assignment!
check the output here: http://127.0.0.1:5000/predict

