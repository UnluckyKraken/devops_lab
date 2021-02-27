#!/usr/bin/env python

import psutil
import time


class snap_outputs:

    def __init__(self, n=1):
        self.n = n
        self.timestamp = time.ctime()
        self.cpu = psutil.cpu_percent(interval=1)
        self.disk = psutil.disk_usage('/')
        self.mem = psutil.virtual_memory()
        self.disk_io = psutil.disk_io_counters()
        self.net = psutil.net_io_counters()

    def convert(self, value):
        value = value // 1024 // 1024
        return value

    def out_plain(self):
        text = """SNAPSHOT{0}: {1}:
          CPU load(%): {2}
          Memory usage(MB): total={3}, used={4}, free={5}
          Virtual memory usage(MB): total={6}, used={7}, free={8}
          IO(MB): read={9}, write={10}
          Network(MB): sent={11}, recieved={12}"""
        text = text.format(self.n, self.timestamp, self.cpu,
                           self.convert(self.disk.total),
                           self.convert(self.disk.used),
                           self.convert(self.disk.free),
                           self.convert(self.mem.total),
                           self.convert(self.mem.used),
                           self.convert(self.mem.free),
                           self.convert(self.disk_io.read_bytes),
                           self.convert(self.disk_io.write_bytes),
                           self.convert(self.net.bytes_sent),
                           self.convert(self.net.bytes_recv))
        return text

    def out_json(self):
        text = """
            "SNAPSHOT{0}: {1}":[
                #
                "CPU load(%)": "{2}",
                "Memory usage(MB)": "total={3}, used={4}, free={5}",
                "Virtual memory usage(MB)": "total={6}, used={7}, free={8}",
                "IO(MB)": "read={9}, write={10}",
                "Network(MB)": "sent={11}, recieved={12}"
                $
            ]
        """
        text = text.format(self.n, self.timestamp, self.cpu,
                           self.convert(self.disk.total),
                           self.convert(self.disk.used),
                           self.convert(self.disk.free),
                           self.convert(self.mem.total),
                           self.convert(self.mem.used),
                           self.convert(self.mem.free),
                           self.convert(self.disk_io.read_bytes),
                           self.convert(self.disk_io.write_bytes),
                           self.convert(self.net.bytes_sent),
                           self.convert(self.net.bytes_recv))
        text = text.replace("#", "{")
        text = text.replace("$", "}")
        return text
