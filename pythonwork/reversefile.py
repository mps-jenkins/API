from os import fsync
import mmap


def reverse(fw_file_path, bw_file_path):
    with open(fw_file_path, 'rb')as fw_file:
        fw_file_map = mmap.mmap(fw_file.fileno(), 0, access=mmap.ACCESS_READ)
        with open(bw_file_path, "wb") as bw_file:
            bw_file.write(''.join([c for c in reversed(fw_file_map)]))
            bw_file.flush()
            fsync(bw_file.fileno())
        fw_file_map.close()


reverse("/home/s.verma1/Documents/file.in", "/home/s.verma1/Documents/file.out")