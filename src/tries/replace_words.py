"""
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".
Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
Return the sentence after the replacement.
"""


class TrieNode:
    def __init__(self):
        self.val = False
        self.children = [None] * 256


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if node.children[ord(ch)] is None:
                node.children[ord(ch)] = TrieNode()
            node = node.children[ord(ch)]
        node.val = True

    def find_shortest(self, word):
        node = self.root
        for i, ch in enumerate(word):
            if node.children[ord(ch)] is None:
                return word
            node = node.children[ord(ch)]
            if node.val:
                return word[: i + 1]
        return word


def replace_words(dictionary, sentence):
    words = sentence.split(" ")
    dict_trie = Trie()
    for word in dictionary:
        dict_trie.insert(word)

    for i, word in enumerate(words):
        words[i] = dict_trie.find_shortest(word)

    return " ".join(words)


def main():
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(replace_words(dictionary, sentence))


if __name__ == "__main__":
    main()
