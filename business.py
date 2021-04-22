import restaurant
import franchise

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

first_business = Business ("Basta Fazoolin' with my Heart", [franchise.flagship_store, franchise.new_installment])
second_business = Business ("Salad Place with Basta", franchise.salad_bar)