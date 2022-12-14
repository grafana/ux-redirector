import os
from flask import Flask,redirect
from multiprocessing import Value

counter = Value('i', 0)

stacks = [
    "NA",
    "https://s38pilot3.grafana.net/",
    "https://s38pilot4.grafana.net/",
    "https://s38pilot5.grafana.net/",
    "https://s38pilot6.grafana.net/",
    "https://s38pilot7.grafana.net/"
]

app = Flask(__name__)

@app.route('/')
def hello():
    with counter.get_lock():
            counter.value += 1
            out = counter.value
##    return f'{stacks[out]}'
    return redirect(stacks[out], code=302)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)