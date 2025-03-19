Setup (optionally use venv, but it's fine to install globally):

```
python3 -m pip install -r requirements.txt
```

Leave the server running:

```
python3 -m http.server 8083
```

And launch the test in another terminal:

```
python3 test.py
```
