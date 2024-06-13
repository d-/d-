from flask import Flask, redirect
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    new_path = 'https://dwood.io/' + path
    return redirect(new_path, code=302)

if __name__ == '__main__':
    app.run()