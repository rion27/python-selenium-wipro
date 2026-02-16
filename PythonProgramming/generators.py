#generators are a special type of functions - returns 1 value at a time on demand
# yield - keyword to return data
#more memory efficient, useful for large set of test data
#files, retries, batching

def numbers():
    return [1,2,3,4]

print(numbers())
#normal functions loads all value in the memory
#now using generator -
def generator():
    print("Printing 1")
    yield 1
    print("Printing 2")
    yield 2
    print("Printing 3")
    yield 3
    print("Printing 4")
    yield 4

ret_val=generator()
print(next(ret_val))
print(next(ret_val))
print(next(ret_val))
print(next(ret_val))