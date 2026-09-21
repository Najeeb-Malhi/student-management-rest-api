from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

students_list=[
    {
        "id":1, "name":"Najeeb", "age":19, "department":"Computer Engineering"
    },
    {
        "id":2, "name":"Ali", "age":19, "department":"Computer Science"
    },
    {
        "id":3, "name":"Haseeb", "age":21, "department":"Computer Engineering"
    },
    {
        "id":4, "name":"Umar", "age":18, "department":"Electrical Engineering"
    },
    {
        "id":5, "name":"Umair", "age":20, "department":"Computer Science"
    },
]

class Student(BaseModel):
    name: str
    age: int
    department: str

@app.get("/students")
def get_st(age: int, department: str):
     filtered=[
          s for s in students_list 
          if s["age"] == age and s["department"] == department
     ] 
     return {
         "age":age,
         "department": department,
         "count":len(filtered),
         "results":filtered
    }

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for s in students_list:
        if s["id"] == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")
@app.post("/students")
def add_student(student: Student):
    new_id = len(students_list) + 1
    new_student = {
    "id": new_id,
    "name": student.name,
    "age": student.age,
    "department": student.department
}
    students_list.append(new_student)
    return new_student
