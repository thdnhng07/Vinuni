# Get input and reverse the string
inp = input()
inp_rev = inp[:: - 1]

# Check if input is palindrome
def is_palindrome(text):
    
    if text == inp_rev:
        return True
    else:
        return False
    
print(is_palindrome(inp))