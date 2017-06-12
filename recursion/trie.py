import collections

class Trie(object):
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.complete = False

    def add_word(self, s):
        if not s:
            self.complete = True
        else:
            self.children[s[0]].add_word(s[1:])

    def check_word(self, s, prefix_check=False):
        if not s:
            return prefix_check or self.complete
        else:
            if s[0] in self.children:
                return self.children[s[0]].check_word(s[1:], prefix_check)
            else:
                return False

    def show_trie(self, indent=0):
        for child in self.children:
            print "%s%s %r" % (" " * indent, child, self.children[child].complete)
            self.children[child].show_trie(indent=indent+1)

root = Trie()
dictionary = ['and', 'an', 'cat', 'ant']
for word in dictionary:
    root.add_word(word)
root.show_trie()

assert root.check_word("an") == True
assert root.check_word("ca", prefix_check=True) == True
assert root.check_word("card") == False
assert root.check_word("a") == False
assert root.check_word("a", prefix_check=True) == True
