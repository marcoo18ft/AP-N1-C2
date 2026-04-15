# metodos para trabajar con lista
animales = ["gato","perro","vaca","conejo","ornitorrinco","muercielago"]
frutas  = ["durazno","fresa","mango","melon"]

#El metodo APPEND agrega elementos a la lista 
print(animales)
nuevo_animal = input("agregue un nuevo animal a la lista")
animales.append(nuevo_animal)
print(animales)


print(len(animales))
#El metodo INSERT agrega un elemento en la posicion indicada 
otro_nuevo_animal  = input("agregue un nuevo a la lista : ")
animales.insert(0,otro_nuevo_animal)

print(animales)

#el metodo EXTEND permite agregar varios elementos a una lista

animales.extend(["oveja,cerdo"])
print(animales)
animales.extend(frutas)
print(animales)