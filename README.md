# *Option Analysis by PITON Thomas and GOV Kévin*

## **Guidelines**

  In order to use the django framework, you have to put a specific virtual environment in your python interpreter.
  
  The file .env in the github is the virtual environment associated to the django project.
  
  To connect this virtual environment to your EDI, you will have to search the root of the project that you cloned on your local machine.

For example if you use Pycharm, this will be the window to select the virtual environment:

![image](https://github.com/user-attachments/assets/9b97c31c-8b11-4d6b-892b-f5908a0396ee)

After configuring this virtual environment, you will open two local terminal and on both terminal you should be on the root of the project using the virtual environment.

Go on the directory "src" by using (cd src) and launch those commands:

On one terminal you launch:
- python manage.py tailwind start

On another terminal you launch:
- python manage.py runserver

![image](https://github.com/user-attachments/assets/7dc008ef-956a-42a1-b899-2aa392211563)

After launching the server you can access to the link by clicking on:  http://127.0.0.1:8000/ 

### Useful tips:
-  If you want to stop the virtual environment you have to press: CTRL + C
-  If you want to change your terminal root, go to settings and change look for terminal and change the directory
  
![image](https://github.com/user-attachments/assets/b9775b5b-ab0f-4160-97f8-1b9cdffdc166)

- Make sure your device have node.js installed if not, follow this link to install npm : https://nodejs.org/fr

  If after installation, you still don't have npm you can change the variable "NPM_BIN_PATH" in the settings.py of the OptionsAnalysis directory
