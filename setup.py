from networkx import is_path
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:

    """This function returns a list of requirements from the given file path."""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
setup(
    name="mlproject",
    version="0.1.0",
    author="Shivam Mohite",
    author_email="shivammohite2020@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),

)

