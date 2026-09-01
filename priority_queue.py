import random
import time


class MinPriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent_index = self.parent(index)

            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[index]
                )
                index = parent_index
            else:
                break

    def peek(self):
        if len(self.heap) == 0:
            return None

        return self.heap[0]

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]

        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return minimum

    def heapify_down(self, index):
        while True:
            smallest = index
            left = self.left_child(index)
            right = self.right_child(index)

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index]
            )

            index = smallest

    def display(self):
        print(self.heap)


def run_priority_queue_tests():
    print("MIN-HEAP PRIORITY QUEUE TEST")
    print("----------------------------")

    queue = MinPriorityQueue()

    # Lower numbers represent higher priority.
    tasks = [
        (3, "Prepare advising presentation"),
        (1, "Resolve urgent student registration issue"),
        (4, "Update program website"),
        (2, "Review internship paperwork"),
        (3, "Send student outreach email")
    ]

    print("\nAdding tasks:")

    for task in tasks:
        print(task)
        queue.insert(task)

    print("\nHeap contents:")
    queue.display()

    print("\nPeek at highest-priority task:")
    print(queue.peek())

    print("\nRemoving tasks in priority order:")

    extracted_tasks = []

    while queue.peek() is not None:
        task = queue.extract_min()
        extracted_tasks.append(task)
        print(task)

    priorities = [task[0] for task in extracted_tasks]
    correct_order = priorities == sorted(priorities)

    print("\nPriority order correct:", correct_order)


def run_runtime_tests():
    print("\nRUNTIME TESTING")
    print("----------------------------")

    input_sizes = [100, 1000, 10000]

    for size in input_sizes:
        queue = MinPriorityQueue()

        values = [
            (random.randint(1, 1000000), f"Task {i}")
            for i in range(size)
        ]

        start_insert = time.perf_counter()

        for value in values:
            queue.insert(value)

        end_insert = time.perf_counter()

        insert_runtime = end_insert - start_insert

        start_extract = time.perf_counter()

        extracted = []

        while queue.peek() is not None:
            extracted.append(queue.extract_min())

        end_extract = time.perf_counter()

        extract_runtime = end_extract - start_extract

        correct = extracted == sorted(values)

        print(f"\nInput size: {size}")
        print(f"Insertion runtime: {insert_runtime:.6f} seconds")
        print(f"Extraction runtime: {extract_runtime:.6f} seconds")
        print(f"Output correct: {correct}")


if __name__ == "__main__":
    run_priority_queue_tests()
    run_runtime_tests()
