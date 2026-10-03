# tasks = ["email Sam", "book the venue", "pay the band"]

# result = tasks.pop(0)

# print(result)
# print(tasks)

tasks = ["do laundry", "call mom"]

tasks.insert(0, "pay the rent")


todo = tasks.pop()
tasks.insert(0,todo)
print(tasks)