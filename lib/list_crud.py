def create_an_empty_list():
    new_list = []
    return new_list

create_an_empty_list()

def create_a_list():
    new_list = ['one','two','three','four']
    return new_list

print(create_a_list())

def add_element_to_end_of_list(item_list, element):
    item_list.append(element)
    return item_list

print(add_element_to_end_of_list(['one','two','three','four'], "five"))

def add_element_to_start_of_list(item_list, element):
    item_list.insert(0, element)
    return item_list

print(add_element_to_start_of_list(['one','two','three','four'], "zero"))

def remove_element_from_end_of_list(item_list):
    item_list.pop(-1)
    return item_list

print(remove_element_from_end_of_list(['one','two','three','four']))

def remove_element_from_start_of_list(item_list):
    del item_list[0]
    return item_list

print(remove_element_from_start_of_list(['one','two','three','four']))


def retrieve_first_element_from_list(item_list):
    item = item_list[0]
    return item

print(retrieve_first_element_from_list(['one','two','three','four']))

def retrieve_element_from_index(item_list, index):
    item = item_list[index]
    return item

print(retrieve_element_from_index(['one','two','three','four'], 2))

def retrieve_last_element_from_list(item_list):
    item = item_list[-1]
    return item

print(retrieve_last_element_from_list(['one','two','three','four']))