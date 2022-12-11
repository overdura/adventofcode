# -*- coding: utf-8 -*-
DATA_FILE='data.in'
MARKER_START_PACKET = 4
MARKER_MESSAGES = 14

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def clean_line(line):
    return line.replace('\n', '')

def has_repeated_characters(signal):
    result = False
    i = 1
    for s in signal:
        if s in signal[i:len(signal)]:
            return True
        i += 1
    return result

def get_marker(signal, find_message_marker):
    end_signal = len(signal)
    init_token = 0
    marker =  MARKER_MESSAGES if find_message_marker else MARKER_START_PACKET
    end_token = init_token + marker
    while end_token <= end_signal:
        token = signal[init_token : end_token]
        if not has_repeated_characters(token): 
            return end_token
            break
        end_token += 1
        init_token = end_token - marker

def resolve(find_message_marker):
    lines = read_file()
    signal = clean_line(lines[0])
    return get_marker(signal, find_message_marker)

def part_one():
    message = resolve(False)
    print("PART ONE characters_processed: ", message)

def part_two():
    message = resolve(True)
    print("PART ONE characters_processed: ", message) 


if __name__ == "__main__":
    part_one()
    part_two()