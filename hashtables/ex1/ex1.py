#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    
    ht = HashTable(16)
    ht2 = HashTable(16)

    """
    YOUR CODE HERE
    """
    if limit == None:
        return None
    # Declare count property
    count = 0
    # Put array elements into two hash tables, using for loop,
    for i in range(0, len(weights)):
        hash_table_insert(ht, count, weights[i])
        count += 1
    
    # If the count is one, return None
    if count == 1 or count == 0:
        return None

    # Declare answer property
    answer = (1, 0)
    # Declare two index properties
    left_index = 0
    right_index = 1
    # While the sum of the two elements of answer do not equal the wait limit
    while hash_table_retrieve(ht, answer[0]) + hash_table_retrieve(ht, answer[1]) != limit:
        # answer equals (left index, right index)
        if hash_table_retrieve(ht, left_index) != None and hash_table_retrieve(ht, right_index) != None:
            
            answer = (left_index, right_index)
        # If the left index is at the last index already, then break out of the loop here to avoid index out of range errors
        if left_index == count - 1:
            break
        # If the right index is at the last index, then the left index is increased by one and the right index is reset to 0 to start the loop again
        if right_index >= count - 1:
            left_index += 1
            right_index = left_index + 1
        right_index += 1
    # If we are out of the loop but the answer values do not add up to the limit, set the answer to none
    if hash_table_retrieve(ht, answer[0]) + hash_table_retrieve(ht, answer[1]) != limit:
        return None
    # Else if the second element of answer is greater than the first, swap element indexes
    elif answer[1] > answer[0]:
        answer = (answer[1], answer[0])
    # Return answer
    return answer


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
