class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # ct = 0
        # numbers=[1,5,9,10]
        # target=11
        ln = len(numbers)
        post2 = ln
        for i in range(ln):
            x = numbers[i]
            post1 = i
            rest = target - x
            if rest < x:
                continue
            post2 = ln//2
            post1 = post2
            # print(f"this is i: {i}")
            # print(f"this is x: {x}")
            # print(f"this is rest: {rest}")
            # print(f"this is post2: {post2}")
            if rest > numbers[ln-1]:
                continue
            if rest > numbers[post2]:
                while rest > numbers[post2]:
                    post1 = post2
                    post2 = post2 + (ln - post2+1)//2
                    # post2 = max((ln - post2)//2+1,post1+1)
                    # print(post2)
                    # ct +=1
            elif rest == numbers[post2]:
                return [i+1, post2+1]
            else:
                while rest < numbers[post1]:# and ct < 10:
                    post2 = post1
                    post1 = post1//2
                    # print(post1)
                    # ct+=1


            for j in range(post1, post2+1):
                y = numbers[j]
                
                if x + y == target:
                    return [i+1,j+1]
                
            