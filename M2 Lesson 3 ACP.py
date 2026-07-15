class Robot:
    def __init__(self, name, model_version):
        self.name = name
        self.model_version = model_version

    def introduce(self):
        print(f"Hello Harsh! My internal name system is fixed. I am {self.name}, model version {self.model_version}.")


robot_one = Robot("Tom", "T-800")
robot_two = Robot("Jerry", "J-1000")

robot_one.introduce()
robot_two.introduce()