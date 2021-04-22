class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        whats_in_the_menu = '{m} menu available from {st} to {et}'
        return whats_in_the_menu.format (m = self.name, st = self.start_time, et = self.end_time)

    def calculate_bill(self, purchased_items):
        self.purchased_items = purchased_items
        bill = []

        for item in purchased_items:
            for key, value in self.items.items():
                if item == key:
                    bill.append(value)

        cost_of_meal = sum (bill)
        return cost_of_meal

wines = {'cabernet sauvignon': 50, 'merlot': 48, 'pinot noir': 56, 'sangiovese': 67, 'chardonnay': 65, 'madeira': 56, 'champagne': 100}
brunch_meals = {'toasts': 5.60, 'waffles': 7.80, 'crepes with strawberry jam': 11.00, 'coffee': 6.00, 'tea': 5.60}
lunch_meals = {"pizza diavola": 25.00, 'pizza margherita': 20, 'tomato soup with foccacia': 9.00, 'cool drinks': 5.00}
dinner_meals = {'salad': 6.70, '\"eat what you want\" pizza': 30, 'cool drinks': 5, 'red Wine': 15, 'beer': 7.00}
kids_menu_meals = {'french fries': 5, "juice": 4, "penne with tomato sauce": 10}
salad_menu = {'ceasar salad': 7, 'coleslaw': 4, 'greek salad': 8, 'mediterean salad': 8.5}

brunch = Menu ("Brunch",brunch_meals, 11, 16)
lunch = Menu ("Early Dinner", lunch_meals, 15, 18)
dinner = Menu ("Dinner", dinner_meals, 17, 23)
kids_menu = Menu ("Kids Menu",kids_menu_meals , 11, 21)
wine_card = Menu ("Wine Card", wines, 14, 23)
salad = Menu ("Salads", salad_menu, 11, 20)

#sum_of_bill = "The cost of client's meal is {}!"

