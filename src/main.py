from textnode import TextNode, TextType

def main():
    # Create a TextNode object
    text_node = TextNode("Hello, World!", TextType.BOLD, "http://example.com")

    # Print the TextNode object
    print(text_node)

    # Create another TextNode object
    another_text_node = TextNode("Hello, World!", TextType.BOLD, "http://example.com")

    # Compare the two TextNode objects
    print(text_node == another_text_node)  # Should print True

main()
# Output:
