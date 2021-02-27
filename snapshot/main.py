#!/usr/bin/env python

import time
import os.path
import argparse
from snapshot.outputs import snap_outputs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=str, default="txt")
    parser.add_argument("--timer", type=int, default=300)
    args = parser.parse_args()

    counter = 0
    while True:
        counter += 1
        if args.output == "json":
            file_extension = "json"
            output_format = snap_outputs(n=counter).out_json()
        elif args.output == "txt":
            file_extension = "txt"
            output_format = snap_outputs(n=counter).out_plain()

        if os.path.isfile("snapshots.{0}".format(file_extension)):
            f = open("snapshots.{0}".format(file_extension), "a")
            if file_extension == "json":
                f.write("{")
            f.write(output_format + "\n")
            f.close()
            time.sleep(args.timer)
        else:
            f = open("snapshots.{0}".format(file_extension), "w")
            f.write(output_format + "\n")
            f.close()
            time.sleep(args.timer)


if __name__ == "__main__":
    main()
