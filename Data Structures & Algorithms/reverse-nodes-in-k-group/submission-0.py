class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       # 1. need a dummy node to point to head so we can return the "start" later
       # 2. in a regular reversal, we init prev to None, cuz we want the "last element" tbe None. Here, we want the last 
       #     elemetent to be the start of the next group
       # 3. in a regular reveral, we loop as long is cur is valid. here, we need to stop after k so while cur != node at the start
       #    of the next group
       # 4. at the end of the loop, "group_prev" is in a wrong state cuz it now points to the "end" of the list (previoulsy, the start) instead of the start
       #     we need to connect "group_prev" to the new "start" (i.e. the end, kth node) and then reset "group_prev" to the actual
       #     group_prev for the next group

        dummy = ListNode(0, head)
        group_prev = dummy

        def getKthNode(node, k): # if this returns None, there were not enough nodes for the group
            while node and k:
                node = node.next
                k -= 1
        
            return node

        while True:
            kth = getKthNode(group_prev, k)
            if not kth: break # not enough to reverse

            group_next = kth.next # first element of next group

            cur = group_prev.next
            prev = group_next # we want the end the reversed group to attach to the start of the next group

            while cur != group_next: # reverse only k
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # need to reconnect group_prev to the other end, and set group_prev for the next reversal
            temp = group_prev.next
            group_prev.next = kth # attach group_prev to the new "start" i.e. the kth node
            group_prev = temp # set group_prev to thr right spot for the next reversal

        
        return dummy.next