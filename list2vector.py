# coding=utf-8

# Convert list which is represented in text form to vector(initial by C++ code)
class list2vector():
    def __init__(self):
        pass
    # Int list to int vector    
    def int2int(self, input_list):
        input_list_str = '{' + str(input_list).strip('[').strip(']') + '}'
        print 'int n[%d] = %s;'%(len(input_list), input_list_str)
        print 'vector<int> v(n, n+%d);' %(len(input_list))
        
        
if __name__ == "__main__":
    input_list = [27,2,-32,38]
    convetr = list2vector()
    convetr.int2int(input_list)
