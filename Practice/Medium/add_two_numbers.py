
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        result = None
        r1 = None

        p_carry = 0

        n1 = l1
        n2 = l2
        while n1 != None or n2 != None:

            if n1 == None:
                carry, ones = add(0, n2.val, p_carry)
                n2 = n2.next
                p_carry = 0
            elif n2 == None:
                carry, ones = add(n1.val, 0, p_carry)
                n1 = n1.next
                p_carry = 0
            else:
                carry, ones = add(n1.val, n2.val, p_carry)
                n1 = n1.next
                n2 = n2.next

            # print("Carry: {}, Ones: {}".format(carry, ones))

            if result == None:
                result = ListNode(ones, None)
                r1 = result
            else:
                r1.next = ListNode(ones, None)
                r1 = r1.next
                p_carry = 0
            
            p_carry = carry

        if p_carry != 0:
            r1.next = ListNode(p_carry, None)

        return result

def add(d1, d2, pc):
    result = d1 + d2 + pc
    return (result // 10), (result % 10)

def print_list(n_list):

    print("Number Reversed:")

    node = n_list
    while not(node is None):
        print(node.val)
        node = node.next

    print()

def to_linked_list(n_list):
    root = None
    r = None
    for i in n_list:
        if root == None:
            root = ListNode(i, None)
            r = root
            continue

        r.next = ListNode(i, None)
        r = r.next

    return root

if __name__ == "__main__":

    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]

    ll1 = to_linked_list(l1)
    ll2 = to_linked_list(l2)

    sol = Solution()

    r1 = sol.addTwoNumbers(ll1, ll2)

    print_list(r1)