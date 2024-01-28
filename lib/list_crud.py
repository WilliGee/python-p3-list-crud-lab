def create_an_empty_list():
    return []

def create_a_list():
    return ["chest", "shoulders", "squats", "arms"]

def add_element_to_end_of_list(data, element):
    data.append(element)
    return (data)

def add_element_to_start_of_list(data, element):
    data.insert(0,element)
    return (data)

def remove_element_from_end_of_list(data):
    data.pop()
    return (data)

def remove_element_from_start_of_list(data):
    del data[0]
    return data

def retrieve_first_element_from_list(data):
    return data[0]

def retrieve_element_from_index(data, index):
    return data[index]

def retrieve_last_element_from_list(data):
    return data[-1]
