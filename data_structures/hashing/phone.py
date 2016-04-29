'''
Sample 1.
Input:
12
add 911 police
add 76213 Mom
add 17239 Bob
find 76213
find 910
find 911
del 910
del 911
find 911
find 76213
add 76213 daddy
find 76213

Output:
3
Mom
not found
police
not found
Mom
daddy
'''

#!/usr/bin/python
# -*- coding: utf-8 -*-
# python3


class Query:

    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print '\n'.join(result)


def process_queries(queries):
    result = []

    # Keep list of all existing (i.e. not deleted yet) contacts.

    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':

            # if we already have contact with such number,
            # we should rewrite contact's name

            if cur_query.number in contacts.keys():
                val = cur_query.name
                contacts[cur_query.number] = val
            else:

                  # otherwise, just add it

                contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            if cur_query.number in contacts.keys():
                del contacts[cur_query.number]
        else:
            response = 'not found'
            if cur_query.number in contacts.keys():
                response = contacts[cur_query.number]
            result.append(response)

        # print(contacts)

    return result


__name__ = '__main__'
if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

			
