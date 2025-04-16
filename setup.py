from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
    return requirements
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='Sensor Fault Detect',
    version='0.0.1',
    author='Anushka',
    author_email='anushkashelke19@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
    
)
#(C:\Users\HP\Desktop\Pwskill\pwskill) C:\Users\HP\Desktop\Pwskill>pip list - environment path

#MongoDB user name :anu
# password: 171201
# url :mongodb+srv://anu:<db_password>@cluster0.wy20ogo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
# python -m pip install "pymongo[srv]"
# mongodb+srv://anu:171201@cluster0.wy20ogo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0