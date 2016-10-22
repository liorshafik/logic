def my_xor(bin1,bin2):
    if bin1 == bin2:
        return 0
    else:
        return 1
        
def lfsr_3(reg3_init):
    new_reg = [reg3_init[2],my_xor(reg3_init[0],reg3_init[2]),reg3_init[1]]
    return new_reg 
        
        
        
def my_reg(n): 
    if n == 3:
        # p(x)=X^3 + x + 1
        reg_seq = [[1,1,1],[1,0,1],[1,0,0],[0,1,0],[0,0,1],[1,1,0],[0,1,1]]
        reg_format = [1,1,1]
        nreg = [reg_format]

        for i in range(6):
            reg_format = lfsr_3(reg_format)
            nreg.append(reg_format)
           
        
        print(nreg)
        
        if nreg == reg_seq: 
            print("alufa!")
        else:
            print("uuuuhhh")
        

                
                
