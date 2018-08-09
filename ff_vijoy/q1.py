# q1 Write a new class with following requirements
# a. To store a list of items
# b. A method to return all unique items from the list
# c. A method to return all items and their frequency
# d. Should be able to append/insert new items to the list

class list_class:
    
    def __init__(self):
        self.myList = []
        
    # method to add items to the list    
    def put_item(self, item):
        self.myList.append(item)
        
    # method to return all unique items from list    
    def get_unique_items(self):
        return set(self.myList)
        
    # method to get all items and their frequencies
    # as dictionary
    def get_histogram_items(self):
        return {x:self.myList.count(x) for x in self.myList}
    

def main():   
    # sample test case
    alist = list_class()
    alist.put_item(3)
    alist.put_item(1)
    alist.put_item(1)
    alist.put_item(1)
    alist.put_item(2)
    alist.put_item(2)

    print(alist.get_unique_items())
    print(alist.get_histogram_items())
    
if __name__== "__main__":
    main()