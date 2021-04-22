import restaurant
import franchise
import business

while True:
    starting_string = "Welcome to program which saves clients' bills!"
    explanation_string = "If you want to end program and save bill enter: ***"
    thanx = "Thank you fot using our app"
    client_order = []

    print (starting_string)
    print (explanation_string)
    client_no_meals = (input ("How many meals did client ordered? "))

    if client_no_meals != '***':
        client_no_meals = int (client_no_meals)
        for i in range(0, client_no_meals):
            client_meal = input()
            client_meal = client_meal.lower()
            client_order.append(client_meal)

    else: 
        path = 'orders_from_restaurant.txt'
        opened_file = open(path, 'a')

        for element in client_order:
            opened_file.write(element + '\n')
        opened_file.close ()
        
        print(thanx)
        break

