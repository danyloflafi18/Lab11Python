class InsuranceManager:
    def __init__(self, *insurances):
        self.insurances = insurances

    @staticmethod
    def sort_by_alphabetical(insurances, descending=False):
        return sorted(insurances, key=lambda insurance: insurance.name, reverse=descending)

    @staticmethod
    def sorting_based_on_risk_reduction(insurances, descending=True):
        return sorted(insurances, key=lambda insurance: insurance.number_of_days, reverse=descending)

    def filter_by_type(self, insurance_type):
        return list(filter(lambda insurance: insurance.insurance_type == insurance_type, self.insurances))
