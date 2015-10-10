class Trie():
    def __init__(self):
        self.head = {}

    def add(self, word):
        current = self.head
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['$'] = {};

    def hasWord(self, word):
        current = self.head
        for char in word:
            if char not in current:
                return False
            else:
                current = current[char]
        return '$' in current

    def remove(self, word):
        def hasChildren(nodeDict):
            return len(nodeDict.keys()) == 0
        
        def deleteChar(text, index, node):
            if index == (len(text) - 1):
                node.pop('$', None)
                return hasChildren(node)
            else:
                if (deleteChar(text, index + 1, node[text[index + 1]])):
                    node.pop(text[index + 1], None)
                    return hasChildren(node)

            return False        
        deleteChar(word, -1, self.head)        
