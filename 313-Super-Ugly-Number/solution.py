class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        nums = []
        idxes = []
        for dummy_num in primes:
            nums.append(1)
            idxes.append(0)
        cur_best = [1]
        cur = cur_best[0]
        for dummy_num in range(n-1):
            for i in range(len(nums)):
                if nums[i] == cur:
                    nums[i] = cur_best[idxes[i]] * primes[i]
                    idxes[i] += 1
            cur = min(nums)
            cur_best.append(cur)
        return cur_best[-1]
        