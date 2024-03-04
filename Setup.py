from setuptools import find_packages, setup
from typing import List


hyphen_E = "-e ."
def get_requirements(filepath:str)->List[str]:

    requirements = []
    with open(filepath) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace('\n','') for req in requirements]
        

        if hyphen_E in requirements:
            requirements.remove(hyphen_E)

    return requirements


setup (
    name='mlproject',
    version='0.0.1',
    author='Sharaz Haider',
    author_email='sharazhaider80@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)