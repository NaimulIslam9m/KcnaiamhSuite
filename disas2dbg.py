#!/usr/bin/env python3

__description__ = 'disassembler and debugger address converter'
__author__ = 'Naimul Islam'
__version__ = '0.0.1'
__date__ = '02/08/2023'

"""
History:

Todo:
"""

def add0x(tmp):
    if tmp[:2] != "0x":
        tmp = "0x" + tmp
    return tmp

def disas2dbg():
    while True:
        try:
            disas_cur = int(add0x(input("\ndisassembler's address: ")), 16)
            diff = disas_cur - disas_base
            dbg_cur = dbg_base + diff
            print(f"dbg's address: {hex(dbg_cur)}")
        except ValueError:
            print("Invalid input. Please enter valid hexadecimal values.")
            exit

def dbg2disas():
    while True:
        try:
            dbg_cur = int(add0x(input("\ndebugger's address: ")), 16)
            diff = dbg_cur - dbg_base
            disas_cur = disas_base + diff
            print(f"disassembler's address: {hex(disas_cur)}")
        except ValueError:
            print("Invalid input. Please enter valid hexadecimal values.")
            exit

if __name__ == "__main__":

    global disas_base
    global dbg_base
    disas_base = int(add0x(input("Base address (disassembler): ")), 16)
    dbg_base = int(add0x(input("Base  address (debugger): ")), 16)

    print("Press 1 to convert disassembler's address to debugger's address.")
    print("Press 2 to convert debugger's address to disassembler's address.")
    print("Press any key to exit.")

    op = input()
    if (op == "1"):
        disas2dbg()
    elif (op == "2"):
        dbg2disas()

    print("Bye!")
