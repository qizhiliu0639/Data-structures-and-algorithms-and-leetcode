class tritree:
    def __init__(self):
        self.dict={}
        self.isWord=False

    def insert(self,word):
        curr = self
        for char in word:
            if char not in curr.dict:
                curr.dict[char] = tritree()
            curr = curr.dict[char]
        curr.isWord = True


    def search(self,word):
        curr = self
        for char in word:
            if char not in curr.dict:
                return False
            curr = curr.dict[char]
        return curr.isWord

if __name__ == "__main__":
    trie = tritree()
    texts = [["葬爱", "少年", "葬爱", "少年", "慕周力", "哈哈"], ["葬爱", "少年", "阿西吧"], ["烈", "烈", "风", "中"], ["忘记", "了", "爱"],
             ["埋葬", "了", "爱"]]
    for text in texts:
        trie.insert(text)
    markx = trie.search(["忘记", "了", "爱"])
    print(markx)
    markx = trie.search(["忘记", "了"])
    print(markx)
    markx = trie.search(["忘记", "爱"])
    print(markx)
