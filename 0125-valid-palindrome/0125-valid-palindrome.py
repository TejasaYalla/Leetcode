class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=''.join(ch for ch in s if ch.isalnum())
        return new.lower()==new[::-1].lower()