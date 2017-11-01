from collections import defaultdict
items = [3,1,7,6,4,1,1,5,4,7,9,0,9,7,7,43,2,6,87,67,4,2,532] # The array of integers
counter = defaultdict(lambda: 0)	# Counts how many integers there are
for i in items:	
    counter[i] += 1
item, amount = sorted(counter.items(), key=lambda x: x[1], reverse=True)[0]	# Sorts the array and reverses it
print(item, amount)
