# =========================
# Custom length function
# =========================

def my_len(x):
    """
    PSEUDOCODE:

    FUNCTION my_len(array)

        count = 0

        FOR every item in array
            add 1 to count

        RETURN count
    """

    count = 0

    # Loop through every item
    for char in x:
        count += 1

    return count


# =========================
# Custom Array Class
# =========================

class myArray:

    # -------------------------
    # Constructor
    # -------------------------
    def __init__(self, items):
        """
        PSEUDOCODE:

        FUNCTION constructor(items)

            save items inside object

        END
        """

        self.items = items


    # -------------------------
    # Get item by index
    # -------------------------
    def getIndex(self, index):
        """
        PSEUDOCODE:

        FUNCTION getIndex(index)

            RETURN item at index

        END
        """

        return self.items[index]


    # -------------------------
    # Append item
    # -------------------------
    def myAppend(self, item):
        """
        PSEUDOCODE:

        FUNCTION append(item)

            find length of array

            go to end of array

            insert item there

            RETURN updated array

        END
        """

        arr = my_len(self.items)

        # Insert item at end
        self.items[arr:arr] = [item]

        return self.items


    # -------------------------
    # Remove item by index
    # -------------------------
    def myPop(self, index):
        """
        PSEUDOCODE:

        FUNCTION pop(index)

            save item at index

            take left side before index

            take right side after index

            combine both sides

            replace original array

            RETURN removed item

        END
        """

        item = self.items[index]

        self.items = (
            self.items[:index] +
            self.items[index + 1:]
        )

        return item


    # -------------------------
    # Clear array
    # -------------------------
    def myClear(self):
        """
        PSEUDOCODE:

        FUNCTION clear()

            replace array
            with empty array

            RETURN empty array

        END
        """

        self.items = []

        return self.items


    # -------------------------
    # Copy array
    # -------------------------
    def myCopy(self):
        """
        PSEUDOCODE:

        FUNCTION copy()

            create duplicate array

            RETURN copied array

        END
        """

        return self.items[:]


    # -------------------------
    # Count occurrences
    # -------------------------
    def myCount(self, item):
        """
        PSEUDOCODE:

        FUNCTION count(item)

            count = 0

            FOR every value in array

                IF value equals item
                    add 1 to count

            RETURN total count

        END
        """

        count = 0

        for i in self.items:
            if i == item:
                count += 1

        return count


    # -------------------------
    # Extend array
    # -------------------------
    def myExtend(self, iterable):
        """
        PSEUDOCODE:

        FUNCTION extend(iterable)

            add all items from iterable
            into current array

            RETURN updated array

        END
        """

        self.items += iterable

        return self.items
    def myReverse(self): 
        """
        FUNCTION reverse(self)

            create empty list reversed_list

            FOR i from last index to first index
                add self.items[i] to reversed_list

            replace self.items with reversed_list

            RETURN self.items

        END
        
        """
        
        reversed_list = []
        for i in range(len(self.items) - 1, -1, -1):
            reversed_list.append(self.items[i])

        self.items = reversed_list

        return self.items
    

    # -------------------------
    # Find index of item
    # -------------------------
    def myIndex(self, item):
        """
        PSEUDOCODE:

        FUNCTION index(item)

            FOR every index and value

                IF value equals item
                    RETURN index

            IF item not found
                raise error

        END
        """

        for index, value in enumerate(self.items):

            if value == item:
                return index

        raise ValueError(f"{item} not found in array")
    def myInsert(self, index, item):
        """
        PSEUDOCODE:
        
        FUNCTION insert(index, item)
        
            go to index in array

            insert item there

            RETURN updated array

        END        
        """
        self.items[index:index] = [item]
        return self.items
    def myRemove(self, index):
        """ 
        PSEUDOCODE
        
        FUNCTION remove(index, item)
            go to index in array
            
            remove item there
            
            Return updated array
        END
        """
        
        self.items[index:index+1] = []
        return self.items

# =========================
# Create objects
# =========================

cars = myArray(["BMW", "Mercedes", "Audi"])

cars2 = ["BMW", "Mercedes", "Audi"]


# =========================
# MyArray Methods
# =========================

print("=== MyArray Methods ===")

print("MyArray count:", cars.myCount("Audi"))

print("MyArray get index:", cars.getIndex(0))

print("MyArray append:", cars.myAppend("Toyota"))

print("MyArray pop:", cars.myPop(1))

print("MyArray items:", cars.items)

print("MyArray copy:", cars.myCopy())

print("MyArray extend:", cars.myExtend(["Honda", "Ford"]))

print("MyArray index:", cars.myIndex("Audi"))

print("MyArray insert:", cars.myInsert(0, "Lexus"))

# print("MyArray remove: ", cars.myRemove("Audi"))
print("MyReverse reverse", cars.myReverse())
print("MyArray clear:", cars.myClear())


# =========================
# Python List Methods
# =========================

print("\n=== Python List Methods ===")

print("Python list count:", cars2.count("Audi"))

print("Python list pop:", cars2.pop(1))

print("Python list items:", cars2)

print("Python list copy:", cars2.copy())

cars2.extend(["Honda", "Ford"])

print("Python list items after extend:", cars2)
print("Python list index:", cars2.index("Audi"))
cars2.sort()
print(cars2)