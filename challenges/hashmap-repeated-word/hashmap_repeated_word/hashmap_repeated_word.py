import sys
sys.path.append("/home/ebrahimayyad11/data-structures-and-algorithms/Data-Structures/hash-table")
from hash_table.hash_table import Hashtable

def repeated_word(str):
    str = str.replace(',' , ' ')
    str = str.lower()
    arr = str.split()
    repeated_hash = Hashtable()

    for i in range(len(arr)):
        contain = repeated_hash.contains(arr[i])
        if contain == True:
            return arr[i]
        else:
            repeated_hash.add(arr[i],arr[i])

    return 'There is no repeated words'

