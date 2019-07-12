#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # Put array elements into hash table, using for loop
    for i in range(0, len(weights)):
        ht.hash_table_insert(ht, weights[i], weights[i])
    # Return the two elements that, when added up, result in the greatest number within the limit
    
    # Declare largest_number property
    largest_number = 0
    # Declare current_number property
    current_number = ht.storage[0]
    # Declare an answer tuple property
    answer = (0, 0)
    # Go into a for loop with the weights array
    for i in range(0,len(weights)):
        # If current number plus array[index] number is greater than largest_number property, largest number is now equal to the two numbers' sum and the answer tuple is updated with the two numbers, the greatest first and the least last
        if current_number + weights[i] > largest_number:
            largest_number = current_number +weights[i]
            if current_number > weights[i]:
                answer = (current_number, weights[i])
            else:
                answer = (weights[i], current_number)
    
    # I am going to assume that, even though the test file has no duplicates in the int array, I should account for duplicates

    return answer


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
