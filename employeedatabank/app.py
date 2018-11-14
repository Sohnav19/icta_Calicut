from flask import Flask,render_template,request
from emplodata import Employee
app=Flask(__name__)

@app.route("/")
def Index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/employee details")
def employee():
    getEmployee=Employee()

    return render_template('employeedata.html',myEmployeedetails=getEmployee)

    



if(__name__=='__main__'):
    app.run()