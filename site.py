from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs

# Mais informações sobre FLASK:
# http://flask.pocoo.org/docs/0.12/quickstart/


app = Flask(__name__)
flatpages = FlatPages(app)
app.config.from_pyfile('config_flask.cfg')

@app.route("/")
def home():
	cacic_sobre =  flatpages.get_or_404("cacic_sobre")
#	cacic_sobre = "dahora"
	return render_template('index.html', cacic_sobre= cacic_sobre)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
