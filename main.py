import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()


db = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user =os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  database=os.getenv("DB_DATABASE")
)

cursor = db.cursor()


class student_managment_system:
  def __init__(self, database, cursor):
    self.database = database
    self.cursor = cursor

  def add_student(self):
    name =input("Enter your name: ")
    course_name = input("Enter your course name: ")
    teacher_name = input("Enter your class teacher name: ")
    end_date = input("Enter course end date (YYYY-MM-DD): ")

    sql = """
    INSERT INTO Student_details(name, course_name, class_teacher_name, course_end_date)
    values(%s, %s, %s, %s)
    """
    values=(
      name,
      course_name,
      teacher_name,
      end_date
    )

    self.cursor.execute(sql,values)
    self.database.commit()

    print("Student add successfuly ")

  def view_data(self):

    self.cursor.execute(
      "SELECT * FROM Student_details "
    )

    students= self.cursor.fetchall()

    if not students:
      print("\n Data not Found!")
      return

    print("==============STUDENTS============")

    count =1
    for student in students:
      print(
        f"Count:{count} |"
        f"ID: {student[0]} | "
            f"Name: {student[1]} | "
            f"Course: {student[2]} | "
            f"Teacher: {student[3]} | "
            f"End Date: {student[4]}"
      )
    count +=1

student_system=student_managment_system(db,cursor)

try :
  while True:
    print("=========STUDENT MANAGEMNT SYSTEM==========")
    print("1. Add Student")
    print("2. View Student")
    print("3. Exit")

    try:
      Choice = int(input("Enter your choice: "))
    except ValueError:
      print("\n Enter valid number!")
      continue

    if Choice ==1:
      student_system.add_student()

    elif Choice ==2:
      student_system.view_data()

    elif Choice ==3:
      print("Goodby!")
      break

    else:
      print("Invalid choice")

finally:
  cursor.close()
  db.close()