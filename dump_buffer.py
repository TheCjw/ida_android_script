#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: TheCjw<thecjw@live.com>
# Created on 10:19 2015/3/6

__author__ = "TheCjw"

import os
import idc


def main():
    address = AskAddr(BADADDR, "Enter address: ")
    if address is None:
        # cancel
        return

    if address == BADADDR:
        print "Invalid address."
        return

    size = AskLong(0, "Enter size: ")
    if size is None:
        # cancel
        return

    if size == 0:
        print "Invalid size."
        return

    print "Range: ", hex(address), hex(size)

    buffer = idc.GetManyBytes(address, size, True)
    if buffer is not None:
        output_file = os.path.join(os.path.dirname(GetIdbPath()), "dump_%08x_%08x.dat" % (address, size))

        with open(output_file, "wb") as f:
            f.write(buffer)
            print "Saved data success", output_file


if __name__ == "__main__":
    main()
