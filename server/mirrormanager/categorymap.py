# Some Categories only exist for certain Product-Version combinations.
# e.g. Fedora Extras doesn't exist for Fedora <= 3.
# and Fedora Core and Fedora Extras don't exist for Fedora >= 7.

from mirrormanager.model import *
from math import ceil
from IN import INT_MAX

def categorymap(productname, vername):
    categories = []
    categoriesToDrop = set()
    vernum = INT_MAX
    try:
        if u'development' in vername:
            vernum = INT_MAX
        elif '.' in vername:
            vernum = int(ceil(float(vername)))
        else:
            vernum = int(vername)
    except:
        pass

    try:
        product = Product.byName(productname)
        categories = [c.name for c in product.categories]
    except:
        return []

    if productname == u'Fedora':
        if vernum < 3:
            categoriesToDrop.add(u'Fedora Extras')
        if vernum > 6:
            c = (u'Fedora Core', u'Fedora Extras')
            for e in c:
                categoriesToDrop.add(e)
                
    for c in categoriesToDrop:
        try:
            categories.remove(c)
        except KeyError:
            pass

    return categories
