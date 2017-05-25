'''
Given a dictionary dict, write a function flattenDictionary that 
returns a flattened version of it .

Example:

input:  dict = {
            Key1 : 1,
            Key2 : {
                a : 2,
                b : 3,
                c : {
                    d : 3,
                    e : 1
                }
            }
        }

output: {
            Key1: 1,
            Key2.a: 2,
            Key2.b : 3,
            Key2.c.d : 3,
            Key2.c.e : 1
        }
'''
res = {}
def flattenDictionary(dict1):
   helper(dict1, "")
   return res

def helper(dict1, initialKey):
   for key in dict1.keys():
      val = dict1[key]
      # if dictionary keep recursing
      if type(val) is dict:
         if not initialKey or initialKey == "":
            helper(val, key)
         else:
            helper(val, initialKey + "." + key)
      # if not dictionary add to result      
      else:
         if not initialKey or initialKey == "":
            res[key] = val
         else:
            res[initialKey + "." + key] = val

dict1 = {'Key1' : 1,
        'Key2' : {
                'a' : 2,
                'b' : 3,
                'c' : {
                    'd' : 3,
                    'e' : 1
                }
            }
        }
print flattenDictionary(dict1)
