# ============================================================
# Mini Project: Auto Suggestion System Using Trie Data Structure
# Developed using Object-Oriented Programming (OOP)
# ============================================================

# Trie Node Class
class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes
        self.children = {}

        # Marks end of a complete word
        self.is_end_of_word = False


# Trie Class
class Trie:
    def __init__(self):
        # Root node of Trie
        self.root = TrieNode()

    # Function to insert a word into Trie
    def insert(self, word):
        current = self.root

        for char in word:
            # Create node if character not present
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        # Mark last character as end of word
        current.is_end_of_word = True

    # Recursive function to collect suggestions
    def get_suggestions(self, node, prefix, suggestions):
        # If end of word found, add to suggestions list
        if node.is_end_of_word:
            suggestions.append(prefix)

        # Visit all child nodes
        for char, child_node in node.children.items():
            self.get_suggestions(
                child_node,
                prefix + char,
                suggestions
            )

    # Function to search prefix and return suggestions
    def search_prefix(self, prefix):
        current = self.root

        # Traverse Trie according to prefix
        for char in prefix:
            if char not in current.children:
                return []

            current = current.children[char]

        suggestions = []

        # Collect all matching words
        self.get_suggestions(current, prefix, suggestions)

        return suggestions


# ==========================
# Main Program
# ==========================

# Create Trie object
trie = Trie()

# Sample words
words = [
    "app",
    "apple",
    "application",
    "apply",
    "banana",
    "bat",
    "ball",
    "cat",
    "care"
]

# Insert words into Trie
for word in words:
    trie.insert(word)

print("\n========== AUTO SUGGESTION SYSTEM ==========")

# Accept prefix from user
prefix = input("Enter a prefix: ").lower()

# Get suggestions
suggestions = trie.search_prefix(prefix)

# Display result
if suggestions:
    print("\nSuggested Words:")
    for i, word in enumerate(suggestions, start=1):
        print(f"{i}. {word}")
else:
    print("\nNo matching words found!")

print("\n============================================")