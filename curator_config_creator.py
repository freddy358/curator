import os,subprocess

curator_dir = '.'
indices_file = './indices.txt'
indices_name = './uniq_indices_names.txt'

config_file = './template.yml'


def write_indices():
    os.system("cd {} ; curator_cli show_indices > {} ".format(curator_dir, indices_file))

def run_curator_confs():
    with open(indices_file , 'r') as f:
        content = f.readlines()
        for line in content:
            os.system("cut -d '_' -f 1 {} | grep -iEv ^20[2-9][0-9]-[0-1][0-9]-[0-3][0-9] | grep -iEv '\.' | uniq > {}".format(indices_file, indices_name))
    with open(indices_name , 'r') as f:
        content = f.readlines()
        content = [line.replace('\n', '')for line in content]
        for line in content:
            os.system('sed "s/var_value/{}/g" {} > {}.yml'.format(line, config_file, line))




write_indices()
run_curator_confs()
