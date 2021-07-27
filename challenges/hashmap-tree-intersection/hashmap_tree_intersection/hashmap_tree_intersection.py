import sys
sys.path.append("/home/ebrahimayyad11/data-structures-and-algorithms/Data-Structures/hash-table")
from hash_table.hash_table import Hashtable

def tree_intersection(tr1,tr2):
    arr1 = tr1.pre_order()
    arr2 = tr2.pre_order()

    if arr1 == 'the tree is empty!' or arr2 == 'the tree is empty!':
        return 'There is no match between the trees'
    
    hm = Hashtable()
    result = []

    for i in arr1:
        hm.add(str(i),i)

    for j in arr2:
        contain = hm.contains(str(j))
        if contain == True:
            result += [j]
        
    if len(result) == 0:
        return 'There is no match between the trees'
    else:
        return result