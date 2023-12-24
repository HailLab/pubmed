import requests
from bs4 import BeautifulSoup
from ftplib import FTP
import os
import tarfile
import csv

def main():
    pmid_to_path = {}
    get_pmid_to_paths("oa_file_list.csv", pmid_to_path)
    #get_pmid_to_paths("oa_non_comm_use_pdf.csv", pmid_to_path)
    print("map done")

    f = open("pmids.txt")
    pmids = f.readlines()
    f.close()

    for line in pmids:
        pmid = line.strip() 
        if pmid in pmid_to_path:
            print("-- Got", pmid)
            process_pmid(pmid, pmid_to_path[pmid])
        else:
            print("No match for", pmid)

def get_pmid_to_paths(file_name, pmid_to_path):
    print(f"getting paths for {file_name}")
    f = open(file_name)
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=',')
        for line in reader:
            try:
                path = line[0]
                pmid = line[4]
                #print(path, pmid)
            except Exception as e:
                print(e)
                continue

            if len(pmid) == 0:
                continue

            if pmid in pmid_to_path:
                print("uhhhh", pmid, path)
                continue

            pmid_to_path[pmid] = path
     
def download_file(ftp_server, ftp_path, local_path):
    with FTP(ftp_server) as ftp:
        ftp.login()
        with open('data/' + local_path, 'wb') as file:
            ftp.retrbinary('RETR ' + ftp_path, file.write)
        
        if '.pdf' in local_path:
            pass
        else:
            with tarfile.open('data/' + local_path, 'r:gz') as tar:
                extract_to = 'data/'
                tar.extractall(path=extract_to)

def process_pmid(pmid, path_to_file):
    ftp_base_url = 'ftp.ncbi.nlm.nih.gov'
    fpt_pre_path = 'pub/pmc/'
    ftp_file_path = fpt_pre_path + path_to_file
    if '.pdf' in os.path.basename(path_to_file):
        write_path = pmid + '.pdf'
    else:
        write_path = pmid + '.tar.gz'

    download_file(ftp_base_url, ftp_file_path, write_path)

if __name__ == "__main__":
    main()
