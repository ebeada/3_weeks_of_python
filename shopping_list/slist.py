
from flask import Flask
from flask import render_template, request
app = Flask(__name__)


@app.route('/')
def shopping_list():
    url = request.base_url
    return render_template(
        'home.html',
        base_url=url
    )


@app.route('/about/')
def about():
    return render_template(
        'about.html'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


