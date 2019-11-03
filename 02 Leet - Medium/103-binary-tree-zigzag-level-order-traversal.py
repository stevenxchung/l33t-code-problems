'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Level Order
    def printBST(self):
        node = self
        queue = []
        queue.append(node)

        print("Printing BST:", end=' ')
        while len(queue) > 0:

            print(queue[0].val, end=' ')
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        print()

    def printZigZag(self):
        node = self
        queue = []
        queue.append(node)
        count = 0

        print("Printing BST:", end=' ')
        while len(queue) > 0:

            # Initial print at head node
            if count == 0:
                print(queue[0].val, end=' ')
                node = queue.pop(0)

                if node.right is not None:
                    queue.append(node.right)
                if node.left is not None:
                    queue.append(node.left)

            elif count % 2 != 0:
                print(queue[0].val, end=' ')
                node = queue.pop(0)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            else:
                print(queue[0].val, end=' ')
                node = queue.pop(0)

                if node.right is not None:
                    queue.append(node.right)
                if node.left is not None:
                    queue.append(node.left)

            count += 1

        print()


# Test
head = Node(3, Node(9), Node(20, Node(15), Node(7)))
head.printBST() # 3 9 20 15 7
head.printZigZag() # 3 20 9 15 7
