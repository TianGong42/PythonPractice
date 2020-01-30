available_toppings = ['mushrooms', 'olive','green peppers',
                        'pepperoni','pineapple','extra cheese']
requestd_toppings = ['mushrooms','french fries', 'extra cheese']

for requestd_topping in requestd_toppings:
    if requestd_topping in available_toppings:
        print("Adding " + requestd_topping + ".")
    else:
        print("Sorry, we don't have " + requestd_topping + '.')
print("\nFinshed making your pizza!")