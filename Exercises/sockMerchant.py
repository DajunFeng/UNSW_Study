    """
    John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
    """
    
    
    def sockMerchant(n, ar):
    
      ar.sort()

    #print(ar)

      result = 0
      iteration = 1
      while len(ar) != 0:
        #print("Iteration {}".format(iteration))
          if ar[0] in ar[1: ]:
         #   print("Pair found {} {}".format(ar[0], ar[1]))
              result += 1
              ar.remove(ar[0])
              ar.remove(ar[0])
          #  print("updated array {}".format(ar))
              iteration += 1
          else:
           # print("Not match!")
              ar.remove(ar[0])
            #print("updated array {}".format(ar))
              iteration += 1
             continue
            
      return result
