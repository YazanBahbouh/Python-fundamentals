from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def chessboard():
    return render_template('index.html')


@app.route('/<x>')
def chessboardRows(x):
    return render_template('rows.html', rows=int(x))

@app.route('/<x>/<y>')
def chessboardRowsCols(x,y):
    return render_template('rowsCols.html', rows=int(x), cols=int(y))

@app.route('/<x>/<y>/<color1>/<color2>')
def chessboardRowsColsColors(x,y,color1,color2):
    return render_template('colors.html', rows=int(x), cols=int(y), color1=color1, color2=color2)



if __name__=="__main__":
    app.run(debug=True)



