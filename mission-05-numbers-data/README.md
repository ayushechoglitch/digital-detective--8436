# Mission 05 — Numbers, Data Representation & Encoding

## 1. Mission Title & Objectives
**Title:** Radix Conversions, Number Systems, and Text Encoding  
**Objective:** Perform step-by-step manual conversions between decimal, binary, and hexadecimal notations; verify results using Python; develop an interactive number converter; and explain character encoding standards.

## 2. Work Completed
### Task 5.1 — Step-by-Step Manual Conversions
To verify the fundamental arithmetic of positional numbering systems, I calculated all seven required conversions by hand using successive division and positional weighting:

1. **Decimal 13 to Binary (Successive Division by 2):**
   - $13 \div 2 = 6$, remainder **1**
   - $6 \div 2 = 3$, remainder **0**
   - $3 \div 2 = 1$, remainder **1**
   - $1 \div 2 = 0$, remainder **1**
   - Reading remainders from bottom to top: **$1101_2$**

2. **Decimal 25 to Binary (Successive Division by 2):**
   - $25 \div 2 = 12$, remainder **1**
   - $12 \div 2 = 6$, remainder **0**
   - $6 \div 2 = 3$, remainder **0**
   - $3 \div 2 = 1$, remainder **1**
   - $1 \div 2 = 0$, remainder **1**
   - Reading remainders from bottom to top: **$11001_2$**

3. **Binary $1010_2$ to Decimal (Positional Expansion):**
   - $(1 	imes 2^3) + (0 	imes 2^2) + (1 	imes 2^1) + (0 	imes 2^0)$
   - $= 8 + 0 + 2 + 0 = \mathbf{10_{10}}$

4. **Binary $1101_2$ to Decimal (Positional Expansion):**
   - $(1 	imes 2^3) + (1 	imes 2^2) + (0 	imes 2^1) + (1 	imes 2^0)$
   - $= 8 + 4 + 0 + 1 = \mathbf{13_{10}}$

5. **Hexadecimal $	ext{A}_{16}$ to Decimal:**
   - In base 16, digits 0–9 represent values 0–9, and letters A–F represent values 10–15.
   - Therefore, $	ext{A}_{16} = \mathbf{10_{10}}$.

6. **Hexadecimal $1	ext{F}_{16}$ to Decimal:**
   - $(1 	imes 16^1) + (15 	imes 16^0)$
   - $= 16 + 15 = \mathbf{31_{10}}$

7. **Binary $1111_2$ to Hexadecimal:**
   - $1111_2 = (1 	imes 8) + (1 	imes 4) + (1 	imes 2) + (1 	imes 1) = 15_{10}$
   - In hexadecimal notation, value 15 is represented by the single symbol **$	ext{F}_{16}$**.

---

### Task 5.2 — Python Verification Checks
I verified every manual calculation in the Python interactive shell:

| Target Conversion | Python Verification Expression | Evaluated Output | Verification Status |
|---|---|:---:|:---:|
| Decimal 13 $ightarrow$ Binary | `bin(13)[2:]` | `'1101'` | Matches ($1101_2$) |
| Decimal 25 $ightarrow$ Binary | `bin(25)[2:]` | `'11001'` | Matches ($11001_2$) |
| Binary 1010 $ightarrow$ Decimal | `int('1010', 2)` | `10` | Matches ($10_{10}$) |
| Binary 1101 $ightarrow$ Decimal | `int('1101', 2)` | `13` | Matches ($13_{10}$) |
| Hexadecimal A $ightarrow$ Decimal | `int('A', 16)` | `10` | Matches ($10_{10}$) |
| Hexadecimal 1F $ightarrow$ Decimal | `int('1F', 16)` | `31` | Matches ($31_{10}$) |
| Binary 1111 $ightarrow$ Hexadecimal | `hex(int('1111', 2))[2:].upper()` | `'F'` | Matches ($	ext{F}_{16}$) |

---

### Task 5.3 — The Number Converter Program
I wrote [`number_converter.py`](number_converter.py) to accept positive decimal integers and display clean binary and uppercase hexadecimal representations.

**Sample Interactive Test Runs:**
- Input `13` $ightarrow$ Binary: `1101`, Hexadecimal: `D`
- Input `25` $ightarrow$ Binary: `11001`, Hexadecimal: `19`
- Input `255` $ightarrow$ Binary: `11111111`, Hexadecimal: `FF`

Full test runs are logged in [Converter Runs Evidence](evidence/converter-runs.md).

---

### Task 5.4 — Character Encoding: ASCII & UTF-8
Computers only store binary bits (0s and 1s), so human characters require standard encoding maps:
- **ASCII (American Standard Code for Information Interchange):**
  - A 7-bit encoding standard supporting 128 characters (English alphabet, digits, punctuation, and control characters).
  - Uppercase **'A'** has decimal code **65** (`0b1000001` / `0x41`).
  - Lowercase **'a'** has decimal code **97** (`0b1100001` / `0x61`).
  - Notice the difference: $97 - 65 = 32$ (`0b00100000`). Lowercase conversion is simply toggling bit 5!
- **Unicode & UTF-8:**
  - ASCII cannot represent non-English scripts, accented letters, or emojis.
  - Unicode assigns a unique code point to every character in all human languages.
  - **UTF-8** is a variable-length encoding (1 to 4 bytes per character) that is 100% backward-compatible with 7-bit ASCII while allowing representation of millions of symbols and emojis (e.g. `🎉` code point `U+1F389`, encoded as 4 bytes in UTF-8).

## 3. Practical Difficulties & Solutions
- **Challenge:** Keeping remainders in the correct order during successive division.
- **Resolution:** Practiced writing down the quotients and remainders in a two-column table and explicitly drawing an upward arrow to read remainders from bottom to top.

## 4. Commit & Verification Status
- **Commits:**
  1. `Add number converter Python script` (Script file)
  2. `Build number converter and practise data representation` (Calculations and report)
- **Status:** Verified and pushed to `main`.
