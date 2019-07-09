
def earliest_ancestor(ancestors, starting_node):
    #create a stack
    stack = [starting_node]
    #create a path
    path = []
    #create a visited set so we're not caught in infinite loop
    visited = set()
    
    #create a while loop to go through stack till earliest ancestor is reached
    while stack:
