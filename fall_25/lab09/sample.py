class MaxHeap:
    def __init__(self):
        # initialize heap
        self.heap = []

    def insert(self, patient):
        # insert patients inside of the heap
        self.heap.append(patient)
        self.up_heap(len(self.heap) - 1)

    def up_heap(self, index):
        # Calculate parent index Formula: parent_index = (index - 1) // 2
        # Check whether it is in valid range i.e index > 0 and self.heap[index] > self.heap[parent_index]
        # True?
        # Swap the current node with its parent if it is greater hint; > self.heap[index], self.heap[parent_index] -> self.heap[parent_index], self.heap[index]
        # up_heap parent index hint: self.up_heap(parent_index)
        pass

    def down_heap(self, index):
        # Assume the current index is the largest largest = index
        # Calculate left child index left_child = 2 * index + 1
        # Calculate right child index right_child = 2 * index + 2

        # # Check if the left child exists and is greater than the current largest
        # True?
        #     largest = left_child

        # # Check if the right child exists and is greater than the current largest
        # True?
        #     largest = right_child

        # # If the largest is not the current node, swap and continue downheap
        # True?
        #     Swap values. Hint: self.heap[index], self.heap[largest] => self.heap[largest], self.heap[index]
        #     down heap largest. Hint: self.down_heap(largest)
        pass
