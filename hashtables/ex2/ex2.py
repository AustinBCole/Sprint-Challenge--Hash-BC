#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Populate the hash table using for loop, source is key and dest is value
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # Declare an array
    answer_array = []
    # Place the first value in array
    answer_array.append(hash_table_retrieve(hashtable, "NONE"))

    for count in range(1, length):
        answer_array.insert(count, hash_table_retrieve(hashtable, answer_array[-1]))
    # Return array
    return answer_array
