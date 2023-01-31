name=" berdzenishvili"
print(len(name))
print(name[3:8:2])
print("l"in name)
print("g" not in name)

print("K"in name)
print("l" not in name)

print(len (name))
print(name.strip())
print(name.upper())

print(name.replace("e", "%"))



my_sentence="""""ჩემი პირველი შეფასებიტ შემიძლია ვთქვა,
რომ ამ აკადემიაში მოხვედრით,
ძალიან კმაყოფილი ვარ
და მინდა მივაღწიო წარმატებას"""
print(my_sentence.replace("ა","ი"))
print("ა" in my_sentence)
print("ჭ" not in my_sentence)


name2="    barcelona      "
print(name2)
print(name2.strip())
print(name2.replace(" ","b"))
print(name2.upper(), name2.replace(" ", "f"))
