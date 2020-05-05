# Repo4U

It's a mini ``GitHub Repository Recommender`` that uses a collaborative filtering type to provide new users a recommendation of the list of repositores they might like given the list of repo or language or tools or libraries etc., they already like.

Wanna play with my project go to the link: https://repo4u.herokuapp.com/

## Project Diagram

![images](assets/project-diagram.png)

## Requirements

**Note**: The main requirement is only **``pip``** and **``pipenv``**. After that ``pipenv`` install all dependencies for you by running **``pipenv install``** command.

+ pipenv
+ python
+ flask
+ gunicorn
+ pandas
+ scikit-learn==0.21.3

## Local Run

Six Simple Steps to run-app locally:
  1. ``Clone`` the repository using **``git clone <link of the repository> ``** command
  2. Change your directory to the root directory of the project
  3. Run **``pipenv install``** (it will install all the dependencies and create a virtual environment for you)
  4. Run **``pipenv shell``** (to activate the virtual environment)
  5. Then run **``python wsgi.py``** (to run your flask server)
  6. Go-to: **http://127.0.0.1:5000/** (to see app running in your local host)

## Competition Page
[Click Here](https://devhacks.deta.dev/challenge)

## Team Detail

**Team ID**: 4242a3aec90c7439453bb6254000b1324879 <br/>
**Team Name**: DevDevil <br/>
**Team Member**: [Sushil Singh](https://github.com/OddExtension5) & [Harsh Sinha](https://github.com/justarandomcontributor)

## Copyright & License
Copyright (c) 2020 Repo4U - Released under the [MIT license](https://github.com/OddExtension5/repo-recommender/blob/master/LICENSE). 

