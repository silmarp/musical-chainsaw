#! /usr/bin/env python

def valida_cdvpy(cdvpy):
    raise NotImplementedError

if __name__ == '__main__':
    cdvpy = input('Digite um CDvPy:')
    print(valida_cdvpy(cdvpy))