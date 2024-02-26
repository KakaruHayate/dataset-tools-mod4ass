import json
import re
import csv
import os
import argparse

def ds_to_marker(ds_file, csv_file):
    sample_rate = 44100  # Sample rate is always 44100 Hz for .ds files

    with open(ds_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['Name', 'Start', 'Duration', 'Time Format', 'Type', 'Description'])

        for i, segment in enumerate(data):
            start_time = segment["offset"] * sample_rate
            duration = sum(float(x) for x in segment["ph_dur"].split()) * sample_rate
            writer.writerow([f'Marker {i}', start_time, duration, f'{sample_rate} Hz', 'Cue', ''])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help='Path to the directory containing the .ds files')
    parser.add_argument('--out_path', default=None, help='Path to the output directory')
    args = parser.parse_args()
    
    ds_files = [f for f in os.listdir(args.path) if f.endswith('.ds')]
    total_files = len(ds_files)
    for i, ds_file in enumerate(ds_files, start=1):
        print(f'Processing file {i} of {total_files} ({i / total_files * 100:.2f}%)')
        csv_file = ds_files.replace('.ds', '.csv')
        if args.out_path is None:
            args.out_path = args.path
        ds_to_marker(os.path.join(args.path, ds_file), os.path.join(args.out_path, csv_file))

if __name__ == '__main__':
    main()
