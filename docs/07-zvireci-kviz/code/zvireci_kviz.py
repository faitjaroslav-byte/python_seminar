score = 0

print("Zvířecí kvíz")

answer = input("Které zvíře říká mňau? ").lower()
if answer == "kočka":
    print("Správně!")
    score += 1
else:
    print("Špatně. Správná odpověď je kočka.")

answer = input("Kolik nohou má pavouk? ")
if answer == "8":
    print("Správně!")
    score += 1
else:
    print("Špatně. Pavouk má 8 nohou.")

answer = input("Který savec umí létat? ").lower()
if answer == "netopýr":
    print("Správně!")
    score += 1
else:
    print("Špatně. Je to netopýr.")

print("Tvoje skóre je", score, "ze 3.")
