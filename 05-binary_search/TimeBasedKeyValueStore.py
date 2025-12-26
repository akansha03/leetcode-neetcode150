"""
Problem: [Time Based Key-Value Store]
Link: https://leetcode.com/problems/time-based-key-value-store/description/
Difficulty: [Medium]
Topics: [List, Binary Search, Dictionary]

Pattern: [Binary Search]
Key Insight:
* First intuition, was to take a dictionary as key value is involved and map value and timestamp to key.
* So a default dictionary with list is used to store the data.
* And, since the query was to search for a value based on the key and timestamp then list is in strictly increasing
order, in this case binary search would be great.
* In case there is no matching timestamp, then the immediate lesser one would be considered for result. To make
this work - I added a time variable to store the value of mid when timestamp is greater than the mid.
* If time is updated then get that value from the list and return it to the user.

Time Complexity: O(log n)
Space Complexity: O(m * n) : m being the number of keys and value being the list of timestamp and value

Solved: [25/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        self.timestore = defaultdict(list)

    def set(self, key, value, timestamp):
        self.timestore[key].append((timestamp, value))

    def get(self, key, timestamp):
        times = self.timestore[key]
        time = -1
        low, high = 0, len(times)-1
        while low<=high:
            mid = (low + high)//2
            if times[mid][0] == timestamp:
                return times[mid][1]
            elif timestamp < times[mid][0]:
                high = mid-1
            else:
                time = mid
                low = mid+1
        value = ""
        if time != -1:
            value = times[time][1]
        return value

if __name__ == "__main__":
    sol = TimeMap()
    instructions = ["set", "get", "get", "set", "get", "get"]
    inputs = [["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    outputs = [None, "bar", "bar", None, "bar2", "bar2"]
    for i, instruction in enumerate(instructions):
        if instruction == 'set':
            sol.set(inputs[i][0], inputs[i][1], inputs[i][2])
        else:
            assert sol.get(inputs[i][0], inputs[i][1]) == outputs[i]
    print("✅ All tests passed!")