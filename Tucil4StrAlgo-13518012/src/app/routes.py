from flask import request, render_template, url_for
from app import app
from app.forms import inputForm
from app.result import getResults

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = inputForm()
    results = None
    if request.method == 'POST':
        results = getResults(request.form)
    return render_template('index.html', form=form, results=results)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)