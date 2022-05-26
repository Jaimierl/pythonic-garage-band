class Band:
    to_list = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. Name = {self.name}, members={self.members}"

    # def play_solo(self):
    #     return [member.play_solo() for member in self.members]
    #     #This is saying the members in the band will each play their solo

    # @classmethod
    # def play_solo(cls):
    #     return cls.to_list
    #     #This is a class method that will loop through the musician attributes

class Musician(Band):
    def __init__(self, name, members=None):
        super(Musician, self).__init__(self, name, instrument, solo)
    #When passing a super class it seems ilke the parents properties are by the class initialization and the child's properties (aka all of the functions you created for them) are after the super call
        self.name = name
        self.instrument = instrument
        self.solo = solo


class Guitarist(Musician):
    def __init__(self, name):
        super(Guitarist, self).__init__(name,"Guitarist", "guitar", "face melting guitar solo")

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    def name(self):
        return f"{self.name}"
        
    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

class Bassist:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    
    def name(self):
        return f"{self.name}"
        
    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

class Drummer:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
    def name(self):
        return f"{self.name}"
        
    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"

# if __name__ == '__main__':
