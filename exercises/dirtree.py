import os 

from tree import Tree

def read_directory(path: str) -> list[tuple[str, list[str]]]:
    return [
        (os.path.split(root)[-1], dirs + files)
        for root, dirs, files in os.walk(path)
    ]

def build_tree(dir_list: list[tuple[str, list[str]]]) -> Tree:
    if not dir_list:
        raise ValueError("Directory listing is empty; check the path")
    dir_root = dir_list[0][0]
    dir_tree = Tree(dir_root)
    for parent, children in dir_list:
        for child in children:
            dir_tree.add_edge(parent, child)
    return dir_tree

def main():
    dir_list = read_directory('.')
    print(dir_list)
    dir_tree = build_tree(dir_list)
    print(dir_tree.leaves())

if __name__ == '__main__':
    main()
