import os
from argparse import Action, ArgumentTypeError, ArgumentParser
import midwife
    
class ReadableDirectory(Action):
    
    def __call__(self, parser, namespace, value, option_string = None):
        value = os.path.expanduser(value) if value.startswith('~') else value
        value = os.path.abspath(value) if value.startswith('.') else value
        if not os.path.isdir(value):
            raise ArgumentTypeError('ReadableDirectory: {0} is not a valid path to a directory'.format(value))
        if not os.access(value, os.R_OK):
            raise ArgumentTypeError('ReadableDirectory: {0} is not a readable directory'.format(value))
        setattr(namespace, self.dest, value)
        
class ReadableFile(Action):
    
    def __call__(self, parser, namespace, value, option_string = None):
        value = os.path.expanduser(value) if value.startswith('~') else value
        value = os.path.abspath(value) if value.startswith('.') else value
        if not os.path.isfile(value):
            raise ArgumentTypeError('ReadableFile: {0} is not a valid path to a file'.format(value))
        if not os.access(value, os.R_OK):
            raise ArgumentTypeError('ReadableFile: {0} is not a readable file'.format(value))
        setattr(namespace, self.dest, value)
        
url = 'https://github.com/adrianohrl/midwife'
parser = ArgumentParser(
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
parser.add_argument(
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
    action = ReadableDirectory,
    default = None,
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
    action = ReadableFile,
    default = None,
    help = 'identify the path of the |configuration file (.json) to automaticly generate the project',
)

def show(args):
    print('{}: {}'.format('language', args.language))
    print('{}: {}'.format('path', args.path))
    print('{}: {}'.format('name', args.name))
    print('{}: {}'.format('verbose', args.verbose))
    print('{}: {}'.format('quiet', args.quiet))
    print('{}: {}'.format('yes', args.yes))
    print('{}: {}'.format('git', args.git))
    print('{}: {}'.format('config', args.config))
    
if __name__ == '__main__':
    show(parser.parse_args())