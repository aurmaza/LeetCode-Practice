class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            # Gets bit at index i
                #First, right shift the bit i times
                #This gives us a binary number where i is the
                #least significant bit 
                    #IE: 0000 1010 
                    #i = 1
                    #Will shift  to 0000 0101
                #Then, & the entire number with 1
                #This gives the value of the LSB
                #All the other numbers will be set to zero left of the i value
                #ie
                # 0000 0101
                # & 
                # 0000 0001
                # --
                # 0000 0001
                #Store this value in bit
            bit = (n>>i) & 1

            # Sets the bit at index 31-i
                # (bit<< (31 - i))
                    # Left shifts the extracted bit to its correct position
                    # 0000 0001 << 7 - 0 = 7
                    # goes to
                    # 1000 0000
                    # As it removes the 7 zeros
                    # Sets the bitwise position to its correct place in res
                    # without affecting other bits
            res = res | (bit << (31-i))
        return res