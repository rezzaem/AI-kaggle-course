def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    return True if arrivals.index(name)>=len(arrivals)//2 and name!=arrivals[-1] else False

if __name__=='__main__':
    arrivals=['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
    print(fashionably_late(arrivals, 'Adela'))