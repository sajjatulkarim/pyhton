
# 1. Sorting simple lists
numbers = [23, 45, 12, 9, 78, 1]
print("Original numbers:", numbers)
# Sort in ascending order
sorted_numbers = sorted(numbers, key=lambda x: x)
print("Sorted ascending:", sorted_numbers)
# Sort in descending order
sorted_numbers_desc = sorted(numbers, key=lambda x: -x)
print("Sorted descending:", sorted_numbers_desc)


sorted_desc = sorted(numbers, key=lambda x: -x)  # or use reverse=True
print("Sorted descending:", sorted_desc)


# 6. Using list.sort() with lambda (modifies list in place)
scores = [("Math", 85), ("Physics", 92), ("Chemistry", 78)]
print("\nOriginal scores:", scores)
scores.sort(key=lambda x: x[1], reverse=    True)  # Sort by score descending
print("Sorted scores (in-place):", scores)

# 2. Sorting strings by length
words = ["python", "java", "javascript", "c", "ruby", "go"]
print("\nOriginal words:", words)
# Sort by length
sorted_by_length = sorted(words, key=lambda s: len(s))
print("Sorted by length:", sorted_by_length)
# Sort by length descending


# 5. Complex sorting (multiple criteria)
people = [
    ("John", 30, "New York"),
    ("Alice", 25, "Boston"),
    ("Bob", 30, "Chicago"),
    ("Eve", 25, "Boston")
]
print("\nOriginal people:", people)
# Sort by age then name
sorted_people = sorted(people, key=lambda x: (x[1], x[0]))
print("Sorted by age then name:", sorted_people)
# Sort by city then age
sorted_by_city_age = sorted(people, key=lambda x: (x[2], x[1]))
print("Sorted by city then age:", sorted_by_city_age)


orted_by_length_desc = sorted(words, key=lambda s: len(s), reverse=True)
print("Sorted by length (descending):", sorted_by_length_desc)

# 3. Sorting dictionaries
students = [
    {"name": "Alice", "age": 22, "grade": 85},
    {"name": "Bob", "age": 20, "grade": 92},
    {"name": "Charlie", "age": 21, "grade": 78}
]
print("\nOriginal students:", students)
# Sort by age
sorted_by_age = sorted(students, key=lambda student: student["age"])
print("Sorted by age:", sorted_by_age)
# Sort by grade descending
sorted_by_grade = sorted(students, key=lambda student: student["grade"], reverse=True)
print("Sorted by grade (descending):", sorted_by_grade)

# 4. Sorting tuples
coordinates = [(3, 7), (1, 2), (5, 1), (2, 8)]
print("\nOriginal coordinates:", coordinates)
# Sort by x coordinate
sorted_by_x = sorted(coordinates, key=lambda coord: coord[0])
print("Sorted by x:", sorted_by_x)
# Sort by y coordinate
sorted_by_y = sorted(coordinates, key=lambda coord: coord[1])
print("Sorted by y:", sorted_by_y)
# Sort by sum of coordinates
sorted_by_sum = sorted(coordinates, key=lambda coord: coord[0] + coord[1])
print("Sorted by sum:", sorted_by_sum)