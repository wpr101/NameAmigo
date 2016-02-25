from flask import Flask
import TwoWordProjects as twp
app = Flask(__name__)


@app.route('/')
def hello_world():
    project_names = twp.create_names()
    string_names = "<h1>Names For Your Project</h1>"
    for i in range(len(project_names)):
        string_names += "<h3>" + str(i+1) + ") " + project_names[i] + "</h3>"
    
    #stringNames = '\n'.join(projectNames)
    #return 'Hello William!\n'
    return string_names

@app.route('/nameYourOwn')
def name_your_own():
    return "William"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
