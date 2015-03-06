#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: TheCjw<thecjw@qq.com>
# Created on 10:19 2015/3/6

__author__ = "TheCjw"

import os

import idaapi


def main():
    address = AskAddr(BADADDR, "Enter address: ")
    if address == BADADDR:
        print "Invalid address."
        return

    size = AskLong(0, "Enter size: ")

    if size == 0:
        print "Invalid size."
        return

    print "Range: ", hex(address), hex(size)

    buffer = idaapi.dbg_read_memory(address, size)
    if (len(buffer)) != 0:
        output_file = os.path.join(os.path.dirname(GetIdbPath()), "dump_%08x_%08x.bin" % (address, size))

        with open(output_file, "wb") as f:
            f.write(buffer)
            print "Saved data success", output_file


if __name__ == "__main__":
    main()
