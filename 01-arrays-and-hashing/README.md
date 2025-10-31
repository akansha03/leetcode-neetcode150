# Arrays and Hashing

## 🎯 Core Patterns

### 1. Hash Map for O(1) Lookups
Use when you need to check "have I seen this before?"
```python
seen = {}
for item in items:
    if item in seen:
        # Found duplicate/complement
```

### 2. Frequency Counting
```python
from collections import defaultdict, Counter
freq = defaultdict(int)
# or
freq = Counter(items)
```

### 3. Two-Pass vs One-Pass
- Two-pass: Build map → Query map
- One-pass: Check and update simultaneously

---

## ✅ Problems (9/9)

| # | Problem | Difficulty | Pattern | Confidence |
|---|---------|------------|---------|------------|
| 1 | Two Sum | Easy | Hash Map (complement) | ⭐⭐⭐⭐⭐ |
| 2 | Valid Anagram | Easy | Frequency Count | ⭐⭐⭐⭐⭐ |
| 3 | Contains Duplicate | Easy | Hash Set | ⭐⭐⭐⭐⭐ |
| 4 | Group Anagrams | Medium | Hash Map + Sorting | ⭐⭐⭐⭐ |
| 5 | Top K Frequent | Medium | Hash Map + Min Heap | ⭐⭐⭐⭐ |
| 6 | Product Except Self | Medium | Prefix/Suffix Arrays | ⭐⭐⭐ |
| 7 | Valid Sudoku | Medium | Hash Sets | ⭐⭐⭐⭐ |
| 8 | Encode/Decode Strings | Medium | String Manipulation | ⭐⭐⭐⭐ |
| 9 | Longest Consecutive | Medium | Hash Set + Logic | ⭐⭐⭐ |

---

## 🔑 Key Takeaways

1. **When to use Hash Map:**
   - Finding pairs/complements (Two Sum)
   - Frequency counting (Top K)
   - Grouping similar items (Group Anagrams)

2. **Time/Space Tradeoffs:**
   - Hash Map: O(1) lookup but O(n) space
   - Often worth the space for time improvement

3. **Common Mistakes:**
   - Forgetting to handle edge cases (empty array)
   - Not considering hash collisions in theory
   - Using list when set would suffice

---

## 📝 Revision Log
- **Solved:** [27/10/2025]
- **Last Revised:** [28/10/2025]
- **Next Revision:** [04/11/2025]

---

## 🎓 Interview Tips
- Always clarify: "Can I use extra space?"
- Mention O(1) lookup as reason for hash map
- Walk through example before coding