i=int(input()) #typecasting input
while True:
    i+=1
    if len(set(str(i)))==len(str(i)):
        print(i)
        break
    
