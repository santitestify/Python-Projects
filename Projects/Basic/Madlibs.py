# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to____"

#y outuber = "santiago sosa"  # some string variable

# a few ways to do this
# print("Subscribe to " + youtuber)
# print("Subscribe to {}" .format(youtuber))
# print(f"Subscribe to {youtuber}")

adj = input("Adjective : ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programmins is {adj}! it makes me so excited all the time because" \
         f" i love {verb1}. stay hydrated and {verb2} like you are {famous_person}"

print(madlib)



