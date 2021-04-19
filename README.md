# Password-tester application

This is a web-app using the Python flask package that will enable you to open a window on your local machine and test password formatting according to the specifications originally provided in the assignment.

## Steps to run application
1. Install the latest [version](https://www.python.org/downloads/) of python on your machine.
2. clone a local copy of this repo on your computer
3. You can then setup a virtual env in the directory of your cloned repo to store additional package downloads.
    ```
    python -m venv env
    ```
    Then activate the virtual enviornment at the command line according to specifications of your OS. You can reference instructions [here](https://docs.python.org/3/tutorial/venv.html).
4. Install the required packages and modules from the requirements file
    ```
    pip install -r requirements
    ```
5. Once everything is installed, you can run the password_tester module and will be given instructions in your terminal about where the app is being hosted on your local machine.
    ```
    python password-verify.py
    ```
    Should look something like:
    ```
    * Serving Flask app "password-verify" (lazy loading)
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: on
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 295-082-906
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```
    Simply navigate with your browser to where the app is running. In this example, that's locally at http://127.0.0.1:5000/.

## Testing
You can run the unittests in the command line with the following command:
```
python test.py -v
```