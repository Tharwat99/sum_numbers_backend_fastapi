# Sum Numbers Backend FastAPI

## Clone Project
The first thing to do is to clone the repository:

```sh
git clone https://github.com/Tharwat99/sum_numbers_backend_fastapi.git
```

```sh
cd sum_numbers_backend_fastapi
```

## Setup
Create a virtual environment to install dependencies in and activate it:

```sh
python -m venv env
cd env/Scripts
activate
```

Then install the dependencies:

```sh
cd ../../
pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:

## Runserver

```sh
cd app
uvicorn main:app --port 8888
```
