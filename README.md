# myToDoList23: Django Web App
## About this project and Goals
I created this to do list web app using freeCodeCamp's Video tutorial and chapters from the textbook I'm currently reading, *Test-Driven Development with Python: Obey the Testing Goat: Using Django, Selenium, and JavaScript* by Harry Percival. I deployed my app using 

#### Goals
1. Gain experience using Python's Django framework and understand basic application structure on the front end and backend.
2. Work on Python, HTML, CSS, and Javascript skills.
3. Create a simple web app that uses database migration, which in this case stores and updates to do list tasks that the user inputs, into a database.
4. Deploy an app onto a cloud platform and get more comfortable using cloud platforms like SalesForces Heroku platform in this app.

## Problems encountered
1. I had to download Heroku's command line interface in order to correctly deploy the app instead of just using Python's heroku libraries.
2. The runtime.txt had the wrong dependencies and versions of libraries after the ```pip freeze > requirements.txt``` command. I had to delete all the links in the runtime.txt file after finding a solution on stackoverflow.
3. Procfile file had to begin with a capital letter and won't be recognized otherwise. This file is imperative in order to deploy on Heroku's platform.
4. You must also disable the static settings in your app in order to deploy on Heroku's platform. This is done by the command `heroku config:set DISABLE_COLLECTSTATIC=1`
