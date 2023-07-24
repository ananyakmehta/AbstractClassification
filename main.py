from flask import Flask, render_template, request, url_for, flash, redirect
import framework.davinci as davinci
import framework.gpt_3p5 as gpt_3p5
import base64
from io import BytesIO
from matplotlib.figure import Figure
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'

def plot_model_accuracy():
    # Generate the figure **without using pyplot**.
    fig = Figure(figsize=(10,5))
    ax = fig.add_subplot(projection='3d')

    colors = ['r', 'g', 'b', 'y']
    yticks = [3, 2, 1, 0]
    for c, k in zip(colors, yticks):
        # Generate the random data for the y=k 'layer'.
        xs = np.arange(20)
        ys = np.random.rand(20)

        # You can provide either a single color or an array with the same length as
        # xs and ys. To demonstrate this, we color the first bar of each set cyan.
        cs = [c] * len(xs)
        cs[0] = 'c'

        # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
        ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # On the y-axis let's only label the discrete values that we have data for.
    ax.set_yticks(yticks)

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def map_model_output(model_dict):
    display = [
            {'title': 'Title',
             'content': 'Summary',
             'extra': 'Abstract'},
            {'title': 'PublicationType',
             'content': '',
             'extra': ''},
            {'title': 'DataType',
             'content': '',
             'extra': ''},
            {'title': 'Population',
             'content': '',
             'extra': ''},
            {'title': 'Subpopulation',
             'content': '',
             'extra': ''},
            {'title': 'Purpose',
             'content': '',
             'extra': ''},
            {'title': 'RecordingType',
             'content': '',
             'extra': ''},
            {'title': 'RecordingTech',
             'content': '',
             'extra': ''},
            {'title': 'BrainSignal',
             'content': '',
             'extra': ''},
            {'title': 'Paradigm',
             'content': '',
             'extra': ''},
            {'title': 'Application',
             'content': '',
             'extra': ''},
            {'title': 'Contribution',
             'content': '',
             'extra': ''},
            {'title': 'SubContribution',
             'content': '',
             'extra': ''},
            ]
    display[0]['title'] = model_dict['Title']
    display[0]['content'] = model_dict['Summary']
    display[0]['extra'] = model_dict['Abstract']
    for i in range(1,13):
        display[i]['content'] = model_dict[display[i]['title']]
        display[i]['extra'] = model_dict[display[i]['title']+'Reason']
    return display

@app.route('/')
def index():
    return redirect(url_for('classify'))

@app.route('/classify/', methods=('GET', 'POST'))
def classify():
    if request.method == 'POST':
        title = request.form['title']
        abstract = request.form['content']

        if not title:
            flash('Title is required!')
        elif not abstract:
            flash('Abstract is required!')
        else:
            title = "Title: " + title + "\n"
            abstract = "Abstract: " + abstract + "\n"
            model = request.form.get('model')
            temperature = float(request.form.get('temperature'))
            if model == "Model A":
                model_dict = gpt_3p5.classify_abstract(title, abstract, temperature)
                output = map_model_output(model_dict)
            elif model == "Model B":
                model_dict = davinci.model_davinci(title, abstract, temperature)
                output = map_model_output(model_dict)
            return render_template('result_classify.html', messages=output)

    return render_template('input_classify.html')

@app.route('/evaluate/', methods=('GET', 'POST'))
def evaluate():
    if request.method == 'POST':
        mintemp = float(request.form.get('mintemp'))
        print(mintemp)
        maxtemp = float(request.form.get('maxtemp'))
        print(maxtemp)
        for checkbox in 'model1', 'model2':
            value = request.form.get(checkbox)
            print(value)

        data = plot_model_accuracy()
        return render_template('result_evaluate.html', messages=data)

    return render_template('input_evaluate.html')

if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
