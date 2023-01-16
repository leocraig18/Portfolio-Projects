from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = "ytcttuvil9iubojmoni"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=True)
