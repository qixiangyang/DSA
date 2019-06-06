"""
Description:
Author:qxy
Date: 2019-06-06 17:34
File: graph_search 
"""

from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'


def get_seller():
    search_queue = deque()
    search_queue += graph['you']

    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print("{} is mango seller".format(person))
            return person
        else:
            print(person)
            print(search_queue)
            search_queue += graph[person]
            print(search_queue)

get_seller()



