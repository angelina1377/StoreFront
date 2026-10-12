from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Обработчик ошибки 404 (страница не найдена)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    print("Сервер запущен! Откройте http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
