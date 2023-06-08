from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eight_by_eight():
    return render_template("index.html", row=8, col=8, color_one="black", color_two="red")

#http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/<int:x>')
def eight_by_four():
    return render_template("index.html", row=x, col=8,color_one="black", color_two="red")

@app.route('/<int:x>/<int:y>')
def hello(x, y):
    return render_template("index.html", row=x, col=y, color_one="black", color_two="red")




if __name__=="__main__": 
    app.run(debug=True)   
