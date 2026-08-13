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