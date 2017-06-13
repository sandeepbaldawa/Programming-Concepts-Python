'''
Strategy
Implement lock, unlock and islocked
We cannot lock a node if it's ancestors and  descendants are not locked
unlock can be done regardless of state on ancestors or descendants

Brute Force :- Check each parent and child on trying to lock
               O(m+d), m=> no of nodes in subtree and d is the depth
               For root node O(N)
               
Optimization :- While trying to lock we dont care to check if all nodes are locked
                as soon as we find some node is locked we can return, so we maintain
                __num_of_descendants in each node and as soon as this is > 0 we see we cant lock,
                no need to check other nodes
                Time Complexity :- O(h) 
                Space Complexoty :- O(N) (each node stores an additional variable) 
'''

class Node():
    def __init__(self):
        self.val , self.left, self.right = None
        self.__locked = False
        self.__num_of_descendants = 0
        self.parent= None
        
    
    def lock(self):
        '''a node can be locked only if it's ancestors or descendants are both unlocked'''
        if self.__num_of_descendants or self.__locked:
            return False
        
        '''Go through parents to see if they are locked'''
        curr = self.parent
        while(curr):
            if curr.__num_of_descendants:
                return False
            curr = curr.parent
            
        '''Acquire lock since both parent and child are not locked'''
        self.__locked = True
        curr = self.parent
        while (curr):
            curr.__num_of_descendants += 1
            curr = curr.parent
            
        return True
    
    def islocked(self):
        '''Check if locked'''
        return self.__locked
    
    def unlock(self):
        '''Unlock lock, just needs to inform all parents so that they can update themselves'''
        if self.__locked:
            self.__locked = False
            curr = self.parent
            while (curr):
                curr.__num_of_descendants -= 1
                curr = curr.parent
            
            
        
