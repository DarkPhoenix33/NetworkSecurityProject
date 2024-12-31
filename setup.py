from setuptools import find_packages,setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #Process the lines
            for line in lines:
                requirement=line.strip()
                #Remove empty lines
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requiments.txt file does not exist")

    return requirement_lst 

setup(
    name="NetworkSecurityProject",
    version="0.0.0.1",
    author="M Faizan Shabbir",
    packages=find_packages(),
    install_requires=get_requirements()

)

