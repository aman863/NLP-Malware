
import os
import glob
from subprocess import check_call
import sys
import argparse
from context import cd



parser = argparse.ArgumentParser(description="pre-process dataset")
parser.add_argument("-x", "--prefix", default=None, 
        help="specify the prefix to add to all the pcap filenames")
parser.add_argument("-f", "--folder", default=None,
        help="specify the folder to look for dataset")

args = parser.parse_args()

if args.prefix:
    pre_name = args.prefix
else:
    print("ERROR! Missing prefix.")
    parser.print_help()
    exit()
if args.folder:
    f_name = args.folder
else:
    print("ERROR! Missing folder.")
    parser.print_help()
    exit()


with cd(f_name):
    for zipped_file_name in glob.glob(os.path.join(os.getcwd(), "*.7z")):
        print("--> start to process 7z_file: [%s]"%(zipped_file_name))
        cmd = "p7zip -k -d %s" % (zipped_file_name)
        check_call(cmd, shell=True)

with cd(f_name):
    for pcap_file_name in glob.glob(os.path.join(os.getcwd(), "*.pcap")):
        print("--> start to process pcap_file: [%s]" % (pcap_file_name))
        new_pcap_file_name = "/".join(pcap_file_name.rsplit('/')[:-1]) + "/" + pre_name + "_" + pcap_file_name.rsplit('/')[-1]
        #print(new_pcap_file_name)
        cmd = "mv %s %s" % (pcap_file_name, new_pcap_file_name)
        check_call(cmd, shell=True)
