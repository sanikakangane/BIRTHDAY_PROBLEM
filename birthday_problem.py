import random

def has_duplicate_birthday(people):
    birthdays = []  # list to store birthdays
    for _ in range(people):
        # random birthday between 1 and 365
        day = random.randint(1, 365)
        if day in birthdays:
            return True  # duplicate found
        birthdays.append(day)
    return False  # no duplicates

# Simulate many trials
trials = 10000
group_size = 30  #group size is 30
duplicate_count = 0

for _ in range(trials):
    if has_duplicate_birthday(group_size):
        duplicate_count += 1

probability = duplicate_count / trials
print(f"Probability of shared birthday in a group of {group_size} people: {probability:.2f}")
