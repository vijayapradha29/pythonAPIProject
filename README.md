# Python API Automation Framework
    Hybrid Custom Framework to test the REST APIs

### Tech Stack
    1.Python 3.12.6
    2.Requests-HTTP Requests
    3.PyTest-Testing Framework
    4.Reporting-Allure Report,PyTest HTML
    5.Test Data-CSV,Excel,JSON
    6.Parallel Execution-X Distribute

### How To Install Packages:
``pip install requests pytest pytest-html faker allure-pytest jsonschema``

### To Freeze Your Package Version:
``pip freeze > requirements.txt``

### To Install the Freeze Version:
``pip install -r requirements.txt``

### How To Run your test cases Parallely:
``pip install pytest-xdist``

``pytest -n auto .\tests\integration_test\test_create_booking_negative.py -s -v``

### To Work with the Excel File:
``pip install openpyxl``
### To work with Json Schema:
``pip install jsonschema``