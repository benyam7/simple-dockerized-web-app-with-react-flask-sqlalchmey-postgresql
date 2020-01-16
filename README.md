#Simple-dockerized-app-with-react-flask-sqlalchemy-postgres
- Simple dockerized app made with react, flask, sqlalchemy and postgresql, to demonsrate benefits of running on separate containers, and to implement the concept of microservices.

## Features

- flask rest api
- this app has 3 independent services, runnning on separate ports
  1. headline news service
  2. buisiness news service
  3. sport news service

- all 3 services has GET and POST request methods implemented

- with hot reloading

## setup
- change your database name and password in each config.py file which inside all the 3 directories
- change your databse name, password and user name in docker-compose.yml file

## Running
- open the file in terminal window and run 

``` docker-compose up --build ```


## Made with ❤
