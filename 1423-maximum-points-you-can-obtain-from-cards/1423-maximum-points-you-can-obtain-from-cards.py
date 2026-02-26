class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsm=rsm=maxi=0
        lsm=sum(cardPoints[:k])
        rd=len(cardPoints)-1
        maxi=lsm
        for i in range(k-1,-1,-1):
            lsm=lsm-cardPoints[i]
            rsm+=cardPoints[rd]
            rd-=1
            maxi=max(maxi,lsm+rsm)
        return maxi