import restaurant

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return str (self.address)

    def available_menus(self, time):
        self.time = time
        menulist = []
        
        for menu in self.menus:
            if time <= menu.end_time and time >= menu.start_time:
                for keys in menu.items:
                    menulist.append(keys)
        print(menulist)


franchise_menu = [restaurant.brunch, restaurant.lunch, restaurant.dinner, restaurant.kids_menu]
new_installment_menu = [restaurant.brunch, restaurant.lunch, restaurant.dinner, restaurant.wine_card]
salad_bar_menu = [restaurant.salad_menu, restaurant.kids_menu]

flagship_store = Franchise('2137 Vatican Street', franchise_menu)
new_installment = Franchise('1 Ben Kenobi Alley', new_installment_menu)
salad_bar = Franchise ('420 Green Rode',salad_bar_menu)