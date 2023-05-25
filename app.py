from flask import Flask,request, jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hey')
def hello_world1():
    return 'Hello dsdsd'

@app.route('/audio_feedback', methods=['GET', 'POST'])
def get_audio_feedback():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return (jsonify(f.filename))

if __name__ == '__main__':
    app.run()
