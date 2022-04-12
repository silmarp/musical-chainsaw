#! /usr/bin/env python

def valida_cdvpy(cdvpy):
    
    if type(cdvpy) != str:    #type == str
        return False
    elif not(cdvpy.isdigit()):    #digits 0-9 only
        return False
    elif len(cdvpy) != 6:   #length == 6
        return False
    elif cdvpy[0] == "0":    #first digit != 0
        return False


    for i in range(5): 
        counter = 0
        for j in range(5):
            if cdvpy[i:i+2] == cdvpy[j:j+2]:
                counter+=1
        if counter > 1:
            return False


    return True



if __name__ == '__main__':
    cdvpy = input('Digite um CDvPy:')
    print(valida_cdvpy(cdvpy))
