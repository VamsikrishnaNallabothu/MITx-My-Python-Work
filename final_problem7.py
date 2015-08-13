# Paste your entire definition of the Family class in the following box.

class Member(object):
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a member. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent 

    def is_parent(self, mother):
        """
        mother: Member
        Returns: Boolean, whether or not `mother` is the 
        parent of this Member
        """
        return self.parent == mother  

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children 


class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor
        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 
        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # Convert name to Member node (should check for validity).
        mom_node = self.names_to_nodes[mother]   
        # Add each child.
        for c in list_of_children:           
            # Create Member node for a child.   
            c_member = Member(c)               
            # Remember its name to node mapping.
            self.names_to_nodes[c] = c_member    
            # Set child's parent.
            c_member.add_parent(mom_node)        
            # Set the parent's child.
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 
        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 
        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 
        Keyword arguments: 
        a -- string that is the name of node a
        b -- string that is the name of node b
        cousin type:
          -1 if a and b are the same node.
          -1 if either one is a direct descendant of the other
          >=0 otherwise, it calculates the distance from 
          each node to the common ancestor.  Then cousin type is 
          set to the smaller of the two distances, as described 
          in the exercises above
        degrees removed:
          >= 0
          The absolute value of the difference between the 
          distance from each node to their common ancestor.
        """
        # Check if a and b are the same node.
        if (a == b):
            return (-1, 0)
        
        # Search the list of ancestors for a and b.
        ancestors = {a:[],b:[]}
        for node in ancestors:
            parent = self.names_to_nodes[node]
            while (parent.name != self.root.name):
                parent = self.names_to_nodes[parent.name].get_parent()
                ancestors[node].append(parent.name)
        
        # Check if either one is a direct descendant of the other.
        if (a in ancestors[b]) :
            return (-1, ancestors[b].index(a) + 1)
        elif (b in ancestors[a]):
            return (-1, ancestors[a].index(b) + 1)
        
        # Search the common ancestor to calculate the cousin type 
        # and the degrees removed.
        if (len(ancestors[a]) >= len(ancestors[b])):
            lst1 = ancestors[a]
            lst2 = ancestors[b]
        else:
            lst1 = ancestors[b]
            lst2 = ancestors[a]
            
        for ancestor in lst1:
            if (ancestor in lst2): # Common ancestor found.
                d1 = lst1.index(ancestor)
                d2 = lst2.index(ancestor)
                return (min(d1,d2), abs(d1-d2))
            


f = Family("a")
f.set_children("a", ["b", "c"])
f.set_children("b", ["d", "e"])
f.set_children("c", ["f", "g"])

f.set_children("d", ["h", "i"])
f.set_children("e", ["j", "k"])
f.set_children("f", ["l", "m"])
f.set_children("g", ["n", "o", "p", "q"])

words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]

## These are your test cases. 

## The first test case should print out:
## 'b' is a zeroth cousin 0 removed from 'c'.
t, r = f.cousin("b", "c")
print "'b' is a", words[t],"cousin", r, "removed from 'c'"

## For the remaining test cases, use the graph to figure out what should 
## be printed, and make sure that your code prints out the appropriate values.

t, r = f.cousin("d", "f")
print "'d' is a", words[t],"cousin", r, "removed from 'f'"

t, r = f.cousin("i", "n")
print "'i' is a", words[t],"cousin", r, "removed from 'n'"

t, r = f.cousin("q", "e")
print "'q' is a", words[t], "cousin", r, "removed from 'e'"

t, r = f.cousin("h", "c")
print "'h' is a", words[t], "cousin", r, "removed from 'c'"

t, r = f.cousin("h", "a")
print "'h' is a", words[t], "cousin", r, "removed from 'a'"

t, r = f.cousin("h", "h")
print "'h' is a", words[t], "cousin", r, "removed from 'h'"

t, r = f.cousin("a", "a")
print "'a' is a", words[t], "cousin", r, "removed from 'a'"