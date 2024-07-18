class Solution:
    def numDistinct(self,s:str, t:str)-> int:
        target_map = {}
        for l in t:
            if l in target_map:
                target_map[l]+=1
            else:
                target_map[l]=1

        input_map = {}
        for l in s:
            if l in input_map:
                input_map[l]+=1
            else:
                input_map[l]=1
        count = 0
        if all(key in target_map for key in input_map):
            for key in target_map.keys():
                if target_map[key] > input_map[key]:
                    return 0
            count+=1
            for key in target_map.keys():
                left_over = (input_map[key] - target_map[key]) * target_map[key]
                if left_over>0:
                    count+= left_over
        return count


if __name__ == "__main__":
    print(Solution.numDistinct('',"aabb", 'ab'))