from setuptools import setup

package_name = "imam"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name, f"{package_name}/IMA_A"],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="dev",
    maintainer_email="niklas.weber2@mailbox.tu-dresden.de",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "console_control = imam.imam:console_control",
            "test = imam.imam:test",
        ],
    },
)
