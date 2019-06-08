#!/usr/bin/python
# -*- coding: utf-8 -*-

#from argparse import ArgumentParser
import os
import git
import shutil
import json
import midwife
import pkg_resources as pr

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

class Form(object):
    def __init__(self, path, language = 'en'):
        self.path = path
        self.language = language
        self.form_filename = '../midwife/templates/form.{}.json'.format(language)
        self.fields = []
        with open(self.form_filename, 'r') as f:    
            self.form = json.loads(f.read())
            self.fields = [Field(**field) for field in self.form['fields']]
        self.info_filename = os.path.join(path, '.midwife_form_info.json')
        self.info = {}
        self.project = None
        
    def ask(self):
        print(self.form['menu'])
        self.info = {}
        if os.path.exists(self.info_filename):
            with open(self.info_filename, 'r') as f:
                self.info = json.loads(f.read())
                print('There is an existing filled form:')
                print([print('\t{}: {}'.format(key, value)) for key, value in self.info.items()])
                answer = input('Would like to continue from this point? [Y/n]')
                if not answer.lower().startswith('y'):
                    self.info = {}
        for field in self.fields:
            if field.key not in self.info:
                key, answer = field.ask()
                self.info[key] = answer
                with open(self.info_filename, 'w') as f:
                    json.dump(self.info, f)
        return self.info
        
    def generate(self, project):
        print('The following project structure will be generated:')
        print(project)
        yes, no = 'y', 'n'
        yes = input('Do you want to continue? [{}/{}]'.format(yes, no)).lower() == yes
        if not yes:
            print('Aborted.')
            return
        project.generate()
        os.remove(self.info_filename)
    
    def init(self, project):
        yes, no = 'y', 'n'
        yes = input('Do you want to initialize git in this project? [{}/{}]'.format(yes, no)) == yes
        if not yes:
            print('Aborted.')
            return
        project.init()
                    
def main():
#     print('\t{}\n\tv{}\n\tby {}\n\t{}\n'.format(
#         'midwife', 
#         midwife.__version__,
#         'Adriano Henrique Rossette Leite', 
#         'A tool for automaticly generating data science projects for python.'
#     ))
    language = 'en' # pode ser um parametro de execucao 
    path = os.path.expanduser('~/Projects/Python') # pode ser um parametro de execucao
    #prefix = os.path.join(os.path.expanduser('~'), '.midware')
    form = Form(path, language)
    info = form.ask()
    project = midwife.Project(**info)
    form.generate(project)
    form.init(project)
    
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

if __name__ == '__main__':
    main()#test()