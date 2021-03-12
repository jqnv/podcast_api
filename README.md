# Podcast catalog

podcast_api is a Python API to get JSON info and display it for the user.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install podcast_api.

```bash
pip install virtualenv
pip install flask
pip install requests
```

## Usage

```python
from flask import Flask, request,render_template
import requests

def my_app(): # returns all podcasts(100) through directory 'resul'
def index() # returns podcasts filtered by name through directory 'resul'

NOTE: to run the home page add '/my_app' at the end of the server name. Example: http://127.0.0.1:8000/my_app
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Joaquin Vasquez](https://github.com/jqnv/)
