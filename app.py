from flask import request
from flask import Flask, jsonify
app = Flask(__name__)

student  = [{"id":1,"name":"Arbaz","age":24},
            {"id":2,"name":"Anas","age":20},
            {"id":3,"name":"Zidan","age":25}
            ]
@app.route('/')
def arbu():
    return "<h1 style= color:magenta> Student </h1>", 200
@app.route('/student',methods=["GET"])
def get_all_student():
    return jsonify(student), 200
@app.route('/student/<int:student_id>',methods= ["GET"])
def get_student(student_id):
  for i in student:
    if i['id'] == student_id:
      return jsonify(i['name']) 
  return "<p>Student not found</p>"

@app.route('/student',methods = ["POST"])
def addstudent():
  student_details = request.get_json()
  print("student_details",student_details)
  new_student_id  = student[-1]["id"]+1
  student_details["id"] = new_student_id
  student.append(student_details)
  return jsonify("Successfully Added") 

@app.route('/student/<int:student_id>',methods = ["GET","PUT"])
def update_student(student_id):
  update_student_details = request.get_json()
  for i in student:
    if i['id'] == student_id:
      if update_student_details.get("name"):
        i['name'] = update_student_details.get('name')
      if update_student_details.get("age"):
        i['age'] = update_student_details.get('age')
  return f"{student}Updated Successfully" 
  

@app.route('/student<int:student_id>',methods = ["DELETE"])
def delete_student(student_id):
  for i in student:
    if i['id'] == student_id:
      student.remove(i)
      return "Removed successfully"
  return "Not found"
if __name__ == "__main__":
    app.run(debug=True)
