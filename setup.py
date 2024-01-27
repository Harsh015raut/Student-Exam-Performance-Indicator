#Builds a package 
from setuptools import find_packages,setup 
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:

    '''This Function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file:
        requirements=file.readlines()
        '''As requirements file has libraries in different lines,when we read it using readlines it also adds '\n',
           so we need to remove this \n.'''  
        requirements = [req.replace("\n","") for req in requirements] 

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Harsh Raut',
    author_email='harsh015raut@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)







