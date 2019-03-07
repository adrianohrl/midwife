#!/usr/bin/python
# -*- coding: utf-8 -*-

#from argparse import ArgumentParser
import os
import git
import shutil
import json
import midwife
import pkg_resources

#parser = argparse.ArgumentParser()
#parser.parse_args()

def ask(label, default, escape = False):
    if label == '':
        return None
    if default is not None:
        label = '\n{} ({})?\n  '.format(label, 'default: \'{}\''.format(default))
        answer = input(label)
        return answer if answer != '' else default
    label = '\n{}?\n  '.format(label)
    answer = input(label)
    if answer == '' and escape:
        return None
    while answer == '':
        answer = input(label)
    return answer

class Field(object):
    
    def __init__(self, **field):
        self.key = field['key']
        self.label = field['label'].capitalize()
        self.default = field['default'] if 'default' in field else None
        self.note = field['note'].capitalize() if 'note' in field else ''
        self.multiple = field['multiple'] if 'multiple' in field else False
        self.fields = field['fields'] if 'fields' in field else []
        self.fields = [Field(**f) for f in self.fields]
        
    def ask(self, i = -1):
        if self.note != '':
            print(self.note)
        if not self.multiple:
            return self.key, ask(self.label.format(i) if i != -1 else self.label, self.default, i > 1)
        answers = []
        while True:
            i = len(answers)
            if len(self.fields) == 0:
                answer = ask('{} #{}'.format(self.key, i + 1), None, True) # how about when it can be empty (default)?
                if answer is None:
                    return self.key, answers
                answers.append(answer)
            else:
                answers.append({})
                for field in self.fields:
                    key, answer = field.ask(i + 1) # how about when it can be empty (default)?
                    if answer is None:
                        answers.pop()
                        return self.key, answers
                    answers[i][key] = answer    
                    
def git_init(root, **info):
    author = git.Actor(info['authors'][0]['name'], info['authors'][0]['email'])
    repo = git.Repo.init(root)
    repo.git.add(A = True)
    commit = repo.index.commit('Created the {} project with the {} tool.'.format(info['name'], 'midwife'), author = author, committer = author)
    origin = repo.create_remote(name = 'origin', url = info['url'])
    repo.git.push('origin', 'master', set_upstream = True)

def main():
    print('\t{}\n\tv{}\n\tby {}\n\t{}\n'.format(
        'midwife', 
        midwife.__version__,
        'Adriano Henrique Rossette Leite', 
        'A tool for automaticly generating data science projects for python.'
    ))
    language = 'en' # pode ser um parametro de execucao 
    #path = '~' # pode ser um parametro de execucao
    #prefix = os.path.join(os.path.expanduser('~'), '.midware')
    prefix = pkg_resources.resource_filename('midwife', 'templates')
    form_filename = os.path.join(prefix, 'form.{}.json'.format(language))
    with open(form_filename, 'r') as f:    
        form = json.loads(f.read())
        info = {}
        fields = [Field(**field) for field in form['fields']]
        print(form['menu'])
        for field in fields:
            key, answer = field.ask()
            info[key] = answer
        project = Project(**info)
        #print report
        yes, no = 'y', 'n'
        yes = input('Do you want to continue? [{}/{}]'.format(yes, no)) == yes
        if not yes:
            print('Aborted.')
            return
        if os.path.exists(project.root):
            path = project.root + str(time())
            print('The {} folder already exists. It will be renamed to {} in order to the creation of the {} project at {}'.format(
                project.root,
                path,
                project.name,
                project.path,
            ))
            shutil.move(project.root, path)
            print('Moved {} to {}.'.format(project.root, path))
        project.generate()
        yes = input('Do you want to initialize git in this project? [{}/{}]'.format(yes, no)) == yes
        if not yes:
            print('Aborted.')
            return
        git_init(project.root, **info)

def test():
    print('''
        Welcome to the midwife tool!!!
        \n
        You will be asked some question in order to automaticly create it for you.\n
        So let\'s get started...
        \n
    ''')
    info = {
        'path': '~',
        'name': 'example',
        'authors': [{
                'name': 'Adriano Henrique Rossette Leite',
                'email': 'contact@adrianohrl.tech',
                'username': 'adrianohrl',
            }, {
                'name': 'Henrique Rossette Leite',
                'email': 'me@adrianohrl.tech',
                'username': 'henriquerl',
            },
        ],
        'description': 'This is an example.',
        'license': 'BSD',
        'url': 'git@gitlab.com:adrianohrl/example.git',
        'keywords': [
            'project',
            'generator',
            'example',
        ],
        'requirements': [
            'pandas >= 0.23.4',
            'numpy >= 1.16.1 ',
        ],
    }
    root = os.path.abspath(os.path.join(info['path'], info['name']))
    if os.path.exists(root):
        shutil.rmtree(root)
        print('Removed the {} directory.'.format(root))
    project = midwife.Project(**info)
    project.generate()
    git_init(root, **info)
    
    ############################################
    ###         requirements.txt             ###
    ###                                      ###
    ### fazer as perguntas de requirimentos  ###
    ### e escrevê-las no arquivo apropriado  ###
    ###                                      ###
    ############################################

if __name__ == "__main__":
    test()