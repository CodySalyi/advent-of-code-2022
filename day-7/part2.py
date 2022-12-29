class TreeNode:
  def __init__(self, name):
    self.name = name
    self.parent = None
    self.dirs = []
    self.files = []
    self.data = None


rootNode = TreeNode('/')
currentNode = rootNode

dir_sizes = []

input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines.pop(0)

for line in lines:
  if '$ cd ' in line:
    if '..' in line:
      dirs_total = 0
      files_total = 0
      if not currentNode.dirs == []:
        for dirNode in currentNode.dirs:
          dirs_total = dirs_total + dirNode.data
      if not currentNode.files == []:
        for fileNode in currentNode.files:
          files_total = files_total + int(fileNode.data)
      currentNode.data = dirs_total + files_total
      dir_sizes.append([currentNode.name, currentNode.data])
      currentNode = currentNode.parent
    else: 
      parts = line.split(' ')
      currentNode = next((node for node in currentNode.dirs if node.name == parts[2]), None)
  elif '$ ls' in line:
    None
  elif 'dir ' in line:
    parts = line.split(' ')
    dirNode = TreeNode(parts[1])
    dirNode.parent = currentNode
    currentNode.dirs.append(dirNode)
  else:
    parts = line.split(' ')
    fileNode = TreeNode(parts[1])
    fileNode.parent = currentNode
    fileNode.data = parts[0]
    currentNode.files.append(fileNode)

while True:
  dirs_total = 0
  files_total = 0
  if not currentNode.dirs == []:
    for dirNode in currentNode.dirs:
      dirs_total = dirs_total + dirNode.data
  if not currentNode.files == []:
    for fileNode in currentNode.files:
      files_total = files_total + int(fileNode.data)
  currentNode.data = dirs_total + files_total
  dir_sizes.append([currentNode.name, currentNode.data])
  if currentNode.parent == None:
    break
  currentNode = currentNode.parent

unused_space = 70000000 - currentNode.data
delete_size = 30000000 - unused_space

dir_can_delete = ['None', 70000000]

for dir in dir_sizes:
  if dir[1] >= delete_size and dir[1] < dir_can_delete[1]:
    dir_can_delete = dir

print(dir_can_delete)
    

