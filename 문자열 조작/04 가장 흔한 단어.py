# https://leetcode.com/problems/most-common-word/


import re
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = [
            p
            for p in re.sub("[^\w]", " ", paragraph.lower()).split()
            if p not in banned
        ]
        return collections.Counter(paragraph).most_common(1)[0][0]
