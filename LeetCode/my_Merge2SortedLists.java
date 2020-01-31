public class MergeTwoSortedLists {
  public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {val = x;}
  }

  public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode n = dummyHead; // Remember this pointer
    while (l1 != null && l2 != null) {
      if (l1.val < l2.val) {
        n.next = l1; // Append dummyHead
        l1 = l1.next; // Update l1 
      } else {
        n.next = l2;
        l2 = l2.next;
      }
      // Now after upper logic, n got some values, need to update n
      n = n.next;
    }
    // One of the list get null which means it is the end of the list, as the prerequiste, all sorted list, we can directly put unfinished segment to the end of the dummy.
    if (l1 != null) n.next = l1;
    if (l2 != null) n.next = l2;
    return dummyHead.next; // dummyHead itself is just non-sense 0, dummyHead.next is the result. 
  }
}
