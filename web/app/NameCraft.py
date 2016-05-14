from flask import Flask, render_template, request, redirect, url_for, Response
import os
from gevent.pywsgi import WSGIServer

import ChooseWord as cw
import CustomNames as cn
import PrepareWords as pw
import VowelPatterns as vp
import Trump as t

app = Flask(__name__)

@app.route('/')
def index():
    
    describe_projects = cw.create_thesaurus_name()

    return render_template('tabbedindex.html',
                           describe_projects = describe_projects)

@app.route('/custom-words/<string:user_word>')
def CustomName(user_word):

    word_list = user_word.split('-')
    project_names = cn.custom_names(word_list)
    
    return render_template('customnames3.html',
                           project_names = project_names,
                           user_word = user_word)

@app.route('/custom-words', methods=['GET'])
def CustomWords():
    
    user_word = request.args['words']
    
    word_list = pw.clean_words(user_word)
    #if not word_list:
        #return redirect(url_for('index'))
        
    redirect_string = pw.create_redirect_string(word_list)
	
    return redirect (redirect_string)

@app.route('/patterns', methods=['GET'])
def Patterns():
    pattern_list = vp.generate_patterns()

    return render_template('patterns.html',
                           pattern_list = pattern_list)

@app.route('/trump', methods=['GET'])
def Trump():
	name_list = t.create_names()
	print(name_list)
	
	return render_template('trump.html',
                           name_list = name_list)
    

@app.route('/sitemap.xml', methods=['GET'])
def SiteMap():
    xml = render_template('sitemap.xml')
    return Response(xml, mimetype='text/xml')
	
if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=33507)
    port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port)
    WSGIServer(('', port), app).serve_forever()
