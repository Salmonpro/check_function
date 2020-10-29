def remove_palindroms(spells):
    for i in range(len(spells)):
        for j in spells:
            if i.replace(" ", "").lower() == i.replace(" ", "")[::-1].lower():
                spells.remove(j)
    return spells
