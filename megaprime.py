def isprime(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
num=int(input())
a=isprime(num)
if a==True:
    while(num):
          d=num%10
          num=num//10
          num=d
          r=isprime(num)
          if r==False:
              print('nm')
              break
    else:
        print('m')        
