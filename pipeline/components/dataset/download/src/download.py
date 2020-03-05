#!/usr/bin/env python3
import argparse
from pathlib import Path

import svn.remote

def download_dataset(repository, path, output_path):
  url = '{}/trunk/{}'.format(repository, path)
  r = svn.remote.RemoteClient(url)
  r.export(output_path, force=True)
  print(r.info())


parser = argparse.ArgumentParser(description='Dataset downloader')
parser.add_argument('--repository',
                    type=str,
                    default='https://github.com/ajchili/autoRMZ.git',
                    help='Github repository to download data from.')
parser.add_argument('--path',
                    type=str,
                    default='dataset',
                    help='Path in repository where data should be downloaded from.')
parser.add_argument('--output-path',
                    type=str,
                    help='Path where dataset should be saved to.')
args = parser.parse_args()

Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)

download_dataset(args.repository, args.path, args.output_path)