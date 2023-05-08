
class director:

    # class variable
    university_name = "Golden"

    def __init__(self, name, age, years_of_service, field, office, gender, managing_the_university, manage_the_schedule, recruiter, supervisor):

        # Attribus d'instance
        self.name = name
        self.age = age
        self.years_of_service = years_of_service
        self.field = field
        self.office = office
        self.gender = gender
        self.managing_the_univertsity = managing_the_university
        self.manage_the_schedule = manage_the_schedule
        self.recruiter = recruiter
        self.supervisor = supervisor


        # méthodes
        def get_name (self):
            return self.name
        
        def set_name (self,name):
            self.name = name

        def get_age (self):
            return self.age

        def set_age (self, age):
            self.age = age

        def get_years_of_service (self):
            return self.years_of_service

        def set_years_of_service (self, years_of_service):
            self.years_of_service = years_of_service

        def get_field (self):
            return self.field

        def set_field (self, field):
            self.field = field

        def get_office (self):
            return self.office

        def set_office (self, office):
            self.office = office

        def get_gendre (self):
            return self.gender

        def set_gender (self, gender):
            self.gender = gender

        def get_managing_the_university (self):
            return self.managing_the_university
            
        def set_managing_the_university (self, managing_the_university):
            self.managing_the_university = managing_the_university

        def get_manage_the_schedule (self):
            return self.manage_the_schedule

        def set_manage_the_schedule (self, manage_the_schedule):
            self.manage_the_schedule = manage_the_schedule

        def get_recruiter (self):
            return self.recruiter

        def set_recruiter (self, recruiter):
            self.recruiter = recruiter

        def get_supervisor (self):
            return self.supervisor

        def set_supervisor (self, supervisor):
            self.supervisor = supervisor

        # years_of_service
        if years_of_service <= 2012:
            self.years_of_service = True
        else:
            self.years_of_service = False

        for years_of_service in self.years_of_service:
            return self.years_of_service

        i = 10
        while i < len(self.years_of_service):
            i = 10
            return self.years_of_service

        # recruiter
        if recruiter > 20:
            self.recruiter = True
        else:
            self.recruiter = False

        for recruiter in self.recruiter:
            return self.recruiter


        i = 25
        while i > len(self.recruiter):
            i = 25
            return self.recruiter