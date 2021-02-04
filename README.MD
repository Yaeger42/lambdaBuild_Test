# How to run the tests locally:
In the root folder, create a new virtual environment with this command
```$ python3 -m venv venv``` 
After that, run the following command to activate the virtual environment:
```$ source venv/bib/activate``` 
Once that's activated, navigate to the ```src``` folder and run this command to install the required dependencies
```(venv)$ pip3 install -r requirements.txt ``` 

Once that's installed go back to the root folder and run: 
```$ python3 -m unittest discover -v ```