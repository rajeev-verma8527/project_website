import os

def get_tree(cwd=os.getcwd()):
    path = os.path.join(cwd,"templates","cities")
    cities = [i for i in os.listdir(path) if not i.endswith(".html")]
    tree = {}

    for i in cities:
        files = [i for i in os.listdir(os.path.join(path,i)) if i!= "main.html"]
        tree[i] = files

    return tree

