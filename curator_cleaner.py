import os,subprocess

curator_dir = '/root/.curator/'
list_file = '/root/curator_list'
curator_logs = '/root/curator.log'


def write_curator_list():
    os.system("cd {} ; ls -l *.yml | grep -v total | grep -v curator.yml | awk '{{print $9}}' > {}".format(curator_dir, list_file))

def run_curator_confs():
    with open(list_file , 'r') as f:
        content = f.readlines()
        for line in content:
            os.system('curator {}{} > {}'.format(curator_dir, line, curator_logs))


write_curator_list()
run_curator_confs()