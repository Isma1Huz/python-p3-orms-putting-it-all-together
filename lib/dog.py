
import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()


class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed
        self.id = None
    
    @classmethod
    def create_table(cls):
        sql = """
          CREATE TABLE IF NOT EXIST dog (id INTERGER, name TEXT, breed TEXT)
        """
        CURSOR.execute(sql)
    def drop_table(cls):
        sql = """
            DROP TABLE IF  EXIST dog 
        """
        CURSOR.execute(sql)

    def save(self):
        # If the Dog instance has an ID, update the existing record; otherwise, insert a new one.
        if self.id:
            self.update()
        else:
            self.insert()

    def insert(self):
        # Insert a new row into the database and update the instance's ID.
        connection = sqlite3.connect('dogs.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO dogs (name, breed) VALUES (?, ?)", (self.name, self.breed))
        self.id = cursor.lastrowid
        connection.commit()
        connection.close()

    def update(self):
        # Update an existing row in the database.
        connection = sqlite3.connect('dogs.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE dogs SET name = ?, breed = ? WHERE id = ?", (self.name, self.breed, self.id))
        connection.commit()
        connection.close()

    @classmethod
    def new_from_db(cls, row):
        # Create a new Dog instance from a database row.
        return cls(row[0], row[1], row[2])

    @classmethod
    def find_by_name(cls, name):
        # Find a dog by name and return a Dog instance.
        connection = sqlite3.connect('dogs.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dogs WHERE name = ?", (name,))
        row = cursor.fetchone()
        connection.close()
        if row:
            return cls.new_from_db(row)
        else:
            return None

    @classmethod
    def find_by_id(cls, id):
        # Find a dog by ID and return a Dog instance.
        connection = sqlite3.connect('dogs.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dogs WHERE id = ?", (id,))
        row = cursor.fetchone()
        connection.close()
        if row:
            return cls.new_from_db(row)
        else:
            return None

    @classmethod
    def get_all(cls):
        # Get all dogs from the database and return them as a list of Dog instances.
        connection = sqlite3.connect('dogs.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dogs")
        rows = cursor.fetchall()
        connection.close()
        return [cls.new_from_db(row) for row in rows]





























# import sqlite3

# # CONN = sqlite3.connect('lib/dogs.db')
# # CURSOR = CONN.cursor()

# class Cat:
    
#     all = []

#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#         self.add_to_cat(self)

#     @classmethod

#     def add_to_cat(cls, cat):
#         cls.all.append(cat)
#     def save(self, cursor):
#         cursor.execute(
#             "INSERT INTO cats (name, breed, age) VALUES(?,?,?)",
#             (self.name, self.breed, self.age)

#         )



# db_connection = sqlite3.connect("data.db")
# db_cursor = db_connection.cursor()
# db_cursor.execute("CREATE TABLE cats (name TEXT, breed TEXT, age INTERGER)")

# Cat("me", "you", 12)
# Cat("me", "you", 12)

# for cat in Cat.all :
#     cat.save(db_cursor)

