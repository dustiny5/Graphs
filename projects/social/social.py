import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
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
        # Call addUser() until the nuumber of users == numUsers
        for i in range(numUsers):
            self.addUser(f'User: {i+1}')

        # Create friendships
        # totalFriendships = avgFriendships * numUsers
        # Generate a list of all possible friendships
        possibleFriendships = []

        # Avoid dupes by ensuring the first ID is smaller than the second ID
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        # Shuffle the list
        random.shuffle(possibleFriendships)
        print("Random Friendships")
        print(possibleFriendships)

        # Slice off totalFriendships from the front, create friendships
        totalFriendships = avgFriendships * numUsers // 2
        print(f'Friendships to create: {totalFriendships}\n')
        for i in range(totalFriendships):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        # Create empty queue
        q = Queue()

        # Enqueue a path, userID
        q.enqueue([userID])

        # Put all social paths connected to userID
        social_paths = {}

        # While the queue is not empty...
        while q.size() > 0:
            
            # Dequeue the first path
            path = q.dequeue()

            # Get the last vertex
            last_vertex = path[-1]
            
            # If last vertex not in visited
            if last_vertex not in visited.keys():
                # Put in the visited dictionary
                visited[last_vertex] = self.friendships[last_vertex]

                # Update social_paths to include its connections
                social_paths.update({last_vertex: path})

                # Add a path to its neighbors to the back of the queue
                for neighbor in self.friendships[last_vertex]:
                    copy_path = list(path)
                    copy_path.append(neighbor)
                    q.enqueue(copy_path)

        return social_paths


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print("USERS:")
    print(sg.users)
    print("FRIENDSHIPS:")
    print(sg.friendships)
    print("CONNECTIONS")
    connections = sg.getAllSocialPaths(1)
    print(connections)
