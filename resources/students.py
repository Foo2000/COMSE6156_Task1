import json


class StudentsResource:
    #
    # This code is just to get us started.
    # It is also pretty sloppy code.
    #

    students_file = \
        "C:\\Users\\zfmya\\Desktop\\Columbia Documents\\Coursework\\COMSE6156\\COMSE6156_Projects\\COMSE6156_Task1\\resources\\old-students.json"

    def __init__(self):
        self.students = None

        with open(self.students_file, "r") as j_file:
            self.students = json.load(j_file)

    def get_students(self):
        return self.students
