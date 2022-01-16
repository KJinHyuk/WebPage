from flask import Flask, request, render_template, redirect


app = Flask(__name__)
if __name__ == '__main__':
    app.run( debug=True) #요청 대기..

@app.route("/hello")
def hello():
    return render_template('hello.html')

@app.route("/form")
def form():
    return render_template('form.html')

#@app.route("/formproc")    
#def formproc():
#    # print(requset.args)
#    mylengh = request.args['mylengh']
#    myweght = request.args['myweght']
#    avweght = request.args['avweght = (leght - 100)*0.85']
#    return render_template('formfroc.html', myleght = mylengh, myweght = myweght, avweght = avweght)
    
    
#@app.route("/img")
#def img():
  
 #       return render_template('img.html')


