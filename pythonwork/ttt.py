items = "Whats the simpliest way to add the list items to a dictionary "

statsi = {}
for i in items:
    if i in statsi:
        statsi[i] += 1
    else:
        statsi[i] = 1

# bonus
print(statsi, i)
