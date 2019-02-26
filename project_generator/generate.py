#!/usr/bin/python
# -*- coding: utf-8 -*-

#from argparse import ArgumentParser
import os
import shutil
from project_generator import Project

#parser = argparse.ArgumentParser()
#parser.parse_args()

def ask(label, default, escape = False):
    if label == '':
        return None
    label += '?'
    if default is not None:
        label = '{} ({})'.format(label, 'default: \'{}\''.format(default))
        answer = input(label)
        return answer if answer != '' else default
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
                    print('final answer: \'{}\''.format(answer))
                    if answer is None:
                        answers.pop()
                        return self.key, answers
                    answers[i][key] = answer            

def main():
    language = 'en' # pode ser um parametro de execucao 
    #path = '~' # pode ser um parametro de execucao
    form_filename = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 
        os.pardir,
        'templates',
        'form.{}.json'.format(language),
    ))    
    with open(form_filename, 'r') as f:    
        form = json.loads(f.read())
        info = {}
        fields = [Field(**field) for field in form['fields']]
        print(form['menu'])
        for field in fields:
            key, answer = field.ask()
            info[key] = answer
        project = Project(**info)
        project.generate()

def test():
    print('''
        Welcome to the project_generator tool!!!
        \n\n
        You will be asked some question in order to automaticly create it for you.\n\n
        So let\'s get started...
        \n\n
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
    project = Project(**info)
    project.generate()
    
    ############################################
    ###         requirements.txt             ###
    ###                                      ###
    ### fazer as perguntas de requirimentos  ###
    ### e escrevê-las no arquivo apropriado  ###
    ###                                      ###
    ############################################

if __name__ == "__main__":
    main()