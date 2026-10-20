# Problem: Daily Temperatures (NeetCode 18) 
# Category: Stack (Monotonic Decreasing Stack) 
# Time Complexity: O(N) - Linear time; each element is pushed and popped from the stack at most once 
# Space Complexity: O(N) - Linear space auxiliary allocation for the monotonic stack and output array

class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        output = [0] * len(t)

        for i in range(len(t)):
            current_temp = t[i]

            while stack and current_temp > stack[-1][0]:
                pop_temp, pop_index = stack.pop()
                output[pop_index] = i - pop_index
                
            stack.append([current_temp, i])

        return output
