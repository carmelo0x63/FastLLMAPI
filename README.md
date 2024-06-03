# FastLLMAPI
API-first frontend to Ollama (backend), based on FastAPI

### Prerequisite
[Ollama](https://ollama.com/) must be installed and running on the destination host.

### Install
```
$ git clone https://github.com/carmelo0x63/FastLLMAPI.git

$ cd FastLLMAPI

$ python3 -m venv .

$ source bin/activate

$ python3 -m pip install --upgrade pip setuptools wheel

$ python3 -m pip install --upgrade fastapi Flask requests
```

### Run
In two separate terminal windows, run the following commands:
1. `python3 main_app.py`
2. `python3 gui_app.py`
<br/>
The graphical interface will be available on the host where the applications are run, on port 5000: `http://&lt;ip_address&gt;:5000/`
