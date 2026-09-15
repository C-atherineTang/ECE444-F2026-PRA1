class utils:

    def reversed(self, number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        
        #[start:end:step] start default end - end default before beginning 
        # step negative - backward 
        return int(str(number)[::-1])

    def formatter(self, number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")

        return bin(number), oct(number)