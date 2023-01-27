from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/play')
def boxes():
    return render_template('index.html')

@app.route('/play/<times>')
def xBoxes(times):
    return render_template(
        'index.html', numTimes = int(times))

@app.route('/play/<times>/<color>')
def colorBoxes(times,color):
    return render_template(
        'index.html', numTimes = int(times), boxColor = str(color))


if __name__=="__main__":
    app.run(debug=True) 