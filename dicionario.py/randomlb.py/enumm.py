import enum
class animal(enum.Enum):
    cachorro=1
    gato=2
    pantera=2

if animal.cachorro is animal.gato:
    print("Cão e gato são os mesmos animais")
else:
    print("Cão e gato são animais diferentes")

if animal.pantera != animal.gato:
    print("Leão e gato são diferentes")
else:
    print("Pantera e gatos são iguais")