# The class shows how general tree data structure works

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

electronics = TreeNode("Electronics")
laptop = TreeNode("Laptop")
phone = TreeNode("Phone")
tv = TreeNode("TV")

electronics.add_child(laptop)
electronics.add_child(phone)
electronics.add_child(tv)

hp = TreeNode('HP')
dell = TreeNode("Dell")
asus = TreeNode("Asus")
laptop.add_child(hp)
laptop.add_child(dell)
laptop.add_child(asus)

iphone = TreeNode("Iphone")
samsung = TreeNode("Samsung")
phone.add_child(iphone)
phone.add_child(samsung)

lg = TreeNode("LG")
sony = TreeNode("Sony")
walton = TreeNode("Walton")
tv.add_child(lg)
tv.add_child(sony)
tv.add_child(walton)

electronics.print_tree()