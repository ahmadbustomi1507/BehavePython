----------------------------------------------------------------------
AUTOMATION TEST WITH BEHAVE PYTHON
----------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------
About:
---------------------------------------------------------------------------------------------------------
Running automation test by BDD style using Behave python

---------------------------------------------------------------------------------------------------------
Requirements:
---------------------------------------------------------------------------------------------------------
- Python 3.5 or above, recommended 3.10 (please include pip installation)

---------------------------------------------------------------------------------------------------------
INSTALLATION
---------------------------------------------------------------------------------------------------------
1. Running in CLI:
	- pip install behave 
	- pip install allure-behave
	- pip install asyncio
	- pip install bs4
	- pip install cx-Oracle
	- pip install mysql
	- pip install requests
	- pip install httpx

2. install Allure via powershell by executing (please refer to https://scoop.sh/)
	- scoop install allure
   
---------------------------------------------------------------------------------------------------------   
HOW TO RUN
---------------------------------------------------------------------------------------------------------
Execute the test

	> behave -f allure_behave.formatter:AllureFormatter -f pretty -o <output folder> <feature> --tags=<name_of_tags> --no-capture 
   
	for example:
		> behave -f allure_behave.formatter:AllureFormatter -f pretty -o results .\test\SIT_630_BDD\SIT_646_Demo_Scenario.feature --no-capture
	
Show the results into host 
	> allure serve results -h <host> -p <port> 

	for example :
		> allure serve results -h localhost -p 8080

To publish the report 	
	> allure generate results -o results_25042022
	
	currently we are using this https://github.com/MihanEntalpo/allure-single-html-file
	to generate into one single html 
	> python combine.py results
	
	
---------------------------------------------------------------------------------------------------------	
Overview
---------------------------------------------------------------------------------------------------------

Structure of the project:

src -
	|- API 
	|
	|- test - | 
	|		  | - <Project name>-|
	|								|- steps-|
	|								|		 |- <service name>_steps.py
	|								|
	|								|- environtment.py
	|								|- <service name>.feature 
	|
	|
	|- tools
	|
	|- behave.ini


API
	Place the API Abstraction in here, the structure must be in a method , to be called by steps 
test 
	Place the test suite of each project here 
tools
	Put the IP port , api endpoint definition or any other static information in here, including
	for the query method 
behave.ini
	special file to determine how behave will be executed, please refer to the documentation
	
---------------------------------------------------------------------------------------------------------
Sample of Test 	
---------------------------------------------------------------------------------------------------------
In BDD style we configure each procedure in the test case as a method , in general these are the flow
of the test in the BDD

- environtment.py / before_feature(...)
	This special method will always be run ONCE in every *.feature file, it will be used to get all of the
	external data from table (query table) , and saved into a variable
	
- environtment.py / before_scenario(...)
	This Special method will always be run ONCE in every scenario inside *.feature file, currently this function
	will be replaced by Background

- *.feature

	Feature : name of feature 

		Background : Some background
			Given User prepared the list of data from external 
			    |scenario_id|scenario_name |msisdn |
				|.          |.             | .     |

		Scenario : name of Scenario  
			Given User using data  <msisdn>
			When  User hit the API with payload
			Then  User successfully hit the API with status code 200
	
	
- environtment.py / after_scenario(...)
	This special method will be run once in every after scenario  is done . It will be used to reset the target number
	as before running the test
	
- environtment.py / after_feature(...)
	This special method will be run after the feature is done. it will be planned to hit JIRA API, so the final result
	will be integrated with JIRA



