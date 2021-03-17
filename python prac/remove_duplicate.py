def remove_duplicate():
    a=['a','b','c','d','a']
    seen=set(a)
    uniq=[]

    for i in a:
        if i not in seen:
            uniq.append(i)
            seen.add(i)

    return uniq, seen

print(remove_duplicate())
