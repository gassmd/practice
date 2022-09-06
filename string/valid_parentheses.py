'''
Pseudocode

1. Create stack data structure
2. Traverse each character in input string
3. Check if c is close parentheses (in map)
4.
'''




class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")":"(", "]":"[", "}":"{"}

        for c in s:                                  # traverse string from left to right
            if c in closeToOpen:                        #if character is closing parentheses
                if stack and stack[-1] == closeToOpen[c]:   # if (stack) is not empty and last element added to stack (value at top of stack) is matching open parentheses
                    stack.pop()                                 # valid, keep going
                else:
                    return False                                # otherwise stack is invalid

            else:
                stack.append(c)                             # adds to stack

        return True if not stack else False


print(Solution().isValid("([])"))
print(Solution().isValid("{()){"))