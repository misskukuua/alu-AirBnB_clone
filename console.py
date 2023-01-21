"""A function to calculate the average"""

def calculate_average(number_list):
    sum_list = 0
    for number in number_list:
        sum_list = sum_list + number

    average = 0
    average = sum_list / len(number_list)

   return average
   
