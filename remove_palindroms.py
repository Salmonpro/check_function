def remove_palindroms(spells):
    for i in spells:
        a = i.lower()
        if a == a[::-1]:
            spells.remove(a)
    return spells
