from flask import Flask, render_template
import TwoWordProjects as twp
import OneWordProjects as owp
import ChooseWord as cw
app = Flask(__name__)


@app.route('/')
def index():
    
    two_word_names = twp.create_names()
    one_word_names = owp.create_names_with_meanings()
    describe_projects = cw.create_thesaurus_name()

    return render_template('index.html', two_word_names = two_word_names,
                           one_word_names = one_word_names,
                           describe_projects = describe_projects)

@app.route('/TwoWordProjects')
def TwoWordProjects():
    project_names = twp.create_names()
    return render_template('twowordprojects.html', project_names = project_names
                           )
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
