import setuptools

from distutils.core import setup
from os.path import join, dirname

with open(join(dirname(__file__), 'requirements.txt'), 'r') as f:
    install_requires = f.read().split("\n")

setup(
    name='rubix-rest-client',
    version='v1.0.0',
    packages=['rubix', 'rubix.utils'],
    url='https://github.com/NubeIO/rubix-rest-client-python',
    license='',
    author='ap',
    author_email='ap@nube-io.com',
    description='nube api cli'
)
