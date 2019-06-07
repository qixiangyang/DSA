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
    searched_list = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched_list:

            if person_is_seller(person):
                print("{} is mango seller".format(person))
                return person
            else:
                search_queue += graph[person]
                searched_list.append(person)


get_seller()



