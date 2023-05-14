# chatgpt-prompt-engineering

Following along [this course](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/).

Using a simple python setup found [here](https://medium.com/@cgrinaldi/a-simple-python-starter-project-c71b0e57b929) to expedite development.

## Project Setup

This project assumes you are using [pipenv](https://github.com/pypa/pipenv) to manage
virtual environments and project dependencies.

#### 1. Install project dependencies:
```
pipenv install --dev
```

#### 2. Setup project to use **pre-commit**:
```
pipenv run pre-commit install
```

#### 3. Install additional project dependencies:
```
pipenv install [package]
```
Use the **--dev** flag if needed.

#### 4. Run tests:
```
make test
```
Tests will be automatically run prior to every commit.

## Additional Notes
In addition to autoformatting the code via **Black** and **flake8** for each commit,
it does the following:
- Runs the unit tests
- Runs mypy for type checking

If you would like to disable this, edit this [file](.pre-commit-config.yaml).

# Principles for prompt engineering: 

1. Write clear and specific instructions.
2. Give the model time to think.