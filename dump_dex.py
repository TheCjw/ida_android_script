__author__ = "TheCjw"

import idaapi
import struct


def main():
    start_address = 0x63A79034
    # check valid dex header.
    header = idaapi.dbg_read_memory(start_address, 0x08)
    if header == "\x64\x65\x78\x0A\x30\x33\x35\x00":
        dex_size = idaapi.dbg_read_memory(start_address + 0x20, 0x04)
        file_size = struct.unpack("i", dex_size)[0]
        dex_data = idaapi.dbg_read_memory(start_address, file_size)
        file_name = "%s_%08x_%08x.dex" % (GetIdbPath()[:-4], start_address, file_size)
        file_out = open(file_name, "wb")
        file_out.write(dex_data)
        file_out.close()
        print "Writing buffer %0x(%x) to %s" % (start_address, file_size, file_name)
    else:
        print "Invalid dex header."


if __name__ == "__main__":
    main()