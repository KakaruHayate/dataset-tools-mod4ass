import re
import csv
import os
import argparse
import wave



def ass_to_csv(ass_file, csv_file, include_comments=True):

    with open(ass_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    events = [line for line in lines if line.startswith('Dialogue') or (include_comments and line.startswith('Comment'))]

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['Name', 'Start', 'Duration', 'Time Format', 'Type', 'Description'])

        for i, event in enumerate(events):
            start_time, end_time = re.findall(r'\d:\d{2}:\d{2}.\d{2}', event)
            start_time = sum(float(x) * 60 ** (2 - i) for i, x in enumerate(start_time.split(':'))) * sample_rate
            end_time = sum(float(x) * 60 ** (2 - i) for i, x in enumerate(end_time.split(':'))) * sample_rate
            duration = end_time - start_time
            writer.writerow([f'Marker {i}', start_time, duration, f'{sample_rate} Hz', 'Cue', ''])

def check_wav(wav_file):
    with wave.open(wav_file, 'rb') as f:
        if f.getframerate() != 44100:
            print(f'{wav_file} does not have a sample rate of 44100 Hz')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help='Path to the directory containing the ASS files')
    parser.add_argument('--skip_comments', action='store_false', help='Skip comments in the ASS files')
    parser.add_argument('--check_wav', action='store_true', help='Check the sample rate of the corresponding WAV files')
    args = parser.parse_args()

    ass_files = [f for f in os.listdir(args.path) if f.endswith('.ass')]
    total_files = len(ass_files)
    global sample_rate
    for i, ass_file in enumerate(ass_files, start=1):
        sample_rate = 44100     #一般进行到这一步骤时，音频已经完成响度匹配和格式采样率转换等步骤，音频采样率应为44100kHz.
        if args.check_wav:
            wav_file = ass_file.replace('.ass', '.wav')
            check_wav(os.path.join(args.path, wav_file))
            with wave.open(wav_file, 'rb') as f:
                sample_rate = f.getframerate()
        print(f'Processing file {i} of {total_files} ({i / total_files * 100:.2f}%)')
        csv_file = ass_file.replace('.ass', '.csv')
        ass_to_csv(os.path.join(args.path, ass_file), os.path.join(args.path, csv_file), args.skip_comments)

if __name__ == '__main__':
    main()