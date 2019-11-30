# parent class
class Bird:

    def __init__(self, something):
        self.something = something
        self.species = 'bird'
        print("Bird is ready")

    def who_is_this_bird(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):

    def __init__(self, something):
        # call super() function
        super(Penguin, self).__init__(something)
        # super(Penguin, self).__init__(something)
        print("Penguin is ready")

    def what_species_is_this(self):
        print(self.species)

    def who_is_this_bird(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.who_is_this_bird()
peggy.swim()
peggy.run()
peggy.what_species_is_this()
