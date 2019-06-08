import os
import midwife
import setuptools

def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    with open(filename, 'r') as f:
        content = f.read()
        f.close()
        return content

if __name__ == '__main__':
    name = 'midwife'
    prefix = os.path.join(os.path.expanduser('~'), '.{}'.format(name))
    if not os.path.exists(prefix):
        os.mkdir(prefix)
        print('Created the {} directory.'.format(prefix))
        for path in [os.path.join(prefix, path) for path in ['logs', 'templates']]:
            os.makedirs(path)
            print('Created the {} directory.'.format(path))
    setuptools.setup(
        name = name,
        version = midwife.__version__,
        author = 'Adriano Henrique Rossette Leite',
        author_email = 'adrianohrl@gmail.com',
        description = 'This is a tool for automaticly generating data science projects based on its metadata.',
        license = 'BSD',
        keywords = 'Automated, Data Science, Project, Generation',
        url = 'https://github.com/adrianohrl/{}'.format(name),
        packages = setuptools.find_packages(),
        long_description = read('README.md'),
        classifiers = [
            'Programming Language :: Python :: 3',
            'Operational System :: Independent',
            'Topic :: Data Science Project',
            'License :: OSI Approved :: BSD License',
        ],
        #entry_points = {
        #    'console_scripts': [
        #        '{0}_generate = {0}.generate:main'.format(name),
        #    ],
        #},
        include_package_data = True,
    )