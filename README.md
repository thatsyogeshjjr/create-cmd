# Create Command
Automate your project's initial steps with create-cmd
that includes:
* Create a folder for the project
* Creating a git repo
* Adding remote to that repo
* First initial commit

## Setup
**for powershell**
* clone the repo and note its path using `pwd`
* create .env file and type your username & password
`
notepad .env
`
* Inside the .env type:
		
		USER='<your username>'
		PASS='<your password>'
* Save the .env in folder with app.py
* open Poweshell's profile
`notepad $PROFILE`
* add the following lines
```
function create {<path\to\create-cmd>\env\Scripts\python.exe <path\to\create-cmd>\app.py $args[0]}
```
* Reopen powershell
* Setup complete
* `Note: This project is for firefox, I also assume you already have the geckodriver in folder(hooked up with env variables) `

# Using the create command

* Go to the desired folder
* Type `create <project name>`

 
## Packages used
* Selenium
* os
* sys
* dotenv

Inspired by Hallden
