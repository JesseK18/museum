import numpy as np
import pymysql


conn = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    db='mydatabase',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
#how to insert result into db
try:
    with conn.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('john@example.com', 'mypassword'))

    # Commit changes
    conn.commit()

    #print("Record inserted successfully")
finally:
    conn.close()

pieces_number = 15
class artwork:
    categories = {}
    def __init__(name,category,artist):
        self.name = name
        self.category = category
        self.artist = artist
        if self.category in categories:
            categories[self.category][self.name] = self.artist
        else:
            categories[self.category] = {self.name: (self.artist)}
            
    def iscorrectguess(category,name,artist):
        try:
            correct_guess = artwork.categories[category][name]
        except:
            print("you are trying to access a non existing entry in the guess")
        if correct_guess == "AI" and artist == "AI":
            guess_v= True
            return True
        elif correct_guess != "AI" and artist != "AI":
            guess_v= True
            return True
        else:
            guess_v= False
            return False
        
        try:
           with conn.cursor() as cursor:
        # Create a new record
               sql = "INSERT INTO `users` (`guess`) VALUES (%s, %s)"
               if guess_v== True: 
                   x= "True"
               else: 
                   x= "False"

               cursor.execute(sql, (x))

    # Commit changes
           conn.commit()

    #print("Record inserted successfully")
        finally:
            conn.close()
class player:
    def __init__(name):
        self.name = name
        self.place = ""
    def guess(self, artname, isrealpainter):
        #TODO implements a guess method that updates some sort of tracker
        pass
    def change_place(self, new_place):
        #TODO implements a method that updated the place and saves the progress
        pass
    def ends_expedition(self):
        #TODO implements a method that handles the end of the expedition
        pass    


