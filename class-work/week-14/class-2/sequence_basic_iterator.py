class SequenceIteratable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return Sequence(self.start, self.end)
    
    def __len__(self):
        return self.end - self.start + 1 # including last value

class Sequence: # building the range function
    def __init__(self, start, end):
        self.start_num = start
        self.end_num = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start_num > self.end_num:
            raise StopIteration
        else:
            self.start_num += 1
        return self.start_num - 1
    
    def __len__(self):
        return self.end_num - self.start_num + 1
    
if __name__ == '__main__':
    start, end = 3, 10
    seq = SequenceIteratable(start, end) # notice its not sequence class
    
    print(len(seq))
    for elm in seq:
        print(f'Counting: {elm}')

    print(len(seq)) # sequenceiteratble allows us to repeat 
    for elm in seq:
        print(elm)