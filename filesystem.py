class FileSystem:
    def __init__(self):
        self.trie = {}
        self.files = {}

    def add(self, path: str, size: int):
        # Add a file with its size
        dirs = path.split('/')
        node = self.trie
        for dir in dirs[:-1]:
            if dir not in node:
                node[dir] = {}
            node = node[dir]
        node[dirs[-1]] = {'_size': size}
        self.files[path] = size

    def copy(self, src: str, dest: str):
        # Copy a file to a new path
        if src not in self.files:
            raise FileNotFoundError(f"Source file {src} not found")
        size = self.files[src]
        self.add(dest, size)

    def query_size(self, path: str) -> int:
        # Query the size of a file
        if path not in self.files:
            raise FileNotFoundError(f"File {path} not found")
        return self.files[path]

    def find_prefix(self, prefix: str) -> list:
        # Find all files with a specific prefix in their path
        result = []
        nodes = [self.trie]
        for part in prefix.split('/'):
            new_nodes = []
            for node in nodes:
                if part in node:
                    new_nodes.append(node[part])
            nodes = new_nodes
        self._dfs(nodes, prefix, result)
        return result

    def _dfs(self, nodes, path, result):
        for node in nodes:
            for key, value in node.items():
                if key == '_size':
                    result.append((path, value))
                else:
                    self._dfs([value], f"{path}/{key}", result)

    def find_suffix(self, suffix: str) -> list:
        # Find all files with a specific suffix in their path
        result = []
        for path, size in self.files.items():
            if path.endswith(suffix):
                result.append((path, size))
        return result

    def delete(self, path: str):
        # Remove a file or directory from the filesystem
        if path in self.files:
            del self.files[path]
        dirs = path.split('/')
        node = self.trie
        for dir in dirs[:-1]:
            if dir in node:
                node = node[dir]
            else:
                raise FileNotFoundError(f"Path {path} not found")
        if dirs[-1] in node:
            del node[dirs[-1]]
        else:
            raise FileNotFoundError(f"Path {path} not found")

    def move(self, src: str, dest: str):
        # Move a file or directory to a new location
        if src not in self.files:
            raise FileNotFoundError(f"Source path {src} not found")
        size = self.files[src]
        self.add(dest, size)
        self.delete(src)

    def list_dir(self, path: str) -> list:
        # List all files and subdirectories within a specified directory
        dirs = path.split('/')
        node = self.trie
        for dir in dirs:
            if dir in node:
                node = node[dir]
            else:
                raise FileNotFoundError(f"Directory {path} not found")
        return list(node.keys())

    def get_path(self, name: str) -> list:
        # Get the full path of a file or directory given its name or part of its path
        result = []
        self._dfs_find_path(self.trie, "", name, result)
        return result

    def _dfs_find_path(self, node, current_path, name, result):
        for key, value in node.items():
            new_path = current_path + "/" + key
            if key == name or name in new_path:
                result.append(new_path)
            if isinstance(value, dict):
                self._dfs_find_path(value, new_path, name, result)

    def rename(self, old_path: str, new_name: str):
        # Rename a file or directory
        dirs = old_path.split('/')
        new_path = '/'.join(dirs[:-1]) + '/' + new_name
        if old_path in self.files:
            size = self.files[old_path]
            self.add(new_path, size)
            self.delete(old_path)
        else:
            raise FileNotFoundError(f"Path {old_path} not found")

    def exists(self, path: str) -> bool:
        # Check whether a specified file or directory exists
        dirs = path.split('/')
        node = self.trie
        for dir in dirs:
            if dir in node:
                node = node[dir]
            else:
                return False
        return True

# Example usage
fs = FileSystem()
fs.add("/a/b/c.txt", 100)
fs.add("/a/b/d.txt", 200)
fs.add("/a/e/f.txt", 300)
fs.copy("/a/b/c.txt", "/a/b/c_copy.txt")
print(fs.query_size("/a/b/c.txt"))  # Output: 100
print(fs.query_size("/a/b/c_copy.txt"))  # Output: 100
print(fs.find_prefix("/a/b"))  # Output: [('/a/b/c.txt', 100), ('/a/b/d.txt', 200), ('/a/b/c_copy.txt', 100)]
print(fs.find_suffix("d.txt"))  # Output: [('/a/b/d.txt', 200)]
print(fs.exists("/a/b/c.txt"))  # Output: True
print(fs.exists("/a/b/nonexistent.txt"))  # Output: False
fs.delete("/a/b/c.txt")
print(fs.exists("/a/b/c.txt"))  # Output: False
fs.rename("/a/b/d.txt", "d_renamed.txt")
print(fs.exists("/a/b/d_renamed.txt"))  # Output: True
print(fs.list_dir("/a/b"))  # Output: ['c_copy.txt', 'd_renamed.txt']