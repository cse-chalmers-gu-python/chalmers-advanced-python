import sys
import os


class Tree():

    def __init__(self, root: str, subtrees: List):
        self._root = root
        self._subtrees = subtrees

    def __str__(self):
        return '\n'.join(self.pretty(0))

    def pretty(self, indent):
        lines = [indent*'+' + self._root]
        for t in self._subtrees:
            if isinstance(t, Tree):
                lines.extend(t.pretty(indent+2))
            else:
                lines.append((indent+2)*'-' + str(t))
        return lines


def depth(tree):
    if isinstance(tree, Tree):
        return 1 + max([depth(t) for t in tree._subtrees])
    else:
        return 1

        
def build_dir_tree(path: str) -> Tree:
    files = os.listdir(path)
    return Tree(path, [build_dir_tree(f) if os.path.isdir(f:= path+'/'+file) else file for file in files])


tree = build_dir_tree(sys.argv[1])
print(tree)
print(depth(tree))

