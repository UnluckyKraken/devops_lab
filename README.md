# Snapshot tool
It is a simple tool which writes snapshots with some of your system's statistics to a file.

## Installing
Simply clone this repository and run "pip install ." in the directory.

## Uninstalling
Just run "pip uninstall snapshot"

## Usage
Run "snapshot" in console. Script will be writing data to a snapshot.txt every 5 minutes.

Optional arguments:
--output [txt|json] - you can choose the format of the output. Default is txt.
--timer [int(sec)] - allows you to set an interval of snapshots (in seconds). Deafult is 300 sec (5 min).

Example:
snapshot --output json --timer 600

