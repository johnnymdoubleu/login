import authentication as a
input_id = input("Please insert your ID. \n아이디를 입력해주세요. \n")
if a.login(input_id):
    print('Welcome ' + input_id + "\n")
    input_pw = input("password: ")
    a.password(input_pw)
else:
    print("Wrong login ID or password, please check")

#Version 3
# input_id = input("Please insert your ID. \n아이디를 입력해주세요. \n")
# def login(_id):
#     members = ['mdoubleu', 'egoing', 'flamewndls']
#     for member in members:
#         if member == _id:
#             return True
#     return False
# if login(input_id): #since the function "login" is already a boolean type, we can directly use in the if/else
#     print ('Welcome, ' + input_id)
# else:
#     print("Wrong login ID or password, please check")

#Version 2
# input_id = input("아이디를 입력해주세요.\n")
# members = ['mdoubleu', 'egoing', 'flamewndls']
#
# for member in members:
#     if member == input_id:
#         print("Welcome!, " + member)
#         import sys
#         sys.exit()
# print("Wrong login ID or password, please check")

#Version 1
# real_mdoubleu = "mdoubleu"
# real_egoing = "egoing"
# if real_mdoubleu == in_str:
#     print("Hello!, MDoubleU")
# elif real_egoing == in_str:
#     print("Hello!, egoing")
# else:
#     print("Wrong login ID or password, please check")
