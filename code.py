# --------------
def palindrome(num):
    if num < 9:
        num = num+1
        return num
    else:
        while(str(num) != str(num)[::-1]):
            num = num + 1
        return int(num)
palindrome(13456)


# --------------
def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)
a_scramble('Yes','Yessss')


# --------------
#Code starts here
def check_fib(num):
  fib=list()
  num_1 = 0
  num_2 = 1
  num_3 = 0
  fib.append(num_1)
  fib.append(num_2)
  while(num_3 < num):
    num_3 = num_1 + num_2
    fib.append(num_3)
    num_1,num_2 = num_2,num_3
  return(num in fib)

check_fib(456)
check_fib(987)


# --------------
#Code starts here
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)


# --------------
#Code starts here
def k_distinct(string,k):
    string = string.lower()
    a = len(set([*string]))
    if a == k:
      return(True)
    else:
      return(False)
k_distinct("BananA",3)


