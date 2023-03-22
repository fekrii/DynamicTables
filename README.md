
  <h3 align="center">Dynamic Tables Project</h3>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li>
      <a href="#Notes">Notes</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



This project is a simple Dynamic Table Creation app, it uses Django for backend, docker for deployement , and swagger for api documentaion<br>

you can run it locally, or with docker-compose


you can check the api swagger documentaion from : <i>swagger\/schema/<i/> <br>







<!-- GETTING STARTED -->
## Getting Started

You can run this app locally or with Docker-compose

### Locally


* create virtual environment, and activate it then install the required packages from requirements.txt file
  ```sh
  pip install -r requirements.txt
  ```

* then run the local server 
  ```sh
  pip manage.py runserver
  ```
 
* then open your local server
  ```sh
  localhost:8000
  ```

#### at local host i used SQL lite DB but in production you can use PostgreSQL, you will find it's configuration commented in settings.py file

### Using Docker



* first build docker image
  ```sh
  docker-compose build
  ```

* then run the image
  ```sh
  docker-compose up
  ```
  
* then open the server
  ```sh
  localhost:8000
  ```

<!-- Notes -->
## Notes

<ul>
  <li>superuser account is :
    <ul>
      <li>username: admin</li>
      <li>password: admin</li>
    </ul>
  </li>
  <li>you will find a postman collection with all the requestes and its bodies</li>
</ul>