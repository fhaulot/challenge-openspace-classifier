import random
import pandas as pd

class Openspace:

    def __init__(self, tables):
        self.tables = tables
        self.number_of_tables = len(tables)

    
    # Method to assign the names of the list to the tables created based on length of input file
    def organize(self, names):
         
         random.shuffle(names)

         for n in names:
               for t in self.tables:
                    table.assign_seat(n)
  

     # Method to show the configuration of the tables based on input
     def display():
         for num, table in enumerate(self.tables, start=1):
             print(f"Table {num}:")
             for seat in table.seats:
                 occupant = seat.occupant
                 print(f"\n{occupant}")
             print("\n")

     # Method to save the configuration of the table in an excel file
     def store(filename):
             data = []
            
             for num, table in enumerate(self.tables, start=1):
                 for seat in table.seats:  
                      data.append(
                           f"Table {num} ",
                           seat.occupant
                      )            
             df = pd.DataFrame(data)
             df.to_excel(fileName, index=False)