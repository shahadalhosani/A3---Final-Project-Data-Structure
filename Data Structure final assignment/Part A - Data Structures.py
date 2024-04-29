import heapq
class Post:  # define a class named Post to represent a social media post
    def __init__(self, datetime, content, views, userName):  # constructor method for initializing a Post object with attributes
        self.datetime = datetime  # adding an attribute of date time
        self.content = content  # adding an attribute of content
        self.views = views  # adding an attribute of views
        self.userName = userName  # adding an attribute of user name

    def __str__(self):  # define a function to display all attributes of the post after creating objects for it with string representation
        return f"DateTime: {self.datetime}, Content: {self.content}, Views: {self.views}, UserName: {self.userName}"


# HashTable implementation to find post by datetime value
class HashTable:  # define a class named Hash Table to implement the hash table data structure for finding a post by its datetime value
    def __init__(self, size):  # constructor method for initializing the HashTable object with a specified size.
        self.size = size  # size of the hash table
        self.table = {}  # initialize an empty dictionary that we will be adding various posts in

    def hash_function(self, datetime):  # define a hash function to calculate the hash value of a datetime
        return hash(datetime) % self.size

    def insert(self, post):  # define a function to insert a post into the hash table.
        index = self.hash_function(post.datetime)  # Get hash index for given datetime
        if index not in self.table:  # Check if index exists in table
            self.table[index] = {}  # If not, create an empty dictionary
        self.table[index][post.datetime] = post  # Add post to hash table

    def find(self, datetime):  # define a function to find the post with the specified date time value
        index = self.hash_function(datetime)  # Get hash index for given datetime
        if index in self.table and datetime in self.table[index]:  # Check if index and datetime exist in table
            return self.table[index][datetime]  # Return post if found
        return None  # Return None if not found


# BST implementation to find posts in a specific time range
class TreeNode:  # define a class named TreeNode to represent a node in a binary seach tree
    def __init__(self, post):  # constructor method for initializing a TreeNode object with a post
        self.post = post  # include an attribute for post since we will be adding it to the tree
        self.left = None  # initialize left child
        self.right = None  # initialize right child

    def insert(self, post):  # define a function to insert a post into the binary seach tree
        if post.datetime < self.post.datetime:  # compare the date time values
            if self.left is None:  # check if the left child is None
                self.left = TreeNode(post)  # if the left child is None, create a new node
            else:
                self.left.insert(post)  # otherwise, recursively insert on the left subtree
        elif post.datetime > self.post.datetime:  # compare the date time values
            if self.right is None:  # check if the right child is None
                self.right = TreeNode(post)  # if the right child is None, create a new node
            else:
                self.right.insert(post)  # otherwise, recursively insert on the right subtree

    def get_posts_in_range(self, start_datetime, end_datetime, result):  # define a function to retreive posts within a specified time range
        if self.left is not None:  # Traverse left subtree if not None
            self.left.get_posts_in_range(start_datetime, end_datetime, result)
        if start_datetime <= self.post.datetime <= end_datetime:  # Check if post falls within the range
            result.append(self.post)  # Add post to result list
        if self.right is not None:  # Traverse right subtree if not None
            self.right.get_posts_in_range(start_datetime, end_datetime, result)


class BST:  # define a class named BST to implement a binary search tree
    def __init__(self):  # constructor method for initializing a BST object
        self.root = None  # initialize root as None

    def insert(self, post):  # define a function to insert a post into the binary search tree
        if self.root is None:
            self.root = TreeNode(post)  # if the tree is empty. set posts as root
        else:
            self.root.insert(post)  # otherwise, insert post recursively

    def get_posts_in_range(self, start_datetime, end_datetime):  # define a function to retrieve posts within a specified time range
        result = []  # initialize result list
        if self.root is not None:
            self.root.get_posts_in_range(start_datetime, end_datetime, result)  # start recursive traversal
        return result  # return posts within the range


# Heap implementation to find a post with the most views
class MaxHeap:  # define a class named MaxHeap to implement a max heap
    def __init__(self):  # constructor method for initializing a MaxHeap object
        self.heap = []  # initialize heap as an empty list

    def add_post(self, post):  # define a function to add a post to the max heap
        heapq.heappush(self.heap, (-post.views, post))  # push post onto the heap with negated views

    def get_post_with_most_views(self):  # define a function to retrieve the post with the most views from the max heap
        if self.heap:  # if statement to check if heap is not empty
            return heapq.heappop(self.heap)[1]  # pop and return post with most views
        else:
            return None  # otherwise, return None if heap is empty



# Test case for Hash table to find a certain post by its date time value

# Create objects for the posts with various attributes
post1 = Post("2024-02-01 10:00", "Food Content", 100000, "Ahmed123")
post2 = Post("2020-01-03 11:00", "Travel Content", 20000000, "SaraAl77")
post3 = Post("2024-05-11 12:00", "Family Content", 500000, "Maha101")
post4 = Post("2021-09-20 2:00", "Education Content", 40000, "Khaled234")

# Create HashTable instance
hash_table = HashTable(size=10)
hash_table.insert(post1)  # inserting post 1 into the hashtable
hash_table.insert(post2)  # inserting post 2 into the hashtable
hash_table.insert(post3)  # inserting post 3 into the hashtable
hash_table.insert(post4)  # inserting post 4 into the hashtable

# Retrieve posts from HashTable
print("\nFind post by its unique datetime value:")
print(hash_table.find("2024-02-01 10:00"))
print(hash_table.find("2024-05-11 12:00"))
print(hash_table.find("2020-01-03 11:00"))



# Test case for Binary search tree to find a certain posts that are within a specific time range (start date - end date)

# Create objects for the posts with various attributes
post1 = Post("2021-12-01 1:00", "Daily routine Content", 1000000, "Saif321")
post2 = Post("2019-10-10 9:00", "Rating dramas Content", 50000, "Mohammed.Kl67")
post3 = Post("2017-11-11 7:00", "School Content", 2000, "Mahra101")
post4 = Post("2023-09-19 11:00", "News Content", 300000, "Zayed234")

# Create BST instance
bst = BST()
bst.insert(post1)  # inserting post 1 into the BST
bst.insert(post2)  # inserting post 2 into the BST
bst.insert(post3)  # inserting post 3 into the BST
bst.insert(post4)  # inserting post 4 into the BST

# Retrieve posts that are within a specific time range
print("\nFind posts in a specific time range:")
posts_in_range = bst.get_posts_in_range("2019-10-10 9:00", "2023-09-19 11:00")
for post in posts_in_range:  # for loop to retrieve each post within the specified time range
    print(post)



# Test case for Heap to the post with the highest number of views

# Create objects for the posts with various attributes
post1 = Post("2020-11-02 10:00", "Interior design Content", 2000000, "Rashed321")
post2 = Post("2015-10-11 11:00", "Job Applications Content", 40000, "Shahad.A05")
post3 = Post("2018-04-02 5:00", "Weather Conditions Content", 1000, "Aisha12")
post4 = Post("2021-02-30 8:00", "UAE News Content", 500000, "Leyan009")

# Create MaxHeap instance
max_heap = MaxHeap()
max_heap.add_post(post1)  # inserting post 1 into the heap
max_heap.add_post(post2)  # inserting post 2 into the heap
max_heap.add_post(post3)  # inserting post 3 into the heap
max_heap.add_post(post4)  # inserting post 4 into the heap

# Retrieve the post with the most views
print("\nFind post with the most views:")
print(max_heap.get_post_with_most_views())
