import os
from flask import Flask,redirect
from multiprocessing import Value
import random

counter = Value('i', 0)

stacks = [
    "https://s38p1.grafana.net/",
    "https://s38p2.grafana.net/",
    "https://s38p3.grafana.net/",
    "https://s38p4.grafana.net/",
    "https://s38p5.grafana.net/",
    "https://s38p6.grafana.net/",
    "https://s38p7.grafana.net/",
    "https://s38p8.grafana.net/",
    "https://s38p9.grafana.net/",
    "https://s38p10.grafana.net/"
]

app = Flask(__name__)

@app.route('/')
def hello():
    # out = random.randrange(9)
    # return redirect(stacks[out], code=302)
    with counter.get_lock():
            out = counter.value
            counter.value += 1
    # return f'{stacks[out]}'
    return redirect(stacks[out], code=302) 

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)