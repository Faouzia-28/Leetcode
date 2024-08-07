class Solution:
    def interpret(self, command: str) -> str:
        # Initialize an empty result list to store the interpreted parts
        result = []
        
        # Initialize an index to traverse the command string
        i = 0
        
        while i < len(command):
            if command[i] == 'G':
                # If the character is 'G', append 'G' to the result
                result.append('G')
                i += 1
            elif command[i:i+2] == '()':
                # If the substring is '()', append 'o' to the result
                result.append('o')
                i += 2
            elif command[i:i+4] == '(al)':
                # If the substring is '(al)', append 'al' to the result
                result.append('al')
                i += 4
        
        # Join the list into a string and return it
        return ''.join(result)

# Example usage
solution = Solution()
print(solution.interpret("G()(al)"))         # Output: "Goal"
print(solution.interpret("G()()()()(al)"))   # Output: "Gooooal"
print(solution.interpret("(al)G(al)()()G"))  # Output: "alGalooG"