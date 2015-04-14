'''
You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique elements in this list. To do so you will need to remove all unique elements (elements which are contained in a given list only once). When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

non-unique-elements

Input: A list of integers.

Output: The list of integers.

Example:

checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
checkio([1, 2, 3, 4, 5]) == []
checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]

How it is used: This mission will help you to understand how to manipulate arrays, something that is the basis for solving more complex tasks. The concept can be easily generalized for real world tasks. For example: if you need to clarify statistics by removing low frequency elements (noise).

Precondition:
0 < len(data) < 1000

'''



def checkio():
    # Source: http://www.tutorialspoint.com/python/python_lists.htm
    print('Please enter some numbers (separated by a space): ')
    user_input = [int(x) for x in input().split()] # Source: http://stackoverflow.com/questions/4663306/how-can-i-get-a-list-as-input-from-the-user-in-python
    print('Your list is: ', user_input)
    result_list = [] # bucket for non-uniques
    for element in user_input:
        if user_input.count(element) > 1:
            result_list.append(element) # filling up the bucket for non-uniques
    print('Your checked list is: ', result_list) # final non-unique bucket



# checkio solution I made (that worked):

def non_unique(data):

    #user_input = [int(x) for x in data.split()]
    new_data = []
    for element in data:
        if data.count(element) > 1:
            new_data.append(element) 
    return new_data

