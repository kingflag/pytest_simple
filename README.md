# pytest_simple

## intall python

    windows 
    ```bash
    winget install python3.11
    ```

    linux/macos
    ```bash
    sudo apt-get install python3.11
    ```
    check if python is installed by typing python in the terminal. if you can see the python version, then python is installed. if not, then you need to add python to path if not added automatically.

## create requirements.txt file
 this file will contain all the dependencies of the project. It will be used to install the dependencies of the project. 

## create venv
```bash
python -m venv venv
```
  this will create a virtual environment in the venv folder. all dependencies will be installed in this folder. and will not be installed in the global environment.

### activate venv

linux/macos
```bash
source venv/bin/activate
```

windows powershell
```bash
.\venv\Scripts\activate.ps1
```
  this will activate the virtual environment. 
  if you can see (venv) in the terminal, then the virtual environment is activated.
  if not,you need grant execute permission to the activate.ps1 file.
  ```powershell
  Get-ExecutionPolicy -Scope CurrentUser
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  Remove-Item -Recurse -Force venv
  python -m venv venv
  ```
### exit venv
```bash
deactivate
```
  this will exit the virtual environment.


## install dependencies in the venv
```bash
pip install -r requirements.txt
```
  this will install all the dependencies in the requirements.txt file. and will be installed in the venv folder. and will not be installed in the global environment.

## add tests in the tests folder. and run tests.
```bash
pytest .\python_test_case.py
```