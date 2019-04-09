from models.ua.lviv.iot.insuranceType import InsuranceType


class Insurance:

    def __init__(self,
                 name=None,
                 surname=None,
                 number_of_days=0,
                 telephone=None,
                 insurance_type=InsuranceType.PERSONAL
                 ):
        self.name = name
        self.surname = surname
        self.number_of_days = number_of_days
        self.telephone = telephone
        self.insurance_type = insurance_type

    def __str__(self):
        return "{" + "name='" + self.name + '\'' \
               + ", surname='" + self.surname + '\'' \
               + ", number_of_days=" + str(self.number_of_days) \
               + ", telephone=" + str(self.telephone) \
               + ", insurance_type=" + str(self.insurance_type)