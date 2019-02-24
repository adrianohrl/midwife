#!/usr/bin/python
# -*- coding: utf-8 -*-

#from argparse import ArgumentParser
import os
import shutil
from project_generator import Project

#parser = argparse.ArgumentParser()
#parser.parse_args()

def main():
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