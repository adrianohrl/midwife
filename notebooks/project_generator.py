import os
import json
import shutil
import subprocess

class Project(object):
    
    params_filename = '../templates/params.json'
    
    def __init__(self, **info):
        self.parent = info['parent']
        self.name = info['name']
        self.authors = info['authors']
        self.params = self._load()
        self.metadata = {
            'name': info['name'],
            'author': ', '.join([author['name'] for author in info['authors']]),
            'email': ', '.join([author['email'] for author in info['authors']]),
            'description': info['description'],
            'license': info['license'],
            'keywords': info['keywords'],
            'url': '/'.join(
                self.params['gitlab']['url'], 
                self.params['gitlab']['namespace'],
                self.name,
            )
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
        print('Created the {} project at {}, successfully!'.format(self.name, self.parent))
  
    def _makedirs(self):
        for directory in self.params['directories']:
            os.makedirs(directory)
            print('Created the {} directory.'.format(directory))
            
    def _create_setup(self):
        with open(self.params['templates']['setup'], 'r') as fr:
            with open(self.params['files']['setup'], 'w') as fw:
                fw.write(fr.read().format(**self.metadata))
                print('Created {}'.format(self.params['files']['setup']))
            
    def _create_init(self):
        shutil.copy2(self.params['templates']['init'], self.params['files']['init'])
        print('Created the {} file.'.format(self.params['files']['init']))

    def _create_requirements(self):
        with open(self.params['file']['requirements'], 'w') as f:
            f.write('')
            print('Created the {} file.'.format(self.params['file']['requirements']))
    
    def _create_readme(self):
        authors = ['[{name}](mailto:{email})(@{racf})'.format(**author) for author in self.answers['authors']]
        with open(self.params['templates']['readme'], 'r') as fr:
            with open(self.params['file']['readme'], 'w') as fw:
                fw.write(fr.read().format(
                    name = self.name, 
                    description = self.metadata['description'],
                    authors = ' e '.join(', '.join(authors[:-1]), authors[-1]),
                    url = self.metadata['url'],
                ))
                print('Created the {} file.'.format(self.params['file']['readme']))
            
    def _create_gitignore(self):
        shutil.copy2(self.params['templates']['gitignore'], filename)
        with open(filename, 'a') as f:
            f.write('\n\n# Data Science')
            for ignore in self.params['gitignores']:
                f.write('\n' + ignore)    
            print('Created the {} file.'.format(self.params['files']['gitignore']))
    
    def _create_makefile(self):
        shutil.copy2(self.params['templates']['makefile'], self.params['files']['makefile'])
        print('Created the {} file.'.format(self.params['files']['makefile']))
              
    def _create_others(self):
        for source, destination in zip(self.params['templates']['others'], self.params['files']['others']):
            shutil.copy2(source, destination)
            print('Created the {} file.'.format(destination))

    def _load(self):
        replaces = {
            '{name}': self.name,
            '{parent}': self.parent,
            '{path}': os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
        }
        with open(Project.params_filename, 'r') as f:    
            self.params = f.read()
            for key, value in replaces.items():
                self.params = self.params.replace(key, value)
        
    def install(self): 
        subprocess.run(['python', os.path.join(self.parent, self.name, 'setup.py'), 'install'])
        
    def git_init(self):
        subprocess.run(['git', 'init'])
        url = self._create_repo()
    
    def _create_repo():
        return ''

def get_answers():
    return {}

def check_sshkey():
    pass
    
def create_sshkey():
    pass