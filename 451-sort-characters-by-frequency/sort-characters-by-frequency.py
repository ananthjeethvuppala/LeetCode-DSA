class Solution(object):
    def frequencySort(self, s):
        count = Counter(s)
        sort = sorted(count.items(), key = lambda x:x[1], reverse = True)
        result = ""
        for i,f in sort:
            result += i*f

        return result
        