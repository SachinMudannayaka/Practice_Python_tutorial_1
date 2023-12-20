#Classes and Objects
class Student:

    def _init_(self,name,major,gpa,is_In_probatoin):
        self.name=name
        self.major=major
        self.gpa=gpa
        self.is_In_probation=is_In_probatoin
    def on_honor_roll(self):
        if self.gpa>=3.2:
            return True
        else:
            return False
