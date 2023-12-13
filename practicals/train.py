import sys

word_tag = {}
word_total_count = {}
total_tokens = 0

with sys.stdin as fd:
    for line in fd:
        line = line.strip('\n')
        if '\t' not in line:
            continue
        row = line.split('\t')
        tag = row[2]
        form = row[1]
        
        if form not in word_tag:
            word_tag[form] = {}
        if tag not in word_tag[form]:
            word_tag[form][tag] = 0
        word_tag[form][tag] += 1
        total_tokens += 1

# Calculate frequencies and print the output
print("# P\tcount\ttag\tform")
for form in word_tag:
    for tag, count in word_tag[form].items():
        freq = count / word_total_count[form]
        #freq = count / total_tokens
        print(f"{freq:.2f}\t{count}\t{tag}\t{form}")
