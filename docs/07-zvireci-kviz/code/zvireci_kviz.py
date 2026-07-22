score = 0

print("Zvireci kviz")

answer = input("Ktere zvire rika mnau? ").lower()
if answer == "kocka":
    print("Spravne!")
    score = score + 1
else:
    print("Spatne. Spravna odpoved je kocka.")

answer = input("Kolik nohou ma pavouk? ")
if answer == "8":
    print("Spravne!")
    score = score + 1
else:
    print("Spatne. Pavouk ma 8 nohou.")

answer = input("Ktery savec umi letat? ").lower()
if answer == "netopyr":
    print("Spravne!")
    score = score + 1
else:
    print("Spatne. Je to netopyr.")

print("Tvoje skore je", score, "ze 3.")
