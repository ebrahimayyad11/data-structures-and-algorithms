def ll_zip(ll1, ll2):
    first_current = ll1.head
    second_current = ll2.head

    if first_current == None or second_current == None:
      return "one of the linked lists is empty"
    else:
      arr = []
      while first_current or second_current:
        if(first_current):
            arr+=[first_current.value]
            first_current = first_current.next
        if(second_current):
            arr+=[second_current.value]
            second_current = second_current.next
      x='Head -> '
      for i in arr:
        x+=f'({i}) -> '
      x+='Null'
      return x