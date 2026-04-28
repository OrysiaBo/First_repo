import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            print(file)
            
    print(f"root: {root}, dirs: {dirs}, files: {files}")
