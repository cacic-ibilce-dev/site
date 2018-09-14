from flask import Flask, render_template, send_from_directory,send_file
from flask_flatpages import FlatPages, pygments_style_defs
import os


# Mais informações sobre FLASK:
# http://flask.pocoo.org/docs/0.12/quickstart/

ROOT = os.path.dirname(os.getcwd())
app = Flask(__name__)
flatpages = FlatPages(app)
app.config.from_pyfile('config_flask.cfg')
INDICES = '/templates/*.html' # Usado para a definição dos linkis


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
def contato():
	return render_template('contato.html')

#
#	ARQUIVOS CSS IMAGENS ETC...
#
@app.route("/atas.html")
def atas():
    return render_template('/atas.html')

@app.route("/pautas.html")
def pautas():
    return render_template('pautas.html')

@app.route("/eventos.html")
def eventos():
	return render_template('eventos.html')

@app.route("/css/<arq>")
def getCSS(arq):
	return send_from_directory("static/css/",arq, mimetype="text/css")

@app.route("/js/<arq>")
def getJS(arq):
	return send_from_directory("static/js/",arq)

@app.route("/img/<arq>")
def getIMG(arq):
	return send_from_directory("static/img/",arq, mimetype='image/gif')

@app.route("/fonts/<arq>")
def getFONTS(arq):
	return send_from_directory("static/fonts/",arq)

#
#	COISAS EXTRAS 
#	DESENVOLVLIMENTO
#

'''
Essa função é mais para ser usada no desenvolvimento

Qualquer site que já não foi roteado acima será roteado abaixo. Facilitando
o desenvolvimento (Especialmente para a galera do front)

O ARQUIVO HTML TEM QUE ESTAR DENTRO DO DIRETORIO TEMPLATES
'''
@app.route('/<path:path>/')
def catch_all(path):
	print(path)
	return render_template(path)

if __name__ == '__main__':
   app.debug = True
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)