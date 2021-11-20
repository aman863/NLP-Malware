#!/usr/bin/env python

from __future__ import print_function, division
from p2flib import *
from f2nlib import *
import os

def loop_folder(folder_name, time_out, no_words):

    import glob
    pcap_inputs = []
    for pcap_file_name in glob.glob( os.path.join(folder_name, '*.pcap') ):
        print("--> start to process pcap_file_nam: [%s]"%(pcap_file_name))
        pcap2words(pcap_file_name, pcap_file_name.rsplit('.pcap')[0] + ".words", time_out)
        words2ngram(pcap_file_name.rsplit('.pcap')[0] + ".words", 
		pcap_file_name.rsplit('.pcap')[0] + "ngram.csv", int(no_words))

if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='convert txt file to flows')
    parser.add_argument('-p', '--pcap', default=None,
            help='specify the pcap file you want to process')
    parser.add_argument('-f', '--folder', default=None,
            help='specify the folder you want to loop through')

    parser.add_argument('-t', '--time_out', default=10, type=float,
            help='time out time')

    parser.add_argument('-n', '--no_words', default=3,
            help='specify the number of words in a n-gram')

    args = parser.parse_args()

    if args.pcap:
        pcap2words(args.pcap, args.pcap.rsplit('.pcap')[0] + '.words', args.time_out)
        words2ngram(args.pcap.rsplit('.pcap')[0] + ".words",
                args.pcap.rsplit('.pcap')[0] + "ngram.csv", int(args.no_words))
    elif args.folder:
        loop_folder(args.folder, args.time_out, args.no_words)
    else:
        parser.print_help()
