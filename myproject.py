from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
# DB creation
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///collegeinfo.sqlite3'
mydb =SQLAlchemy(app)

# Table creation
class Signup(mydb.Model):
    id=mydb.Column(mydb.Integer,primary_key=True)
    s_name=mydb.Column(mydb.String(200))
    s_rollno=mydb.Column(mydb.String(40))
    s_mailid=mydb.Column(mydb.String(100))
    s_phno=mydb.Column(mydb.String(40))
    s_branch=mydb.Column(mydb.String(40))

    # constructor creation
    def __init__(self,name,rollno,emailid,phno,branch):
        self.s_name=name
        self.s_rollno=rollno
        self.s_mailid=emailid
        self.s_phno=phno
        self.s_branch=branch

@app.route('/myportal/signup',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        data=request.form
        # print(data)
        stu_name=data['name']
        stu_rollno=data['rollno']
        stu_emailid=data['emailid']
        stu_phno=data['phno']
        stu_branch=data['branch']

        sgn=Signup(stu_name,stu_rollno,stu_emailid,stu_phno,stu_branch)
        mydb.session.add(sgn)
        mydb.session.commit()

        return render_template('status.html')

    return render_template('signup.html')

@app.route('/myportal/studentlist')
def display():
    return render_template('showDetails.html',data=Signup.query.all())

@app.route('/myportal/delete/<int:id>')
def Delete(id):
    mydb.session.query(Signup).filter(Signup.id==id).delete()
    mydb.session.commit()
    return redirect(url_for('display'))

if __name__=='__main__':
    mydb.create_all()
    app.run(debug=True)
