# -*- coding: utf-8 -*-

import os
import json
import shutil
import subprocess

class ProjectGenerationException(Exception):
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

class Project(object):
    
    params_filename = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 
        os.pardir,
        'templates',
        'params.json',
    ))
    
    def __init__(self, **info):
        self.path = os.path.abspath(info['path'])c d..
        self.name = info['name']
        self.authors = info['authors']
        self.requirements = info['requirements']
        self._load()
        self.metadata = {
            'name': info['name'],
            'author': ', '.join([author['name'] for author in info['authors']]),
            'email': ', '.join([author['email'] for author in info['authors']]),
            'description': info['description'],
            'license': info['license'],
            'keywords': ','.join(info['keywords']) if len(info['keywords']) > 1 else info['keywords'],
            'url': '/'.join([
                self.params['gitlab']['url'], 
                self.params['gitlab']['namespace'],
                self.name,
            ])
        }
        
    def generate(self):
        self._makedirs()
        self._create_setup()
        self._create_init()
        self._create_requirements()
        self._create_readme()
        self._create_gitignore()
        self._create_makefile()
        self._create_others()
        print('Created the {} project structure at {}, successfully!'.format(self.name, self.path))
  
    def _makedirs(self):
        root = os.path.join(self.path, self.name)
        if os.path.exists(root):
            raise ProjectGenerationException('Unable to generate the {} project. The {} directory already exists.'.format(self.name, root))
        for directory in self.params['directories']:
            os.makedirs(directory)
            print('Created the {} directory.'.format(directory))
            
    def _create_setup(self):
        with open(self.params['templates']['setup'], 'r') as fr:
            with open(self.params['files']['setup'], 'w') as fw:
                fw.write(fr.read().format(**self.metadata))
                print('Created the {} file.'.format(self.params['files']['setup']))
            
    def _create_init(self):
        shutil.copy2(self.params['templates']['init'], self.params['files']['init'])
        print('Created the {} file.'.format(self.params['files']['init']))

    def _create_requirements(self):
        with open(self.params['files']['requirements'], 'w') as f:
            for requirement in self.requirements:
                f.write(requirement + '\n')
            print('Created the {} file.'.format(self.params['files']['requirements']))
    
    def _create_readme(self):
        authors = ['[{name}](mailto:{email})(@{username})'.format(**author) for author in self.authors]
        if len(authors) > 1:
            authors = ' e '.join([', '.join(authors[:-1]), authors[-1]])
        with open(self.params['templates']['readme'], 'r') as fr:
            with open(self.params['files']['readme'], 'w') as fw:
                fw.write(fr.read().format(
                    name = self.name, 
                    description = self.metadata['description'],
                    authors = authors,
                    url = self.metadata['url'],
                ))
                print('Created the {} file.'.format(self.params['files']['readme']))
            
    def _create_gitignore(self):
        shutil.copy2(self.params['templates']['gitignore'], self.params['files']['gitignore'])
        with open(self.params['files']['gitignore'], 'a') as f:
            f.write('\n\n# Data Science')
            for ignore in self.params['gitignores']:
                f.write('\n' + ignore)    
            print('Created the {} file.'.format(self.params['files']['gitignore']))
    
    def _create_makefile(self):
        with open(self.params['templates']['makefile'], 'r') as fr:
            with open(self.params['files']['makefile'], 'w') as fw:
                fw.write(fr.read().replace('{name}', self.name))
                print('Created the {} file.'.format(self.params['files']['makefile']))
              
    def _create_others(self):
        for source, destination in zip(self.params['templates']['others'], self.params['files']['others']):
            shutil.copy2(source, destination)
            print('Created the {} file.'.format(destination))

    def _load(self):
        replaces = {
            '{name}': self.name,
            '{root}': os.path.join(self.path, self.name),
            '{path}': os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
        }
        with open(Project.params_filename, 'r') as f:    
            self.params = f.read()
            for key, value in replaces.items():
                self.params = self.params.replace(key, value)
            self.params = json.loads(self.params)