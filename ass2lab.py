import os
import re
import argparse

def ass_to_lab(ass_file, out_path, include_comments=True):
    with open(ass_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    event_lines = [line for line in lines if line.startswith('Dialogue') or (include_comments and line.startswith('Comment'))]
    lab_lines = {re.findall(r'\d:\d{2}:\d{2}.\d{2}', line)[0]: line.split(',')[-1].strip() for line in event_lines if ',lab,' in line}

    for i, time in enumerate(lab_lines.keys()):
        lab = lab_lines.get(time, '')

        lab_file = os.path.join(out_path, f'{os.path.splitext(os.path.basename(ass_file))[0]}_{str(i).zfill(3)}.lab')
        with open(lab_file, 'w', encoding='utf-8') as f:
            f.write(lab)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help='Path to the directory containing the ASS files')
    parser.add_argument('--out_path', default=None, help='Path to the output directory')
    parser.add_argument('--skip_comments', action='store_false', help='Skip comments in the ASS files')
    args = parser.parse_args()

    if args.out_path is None:
        args.out_path = args.path

    ass_files = [f for f in os.listdir(args.path) if f.endswith('.ass')]
    for ass_file in ass_files:
        ass_to_lab(os.path.join(args.path, ass_file), args.out_path, args.skip_comments)

if __name__ == '__main__':
    main()