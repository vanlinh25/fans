#### Run
uvicorn main:app --reload
### Doc
####  http://localhost:8000

#### http://localhost:8000/docs

#### http://localhost:8000/graphql

### virtual env
python -m venv fans
cd fans
Scripts\activate.bat
### write requirements.txt
#### #1
pip install pipreqs
pipreqs . --force
#### #2 
pip freeze > requirements.txt

### Install
pip install -r requirements.txt

### Deploy 
deta new
