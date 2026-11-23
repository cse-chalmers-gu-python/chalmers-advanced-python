import os 

from tree import Tree

# Helper functions 
def read_directory(path: str | None = None) -> list[tuple[str, list[str]]]:
    return [(root.split('\\')[-1], dirs + files) for root, dirs, files in os.walk(path)]

def build_tree(dir_tree: Tree, dir_list: list[tuple[str, list[str]]]) -> None:
    if not dir_list:
        raise ValueError("Directory listing is empty; check the path")

    # root = dir_list[0][0]
    # dir_tree = Tree(root)

    for parent, children in dir_list:
        for child in children:
            dir_tree.add_edge(parent, child)


def main():
    dir_list = read_directory('test')
    dir_root = dir_list[0][0]
    dir_tree = Tree(dir_root)
    build_tree(dir_tree, dir_list)

    print(dir_tree.leaves())

# some methods return lists of edges or vertices, while we check for sets 

if __name__ == '__main__':
    main()