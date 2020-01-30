public class ValidateBinaryTree {
  public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; } // Constructor assign value
  }

  // 2nd solution prev to record previous node
  private TreeNode prev = null;

  public boolean isValidBST(TreeNode root) {
    // return validate(root, Integer.MIN_VALUE, Integer.MAX_VALUE); //int low is not allow null
    // return validate(root, null, null); // 1st solution
    return isIncreasing(root, 0, "root");  
  }

  // 1st solution
  private boolean validate(TreeNode n, Integer low, Integer high) {
    if (n == null) return true;
    // n.val: Current value
    return (low == null || n.val > low) && (high == null || n.val < high) && validate(n.left, low, n.val) && validate(n.right, n.val, high);
  }

  // 2nd solution
  private boolean isIncreasing(TreeNode n, int stack, String d) {
    System.out.println("stack: " + stack + " direction: " + d);
    if (n != null) {
      System.out.println("n.val: " + n.val);
    } else {
      System.out.println("null");
    }
    System.out.println("====");

    // If n now is the end of node, we can return true
    if (n == null) return true;
  
    if (isIncreasing(n.left, stack + 1, "left")) { // Keep finding left node
      // If current value <= previous value then false, because we compare from left(smaller) to right
      // reason "=" is that in BST, we don't have the same value in each node
      if (prev != null && n.val <= prev.val) return false;
      prev = n; // Update prev to not null
      return isIncreasing(n.right, stack + 1, "right"); // Finish left, here is right  
    }
    return false; // make sure this function return
  }
}
