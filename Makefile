#MakeFile
setup: install build publish package-install

install: # performing poetry install
	poetry install

brain-games:
	poetry run brain-games

build: 
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl


