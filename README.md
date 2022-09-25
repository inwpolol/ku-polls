## Online Polls for Kasetsart University

An application for conducting a poll or survey, written in Python using Django. It is based on the [Django Tutorial project](https://docs.djangoproject.com/en/4.1/intro/tutorial01/), with additional functionality.

This application is part of [the Individual Software Process](https://cpske.github.io/ISP/) course at [Kasetsart University](https://ku.ac.th).

## How to Install and Run

1. Clone this github repository.
2. Change file mysite/sample.env to mysite/.env
3. Create a virtual environment.
* create the virtual env in "env/", only 1 time.
    ```
    python -m venv env
    ```
* start the virtual env in bash or zsh.
    ```
    . env/bin/activate
    ```
* install required packages.
    ```
    pip install -r requirements.txt
    ```

4. Run migrations.
    ```
    python manage.py migrate
    ```

5. Install data from the data fixtures.
    ```
    python manage.py loaddata data/polls.json data/users.json
    ```

6. Run server.
    ```
    python manage.py runserver
    ```

7. Open web application on
http://localhost:8000/polls/ or control+click at suggestion url http://127.0.0.1:8000/

Note: You can create admin account to manage your polls by
```
python manage.py createsuperuser
```
and go to http://localhost:8000/admin

## User Demo

| Username  | Password  |
|-----------|-----------|
|   demo1   | testpass1 |
|   demo2   | testpass2 |

## Project Documents

All project documents are in the [Project Wiki](https://github.com/inwpolol/ku-polls/wiki)

* [Vision Statement](https://github.com/inwpolol/ku-polls/wiki/Vision-Statement)
* [Requirements](https://github.com/inwpolol/ku-polls/wiki/Requirements)
* [Project Plan](https://github.com/inwpolol/ku-polls/wiki/Development-Plan)
* [Iteration 1 Plan](https://github.com/inwpolol/ku-polls/wiki/Iteration-1-Plan) and [Task Board 1](https://github.com/users/inwpolol/projects/2/views/1?filterQuery=iteration%3A1)
* [Iteration 2 Plan](https://github.com/inwpolol/ku-polls/wiki/Iteration-2-Plan) and [Task Board 2](https://github.com/users/inwpolol/projects/2/views/3?filterQuery=iteration%3A2)
* [Iteration 3 Plan](https://github.com/inwpolol/ku-polls/wiki/Iteration-3-Plan) and [Task Board 3](https://github.com/users/inwpolol/projects/2/views/5?filterQuery=iteration%3A3+&layout=board)
* [Iteration 4 Plan](https://github.com/inwpolol/ku-polls/wiki/Iteration-4-Plan) and [Task Board 4](https://github.com/users/inwpolol/projects/2/views/6?layout=board&filterQuery=iteration%3A4)