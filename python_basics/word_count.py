Users-MacBook-Pro:~ user$ vi wc.py

import sys

def print_words(filename):
  res = {}
  with open(filename, "r") as file:
     for line in file:
        words=line.strip("\n").split(" ")
        for each_word in words:
           if each_word in res:
              res[each_word] += 1
           else:
              res[each_word] = 1
        print res
  return res

def print_top(filename):
   print max(print_words(filename).values())
###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
~                                                                                                                                                                                                           
~                       
