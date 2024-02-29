class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        
        carry = '0'

        while a or b or carry == '1':
            i='0'
            j = '0'
            
            if a:
                i = a[-1]
                a = a[:-1]
            if b:
                j = b[-1]
                b = b[:-1]
            k = i + j + carry
            l = '0'
            if k == '111':
                l = '1'
                carry = '1'
            elif k == '101' or k == '110' or k == '011':
                carry = '1'
            elif k == '100' or k == '010' or k == '001':
                l = '1'
                carry = '0'
            else:
                carry = '0'
            res += l
        return res[::-1]
            

                

            


