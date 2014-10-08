_nibbles = {"0":"0000", "1":"0001", "2":"0010", "3":"0011",
            "4":"0100", "5":"0101", "6":"0110", "7":"0111",
            "8":"1000", "9":"1001", "A":"1010", "B":"1011",
            "C":"1100", "D":"1101", "E":"1110", "F":"1111",
            "-":"-"}

def toBase2(number):
    """toBase2(number): given an int/long, converts it to
    a string containing the number in base 2."""
    # From a suggestion by Dennis Lee Bieber.
    if number == 0:
        return "0"
    result = [_nibbles[nibble] for nibble in "%X"%number]
    result[number<0] = result[number<0].lstrip("0")
    return "".join(result)

def tento2(n):
 
  from math import pow

  bin =""

  for i in range(n,0,-1):
    
    bin = bin +  str(i%2)
    n = n - str(i%2)
    
  return bin

  


def isPal(n):

  n=str(n)

  y = n[::-1]

  if n==y:
    return True
  else:
    return False

if __name__ == '__main__':
  
  sum1 = 0

  for i in range(1,1000000):
    #print i, toBase2(i)
    x = isPal(i) ; y = isPal(toBase2(i))
    #print x, isPal(toBase2(i))

    if x==True and y==True:
       sum1 += i

  print sum1



