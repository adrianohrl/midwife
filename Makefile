clean:
	find ./ -name "*~" -exec rm -f {} \;
	find ./ -name "__pycache__" -exec rm -rf {} \; -prune
	find ./ -name ".ipynb_checkpoints" -exec rm -rf {} \; -prune
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	#rm -rf docs/build

install:
	pip install . --user
    
uninstall:
	pip uninstall project_generator
  
generate:
	python ./project_generator/generate.py

ssh:
	python ./project_generator/ssh/create.py

git:
	python ./project_generator/git/init.py
