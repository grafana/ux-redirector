import os
from flask import Flask,redirect
from multiprocessing import Value

counter = Value('i', 0)
## a = "http://www.grafana.com"
## a = 1
## a = a+1

stacks = [
    "NA",
    "http://www.grafana.com",
    "http://www.google.com"
]

app = Flask(__name__)

@app.route('/')
def hello():
    with counter.get_lock():
            counter.value += 1
            out = counter.value
    return f'{stacks[out]}'
##    return redirect(a, code=302)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)