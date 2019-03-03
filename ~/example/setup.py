import os
import example
from setuptools import setup, find_packages

def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    with open(filename, 'r') as f:
        return f.read()

setup(
    name = 'example',
    version = example.__version__,
    author = 'Adriano Henrique Rossette Leite, Henrique Rossette Leite',
    author_email = 'contact@adrianohrl.tech, me@adrianohrl.tech',
    description = 'This is an example.',
    license = 'BSD',
    keywords = 'project,generator,example',
    url = 'https://gitlab.com/adrianohrl/example',
    packages = find_packages(),
    install_requires = read('requirements.txt').split('\n'),
    long_description = read('README.md'),
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operational System :: Independent',
        'Topic :: Data Science Project',
        'License :: OSI Approved :: BSD License',
    ],
)