# python-projects

> My python repo

## How to setup

> I put this repository at: C:/Source, and using VSCode as editor

1. Clone this repository using git or Github Desktop
2. Install Python virtual environment using `pip install virtualenv`
3. Locate this repository parent's directory (for me, it is at `cd C:/Source`)
4. Setup virtual environment for this project `virtualenv <the project folder name>` (<> the tag not include)
   1. Eg: `virtualenv python-project`
5. Open the project folder using VSCode
   1. If you already install VSCode and add it in to PATH,
   2. run this command: `code python-project`
6. When VSCode is opened, click on the `setup.py` file
7. You will see the Python version at the bottom right of VSCode
8. Click on the version number, and select to the virtual environment's Python
   1. If it is not show at the dropdown list
   2. Locate it in the `Scripts/python.exe`
9. And it will show up like: `3.9.13 ('python-projects':venv)`
10. Press `F1` on your keyboard, and search for `Python: Create Terminal`
11. The terminal will start and it will show as: `(python-projects) PS C:\Source\python-projects>`
12. Run the command in the terminal: `pip install -r requirements.txt`
13. Last, Run the `setup.py` for create the important directory.

> Contact me if you meet any issue.