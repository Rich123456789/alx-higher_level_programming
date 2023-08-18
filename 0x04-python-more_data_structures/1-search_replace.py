#!/usr/bin/python3

def search_replace(my_list, search, replace):
	new_list = my_list.copy()
	new_list = my_list.sort()
	new_list = my_list.search(search)
	my_list[-2] = ["replace"]

	print(new_list)
