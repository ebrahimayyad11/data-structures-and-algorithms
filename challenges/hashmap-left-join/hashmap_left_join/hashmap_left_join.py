def left_join(ht1,ht2):
    result = []
    for i in ht1.buckets:
        if i :
            current = i.head
            current_element = current.value

            while current_element:
                key = current_element['key']
                
                if ht2.contains(key):
                    data = [key,current_element['value'],ht2.get(key)]
                    result.append(data)
                else:
                    data = [key,current_element['value'],None]
                    result.append(data)

                if current.next:
                    current.next
                    current_element = current.value
                else:
                    current_element = None
    if result:
        return result
    else:
        return 'The first Hashtable is empty'