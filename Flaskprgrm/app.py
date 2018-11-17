from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send',methods=['GET','POST'])
def send():
    if(request.method=='POST'):
        getName=request.form['name']

        getEmail=request.form['email']
        
        getPhone=request.form['phone']

        getSubject=request.form['subject']

        getMessage=request.form['msg']
        return render_template('result.html',newMessage=getMessage,newSubject=getSubject,newPhone=getPhone,newEmail=getEmail,newName=getName)



if(__name__=='__main__'):
    app.run(debug=True)