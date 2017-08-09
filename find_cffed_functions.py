#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: TheCjw<thecjw@live.com>
# Created on 16:48 2017/7/31

__author__ = "TheCjw"

from idautils import *
from idaapi import *
from idc import *


def main():
    print("An experimental idapython script to find Control-Flow-Flattened functions")

    ea = ScreenEA()
    for func_ea in Functions(SegStart(ea), SegEnd(ea)):
        func = get_func(func_ea)
        flow = FlowChart(func)
        if flow.size > 30:
            print("found susp cffed function at {0:08x}".format(func_ea))

if __name__ == "__main__":
    main()
