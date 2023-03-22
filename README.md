# teach-ua-python
- - -
### Description :
[Teach Ukrainian](https://speak-ukrainian.org.ua/dev/) website test automation project provides UI, API and DB testing
with Selenium and WebDriver Manager using Page Object Model design pattern.
- - -
### Project structure:
Here you can find a short description of main directories and it's content.
1. *teachua*
    - *base* - super class inherited by each page and component
    - *components* - there are sets of methods which are on the modal windows
    - *database* - there is directory with db-models needed for tests
    - *locators* - there are locators of web elements grouped in classes 
    - *pages* - there are sets of methods which are on the page
2. *tests* - there are sets of tests distributed by different functionalities
3. *utils* - this directory contains files responsible for configuration
- - -
### Main technologies :
|Technology       |Version|
|-----------------|-------|
|Python           |3.8.10 |
|PyTest           |7.2.2  |
|SQLAlchemy       |2.0.7  |
|Selenium         |4.8.0  |
|WebDriver Manager|3.8.5  |
|Allure           |2.20.1 |
- - -
### Prerequisites :
In order to run project, firstly install all libraries :
```
pip install -r requirements.txt
```
After that, on the same folders level create *credentials.ini* file with the following :
```ini
[Admin]
email = email@gmail.com
password = password

[User]
email = email@gmail.com
password = password

[Database]
db_username = database_username
db_password = database_password
db_hostname = database_hostname
db_name = database_name
```
- - -
### Run tests :
Run all tests :
```sh
pytest tests
```
Run specific test :
```sh
pytest tests/test_database.py
```
- - -
### Run allure :
Run test :
```sh
pytest --alluredir=[reports directory path] tests/test_database.py
```
See report of this test :
```sh
allure serve [reports directory path]
```
- - -