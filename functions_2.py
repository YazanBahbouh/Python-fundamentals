def countDown(a):
    number_list = []
    for a in range (a, -1, -1) :
        if(a >= 0):
            number_list.append(a)
    print(number_list)
countDown(5)

#2
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

#3
def first_plus_length(nums):
    sum = nums[0] + len(nums)
    return sum
print('first_plus_length',first_plus_length([1,2,3,4,5]))

#4
def values_greater_than_second(list):
    new_list = []
    count = 0
    if len(list) > 2:
        for element in list :
            if (element > list[1]):
                new_list.append(element)
                count += 1
        print('count of greater values',count)
        return new_list
    else:
        return False
print('values_greater_than_second',values_greater_than_second([5,2,3,2,1,4]))    
print('values_greater_than_second',values_greater_than_second([3]))    

#5
def length_and_value(a,b):
    length_and_value_list = [b] * a
    return length_and_value_list
print(length_and_value(7,2))