from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db=SQLAlchemy(app)
ma = Marshmallow(app)


class Student(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String,nullable= False)
    age = db.Column(db.Integer,nullable = False)


class StudentSchema(ma.Schema):
    class Meta:
        model =  Student
        fields = ['id','name','age']
        load_instance = True
student_schema =StudentSchema()
students_schema =StudentSchema(many=True)
with app.app_context():
    db.create_all()
@app.route("/")
def hello():
    return "<p>Arbaz Shaikh</p>"


@app.route('/student',methods =["POST"])    
def add_student():
    student_detail = request.get_json()
    student = Student(name =student_detail['name'],age= student_detail['age'])
    db.session.add(student)
    db.session.commit()
    return {"message":"Successfully"}
@app.route('/student',methods=["GET"])
def get_student():
    students = Student.query.all()
    return students_schema.dump(students)

@app.route('/student/<int:student_id>',methods=["GET"])
def get_student_id(student_id):
    student = Student.query.get(student_id)
    return student_schema.dump(student)


@app.route('/student/<int:student_id>',methods=["PUT"])
def update(student_id):

    student = Student.query.get(student_id)
    update_details=request.get_json()
    
    if update_details.get('name'):
        student.name = update_details.get('name')
    if update_details.get('age'):
        student.age = update_details.get('age')
    db.session.commit()
    return student_schema.dump(student)

@app.route('/student/<int:student_id>',methods=['DELETE'])
def delete(student_id):
    student= Student.query.get(student_id)
    db.session.delete(student)
    db.session.commit()
    return {'message':'Sucessfully deleted'}
if __name__ == "__main__":
    app.run(debug=True)
