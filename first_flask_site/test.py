
from flask import Flask
from flask import render_template, request
app = Flask(__name__)


def factors(num):
    return [x for x in range(1, num + 1) if num % x == 0]


@app.route('/')
def hello_world():
    base_url = request.base_url
    return "<h2>Go to <br></h2>" \
           "<li><a href='{0}test'>test" \
           "<li><a href='{0}hello/adam'>hello adam" \
           "<li><a href='{0}factors/100'>factors/100".format(base_url)


@app.route('/test')
def testing():
    return 'You got to the testing route!'


@app.route('/hello/<name>')
def hallo_name(name):
    return 'Hello ' + name[0].lower() + '!'


@app.route('/factors/<int:n>')
def factors_display(n):
    return render_template(
        'factors.html',
        number=n,
        factors=factors(n)
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


