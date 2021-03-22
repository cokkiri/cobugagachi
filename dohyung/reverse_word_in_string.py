"""https://leetcode.com/problems/reverse-words-in-a-string
Reverse words in string

Example
--
Input: s = "the sky is blue"
Output: "blue is sky the"
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """Reverse words

        Args:
            s (str): a string for reverse

        Returns:
            str: reversed string
        """
        return " ".join(s.strip().split()[::-1])
