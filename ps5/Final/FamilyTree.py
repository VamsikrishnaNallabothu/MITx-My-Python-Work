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
        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
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

        A = self.names_to_nodes[a]
        B = self.names_to_nodes[b]
        if A == B:
            return (-1, 0)

        def findFam(node, isRelated = []):
            if node == self.root:
                return isRelated
            else:
                copy_ancestors = [node] + isRelated
            return findFam(node.get_parent(), copy_ancestors)
        
        def related(related1, related2):
            related=1
            for elt1 in related1:
                for elt2 in related2:
                    if elt1==elt2:
                        related+=1
            return related

        X = len(findFam(A))
        Y = len(findFam(B))
        Z = related(findFam(A),findFam(B))
        return (min(X, Y) - Z , abs(X-Y))