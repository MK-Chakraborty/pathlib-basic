rom pathlib import Path
path = Path("module_practice\\__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
# path = path.with_name("file.txt")
# print(path.absolute)
path = path.with_suffix(".txt")
print(path)

#leter I will also add beautifulsoup programs
