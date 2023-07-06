# HackathonPlatform

Django Rest Backend Api that performs CRUD (Create, Read, Update, Delete) operations.

Python version used : `3.10.6` <br>
Database used : `Sqlite3`   <br>
Built-in database for Django Applications.


## Setup
1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. Make Migrations

To install the required packages
```
pip  install -r requirements.txt
```

For Migrations and start the database
```
python manage.py makemigrations
python manage.py migrate
```

To Run the app
```
python manage.py runserver
```
## API Endpoints
1. GET `/api/hackathons/` - Get all hackathons
2. GET `/api/hackathons/<hackathon_id>` - Get a specific hackathon
3. POST `/api/hackathons/` - Create a hackathon
4. PUT `/api/hackathons/<hackathon_id>` - Update a hackathon
5. DELETE `/api/hackathons/<hackathon_id>` - Delete a hackathon
10. GET `/api/hackathons/user/participate/` - Get all hackathons current user is participating in
14. GET `hackathons/user/atleastone/` -  Get all the users(participants) who have enrolled in atleast one hackathon
15. GET `hackathons/user/notone/` -  Get all the users(participants) who have not enrolled in a single hackathon
