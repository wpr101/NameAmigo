from flask import Flask
import TwoWordProjects as twp
app = Flask(__name__)


@app.route('/')
def hello_world():
    projectNames = twp.createNames()
    stringNames = "<h1>Names For Your Project</h1>"
    for i in range(len(projectNames)):
        stringNames += "<h3>" + str(i+1) + ") " + projectNames[i] + "</h3>"
    
    #stringNames = '\n'.join(projectNames)
    #return 'Hello William!\n'
    return stringNames

@app.route('/nameYourOwn')
def nameYourOwn():
    return "test"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
