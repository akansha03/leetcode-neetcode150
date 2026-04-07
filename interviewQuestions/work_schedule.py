# input = "???8???" output = 888

def findSchedules(workHours, dayHours, pattern):

    result = []
    def helper(index, total, temp_str):

        if index == len(pattern):
            if total == workHours:
                result.append(temp_str)
            return

        if pattern[index] != '?':
            helper(index+1, total + int(pattern[index]), temp_str+pattern[index])

        else:
            for hours in range(0, dayHours+1):
                if total+hours <= workHours:
                    helper(index+1, total+hours, temp_str + str(hours))

    helper(0, 0, '')
    return result

print(findSchedules(24, 4, "08??840"))


