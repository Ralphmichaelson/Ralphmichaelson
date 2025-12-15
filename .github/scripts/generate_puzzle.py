import random

puzzles = [
    """🧩 **Daily Logic Puzzle**

1 = 3  
2 = 3  
3 = 5  
4 = 4  
5 = 4  

❓ What does **6** equal?

🧠 Hint:
- Think like a **programmer**
- Don’t calculate — **interpret**
""",

    """🧠 **Coding Puzzle**

What is the output of this C code?

```c
int x = 5;
printf("%d", x++ + ++x);
"""
]

puzzle = random.choice(puzzles)

with open("README.md", "r", encoding="utf-8") as f:
content = f.read()

content = content.replace("WAITING_FOR_PUZZLE", puzzle)

with open("README.md", "w", encoding="utf-8") as f:
f.write(content)
