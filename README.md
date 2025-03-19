Setup (optionally use venv, but it's fine to install globally).
This is how you set the Chrome release version.

```
python3 -m pip install selenium>=4.29.0 chromedriver-binary==134.0.6998.88
```

Leave the server running:

```
python3 -m http.server 8083
```

And launch the test in another terminal:

```
python3 test.py
```
