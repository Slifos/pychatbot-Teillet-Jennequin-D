import os

dirPath = r"speeches"
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
print(result)
print("helloooo1oo")
