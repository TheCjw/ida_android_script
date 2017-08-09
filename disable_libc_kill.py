#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: TheCjw<thecjw@live.com>
# Created on 11:08 2016/1/2

__author__ = "TheCjw"

from idaapi import *


class DisableKill(DBG_Hooks):
    def __init__(self):
        DBG_Hooks.__init__(self)
        self.function_libc_kill = LocByName("kill")
        if self.function_libc_kill != BADADDR:
            AddBpt(self.function_libc_kill)

    def dbg_bpt(self, tid, ea):
        if ea == self.function_libc_kill:
            r0 = GetRegValue("R0")
            if r0 == tid:
                lr = GetRegValue("LR")
                print "lr:", hex(lr)
                SetRegValue(lr, "PC")
                idaapi.continue_process()
        return 0


# Remove an existing debug hook
try:
    if debughook:
        print("Removing previous hook ...")
        debughook.unhook()
except:
    pass

# Install the debug hook
debughook = DisableKill()
debughook.hook()
debughook.steps = 0
