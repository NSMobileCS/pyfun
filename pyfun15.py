name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(a1, a2):
    return dict(zip(a1, a2))

md = make_dict(name, favorite_animal)
print(md)
print(type(md))
