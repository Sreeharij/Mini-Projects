import os,time
try:
    import pip
    print("True")
except ImportError:
    os.system('python get-pip.py')
    os.system('pip install --no-cache-dir --upgrade pip')

try:
    import bs4
    print("True")
except ImportError:
    os.system('pip install --no-cache-dir bs4')
    os.system('pip install --no-cache-dir --upgrade bs4')

try:
    import requests
    print("True")
except ImportError:
    os.system('pip install --no-cache-dir requests')
    os.system('pip install --no-cache-dir --upgrade requests')
time.sleep(5)
