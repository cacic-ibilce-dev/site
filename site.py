from flask import Flask, render_template, send_from_directory,send_file
from flask_flatpages import FlatPages, pygments_style_defs
import os


# Mais informações sobre FLASK:
# http://flask.pocoo.org/docs/0.12/quickstart/

ROOT = os.path.dirname(os.getcwd())
app = Flask(__name__)
flatpages = FlatPages(app)
app.config.from_pyfile('config_flask.cfg')

#
#	INDICES
#

@app.route("/")
def home():
	cacic_sobre =  flatpages.get_or_404("cacic_sobre")
#	cacic_sobre = "dahora"
	return render_template('index.html', cacic_sobre= cacic_sobre)

@app.route("/sobre.html")
def sobre():
	return render_template('sobre.html')


#
#	ARQUIVOS CSS IMAGENS ETC...
#

@app.route("/css/<arq>")
def getCSS(arq):
	print("------------------------------------------")
	print(arq)
	print(ROOT+"/site/static/css/")
	return send_from_directory("static/css/",arq, mimetype="text/css")

@app.route("/js/<arq>")
def getJS(arq):
	print("------------------------------------------")
	print(arq)
	return send_from_directory(ROOT+"/site/static/js",arq)

@app.route("/img/<arq>")
def getIMG(arq):
	print("------------------------------------------")
	print(arq)
	return send_from_directory(ROOT+"/site/static/img",arq, mimetype='image/gif')

@app.route("/fonts/<arq>")
def getFONTS(arq):
	print("------------------------------------------")
	print(arq)
	return send_from_directory(ROOT+"/site/static/fonts",arq)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)