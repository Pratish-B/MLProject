from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> list[str]:
    """
    This function reads a file and returns a list of requirements.
    """
    requirements= []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="MIPROJECT",
    version="0.1",
    author="Pratish-B",
    author_email="pratishchaitanya1@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt"),
    )