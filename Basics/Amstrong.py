def is_Amstrong(Number):
    Number = int(Number)
    temp = Number
    count = 0
    while Number != 0:
        count+=1
        Number = Number // 10
    
    Number = temp
    result = 0
    while Number != 0:
        result = result + (Number % 10) ** count
        Number = Number // 10
    
    if result == temp:
        print("Hey you i'm Amstrong..",temp)
    else:
        pass
        # print(result,"<-",temp)

for i in range(200):
    is_Amstrong(i)   


# count = c
#  3   3   3
# 1 + 5 + 3  == 153    
# 1 + 125 + 27 = 153