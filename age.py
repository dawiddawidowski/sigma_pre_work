import datetime

# def date_age(old_date):
#     '''
#     Calculates the age of an input date (string) by splitting the date into a list, using the datatime module
#     for the current date and finding the difference between the two.
    
#     INPUTS
#     old_date (str) = Date whose age is to be found.

#     OUTPUTS
#     age (int) = Age of the input date.
#     '''

#     old_date_list = (old_date.split('-'))
#     # print(old_date_list)
#     old_day = int(old_date_list[0])
#     old_month = int(old_date_list[1])
#     old_year = int(old_date_list[2])
#     # print(old_day)
#     current_time = datetime.datetime.now()
#     age =  current_time.year - old_year - ((current_time.month, current_time.day) < (old_month, old_day))
#     return age

old_date = input('Please enter a date in the format dd-mm-yyyy: ')
old_date_list = (old_date.split('-'))
old_day = int(old_date_list[0])
old_month = int(old_date_list[1])
old_year = int(old_date_list[2])
# print(old_day)
current_time = datetime.datetime.now()
age =  current_time.year - old_year - ((current_time.month, current_time.day) < (old_month, old_day))
print(age)

