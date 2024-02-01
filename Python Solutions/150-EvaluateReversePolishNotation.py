class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        arr = []
        symbols = set(["+", "-", "/", "*"])
        for token in tokens:
            if token not in symbols:
                arr.append(int(token))
            else:
                num2 = arr.pop()
                num1 = arr.pop()
                
                # Perform the correct operation
                if token == "+":
                    arr.append(num1 + num2)
                elif token == "-":
                    arr.append(num1 - num2)
                elif token == "/":
                    # Handle negative division
                    arr.append(int(float(num1) / num2))
                elif token == "*":
                    arr.append(num1 * num2)
                    
        return arr[0]
