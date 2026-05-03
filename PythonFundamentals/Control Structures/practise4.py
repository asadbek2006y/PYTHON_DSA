names = ["Alice", "Bob", "Charlie", "David", "Eve"]

search_name = "Charlie"
found = False
for name in names:
    if name == search_name: 
        found = True
        break
if found:
    print(f"{search_name} is in the list.")
else:    
    print(f"{search_name} is not in the list.")