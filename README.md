[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Repository for [Eurobot 2023](https://www.eurobot.org/eurobot-contest/eurobot-2023/) Software Development

## Setup
Clone this repository
```
git clone https://github.com/turag-ev/EB23.git
```
Open the console of your choice in the newly created directory and install all necessary dependencies
with the help of our python script. 
```
py install_requirements.py
or
python install_requirements.py
or
python3 install_requirements.py
````

Make sure to regularly check whether new packages/ requirements were added and if so repeat installing the requirements.
VS Code might not show your import as valid, however it works. If you'd like to have vs code accept the import, add it to path by hovering over the import and execute the suggested quick fix.

**_NOTE:_** In the future this will be handled via docker images. This is a temporary solution.

## Structure
Please make sure to follow the following given structure when working on your modules

<details>
  <summary>Click me</summary>

    
    EB23                                        -> parent directory of this repository
    │   .gitignore
    │   install_requirements.py
    │   LICENSE
    │   README.md
    │   requirements.txt
    │   requirements_local.txt
    │
    └───workspace                               -> global workspace
        ├───python_packages                     -> workspace for python only packages
        │   │   README.md
        │   │
        │   ├───Helpers                         -> subdirectory for helper packages
        │   │   ├───Logger
        │   │   |   │   LICENSE
        │   │   |   │   pyproject.toml
        │   │   |   │   README.md
        │   │   |   │
        │   │   |   └───src
        │   │   |       └───Logger
        │   │   |               Logger.py
        │   │   |               __init__.py
        │   │   |
        │   │   └...                            -> more helper packages (Enumerations,...)
        │   │
        │   ├───InternalMechanics               -> subdirectory for IM python packages
        │   │   │   README.md
        │   │   │
        │   │   └───IMA_Interface
        │   │       │   LICENSE
        │   │       │   pyproject.toml
        │   │       │
        │   │       └───IMA_Interface
        │   │               interface.py
        │   │               __init__.py
        │   │
        │   └───...                             -> more subdirectories (Pathfinding, Gameplanning, ...)
        │
        └───ros_packages                        -> workspace for ros packages
            │   README.md
            │
            └───src
                ├───IMAM                        -> ros package (InternalMechanicsActionsManager)
                |       .gitkeep
                |
                └───...                         -> more ros packages
    

</details>

After making sure your package is installable, add it to the `requirements_local.txt` file with its relative path from said file to your package's `setup.py`.  
Furthermore, add all dependencies having to be installed from online sources (openCV or anything pip install) that are 
not already handled in your `setup.py` files or your package's `requirements.txt` to the main `requirements.txt` file
in the root directory.  
A guide on how to create [Python](https://intern.turag.de/wiki/doku.php?id=050_software:anleitungen:creating_python_packages) and [ROS packages](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html) is on the TURAG Wiki.

## Code Styling
This repository follows [PEP 8 guidelines](https://peps.python.org/pep-0008/) guidelines on formatting and writing code. Formatting has to be done with the python 
[black](https://pypi.org/project/black/) linter. Specific code guidelines for this project are provided in a [code styling entry](https://intern.turag.de/wiki/doku.php?id=01_eurobot:eurobot_2023:code_styling_guidelines) on our TURAG Wiki.

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




