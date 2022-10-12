#!/usr/bin/env python3

import glob, os

read_path = "./train_txt_used_for_training.txt"
write_path = "./train.txt"

print("Open file ",read_path)

with open(read_path) as o:
    data_list = [line.rstrip() for line in o]

print("Convert data")
data_write = ""
for i in data_list:
    file_name = os.path.basename(i)
    file_name = "x64/Release/data/img/" + file_name
    data_write = data_write + file_name + "\n"

print("Write file ",write_path)

with open(write_path, "w") as w:
    w.write(data_write)