from flask import Flask, render_template
import TwoWordProjects as twp
import OneWordProjects as owp
app = Flask(__name__)


@app.route('/')
def index():
    #project_names = twp.create_names()
    #string_names = "<h1>Names For Your Project</h1>"
    #for i in range(len(project_names)):
        #string_names += "<h3>" + str(i+1) + ") " + project_names[i] + "</h3>"
    #return string_names
    two_word_names = twp.create_names()
    one_word_names = owp.create_names_with_meanings()
    print(one_word_names)
    print("DONE")
    return render_template('index.html', two_word_names = two_word_names,
                           one_word_names = one_word_names)

@app.route('/TwoWordProjects')
def TwoWordProjects():
    project_names = twp.create_names()
    return render_template('twowordprojects.html', project_names = project_names)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
