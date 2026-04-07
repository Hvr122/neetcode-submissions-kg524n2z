class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)-1
        for i in range(len(numbers)):
            temp=target-numbers[i]
            
            l,r=i,n

            while l <=r :
                mid=(l+r)//2

                if numbers[mid]==temp:
                    return [i+1, mid+1]
                elif numbers[mid]>temp:
                    r=mid-1
                else:l=mid+1
        return []
            
