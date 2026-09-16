# Question 1
# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.


# result = []

# for numb in range(2000, 3201):
#     if numb % 5 != 0 and numb % 7 == 0:
#         result.append(str(numb))

# # print(result)
# g_result = ','.join(result)

# print(g_result)


# Question 2
# Question:
# Write a program which can compute the factorial of a given number. Suppose the following input is supplied to the program: 8 Then, the output should be:40320

# numb_inp = int(input('enter a desired factorial number:\n'))

# result = 1

# for numb in range(1, numb_inp + 1):
#     result *= numb

# print(result)
    



# Question 3
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

# Then, the output should be:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


# usr_inp = int(input("Enter numb:\n"))

# some_dic = {}



# for numb in range(1 , usr_inp + 1):
#     key = numb
#     value = key ** 2
#     some_dic[key] = value

# print(some_dic)

