# This lab was built by creating sub musicians and giving them attributes (see the commented code). Then we made two overarching classes - Band and Musician.
# Musician takes in all of the sub-musicians by having a super call in the sub musician. 
# Band is its own class that just takes in band names.
# There is NO CORRELATION between the bands and the members, aka the band is NOT keeping track of certain Musicians. 

class Band:
    instances = []
    #The tests are looking for this array to be called instances and the method to be called to_list.

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self)
        #When we make a band this pushes it into the instances list
        #The musician subclass does not need members since Band has it.

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. Name = {self.name}, members={self.members}"

    def play_solos(self):
        return [member.play_solo() for member in self.members]
        #When you call this (Band.play_solo) This is saying the members in the band will each play their solo

    @classmethod
    def to_list(cls):
        return cls.instances
        #This is a class method that will loop through the musician attributes. This is telling us the items in the list.

class Musician():
    #Here we are making musician a new base class.
    def __init__(self, name, instrument, solo):
        #Name is the instrumentalist like Guitarist or the name of the class that extends musician.

        #We no longer need the super here as this is being called as a base class
    #When passing a super class it seems like the parents properties are by the class initialization and the child's properties (aka all of the functions you created for them) are after the super call
        self.name = name
        self.instrument = instrument
        self.solo = solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
        #You CAN call a function in an F-String!

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"
        # This __class__ will pull out the name of the MUSICIAN class instead of the name of the instrumentalist

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    def __init__(self, name):
        #This is the new info that is passed in here. 
        super().__init__(name, "guitar", "face melting guitar solo")
        #This is where we pass in the musician specific information.
        #We don't need to pass up Guitarist as this is the name of the CLASS that gets passed to Musician

#This code is no longer needed when we pass the Musician Method all of the specifics that the Guitarist needs! The first way is preserved below as written in the Test driven development before refactoring.

    # def __str__(self):
    #     return f"My name is {self.name} and I play guitar"

    # def __repr__(self):
    #     return f"Guitarist instance. Name = {self.name}"
    
    # def name(self):
    #     return f"{self.name}"
        
    # def get_instrument(self):
    #     return "guitar"

    # def play_solo(self):
    #     return "face melting guitar solo"
    

class Bassist(Musician):
    def __init__(self, name):
        #This is the new info that is passed in here. 
        super().__init__(name, "bass", "bom bom buh bom")

#class Bassist:
    
#This code is no longer needed when we pass the Musician Method all of the specifics that the Bassist needs! The first way is preserved below as written in the Test driven development before refactoring.

    # def __init__(self, name, members=None):
    #     self.name = name
    #     self.members = members

    # def __str__(self):
    #     return f"My name is {self.name} and I play bass"

    # def __repr__(self):
    #     return f"Bassist instance. Name = {self.name}"
    
    # def name(self):
    #     return f"{self.name}"
        
    # def get_instrument(self):
    #     return "bass"

    # def play_solo(self):
    #     return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name):
        #This is the new info that is passed in here. 
        super().__init__(name, "drums", "rattle boom crash")

# class Drummer:
#     def __init__(self, name, members=None):
#         self.name = name
#         self.members = members
#This code is no longer needed when we pass the Musician Method all of the specifics that the Drummer needs! The first way is preserved below as written in the Test driven development before refactoring.

    # def __init__(self, name, members=None):
    #     self.name = name
    #     self.members = members

    # def __str__(self):
    #     return f"My name is {self.name} and I play drums"

    # def __repr__(self):
    #     return f"Drummer instance. Name = {self.name}"
    
    # def name(self):
    #     return f"{self.name}"
        
    # def get_instrument(self):
    #     return "drums"

    # def play_solo(self):
    #     return "rattle boom crash"

# if __name__ == '__main__':
