class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        ''' Adds a friend to the person's friends list. '''
        if friend not in self.friends:
            self.friends.append(friend)
        else:
            print(f"{friend.name} is already a friend of {self.name}.")

class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
            print(f"Person {name} added to the network.")
        else:
            print(f"Person {name} already exists in the network.")

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"{person1_name} does not exist in the network.")
            return
        if person2_name not in self.people:
            print(f"{person2_name} does not exist in the network.")
            return
        
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

        print(f"{person1_name} and {person2_name} are now friends.")

    def print_network(self):
        if not self.people:
            print("The network is empty.")
            return
        
        for person in self.people.values():
            friends_names = [friend.name for friend in person.friends]
            print(f"{person.name}: {', '.join(friends_names)}")

# Test the implementation
if __name__ == "__main__":
    # Create a social network instance
    network = SocialNetwork()

    # Adding people
    network.add_person("Alice")
    network.add_person("Bob")
    network.add_person("Charlie")
    network.add_person("David")
    network.add_person("Eve")
    network.add_person("Frank")

    # Adding friendships
    network.add_friendship("Alice", "Bob")
    network.add_friendship("Alice", "Charlie")
    network.add_friendship("Bob", "David")
    network.add_friendship("Charlie", "Eve")
    network.add_friendship("David", "Frank")
    network.add_friendship("Eve", "Frank")
    network.add_friendship("Alice", "Frank")
    network.add_friendship("Bob", "Eve")

    # Try adding invalid friendships
    network.add_friendship("Alice", "Zoe")  
    network.add_person("Alice")  

    # Print the network
    print("\nCurrent Social Network:")
    network.print_network() 

# Design memo: should be 226
# A graph is the right structure to use to represent a social network as it can easily mirror how people are connected in real life scenarios. A List would not work as it is simply just a collection of items that would not represent any relationships outside of just existing in the same list as each other, and a tree wouldn't work as the hierarchical structure of the tree would not be able to represent how people are related to one another in a real world setting. The performance and structural trade offs that I noticed include issues with the time complexity as friend connections began to grow, issues that may arise with duplicate friendships appearing. For the time complexity normally it's a O(1) operation but as friend connections begin to grow this operation can easily shift to a O(n) when checking the friends list to ensure that a friend does not already exist when adding them to a new list. This issue will cause the network to slow down especially in larger networks. To avoid duplicate friendships my code will go through the and check that a person is not already present in the friendship before adding them onto the list of friends, this helps avoid redundant data which in turn will help keep it running fast and making it easier to understand. 
