# Steve Jobs App

This version uses Poetry to manage dependencies and ensure a consistent environment. Poetry creates a virtual environment and installs the dependencies in it to isolate them from the global Python installation.

## Install dependencies

Create the virtual environment and install the dependencies.

```sh
$ poetry install
```

Run the app

```sh
$ poetry run python src/main.py "<your prompt>"
```