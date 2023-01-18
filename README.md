# django-otp-login
tack stack: python, django

#### description
A simple django project with sign-up and login functionality, user can log in with the otp. 
In this project we have implemented simple otp based authentication (stored otp as plain text).
we can secure this by encrypting or hashing the otp.


### To run this project follow the billow steps from the root dir

1. Create a virtual environment
2. Run this `pip install -r requirements.txt` this will install all the requirements.
3. Once requirement is installed then make sure to create mysql database with 'custom-auth' name.
4. Run this command to created tables in a database `python manage.py migrate`
5. once above all steps are done. Run `python mange.py runserver` to serve this project locally.
