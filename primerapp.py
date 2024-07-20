meme_dict = {
            "LOL" : "una respuesta a algo gracioso",
            "CRINGE" : "algo raro o embarazoso",
            "ROFL" : "una respuesta a una broma",
            "SHEESH" : "ligera desaprobación",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado"
            }

name = input("Hola,¡Cual es tu nombre?")
print("¡Hola", name)
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Palabra no encontrada")
