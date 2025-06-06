""" In this file, we determine the tables of the project by using classes. 
First, the Seat, to know if the seat is free and what is the name of his occupant if there's one
Second, the Table, to know how many seats are available and allow to assign people to a table"""


class Seat :
    #we define attributes and their types
    def __init__(self, free : bool, occupant : str) :
        self.free = free
        self.occupant = occupant
        
    def __str__(self):
        return "The seast is {self.free} and it is not free there's {self.occupant}in it".format(self=self)
    #we see if the seat is available and put somebody on it if free
    def set_occupant(self, name : str) :
        if self.free == True :
            self.occupant = name
            return self.free == False
    #the idea is to remove all occupants with this formula
    def remove_occupant(self) :
        if self.free != True :
            return self.free == True
    


class Table :
    """we define the attributes and their types, in here, the capacity depends on how many seats are available, the seats value has to be 
    a list that refers to the class Seat"""
    def __init__(self, capacity : int, seats):
        self.capacity = capacity
        self.seats = seats
        #we set the list with four seats

    """we put a string function for a human comprehension of the attributes"""
    def __str__(self):
        return "The capacity of the table is {self.capacity} and {self.seats} in it".format(self=self)

    """to see if a seat is available in the table, first we count how many places are available on the table by counting the seats list.
     with error message if the table is more than 4 """
    def left_capacity(self) : 
        if len(self.seats) > self.capacity :
            raise ValueError
        else : 
            return self.left_capacity = self.capacity - len(self.seats)

    """this one says there's a free spot. It goes back to result of left_capacity. If left_capacity if it is """
    def has_free_spot(self) :
        if self.left_capacity < self.capacity :
            return True
        else :
            return False
    
    # This one allow put a name in the list seats. 
    def assign_seat(self,name) :
        self.assign_seat = self.seats(name)

    
