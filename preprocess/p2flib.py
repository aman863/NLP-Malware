from __future__ import print_function, division
from subprocess import check_call

def parse_records_tshark(f_name):
    records = []
    NAME = ['start_time', 'src_ip', 'dst_ip', 'protocol', 'length',
            'src_port', 'dst_port']
    with open(f_name, 'r') as infile:
        for line in infile:
            line = line.strip()
            items = line.split()
            try:
                rec = (float(items[1]), items[2], items[4], items[5], items[6],
                    int(items[7]), int(items[8]))
                records.append(rec)
            except:
                rec = ()
    return records, NAME

def export_to_txt(f_name, txt_f_name):

    cmd = """tshark -o gui.column.format:'"No.", "%%m", "Time", "%%t", "Source", "%%s", "Destination", "%%d", "Protocol", "%%p", "len", "%%L", "srcport", "%%uS", "dstport", "%%uD"' -r %s > %s""" % (f_name, txt_f_name)

    print('--> ', cmd)
    check_call(cmd, shell=True)

def change_to_words(records, name, time_out):

    words = []
    print(name)
    req_tuple_seq = [name.index(k) for k in ['src_port', 'protocol',
        'dst_port', 'length']]
    for rec in records:
        data_tuple = tuple(str(rec[seq]) for seq in req_tuple_seq)
        word = "".join(data_tuple)
        words.append(word)
    return words

def write_words(words, f_name):

    fid = open(f_name, 'w')
    for w in words:
        fid.write(w + ' ')
    fid.close()

def pcap2words(pcap_file_name, words_file_name, time_out):

    txt_f_name = pcap_file_name.rsplit('.pcap')[0] + '_tshark.txt'
    export_to_txt(pcap_file_name, txt_f_name)
    records, name = parse_records_tshark(txt_f_name)
    words = change_to_words(records, name, time_out)
    write_words(words, words_file_name)
