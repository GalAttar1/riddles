## 7 BOOM

#NAIVE SOLUTION 
def contains_seven(num):
    st= str(num)
    bool= '7' in st
    return bool

def divisible_by_7(num):
    bool= (num%7==0)
    return bool

for x in range (1,40): #semi while loop
    if contains_seven(x) or divisible_by_7(x):
        print ("BOOM")
    else:
        print(x)

  
 
