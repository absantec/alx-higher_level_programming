
#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    new_list = my_list[:]
    for s in range(len(new_list)):
        if new_list[s] == search:
            new_list[s] = replace
    return (new_list)
