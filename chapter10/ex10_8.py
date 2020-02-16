animals = ['cats.txt', 'dogs.txt']
def show_animals(animal):
    try:
        with open(animal, encoding="utf-8") as file_obj:
            print(file_obj.read()) 
    except FileNotFoundError:
        pass
for animal in animals:
    show_animals(animal)