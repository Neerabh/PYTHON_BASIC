# type error 

#ltn() dont like work with integers

num_char = len(input("what is your name "))

#here it is not gonaa work because num_char is integer and other is string

#print("your name has "+num_char+"characters")

#to find the datatype of data

print(type(len(input("what is your name "))))

#typecasting -- here we convert one type of data into another

#convert num_char into string
str_num_char=str(num_char)
print("your name has "+str_num_char+" characters")
