/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func isPalindrome(head *ListNode) bool {
    
    var result string
    var reverse string
    var node *ListNode = head
    
    for node != nil {
        result = result + strconv.Itoa(node.Val)
        reverse = strconv.Itoa(node.Val) + reverse
        node = node.Next
    }
    
    return result == reverse
}