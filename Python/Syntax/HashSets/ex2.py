import time

# Define a function to demonstrate the operation and time complexity of a hash set
def compare_operations():
  
    # Create a list and a set
    data_list = []
    data_set = set()

    # Adding elements to list and set
    for i in range(10**6):
        data_list.append(i)
        data_set.add(i)

    # Set and List are ready; now let's define a non-existing item to search for
    test_item = 10**6 + 1  # This item is not in our set or list

    # Time the 100 consecutive operations of checking whether `test_item` is in `data_set`
    start_time = time.time()
    for _ in range(100):
        result = test_item in data_set
    end_time = time.time()
    set_time = end_time - start_time
    print(f"Set operation result: {result}")
    print(f"Time taken for set operation: {set_time:.6f} seconds")

    # Time the 100 consecutive operations of checking whether `test_item` is in `data_list`
    start_time = time.time()
    for _ in range(100):
        result = test_item in data_list
    end_time = time.time()
    list_time = end_time - start_time
    print(f"List operation result: {result}")
    print(f"Time taken for list operation: {list_time:.6f} seconds")

# Execute the function
compare_operations()