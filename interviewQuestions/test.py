from collections import defaultdict
from heapq import heappush, heappop
from collections import Counter

def helper(inputs):
    output = {}

    for input in inputs:
        temp = input.split(":")
        test_case, status = temp[0], temp[1]

        if test_case in output and output[test_case] == 'FAIL':
            continue

        output[test_case] = status
    return output

inputs = ["testLogin:PASS","testCart:FAIL","testSearch:PASS","testCheckout:FAIL","testCart:PASS","testLogin:FAIL"
]
#print(helper(inputs))

def execution_time(logs):
    result = {}
    start_times = {}
    for line in logs.split("\n"):
        test, action, time = line.split()
        time = int(time)
        if action == "start":
            start_times[test] = time
        else:
            result[test] = time - start_times[test]
    return result

logs = "log1 start 100\n log2 start 105 \n log1 end 110 \n log2 end 120"
print(execution_time(logs))

def frequent_failed_test(failed_test, length):
    count = defaultdict(int)
    for test in failed_test:
        count[test] += 1
    heap = []

    for k, v in count.items():
        heappush(heap, [v, k])
        while len(heap) > length:
            heappop(heap)
    result = []
    for key, value in heap:
        result.append(value)
    return result


failed_tests = ["loginTest", "cartTest", "searchTest", "loginTest", "paymentTest", "cartTest"]
result = frequent_failed_test(failed_tests, 2)
print(result)


def frequency_sorted(lst):
    count = Counter(lst)
    sorted_count = dict(sorted(count.items(), key=lambda x:x[1], reverse=True))
    return sorted_count

# Example usage
lst = ['a','b','c','c','b','b']
print(frequency_sorted(lst))