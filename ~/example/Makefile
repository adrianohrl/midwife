clean:
	find ./ -name "*~" -exec rm -f {} \;
	find ./ -name "__pycache__" -exec rm -rf {} \; -prune
	find ./ -name ".ipynb_checkpoints" -exec rm -rf {} \; -prune
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
    
build:
	python ./setup.py build

install:
	pip install .
    
uninstall:
	pip uninstall example

make:
	python ./example/data/make_dataset.py
    
build:
	python ./example/features/build_features.py
    
train:
	python ./example/models/train_model.py
    
predict:
	python ./example/models/predict_model.py
    
visualize:
	python ./example/eval/visualize.py
