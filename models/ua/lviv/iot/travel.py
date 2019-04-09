from models.ua.lviv.iot.insuranceType import InsuranceType
from models.ua.lviv.iot.dangerLevel import DangerLevel
from models.ua.lviv.iot.insurance import Insurance


class Travel(Insurance):

    def __init__(self,
                 name=None,
                 surname=None,
                 number_of_days=0,
                 telephone=None,
                 insurance_type=InsuranceType.HEALTH,
                 medical_assistance=DangerLevel.HIGH,
                 accident=DangerLevel.LOW
                 ):
        super().__init__(name, surname, number_of_days,
                         telephone, insurance_type)
        self.medical_assistance = medical_assistance
        self.accident = accident

    def __str__(self):
        return "{" + "name='" + self.name + '\'' \
               + ", surname='" + self.surname + '\'' \
               + ", number_of_days=" + str(self.number_of_days) \
               + ", telephone=" + str(self.telephone) \
               + ", insurance_type=" + str(self.insurance_type)
