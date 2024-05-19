# i = ['green','blue','grey','blue']

# colour_count = {}
# for color in i:
#     if color in colour_count:
#         colour_count[color] +=1
#     else:
#         colour_count[color] = 1
    
# for color,count in colour_count.items():
#     print(count)
    
    
    
# print(colour_count)
# # class Test:
# #     def fun1(self):
# #         print("This is fun1")



# # class Test2:
# #     def fun2(self):
# #         print("second class")
# #         return "1"

# # test = Test()
# # test.fun1()

# class Book:
#     def __init__(self,titel):
#         self.titel = titel
    
#     def test(self):
#         print(self.titel)
        

# obj = Book("hello")
# obj.test()

# name = "thajudheen"
# reverse_name = ''
# # output = [for i in name reverse_name = i +reverse_name]
# for i in name :
    
#     reverse_name =  i + reverse_name
#     # print(reverse_name,i)
# print(reverse_name)
# # number = 0
# # name = ""
# # for i in b:
# #     number  += 1
# #     name += i + str(number)
# # print(name)
#     jaht

# star = ""
# for i in range(5):
#     star = '*' 
#     for n in range(5):
        
#     print(star)
    
# name = 'thajudheen'
# output = ""
# num = 0
# for i in name :
#     output = i+output
#     num += 1
#     output = str(num) +output
#     # output +=str(num)
    
# print(output)


# name = 'thajudheen'
# output = ""
# num = 0
# for i in name:
#     if i not in output:
#         output = i + str(num) + output
#         num += 1
#     else :
#         print(i)

# print(output)
# i = 1
# c  = ""
# b = ""
# while i <= 5:
    
#     c += "*"
#     print(c)
#     i = i+1


# name = "thajudheen"
# output = ''
# num = len(name)
# for i in name :
    
    
#     output = i+ str(num) +output 
#     num -= 1
# print(output)

# color  = ['green','blue','grey','blue']
# color_count= {}
# for i in color:
#     if i in color_count:
#         color_count[i] += 1
#     else:
#         color_count[i] = 1
    

# print(color_count)


# def separate_numbers_and_characters(input_string):
#     numbers = ''
#     characters = ''
#     icons = "-"
#     icon = ["-"]
#     for char in input_string:
#         if char <= '9':
#             numbers += char
#         elif char in icon:
#             icons += char
#         else:
#             characters += char
#     return numbers, characters,icons

# input_string = "0abc123def45611-1"
# numbers, characters ,icons= separate_numbers_and_characters(input_string)
# print("Numbers:", numbers)
# print("Characters:", characters)
# print(icons)


import os , random

for i in range(200):
    d = str(i) + 'days ago'
    rand = random.randrange(1, 12)
    with open('test.txt','a') as file:
        file.write(d+'\n')
    os.system('git add test.txt')
    os.system('git commit --date=" 2020-'+str(rand)+'-'+d+'" -m 1')
os.system('git push -u origin main')

#git commit --amend --no-edit --date="Fri Nov 6 20:00:00 2015 -0600" 
#git fetch origin master
#git rebase origin/master