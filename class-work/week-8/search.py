import time 
def search(collection, value):
    '''
    search for value in the collection
    '''
    for i in collection:
        found = value in collection
        print("searching")
    return found
    
lst = list(range(1,50000))

s = set(range(1,50000))

start = time.time() # 1.244 for set and 18.38 for list
search(lst, 50000)
end = time.time()
print(end-start)