'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return path
        
        path_names = []
        if path[0] == '/':
            path_names.append('/')
        
        
        for token in (token for token in path.split("/") if token not in ['.','']):
            if token == "..":
                print token
                if not path_names or path_names[-1] == "..":
                    path_names.append(token)
                else:
                    if path_names[-1] != '/':
                    	path_names.pop()
            else:  
                path_names.append(token)
        result = '/'.join(path_names)  
        return result[result.startswith('//'):]
        
        
