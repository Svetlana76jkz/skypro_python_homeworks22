class StringUtils:
    
    def capitilize(self, string):
        return string.capitalize()
    
    def trim(self, string):
        whitespace = " "
        while (string.startswith(whitespace)):
            string = string.removeprefix(whitespace)
        return string
    
    def to_list(self, string, delimeter):
        if(self.is_empty(string)):
            return []
        
        return string.split(delimeter)

    def contains(self, string, symbol):
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass

        return res
    
    def delete_symbol(self, string, symbol):
        if(self.contains(string, symbol)):
            string = string.replace(symbol, "")    
        return string
    
    def starts_with(self, string, symbol):
        return string.startswith(symbol)
    
    def end_with(self, string, symbol):
        return string.endswith(symbol)
    
    def is_empty(self, string):
        string = self.trim(string)
        return string == ""
    
    def list_to_string(self, lst: list, joiner=", ") -> str:
        
        string = ""
        length = len(lst)
        
        if length == 0: 
            return string 
        
        for i in range(0, length-1):
            string += str(lst[i]) + joiner
        
        return string + str(lst[-1])