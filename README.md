# Automated_Signup
First step clone the repo in your computer 
    git clone https://github.com/Samman2/Automated_Signup.git

Download python 
    Python 3.14.3 
    py --version 
    To check python is installed successfully 

    Setup Enivroment varaiables

    Then Add python path to system varaiable

Second step open the folder in your editor
In terminal 
    Create and setup enviroment
    python -m venv venv # Create
    venv\Scripts\activate # Setup 

    Install playwright 
    pip install playwright pytest-playwright requests

    Install Chromium for Broswer
    playwright install chromium

    To run the program 
    pytest -s --headed --slowmo 500 signup_automation_script.py


#Note 
    # Otp verification cannot be automated as the otp was sent to the user's phone no and its a manual process
    # ( Correction : not in user's email as the website says Email verification code ) 


Tools and Devices
OS: Windows 11
Python Version: 3.x
Browser: Chromium
IDE: VS Code
Git 