def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1

  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]

    # split aList between lists
    for  i in aList:
      tmp = i // placement
      print ("i is " , i)
      print ("placement is " , placement)
      print ("tmp is ", tmp)
      print ("tmp % RADIX is ", tmp % RADIX)
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False

    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1

    # move to next digit
    placement *= RADIX
  return aList

if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(radixsort(unsorted))
