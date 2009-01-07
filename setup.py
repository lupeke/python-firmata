from setuptools import setup, find_packages

setup(
    name = "firmata",
    version = "0.3",
    packages = find_packages(),
    install_requires = ['pyserial>=2.4'],
    author = "laboratorio",
    author_email = "info@laboratorio.us",
    description = "Python bindings for the Firmata protocol",
    license = "GPL v3",
    keywords = "arduino firmata microcontroller ubicomp",
    url = "http://github.com/lupeke/python-firmata/",
    long_description="The aim of this project is to allow developers to communicate with Arduino microcontrollers using Python.",
)