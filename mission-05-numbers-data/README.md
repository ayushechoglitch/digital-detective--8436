# Mission 05 — Numbers and data

## 1. Mission title
Mission 05 — Numbers and data.

## 2. Task / objective
Convert decimal, binary and hexadecimal values, verify conversions using Python, build a small converter and explain text encoding.

## 3. Work completed
### Task 5.1 — Manual number conversions

1. **Decimal 13 to binary:** divide by 2 and record remainders:  
   13 ÷ 2 = 6 remainder 1; 6 ÷ 2 = 3 remainder 0; 3 ÷ 2 = 1 remainder 1; 1 ÷ 2 = 0 remainder 1.  
   Read remainders from bottom to top: **1101₂**.

2. **Decimal 25 to binary:**  
   25 ÷ 2 = 12 r1; 12 ÷ 2 = 6 r0; 6 ÷ 2 = 3 r0; 3 ÷ 2 = 1 r1; 1 ÷ 2 = 0 r1.  
   Bottom to top: **11001₂**.

3. **Binary 1010 to decimal:**  
   \(1×2^3 + 0×2^2 + 1×2^1 + 0×2^0 = 8+0+2+0 = 10\).  
   Answer: **10₁₀**.

4. **Binary 1101 to decimal:**  
   \(1×2^3 + 1×2^2 + 0×2^1 + 1×2^0 = 8+4+0+1 = 13\).  
   Answer: **13₁₀**.

5. **Hexadecimal A to decimal:** A represents 10.  
   Answer: **10₁₀**.

6. **Hexadecimal 1F to decimal:**  
   \(1×16^1 + 15×16^0 = 16+15 = 31\).  
   Answer: **31₁₀**.

7. **Binary 1111 to hexadecimal:** 1111₂ equals 15₁₀, and 15 is F in hexadecimal.  
   Answer: **F₁₆**.

### Task 5.2 — Python verification

Run these expressions in the Python interactive environment:

| Conversion | Python expression | Result |
|---|---|---|
| Decimal 13 to binary | `bin(13)` | `'0b1101'` |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` |
| Binary 1010 to decimal | `int('1010', 2)` | `10` |
| Binary 1101 to decimal | `int('1101', 2)` | `13` |
| Decimal 31 to hexadecimal | `hex(31)` | `'0x1f'` |
| Hexadecimal 1F to decimal | `int('1F', 16)` | `31` |
| Binary 1111 to hexadecimal | `hex(int('1111', 2))` | `'0xf'` |

The `0b` prefix indicates binary and `0x` indicates hexadecimal. Python displays hexadecimal letters in lowercase by default; `f` and `F` represent the same digit.

### Task 5.3 — Number converter
The working program is `number_converter.py`. It asks for a decimal integer and displays its binary and hexadecimal forms.

Example tests:

| Input | Binary output | Hexadecimal output |
|---:|---|---|
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 31 | `0b11111` | `0x1f` |

Run it from the repository root:

```bash
python3 mission-05-numbers-data/number_converter.py
```

`bin(number)` converts an integer to a binary string with a `0b` prefix. `hex(number)` converts an integer to a hexadecimal string with a `0x` prefix.

### Task 5.4 — Text encoding
- ASCII decimal code for uppercase **A**: **65**.
- ASCII decimal code for lowercase **a**: **97**.
- A computer needs an encoding standard so that text characters are represented by agreed numeric values and can be stored, transmitted and interpreted consistently.
- An example outside basic ASCII is **₹** (Indian rupee sign) or **😊**.

ASCII covers a basic character set. UTF-8 can represent a much wider range of characters and is widely used for text on the internet.

## 4. Commands / tools used
- `python3` — opens/runs Python.
- `bin()` — converts an integer to binary text.
- `hex()` — converts an integer to hexadecimal text.
- `int(text, base)` — interprets text as an integer in the specified base.
- `input()` — reads the user's input.
- `print()` — displays the results.

## 5. My understanding
Binary uses base 2, decimal uses base 10 and hexadecimal uses base 16. In binary, each position represents a power of 2; in hexadecimal, each position represents a power of 16. Encoding maps characters to numbers so computers can store and exchange text.

## 6. Difficulties faced
No major difficulties calculating manual conversions and writing the conversion script.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- `number_converter.py`
- Manual conversion working and Python verification
- Three test cases and their actual terminal outputs

## 9. Commit details
Suggested message: `Build number converter and practise data representation`  
Actual commit/push status: Committed and verified on GitHub.
