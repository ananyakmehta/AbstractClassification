from flask import Flask, render_template, request, url_for, flash, redirect
import framework.davinci as davinci
import framework.gpt_3p5 as gpt_3p5
import base64
from io import BytesIO
from matplotlib.figure import Figure
import numpy as np
import framework.prompts as prompts

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

def get_ask(vector, parentvector):
    if vector == 'Summary':
        ask = "Summarize the abstract for a high school student."
    elif vector == 'PublicationType':
        ask = (prompts.pre_prompt + prompts.cat_top[1] + '. ' +
               prompts.post_prompt + '\n' + prompts.pubtypedef)
    elif vector == 'DataType':
        ask = (prompts.pre_prompt + prompts.cat_top[2] + '. ' +
               prompts.post_prompt + '\n' + prompts.datatypedef)
    elif vector == 'Population':
        ask = (prompts.pre_prompt + prompts.cat_top[3] + '. ' +
               prompts.post_prompt + '\n' + prompts.popdef)
    elif vector == 'SubPopulation':
        subask = ""
        if parentvector == "Animal":
            subask = prompts.cat_subpop[0]
        elif parentvector == "Clinical":
            subask = prompts.cat_subpop[1]
        elif parentvector == "Healthy":
            subask = prompts.cat_subpop[2]
        elif parentvector == "Other":
            subask = prompts.cat_subpop[3]
        ask = (prompts.pre_prompt + subask + '. ' + prompts.post_prompt)
    elif vector == 'Purpose':
        ask = (prompts.pre_prompt + prompts.cat_top[5] + '. ' +
               prompts.post_prompt + '\n' + prompts.purposedef)
    elif vector == 'RecordingType':
        ask = (prompts.pre_prompt + prompts.cat_top[6] + '. ' +
               prompts.post_prompt + '\n' + prompts.rectypedef)
    elif vector == 'RecordingTech':
        ask = (prompts.pre_prompt + prompts.cat_top[7] + '. ' +
               prompts.post_prompt + '\n' + prompts.rectypedef)
    elif vector == 'BrainSignal':
        ask = (prompts.pre_prompt + prompts.cat_top[8] + '. ' +
               prompts.post_prompt + '\n' + prompts.signaldef)
    elif vector == 'Paradigm':
        subask = ""
        if parentvector == "Attention":
            subask = prompts.cat_sigpdim[0]
        elif parentvector == "Auditory":
            subask = prompts.cat_sigpdim[1]
        elif parentvector == "Error":
            subask = prompts.cat_sigpdim[2]
        elif parentvector == "Frontal":
            subask = prompts.cat_sigpdim[3]
        elif parentvector == "Hybrid":
            subask = prompts.cat_sigpdim[4]
        elif parentvector == "Motor":
            subask = prompts.cat_sigpdim[5]
        elif parentvector == "Other":
            subask = prompts.cat_sigpdim[6]
        elif parentvector == "SCP":
            subask = prompts.cat_sigpdim[7]
        elif parentvector == "Visual":
            subask = prompts.cat_sigpdim[8]
        ask = (prompts.pre_prompt + subask + '. ' +
               prompts.post_prompt + '\n' + prompts.signaldef)
    elif vector == 'Application':
        ask = (prompts.pre_prompt + prompts.cat_top[10] + '. ' +
               prompts.post_prompt + '\n' + prompts.appdef)
    elif vector == 'Contribution':
        ask = (prompts.pre_prompt + prompts.cat_top[11] + '. ' +
               prompts.post_prompt + '\n' + prompts.contribdef)
    elif vector == 'SubContribution':
        subask = ""
        if parentvector == "Applied Research":
            subask = prompts.cat_subctrb[0]
            subcontribdef = prompts.arsubcontribdef
        elif parentvector == "Basic Research":
            subask = prompts.cat_subctrb[1]
            subcontribdef = prompts.brsubcontribdef
        elif parentvector == "Experimental Development":
            subask = prompts.cat_subctrb[2]
            subcontribdef = prompts.edsubcontribdef
        elif parentvector == "Support":
            subask = prompts.cat_subctrb[3]
            subcontribdef = prompts.supsubcontribdef
        ask = (prompts.pre_prompt + subask + '. ' +
               prompts.post_prompt + '\n' + subcontribdef)
    return ask

@app.route('/')
def index():
    return redirect(url_for('classify'))

@app.route('/answer/<vector>/<model>/<title>/<abstract>/<temperature>/<parentvector>', methods=('GET', 'POST'))
def answer(vector, model, title, abstract, temperature, parentvector=None):
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    prompts.init()
    debug = False
    temperature = float(temperature)
    ask = get_ask(vector, parentvector)
    if model == '"Model A"':
        if vector == 'Summary':
            return gpt_3p5.get_abstract_summary(title, abstract, ask, temperature,
                                                debug)
        else:
            return gpt_3p5.get_category_reason(prompts.knbase, title, abstract,
                                               ask, temperature, debug)
    elif model == '"Model B"':
        if vector == 'Summary':
            return davinci.get_abstract_summary(title, abstract, ask, temperature,
                                                debug)
        else:
            return davinci.get_category_reason(prompts.knbase, title, abstract,
                                               ask, temperature, debug)

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
            model = request.form.get('model')
            temperature = float(request.form.get('temperature'))
            title = title.strip()
            # TODO Use encodeURIComponent() in javascript to escape '/' and '\'
            title = title.translate({ord(c): " " for c in "!@#$%^&*()[]{};:/<>?\|`~-=_+"})
            abstract = abstract.strip()
            # TODO Use encodeURIComponent() in javascript to escape '/' and '\'
            abstract = abstract.translate({ord(c): " " for c in "!@#$%^&*()[]{};:/<>?\|`~-=_+"})

            return render_template('result_classify.html', model=model, title=title,
                                   abstract=abstract, temperature=temperature)

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
