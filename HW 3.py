#%%
def is_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

    return True

print(is_palindrome("racecar"))  
print(is_palindrome("python"))

# %%
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(3, 4)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
# %%
def count_words(word_list):
    word_count = {}
    
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

result = count_words(["hello", "world", "hello", "python"])
print(result)

result2 = count_words(["apple", "banana", "apple", "orange", "banana", "banana"])
print(result2)

# %%
