# LeetCode Master Patterns

## Last Updated: [31/10/2025]

---

## 1️⃣ Arrays & Hashing

### Pattern 1: Hash Map for Complement/Pair Finding
**Recognition:** "Find two elements that sum to X"
**Template:**
```python
seen = {}
for i, num in enumerate(arr):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```
**Problems:** Two Sum, Two Sum II
**Time:** O(n), **Space:** O(n)

---

### Pattern 2: Frequency Counting
**Recognition:** "Find top K", "Count occurrences"
**Template:**
```python
from collections import Counter
freq = Counter(items)
# or
freq = defaultdict(int)
for item in items:
    freq[item] += 1
```
**Problems:** Top K Frequent, Valid Anagram
**Time:** O(n), **Space:** O(n)

---

### Pattern 3: Min Heap for Top-K
**Recognition:** "Find K largest/most frequent"
**Template:**
```python
import heapq
heap = []
for key, val in items:
    heapq.heappush(heap, (val, key))
    if len(heap) > k:
        heapq.heappop(heap)
return [item[1] for item in heap]
```
**Problems:** Top K Frequent, Kth Largest
**Time:** O(n log k), **Space:** O(k)

---

### Common Pitfalls:
- ❌ Forgetting empty array edge case
- ❌ Using list when set is sufficient
- ❌ Not handling duplicate keys in hash map

### Complexity Quick Reference:
- Hash Map access: O(1) average
- Counter creation: O(n)
- Heap push/pop: O(log k)