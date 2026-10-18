# import math
# pos = [0,0]
# while True:
#     s = raw_input()
#     if not s:
#         break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = int(movement[1])
#     if direction=="UP":
#         pos[0]+=steps
#     elif direction=="DOWN":
#         pos[0]-=steps
#     elif direction=="LEFT":
#         pos[1]-=steps
#     elif direction=="RIGHT":
#         pos[1]+=steps
#     else:
#         pass

# print int(round(math.sqrt(pos[1]**2+pos[0]**2)))

# import math

# s = raw_input("something")

# print(s)

# n = 5


# for row in range(1, n + 1):
#     for collumn in range(1, row+1):
#         print("*", end=" ")
#     print()
    



# import string
# def get_rangoli(size):
#     n = size
#     alph = string.ascii_lowercase
#     width = 4 * n - 3

#     ans = []
#     for i in range(n):
#         left = '-'.join(alph[n - i - 1:n])
#         mid = left[-1:0:-1] + left
#         final = mid.center(width, '-')
#         ans.append(final)

#     if len(ans) > 1:
#         for i in ans[n - 2::-1]:
#             ans.append(i)
#     ans = '\n'.join(ans)
#     return(ans)


# print(get_rangoli(5))

# size 0 = -3
# size 1 = 1 width
# size 2 = 5
# size 3 = 9 width
# size 4 = 13 width
# size 5 = 17 width

# using linear stuff


# import string
# n = 3
# width = n * 4 - 3
# alph = list(string.ascii_lowercase)


# norm_alph_n = alph[:n]
# rev_alp_n = norm_alph_n[::-1]
# # print(norm_alph_n)
# # print(rev_alp_n)


# ################################################

# full = []
# for x_axis in range(n): 
#     row = []
#     for index, letter in enumerate(rev_alp_n):
#         if x_axis >=  index:
#             row.append(letter)
    
#     for index, letter in enumerate(norm_alph_n[1:], start=1):
#         if x_axis < index:
#             row.append(letter)
    
#     row = "-".join(row)
    

#     item_amount = len(row)
#     full_padding_dash = width - item_amount
#     one_side_padd = int(full_padding_dash / 2)
#     z = "-" 
#     x = z * one_side_padd
#     y = x + row + x
    
#     full.append(y)



# #################################################

# full2 = []

# for x_axis in range(n - 2, -1, -1):
#     row2 = []
#     for index, letter in enumerate(rev_alp_n):
#         if x_axis >=  index:
#             row2.append(letter)

#     for index, letter in enumerate(rev_alp_n):
#         # print(x_axis, index, letter)
#         if x_axis > index:
#             row2.append(letter)
#     row2 = "-".join(row2)
    

#     item_amm = len(row2)
#     full_padd = width - item_amm
#     one_side_padd = int(full_padd / 2)
    
#     x = "-"
#     y = x * one_side_padd
#     z = y + row2 + y

#     full2.append(z)


# for item in full:
#     print(item)

# for item in full2:
#     print(item)

# #######################################################

# import string

# n = 5
# width = n * 4 - 3

# alph = list(string.ascii_lowercase)
# norm_alph_n = alph[:n]
# rev_alp_n = norm_alph_n[::-1]

# full = []

# for x_axis in range(n):
#     row = []

#     for index, letter in enumerate(rev_alp_n):
#         if x_axis >= index:
#             row.append(letter)

#     for index, letter in enumerate(norm_alph_n[1:], start=1):
#         if index <= x_axis:
#             row.append(letter)

#     row = "-".join(row)

#     item_amount = len(row)
#     full_padding_dash = width - item_amount
#     one_side_padd = full_padding_dash // 2

#     x = "-" * one_side_padd
#     y = x + row + x

#     full.append(y)


# full2 = full[-2::-1]

# for item in full:
#     print(item)

# for item in full2:
#     print(item)