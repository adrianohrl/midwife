# -*- coding: utf-8 -*-

from .project_generator import Project

def ask():
    answers = {}
    answers['path'] = input('')

def main(*kwargs, **args):
    print('Welcome to the project_generator tool!!!\n\nYou will be asked some question in order to automaticly create it for you.\n\nSo let\'s get started...\n\n)

if __main__(*kwargs, **args):
    main(*kwargs, **args)