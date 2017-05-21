'''
Note: Write a solution with O(n2) time complexity, since this is what you would be asked to do during a real interview.

You have an array a composed of exactly n elements. Given a number x, determine whether or not a contains three elements for which the sum is exactly x.

Example

For x = 15 and a = [14, 1, 2, 3, 8, 15, 3], the output should be
tripletSum(x, a) = false;

For x = 8 and a = [1, 1, 2, 5, 3], the output should be
tripletSum(x, a) = true.

The given array contains the elements 1,2, and 5, which add up to 8.

'''

def tripletSum(x, a):
   a = sorted(a)
   
   for i, vali in enumerate(a):
      start = i + 1
      end = len(a) - 1
      while(start < end):
         if (vali + a[start] + a[end]) < x : 
            start += 1
         elif (vali + a[start] + a[end]) > x :
            end -= 1
         elif (vali + a[start] + a[end]) == x:
            print vali, a[start], a[end]
            return True
         else:
            continue
   return False      
         
   
x = 15
a = [14, 1, 2, 3, 8, 15, 3]
tripletSum(x, a)
