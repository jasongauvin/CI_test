init:
	pip3 install -r requirements.txt
test: 
	python test_function_for_test.py
lint:
	pylint ./**.py