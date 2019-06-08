import os
import testings_example
from setuptools import setup, find_packages

def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    with open(filename, 'r') as f:
        return f.read()

setup(
    name = 'testings_example',
    version = testings_example.__version__,
    author = 'Adriano',
    author_email = 'ry@gmail.com',
    description = 'test',
    license = 'BSD',
    keywords = 'testings,and,more',
    url = 'https://gitlab.com/adrianohrl/testings_example',
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