def dirReduc(arr: list) -> list:
    # Dictionary to define what cancels what
    opposites = {
        "NORTH": "SOUTH", 
        "SOUTH": "NORTH", 
        "EAST": "WEST", 
        "WEST": "EAST"
    }
    
    stack = []
    
    for direction in arr:
        # If the stack isn't empty and the current direction 
        # is the opposite of the one we just added...
        if stack and opposites.get(direction) == stack[-1]:
            stack.pop() # Cancel them out
        else:
            stack.append(direction) # It's a valid path so far
            
    return stack

# Test Case
directions = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(f"Reduced path: {dirReduc(directions)}") 
# Output: ['WEST']