def fibonacci(n):
   a =[]
   
   if (n > 0):
      if (n == 1):
         a.append(0)
         print(a)

      elif (n == 2):
         a.append(0)
         a.append(1)
         print(a)
      else:
         a.append(0)
         a.append(1)
         while(n > len(a)) : 
            num=0
            num= + a[(len(a)-2)]+a[(len(a)-1)]
            a.append(num)
         print(a)
    
  
   else:
    print("you most enter positve number")


n=int(input("enter the num"))
fibonacci(n)

