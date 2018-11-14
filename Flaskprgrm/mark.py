from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('generater.html')

@app.route('/generater')
def home():
    return render_template('generater.html')

@app.route('/send',methods=['GET','POST'])
def send():
    if(request.method=='POST'):
        getName=request.form['name']
        
        getRegisterNo=request.form['regno']
        
        getSubject1=request.form['subject1']
        
        getSubject2=request.form['subject2']

        getSubject3=request.form['subject3']
        return render_template('markresult.html',newName=getName,newRegister=getRegisterNo,newSubject1=getSubject1,newSubject2=getSubject2,newSubject3=getSubject3)



if(__name__=='__main__'):
    app.run(debug=True)