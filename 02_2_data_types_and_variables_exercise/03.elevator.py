num_people = int(input())
capacity_persons = int(input())

courses = num_people // capacity_persons
if num_people % capacity_persons != 0:
    courses += 1

print(courses)
