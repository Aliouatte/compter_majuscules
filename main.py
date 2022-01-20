# Compter les majuscules



from itertools import count


def count_majuscule(str):
    nb_maj = 0
    for c in str:
        if c.isupper():
            nb_maj +=1
    return nb_maj


def count_majuscule2(str):
    l = [1 if c.isupper() else 0 for c in s ]
    print("le nombre de majuscule est : ",sum(l))


s = "Bonjour MayliNe"

count_majuscule2(s)
print("le nombre de majuscule est : ",count_majuscule(s))



