const fs = require("fs");

const puzzles = JSON.parse(fs.readFileSync("puzzles.json", "utf8"));
const today = new Date().toISOString().slice(0, 10);

// Pick puzzle based on day (rotates automatically)
const index = Math.abs(
  today.split("").reduce((a, c) => a + c.charCodeAt(0), 0)
) % puzzles.length;

const puzzle = puzzles[index];

const content = `
## 🧩 Daily Brain Teaser (${today})

> **Category:** ${puzzle.type.toUpperCase()}

### 🤔 Puzzle
**${puzzle.question}**

<details>
<summary>✅ Click to reveal the answer</summary>

**${puzzle.answer}**

</details>

---

✨ _Come back tomorrow for a brand-new challenge!_
`;

let readme = fs.readFileSync("README.md", "utf8");

// Replace everything between markers
readme = readme.replace(
  /<!-- DAILY_PUZZLE_START -->[\\s\\S]*?<!-- DAILY_PUZZLE_END -->/,
  `<!-- DAILY_PUZZLE_START -->\n${content}\n<!-- DAILY_PUZZLE_END -->`
);

fs.writeFileSync("README.md", readme);
