def checkio():
    '''
    You are given a non-empty list of integers (X).
    For this task, you should return a list consisting of only the non-unique elements
    in this list. To do so you will need to remove all unique elements
    (elements which are contained in a given list only once).
    When solving this task, do not change the order of the list.
    Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
    
    Source: http://www.tutorialspoint.com/python/python_lists.htm
    '''

    print('Please enter some numbers (separated by a space): ')
    user_input = [int(x) for x in input().split()] # Source: http://stackoverflow.com/questions/4663306/how-can-i-get-a-list-as-input-from-the-user-in-python
    print('Your list is: ', user_input)
    result_list = [] # bucket for non-uniques
    for element in user_input:
        if user_input.count(element) > 1:
            result_list.append(element) # filling up the bucket for non-uniques
    print('Your checked list is: ', result_list) # final non-unique bucket




checkio()


''' checkio solution I made (that worked):

#Your optional code here
#You can import some modules or create additional functions


def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  

    #user_input = [int(x) for x in data.split()]
    new_data = []
    for element in data:
        if data.count(element) > 1:
            new_data.append(element) 
    return new_data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"

'''
