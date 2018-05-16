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
@app.route("/index.html")
def home():
	cacic_sobre =  flatpages.get_or_404("cacic_sobre")
#	cacic_sobre = "dahora"
	return render_template('index.html', cacic_sobre= cacic_sobre)


@app.route("/sobre.html")
def sobre():
	return render_template('sobre.html')

@app.route("/loja.html")
def loja():
	return render_template('loja.html')

@app.route("/contato.html")
def sobre():
	return render_template('contato.html')

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
	return send_from_directory("static/js",arq)

@app.route("/img/<arq>")
def getIMG(arq):
	print("------------------------------------------")
	print(arq)
	return send_from_directory("static/img",arq, mimetype='image/gif')

@app.route("/fonts/<arq>")
def getFONTS(arq):
	print("------------------------------------------")
	print(arq)
	return send_from_directory("static/fonts",arq)

if __name__ == '__main__':
   app.debug = True
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)