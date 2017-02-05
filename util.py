# FOR ADDITIONAL UTILITY FUNCTIONS --

def addToList(i, l):
    if isinstance(i, list):
        l.extend(i)
    else:
        l.append(i)


# [Only works for one argument functions]
def ifList(i, sf, lf, l=None):
    if isinstance(i, list):
        lf(i)
    else:
        sf(i)
