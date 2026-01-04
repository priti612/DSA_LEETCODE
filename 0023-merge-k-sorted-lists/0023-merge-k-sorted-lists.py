# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            temp=[]
            for i in range(0,len(lists),2):
                list1=lists[i]
                list2=lists[i+1] if i+1<len(lists) else None
                temp.append(self.merge_lists(list1,list2))
            lists=temp
        return lists[0]
        
    def merge_lists(self,list1,list2):
        temp=ListNode(-1)
        curr=temp
        while list1 and list2:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        if list1:
            curr.next=list1
        if list2:
            curr.next=list2
        return temp.next
        