install:
    python setup.py install
    
generate:
    python project_generator/generate.py

ssh:
    python project_generator/ssh/create.py

git:
    python project_generator/git/init.py