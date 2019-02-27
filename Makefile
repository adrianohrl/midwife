clean:
	find ./ -name "*~" -exec rm -f {} \;
	find ./ -name "__pycache__" -exec rm -rf {} \; -prune
	find ./ -name ".ipynb_checkpoints" -exec rm -rf {} \; -prune
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	#rm -rf docs/build

install:
	pip install .
    
uninstall:
	pip uninstall midwife
  
generate:
	python ./midwife/generate.py

ssh:
	python ./midwife/ssh/create.py

git:
	python ./midwife/git/init.py
