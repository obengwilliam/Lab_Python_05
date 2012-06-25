'''
creator obeng william
description:PROBLEMS
'''

#PROBLEM 2
'''
This is a factorial function that takes an integer and returns the number factorial.
'''

def factorial(a):
    f=1
    while (a>0):
           f=f*a
           a=a-1
    return f
factorial(5)


#problem 3
def fibonacci(x):
    fibo_list=[]
    for i in range(x,0,-1):
        fibo=find_fibo(i)
        fibo_list.append(fibo)
    return fibo_list[::-1]
   
def find_fibo(j):
    if j==0:
       return 0
    elif j==1:
        return 1
    else:
        return find_fibo(j-1) +find_fibo(j-2)


fibonacci(5)




#problem 4
def prime(x):
    count=0
    true=True
    false=False
    
    for i in range(1,x+1):
        if x%i==0:
            count=count+1
    if count==2:
        return true
    else:
        return false
            

prime(3)



#challenge problems
#problem 4

#PALINDROME
def isPalindrome(s):
    print s[::-1]
    if s == s[::-1]:
        return True
    else:
        return False
print isPalindrome('amanaplanacanalpanama')





#problem 5
def isSubstring(u,s):
    if s.find(u)>=0:
        return True
    else:
        return False
isSubstring('barfoobar','foo')
    




#problem 7
def combined_score(you,fred,jill):
     count=0
     count2=0
     i=0
     while i <6 :
         if you[i]!=fred[i]:
            count=count +1
         elif fred[i]!=jill[i]:
               count=count+1

         i=i+1

     return count
     
print combined_score('AAABCDA','ADDBACA','ADCADDC')











    

