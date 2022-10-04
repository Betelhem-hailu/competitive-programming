class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        List = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                List.insert(i, "FizzBuzz")
            elif i % 3 == 0:
                List.insert(i, "Fizz")
            elif i % 5 == 0:
                List.insert(i, "Buzz")
            else:
                List.insert(i, str(i))
        return List
