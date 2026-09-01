import time


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        total = 0

        for character in str(key):
            total += ord(character)

        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, item in enumerate(bucket):
            if item[0] == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for stored_key, value in bucket:
            if stored_key == key:
                return value

        return None

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, item in enumerate(bucket):
            if item[0] == key:
                del bucket[i]
                return True

        return False

    def display(self):
        for index, bucket in enumerate(self.table):
            print(f"Index {index}: {bucket}")


def run_hash_table_tests():
    print("HASH TABLE TEST")
    print("----------------------------")

    records = HashTable(size=5)

    student_records = [
        ("S101", "Software Development"),
        ("S102", "Computer Science"),
        ("S103", "Cybersecurity"),
        ("S104", "Data Science"),
        ("S105", "Software Development")
    ]

    print("\nAdding student records:")

    for student_id, program in student_records:
        print(student_id, "-", program)
        records.insert(student_id, program)

    print("\nHash table contents:")
    records.display()

    print("\nSearching for existing key S103:")
    print(records.get("S103"))

    print("\nSearching for missing key S999:")
    print(records.get("S999"))

    print("\nDeleting S102:")
    print("Deleted:", records.delete("S102"))

    print("\nSearching for S102 after deletion:")
    print(records.get("S102"))

    print("\nHash table after deletion:")
    records.display()


def run_collision_test():
    print("\nCOLLISION TEST")
    print("----------------------------")

    # A small table increases the likelihood of collisions.
    collision_table = HashTable(size=3)

    keys = [
        ("A101", "Record A"),
        ("B100", "Record B"),
        ("C102", "Record C")
    ]

    for key, value in keys:
        collision_table.insert(key, value)

    collision_table.display()

    print("\nAll collision-test records can still be retrieved:")

    for key, _ in keys:
        print(key, "->", collision_table.get(key))


def run_runtime_tests():
    print("\nRUNTIME TESTING")
    print("----------------------------")

    input_sizes = [100, 1000, 10000]

    for size in input_sizes:
        table = HashTable(size=(size * 2) + 1)

        start_insert = time.perf_counter()

        for i in range(size):
            table.insert(f"S{i}", f"Student Record {i}")

        end_insert = time.perf_counter()

        start_search = time.perf_counter()

        correct = True

        for i in range(size):
            result = table.get(f"S{i}")

            if result != f"Student Record {i}":
                correct = False

        end_search = time.perf_counter()

        insert_runtime = end_insert - start_insert
        search_runtime = end_search - start_search

        print(f"\nInput size: {size}")
        print(f"Insertion runtime: {insert_runtime:.6f} seconds")
        print(f"Search runtime: {search_runtime:.6f} seconds")
        print(f"Output correct: {correct}")


if __name__ == "__main__":
    run_hash_table_tests()
    run_collision_test()
    run_runtime_tests()
