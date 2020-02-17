from pathlib import Path
pathlist = Path('C:\Users\kristiyan.bonev\Desktop\Combining files').glob('**/*.asm')
for path in pathlist:
    # because path is object not string^M
    path_in_str = str(path)
    print(path_in_str)