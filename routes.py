from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return 'Hello World, lorem ipsum dolor sit amet... asdasdas.. asdashjdgashgdjasgdjhasgdjhasgdjgds'

@app.route('/user/<username>')
def show_user_profile(username):
	# mostra o username para o usuario
	return 'User %s' % username

if __name__ == '__main__':
	app.run(debug=True)