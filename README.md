[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Repository for [Eurobot 2023](https://www.eurobot.org/eurobot-contest/eurobot-2023/) Software Development

## Requirements
### Windows
1. Install [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) 
2. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
3. Install [Git](https://git-scm.com/download/win) (take care that GIT Bash will also be installed)
4. Reboot (if not already done)
5. Install [VcXsrv](https://sourceforge.net/projects/vcxsrv/)
6. Start XLaunch App --> click: Next --> Next --> Tick all Checkboxes --> Finish
7. Allow access to all networks when Windows Defender asks

### Ubuntu (native)
1. Install [Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
2. Follow [post installation steps](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) to use docker without root  
3. Log in and out again
4. Test with `docker run hello-world`
5. Install Git `sudo apt install git`

### Ubuntu (WSL2)
0. If you do not use Win11 follow all steps under the Windows section
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Activate your Ubuntu instance inside Docker Desktop: Settings --> Resources --> WSL Integration
3. Steps also described [here](https://docs.docker.com/desktop/windows/wsl/)
4. Install Git `sudo apt install git-all`

## Setup
0. Install the VSCode [Docker Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) and the [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) 
1. Clone this repository
    ```
    git clone https://github.com/turag-ev/EB23.git
    ```
2. Open VSCode and start a Terminal (on Windows this has to be a GIT Bash --> can be selected in the dropdown menu near the plus icon at the top right terminal window).
3. Change to EB23 directory via `cd EB23`
4. Run `./build_container.sh` --> if done for the first time it takes a while (5min)
5. After building was successfull run `./start_container.sh`

**Success!**  
You are now running your own development environment inside a container
You can now [attach an VSCode instance to the Container](https://code.visualstudio.com/docs/devcontainers/attach-container#_attach-to-a-docker-container) to develop inside it. All changes made inside the workspace folder will be mirrored to the host system.

Make sure to regularly check whether new packages/ requirements were added and if so repeat the building process of the Docker container.  

**Attention:** If you use Windows you need to start Docker Desktop and XLaunch (with the same settings) again after every shutdown of your PC.

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

## Logger (CURRENTLY BROKEN FOR EB23)

  
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




