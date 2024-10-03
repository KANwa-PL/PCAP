class Course:
    def __init__(self, distance=1, name="New course"):
        self.distance = distance
        self.name = name

    def __get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def __get_name(self):
        return self.name


course_1 = Course()
course_2 = Course(5, "Bedrock Trip")
print(course_1._Course__get_name())
print(course_2._Course__get_name())
course_1.set_distance(7)
course_2.set_distance(10)
print(course_1._Course__get_distance())
print(course_2._Course__get_distance())
