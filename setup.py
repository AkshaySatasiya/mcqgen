from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Akshay Satasiya',
    author_email='akshaysatasiya2811@gmail.com',
    install_requirement = ['openai','langchain','streamlit','python-dotenv','PyPDF'],
    packages=find_packages()
)