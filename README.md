[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Repository for Eurobot 2023 Software Development

## Setup
Clone this repository
```
git clone https://github.com/turag-ev/Eurobot-2023.git
```
Open the console of your choice in the newly created directory and install all necessary dependencies
```
pip install -r requirements.txt
pip install -r requirements_local.txt
```

Make sure to regularly check whether new packages/ requirements were added and if so repeat installing the requirements.

**_NOTE:_** In the future this will be handled via docker images. This is a temporary solution.

## Structure
Please make sure to follow the following given structure when working on your modules

```
.
│   .gitignore
│   LICENSE
│   README.md
│   requirements.txt
│   requirements_local.txt
│
└───workspace                           
    └───src
        │
        ├───InternalMechanics           -> example: InternalMechanics consisting of three packages
        │   │   README.md               -> README explaining general content of Module
        │   │
        │   ├───Actors                  -> ROS package 
        │   │
        │   ├───IMAM                    -> ROS Node
        │   │
        │   └───IMA_Interface           -> Python Package following python package structure       
        │
        ├───More Modules                -> General modules: CentralTracking, Pathfinding, InternalMechanics ...
        │
        └───...
```
After making sure your package is installable, add it to the `requirements_local.txt` file with its relative path from said file to your package's `setup.py`.  
Furthermore, add all dependencies having to be installed from online (openCV or anything pip install) to the `requirements.txt` file.  
A guide on how to create Python and ROS packages will follow on the TURAG Wiki.

## Code Styling
This repository follows [PEP 8 guidelines](https://peps.python.org/pep-0008/) guidelines on formatting and writing code. Formatting has to be done with the python 
[black](https://pypi.org/project/black/) linter. A guide on specific coding guidelines will follow on the TURAG Wiki.

## Logger
Last year one of our members created a logging module allowing us to easily create and store logging messages from within our code.
It contains multiple log levels:
- DEBUG: smallest logging steps on any small process (for example: moving arm from x to y)
- INFO: information for example when tasks are done/ started
- WARN: when something did not go as it was supposed to
- ERROR: major conflict could cause program to stop

These logs are useful for recreating what happened when executing your code and helps debugging.

Example:
```python
import Logger
logger = Logger.get_logger()

#print with Debug Level:
logger.debug("Hello")
#print with INFO Level:
logger.info("Hello")
#print with WARN Level:
logger.warn("Hello")
#print with INFO Level:
logger.error("Hello")
```

By standard everything starting from the INFO level will be saved into a .log file. This can be changed when initializing the logger.
```python
import Logger
# returns every log level
logger = Logger.get_logger(level=Logger.DEBUG)

# returns all log levels starting and including warn (warn and error
logger2 = Logger.get_logger(level=Logger.WARN)
```




