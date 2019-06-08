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
	pip uninstall testings_example

make:
	python ./testings_example/data/make_dataset.py
    
build:
	python ./testings_example/features/build_features.py
    
train:
	python ./testings_example/models/train_model.py
    
predict:
	python ./testings_example/models/predict_model.py
    
visualize:
	python ./testings_example/eval/visualize.py
