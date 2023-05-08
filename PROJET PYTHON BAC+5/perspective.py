class perspective:

    # class variable
    university_name = "Golden"

    def __init__(self, first_name, last_name, age, phone_number, address, email, language, diploma, job, salary):

        # Attributs d'instance
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.language = language
        self.diploma = diploma
        self.job = job
        self.salary = salary


        # méthodes
        def get_first_name (self):
            return self.first_name

        def set_first_name (self, first_name):
            self.first_name = first_name
        
        def get_last_name (self):
            return self.last_name

        def set_last_name (self, last_name):
            self.last_name = last_name

        def get_age (self):
            return self.age

        def set_age (self, age):
            self.age = age

        def get_phone_number (self):
            return self.phone_number

        def set_phone_number (self):
            self.phone_number = phone_number

        def get_address (self):
            return self.address

        def set_address (self, adress):
            self.address = address

        def get_email (self):
            return self.email

        def set_email (self, email):
            self.email = email

        def get_language (self):
            return self.language

        def set_language (self, language):
            self.language = language

        def get_diploma (self):
            return self.diploma

        def set_diploma (self, diploma):
            self.diploma = diploma

        def get_job (self):
            return self.job

        def set_job (self, job):
            self.job = job

        def get_salary (self):
            return self.salary

        def set_salary (self, salary):
            self.salary = salary

        # email
        if email >= 10:
            self.email = True
        else:
            self.email = False
        for email in self.email:
            return self.email
        i = 10
        while i > len(self.email):
            i = 10
            return self.email

        # language
        if language < 6:
            self.language = True
        else:
            self.language =  False
        for language in self.language:
            return self.language
        i = 6
        while i < len(self.language):
            i = 6
            return self.language

        # diploma
        if diploma <= 2:
            self.diploma = True
        else:
            self.diploma = False
        for diploma in self.diploma:
            return self.diploma
        i = 2
        while i < len(self.diploma):
            i = 2
            return self.diploma
