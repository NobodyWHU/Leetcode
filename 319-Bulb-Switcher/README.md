Math Problem
When all the loop is done, only numbers a^2 which satisfy a<=n&&a^2<=n will be 1, other digits are all flipped to zero, for if a digit wants to remain 1, it must flip twice. for example, n=5 loop k: 2^2<=5,so only digit 4 flips twice, digit 2 and digit 3 and digit 5 only flips once. The last digit also satisfies this. So sqrt(n) means what is the max digit(assume it is a) that satisfies a^2<=n? This 'a' is just what we want.

[链接](https://leetcode.com/discuss/98625/explain-for-int-sqrt-n-method)