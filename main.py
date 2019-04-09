from models.ua.lviv.iot.dangerLevel import DangerLevel
from models.ua.lviv.iot.health import Health
from models.ua.lviv.iot.insuranceType import InsuranceType
from models.ua.lviv.iot.property import Property
from models.ua.lviv.iot.travel import Travel
from managers.ua.lviv.iot.insuranceManager import InsuranceManager


def insurances_list():
    insurances = list()

    insurances.append(Property('Danylo', 'Chalyi', 5, '098-76-54-443',
                               InsuranceType.PERSONAL, DangerLevel.MIDDLE,
                               DangerLevel.MIDDLE, DangerLevel.HIGH))
    insurances.append(Travel('Zenyk', 'Vasyliv', 9, '098-56-76-442',
                             InsuranceType.HEALTH, DangerLevel.HIGH,
                             DangerLevel.LOW))
    insurances.append(Health('Petro', 'Veres', 32, '045-82-69-945',
                             InsuranceType.PERSONAL,
                             True, DangerLevel.HIGH))
    return insurances


def main():
    manager = InsuranceManager(*insurances_list())

    for i in InsuranceManager.sort_by_alphabetical(insurances_list()):
        print(i)
    print()

    for i in InsuranceManager.sorting_based_on_risk_reduction(insurances_list()):
        print(i)
    print()

    filter_list = manager.filter_by_type(InsuranceType.PERSONAL)
    for i in filter_list:
        print(i)


main()