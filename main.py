import os
from flask import Flask,redirect
from multiprocessing import Value
import random
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

config = ConfigParser()
config.read('config.ini')

file = open("test-stacks.txt", "r")

with open('test-stacks.txt') as f:
    stacks = f.read().splitlines()

app = Flask(__name__)

@app.route('/')
def hello():
    # out = random.randrange(9)
    # return redirect(stacks[out], code=302)
    counter = config.getint('counters', 'counter1')
    url = f'https://{stacks[counter]}.grafana.net'
    counter += 1
    config.set('counters', 'counter1', str(counter))
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    return redirect(url, code=302) 

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)