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
        return render_template('result.html',newName=getName)
        getEmail=request.form['email']
        return render_template('result.html',newEmail=getEmail)
        getPhone=request.form['phone']
        return render_template('result.html',newPhone=getPhone)
        getSubject=request.form['subject']
        return render_template('result.html',newSubject=getSubject)
        getMessage=request.form['msg']
        return render_template('result.html',newMessage=getMessage)



if(__name__=='__main__'):
    app.run(debug=True)