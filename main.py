from flask import Flask, render_template, request, url_for, flash, redirect
import davinci
import gpt_3p5

app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'
output = []

@app.route('/')
def index():
    return render_template('result.html', messages=output)

@app.route('/classify/', methods=('GET', 'POST'))
def classify():
    global output
    if request.method == 'POST':
        title = request.form['title']
        abstract = request.form['content']

        if not title:
            flash('Title is required!')
        elif not abstract:
            flash('Abstract is required!')
        else:
            title = title + "\n"
            abstract = abstract + "\n"
            model = request.form.get('model')
            temperature = float(request.form.get('temperature'))
            if model == "Model A":
                output = gpt_3p5.model_gpt_3p5_turbo(title, abstract, temperature)
            elif model == "Model B":
                output = davinci.model_davinci(title, abstract, temperature)

            return redirect(url_for('index'))

    return render_template('input.html')

if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
