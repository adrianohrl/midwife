import os
import midwife
from setuptools import setup, find_packages

def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    with open(filename, 'r') as f:
        return f.read()
    
def get_files(path):
    return [(parent, [os.path.join(parent, file) for file in files]) for parent, _, files in os.walk(path)]

setup(
    name = 'midwife',
    version = midwife.__version__,
    author = 'Adriano Henrique Rossette Leite',
    author_email = 'contact@adrianohrl.tech',
    description = 'This is a tool for automaticly generating data science projects based on its metadata.',
    license = 'BSD',
    keywords = 'Automated, Data Science, Project, Generation',
    url = 'https://gitlab.com/adrianohrl/midwife',
    packages = find_packages(),
    long_description = read('README.md'),
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operational System :: Independent',
        'Topic :: Data Science Project',
        'License :: OSI Approved :: BSD License',
    ],
    data_files = get_files('templates'),
    entry_points = {
        'console_scripts': [
            'midwife_generate = midwife.generate:main',
        ],
    },
)