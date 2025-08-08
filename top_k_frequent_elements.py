class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        ans=[]
        sorted_dict = dict(sorted(d.items(),key=lambda item: item[1], reverse=True))
        for i in sorted_dict.keys():
            if k>0:
                k-=1
                ans.append(i)
        return ans