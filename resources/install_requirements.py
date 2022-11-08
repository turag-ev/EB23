"""
Script to install all packages in developer modus + install all online dependencies.

To execute run:

python install_requirements.py
or
python3 install_requirements.py
or
py install_requirements.py

in a command shell from within the EB23 Directory.
"""

import subprocess


def installLocalRequirements():
    with open("requirements_local.txt") as f:
        packages = f.readlines()

    for package_path in packages:
        command = f"pip install -e {package_path}"
        print(f"[INFO] {command}")
        process = subprocess.Popen(command, shell=True)
        process.wait()
        if process.returncode != 0:
            print(f"[ERROR] Could not install {package_path}")


def installOnlineRequirements():
    command = f"pip install -r requirements.txt"
    print(command)
    process = subprocess.Popen(command, shell=True)
    process.wait()
    if process.returncode != 0:
        print(f"[ERROR] Could not install all packages in requirements.txt")


if __name__ == "__main__":
    installLocalRequirements()
    installOnlineRequirements()
