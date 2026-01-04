# init_message = "Input a name: \n"
# file_to_open = "members.txt"
#
#
#
# while True:
#     name = input(init_message).strip().title()
#     file = open(file_to_open, "r")
#     list_of_names = file.readlines()
#     file.close()
#
#     list_of_names.append(name + "\n")
#     file = open(file_to_open, "w")
#     file.writelines(list_of_names)
#     file.close()
#
#     continue_message = input("Continue?: y/n \n").lower().strip()
#
#     if continue_message == "n":
#         break


# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for filename in filenames:
#     file = open(filename, "w")
#     file.write("hello")
#     file.close()

# init = 'a'
# index = ord(init)
#
# for _ in range(3):
#     file = open(f"{chr(index)}.txt", "r")
#     print (file.read())
#     file.close()
#     index = index + 1
