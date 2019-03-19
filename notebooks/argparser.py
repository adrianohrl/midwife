import os
import argparse
import midwife

url = 'https://github.com/adrianohrl/midwife'
parser = argparse.ArgumentParser(
    prog = 'midwife',
    description = 'A tool for automaticly generating data science projects based on its metadata.',
    epilog = 'If you need any additional support, visit the project website at {}.'.format(url),
)
parser.add_argument(
    '-v',
    '--version',
    action = 'version', 
    version = '%(prog)s {}'.format(midwife.__version__),
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    '--en',
    help = 'select the English language',
    action = 'store_true',
)
group.add_argument(
    '--pt',
    help = 'select the Portuguese language',
    action = 'store_true',
)
group.add_argument(
    '-l',
    '--language',
    type = str,
    default = 'en',
    choices = ['en', 'pt'],
    help = 'select the language (possibilities: en | pt)',
)
parser.add_argument(
    '-p', 
    '--path', 
    type = str,
    default = os.path.abspath('.'),
    help = 'path to the project location',
)
parser.add_argument(
    '-n',
    '--name',
    type = str,
    help = 'specify the name of the project to generated'
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    '-V', 
    '--verbose', 
    help = 'increase output verbosity',
    action = 'store_true',
)
group.add_argument(
    '-q', 
    '--quiet', 
    help = 'disable all outputs',
    action = 'store_true',
)
parser.add_argument(
    '-y', 
    '--yes', 
    help = 'confirm project generation',
    action = 'store_true',
)
parser.add_argument(
    '-g',
    '--git',
    help = 'init and push the generate project the url of the origin git remote',
    type = str,
    default = None,
    metavar = 'ORIGIN_URL',
)
parser.add_argument(
    '-c',
    '--config',
    type = str,
    help = 'identify the path of the |configuration file (.json) to automaticly generate the project',
)
args = parser.parse_args()
print(args)
