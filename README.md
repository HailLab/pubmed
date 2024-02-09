Pull data from pubmed for pubmed ids (in pmdis.txt). Then extract data.

Setup:

    conda create -n pubmed-env python=3.9
    mkdir data

Download FTP info - Got to https://ftp.ncbi.nlm.nih.gov/pub/pmc/ and download csv files such as:

    oa_comm_use_file_list.csv 
    oa_non_comm_use_pdf.csv
    oa_file_list.csv

Create a file pmids.txt that has the pubmed IDs of files you want to download. Eg

    PMID
    15561572
    18590331
    19727526
    26373842

Get going:

    conda activate pubmed-env
    export OPENAI_API_KEY=
    pip install -r requirements.txt

Pull down files -- update `get_pmid_to_paths` to choose which files to use (from csv files above).

Files will be pulled down as pdf or tar.gz in the data directory.

    python pull.py

To extract data, run:

    python extract.py

This currently only processes pdf files in the data directory.

You can update the `model` and `prompt` to test.

The extract script creates an output.txt file.
