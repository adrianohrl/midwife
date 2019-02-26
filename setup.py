import os
import project_generator
from setuptools import setup, find_packages

def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    with open(filename, 'r') as f:
        return f.read()

setup(
    name = 'project_generator',
    version = project_generator.__version__,
    author = 'Adriano Henrique Rossette Leite',
    author_email = 'contact@adrianohrl.tech',
    description = 'This is a tool for automaticly generating a data science project based on its metadata.',
    license = 'BSD',
    keywords = 'Automated, Data Science, Project, Generation',
    url = 'https://gitlab.com/adrianohrl/project_generator',
    packages = find_packages(),
    long_description = read('README.md'),
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operational System :: Independent',
        'Topic :: Data Science Project',
        'License :: OSI Approved :: BSD License',
    ],
    #data_files = [
    #    ('templates', ['./templates/b1.gif', 'bm/b2.gif']), # automatizar
    #    ('config', ['cfg/data.cfg']), # automatizar
    #],
)