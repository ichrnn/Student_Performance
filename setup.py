from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        requirements = [req for req in requirements if not req.startswith('-e ')]

    
    return requirements

setup(
name= 'Student_performance',
version='0.0.1',
author='Charan',
author_email='schrnpendyala@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)

