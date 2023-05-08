
class studnet:

    # class variable
    university_name = "Golden"

    def __init__(self, name, age, master, project, note_math, school_year, exercise, examination, class_informatique, stock_exchange):

        # Attribus d'instance
        self.name = name
        self.age = age
        self.master = master
        self.project = project
        self.note_math = note_math
        self.school_year = school_year
        self.exercise = exercise
        self.examination = examination
        self.clase_informatique = class_informatique
        self.stock_exchange = stock_exchange

       
        # Méthodes
        def get_name (self):
            return self.name

        def set_name (self, name):
            self.name = name

        def get_age (self):
            return self.age
        
        def set_age (self, age):
            self.age = age

        def get_master (self):
            return self.master

        def set_master (self, master):
            self.master = master

        def get_project (self):
            return self.project

        def set_project (self, project):
            self.project = project

        def get_note_math (self):
            return self.note_math

        def set_note_math (self, note_math):
            self.note_math = note_math

        def get_school_year (self):
            return self.school_year

        def set_school_year (self, school_year):
            self.school_year

        def get_exercise (self):
            return self.exercise

        def set_exercise (self, exercise):
            self.exercise

        def get_examination (self):
            return self.examination

        def set_examination (self, examination):
            self.examination

        def get_classe_informatique (self):
            return self.classe_informatique

        def set_classe_informatique (self, classe_informatique):
            self.classe_informatique

        def get_stock_exchange (self):
            return self.stock_exchange

        def set_stock_exchange (self, stock_exchange):
            self.stock_exchange

        
        # note_math

        if note_math >= 10:
            self.is_note_math = True
        else:
            self.is_note_math = False
    

        # school_year
        if school_year <= 2019:
            self.is_school_year = True
        else:
            self.is_school_year = False

        # examination
        if examination <= 15:
            self.is_examination = True
        elif examination < 10 and examination > 15:
            print ("succeed")
        
    