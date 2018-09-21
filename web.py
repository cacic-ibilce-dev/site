from flask import Flask, render_template, send_from_directory,send_file
from flask_flatpages import FlatPages, pygments_style_defs
import os

import cacic_code as cacic

# Mais informações sobre FLASK:
# http://flask.pocoo.org/docs/0.12/quickstart/


ROOT = os.path.dirname(os.getcwd())
app = Flask(__name__)
flatpages = FlatPages(app)
app.config.from_pyfile('config_flask.cfg')


#
#	Ler o "banco de dados"
#

CHAPAS = cacic.Chapas()
SOBRE = flatpages.get_or_404("cacic_sobre")


print("===================")
for c in CHAPAS:
	print("ano"+ c[0])
	for a in c[1]:
		print(a)

#
#	INDICES DO SITE
#

@app.route("/")
@app.route("/index.html")
def home():
	return render_template('index.html')


@app.route("/sobre.html")
def sobre():
	# Pega o arquivo que contém a descrição do CACIC
	

	return render_template('sobre.html',cacic_sobre=SOBRE,chapas = CHAPAS)

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

# favicon é um icone 16x16 que fica no topo do browser
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

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