import random
temperature = random.randint(20,85)
dewpoint = random.randint(20,temperature)

print("At approximately what altitude above the surface would the pilot expect the base of cumuliform clouds if the surface air temp is " + str(temperature) + " F and the dewpoint is " + str(dewpoint) + " F? ")
answer = input("> ")
if float(answer) == round(((temperature - dewpoint) / 4.4) * 1000.0, 0):
    print("Correct.")
else:
    print("Incorrect. (" + str(temperature) + " - " + str(dewpoint) + " / 4.4) * 1000 = " + str(round(((temperature - dewpoint) / 4.4) * 1000.0, 0)))
