class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
        
        node.is_word = True # mark as end of word
        

    def search(self, word: str) -> bool:
        cur_node = self.root

        for char in word:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        
        return cur_node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root

        for char in prefix:
            if char not in cur_node.children:
                return False
            
            cur_node = cur_node.children[char]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)