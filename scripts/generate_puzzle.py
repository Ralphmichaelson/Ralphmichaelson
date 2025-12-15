import random

puzzles = [
    "What comes next: 2, 4, 8, 16, ?",
    "What is the output of: printf(\"%d\", 5 + 3 * 2);",
    "If x = 5, what is x * x?",
    "How many times does this loop run: for(i=0;i<4;i++)?"
]

puzzle = random.choice(puzzles)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("WAITING_FOR_PUZZLE", puzzle)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
