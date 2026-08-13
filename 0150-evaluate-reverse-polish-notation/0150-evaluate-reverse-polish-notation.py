'''
class DoublyLinkedList:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
'''


class Solution:
    '''
    Simplest and most effective among other ones.. Leads to a time complexity of O(n)
    Also possible via Linked-List and Recursion
    '''

    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+','-','*','/']:
                second = stack.pop()
                first = stack.pop()
                match token:
                    case '+':
                        stack.append(first+second)
                    case '-':
                        stack.append(first-second)
                    case '*':
                        stack.append(first*second)
                    case '/':
                        stack.append(int(first/second)) # Floor Division wont work here in case of neagtive numbers (eg. 6//-132 = -1)
            else:
                stack.append(int(token))
        
        return stack[-1]
    

    '''
    Linked-List - Viable Approach but higher runtime and memory usage as compared to simple yet effective stack implementation
    '''

    '''
    def evalRPN(self, tokens: List[str]) -> int:
        head = DoublyLinkedList(tokens[0])
        curr = head

        for token in tokens[1:]:
            curr.next = DoublyLinkedList(val=token, prev=curr)
            curr = curr.next
        
        ans = float('inf')
        while head is not None:
            if head.val in "+-*/":
                first = int(head.prev.prev.val)
                second = int(head.prev.val)
                match head.val:
                    case '+':
                        res = first + second
                    case '-':
                        res = first - second
                    case '*':
                        res = first * second
                    case '/':
                        res = int(first / second) # Floor Division wont work here in case of neagtive numbers (eg. 6//-132 = -1)
                
                head.val = res
                head.prev = head.prev.prev.prev
                if head.prev is not None:
                    head.prev.next = head
            
            ans = int(head.val)
            head = head.next

        return ans
    '''