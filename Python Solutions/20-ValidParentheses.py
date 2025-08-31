class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []

        for bracket in s:
            # Check if stack is empty
            if not stack:
                # Add the current item to stack
                stack.append(bracket)
                continue

            # Check if opening type

            if bracket in ["(", "[", "{"]:
                stack.append(bracket)
                continue
            # Check if closing type
            else:
                top = stack.pop()
                # Check if type matches the same as top 
                if ( bracket == ")" and top == "(" ) or ( bracket == "}" and top == "{" ) or ( bracket == "]" and top == "[" ) :
                    # Valid check
                    continue
                else:
                    return False

        # Check if stack is empty
        return not stack