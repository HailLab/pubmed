Pull data from pubmed for pubmed ids (in pmdis.txt). Then extract data.

Setup:

    conda create -n pubmed-env python=3.9
    mkdir data

Get going:

    conda active pubmed-env
    export OPENAI_API_KEY=
    pip install -r requirements.txt

Pull down files -- update `get_pmid_to_paths` to choose which files to use.

Files will be pulled down as pdf or tar.gz.

    python pull.py

To extract data, run:

    python extract.py

You can update the `model` and `prompt` to test.

The extract script creates a output.txt file.
