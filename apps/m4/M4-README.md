# Technical Brief
# Iterable BeautifulSoup


# 1. Introduction

This project extends the standard `BeautifulSoup` class to make it directly iterable.

Iteration traverses the DOM tree in \*\*depth-first order\*\*, yielding one node at a time.

All node types including `Tag` and `NavigableString` are supported.

Importantly, no pre-collection of nodes into lists is done, ensuring memory efficiency for large HTML documents.



---



# 2. Features

- Iterates over all nodes in \*\*document order\*\* (depth-first traversal)

- Supports `Tag` and `NavigableString`

- Memory-efficient: \*\*no list pre-collection\*\*

- Fully compatible with existing `BeautifulSoup` objects

- Easy to filter nodes during iteration (by tag name, attributes, etc.)



---



# 3. Implementation

The iterable functionality is implemented directly in `BeautifulSoup`:


def __iter__(self):
    yield from self.traverse(self)

def traverse(self, node):
    yield node
    if isinstance(node, Tag):
        for child in node.children:
            yield from self.traverse(child)



