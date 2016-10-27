def permutations(string):
    from itertools import permutations
    perms = list(set(permutations(string)))
    new_list = []
    for tuple in perms:
        perm = ''
        for char in tuple:
            perm += char
        new_list.append(perm)
    return new_list
