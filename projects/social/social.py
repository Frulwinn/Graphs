import random

class User:
    def __init__(self, name):
        self.name = name
    #def __repr__

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        #create an empty queue
        q = Queue()

        #create a visited set to keep track
        visited_set = set()

        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        #O(n)
        for userID in range(numUsers):
            self.addUser(f"User {userID+1}")

        # Create friendships
        #O(n^2)
        #searching sorted binary search O (logn)
        possible_friendships = []
        for userID in range(1, self.lastID + 1):
            for friendID in range(userID + 1, self.lastID + 1):
                possible_friendships.append( (userID, friendID))

                #O(n)
                random.shuffle(possible_friendships)
                print(possible_friendships)

                #need double slash so it doesn't need a float
                #O(n)
                friendship_to_create = numUsers * avgFriendships // 2
                for friendship in possible_friendships[:friendship_to_create]:
                    self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        extended network = connected components
        bfs
        compute connections from user 1

        """
        #starting vertex
        starting_vertex = userID
        #store visited nodes
        visited = {}  # Note that this is a dictionary, not a set
        #store connections
        connections = {}

        #create a queue
        q = Queue()

        q.enqueue([starting_vertex])

        #while the queue is not empty
        while q.size() > 0:
            #dequeue the first path
            path = q.dequeue()
            #grab vertext from end of the path
            vertex = path[-1]
            #if that vertex has not been visited

            if vertex not in visited:
                #mark it as visited
                visited[userID] = path

                #if vertex = target, return path
                if vertex == destination_vertex:
                    return path
                
                #add a path to all of its neighbors to the back of the queue
                for friend in self.vertices[vertex]:
                    if friend not in visited:
                        #copy the path
                        path_copy = path.copy()
                        #append neighbor to the back of the copy
                        path_copy.append(neighbor)

                        #enqueue copy
                        q.enqueue(path_copy)
        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
