# import sys
# import argparse

# def maxmin(num_list):
#     mini = num_list[0]
#     maxi = num_list[0]
#     for i in range(len(num_list)):
#         if num_list[i] < mini:
#             mini = num_list[i]
#         if num_list[i] > maxi:
#             maxi = num_list[i]
#     print([mini, maxi])
#     return [mini, maxi]

# if __name__ == '__main__':
#     globals()[sys.argv[1]](sys.argv[2])

user_numbers = input('Please enter a list of numbers seperated by a space e.g. 10 25 50: ')
numbers_list = user_numbers.split()
# print(numbers_list)
for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
# print(numbers_list)

mini = numbers_list[0]
maxi = numbers_list[0]
for i in range(len(numbers_list)):
    if numbers_list[i] < mini:
        mini = numbers_list[i]
    if numbers_list[i] > maxi:
        maxi = numbers_list[i]

minmax_list = [mini, maxi]
print(minmax_list)
