# WebPageAutotest


Automation test for a web page with an input link to count the number of HTML tags and HTML forms. 

1. For running the test I recommend to use the command "pytest -s testSuite/test_wep_page.py" 

2. Project Structure

It is an OOP autotest. 

-conftest.py - common file for test envirnoment before and after execution. 

-requirement.txt - common file for configurations 

-pytest.ini -  consist of paramtrizing fixtures for this test 

-pages - consist of 1 basic file BasePage and 1 MainPage 

-data - consist the all kind of locators, especially for this project we have selected xpath
