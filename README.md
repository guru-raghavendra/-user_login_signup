# user_login_signup

an API built using Django Rest Framework and MySQL which checks if user does not exist then take all the user related data and store it in mysql DB 
and API which is used for login of exisiting user and shows msg logged in successfully.

## API endpoints.
1. **django admin** <br>
    ```http://127.0.0.1:8000/admin``` fot django admin
    
2. **signup** <br>
    Make a POST request to ```http://127.0.0.1:8000/users_api/signup/``` with data in the JSON format to add an user details
    ```json
    {
        "name":"test8",
        "email" : "test8@gmail.com",
        "password":"1234"
    }
    ```
    - after successful login **_login details_** will be given <br>
    - if the user alread exists, **_already exist... try loging in_** message will be given <br>
    
2. **login** <br>
    Make a POST request to ```http://127.0.0.1:8000/users_api/login/``` with data in the JSON format to login
    ```json
    {
        "email" : "test8@gmail.com",
        "password":"124"
    }
    ```
    
    - if user exists and the credentials are correct, **_login successful!!_** message is given.
    - if user exists and the credentials are incorrect, **_invalid credentials_** message is given.
    - if the user don't exits **_\<email\> user does not exist... try sign up_** message is given.
