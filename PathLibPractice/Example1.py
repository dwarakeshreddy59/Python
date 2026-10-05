from pathlib import Path

file_path1=Path("PathLibPractice/Data/message.txt")

print(file_path1.exists())

file_path2=Path("PathLibPractice/Data/Note.txt")

print(file_path2.absolute())
#file_path2.absolute():-
#ANS:-(method) def absolute() -> Path
#Return an absolute version of this path by prepending the current working directory. No normalization or symlink resolution is performed.
#Use resolve() to get the canonical path to a file.

print(file_path2.glob)
