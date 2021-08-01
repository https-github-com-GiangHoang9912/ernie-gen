import csv
import os
import time 

enter = True
paragraphs = []
answers = []
program_not_end=True

while program_not_end:
    while enter:
        paragraph = raw_input('papragraph:').strip()
        answer = raw_input('answer:').strip()
        paragraphs.append(paragraph)
        answers.append(answer)
        stop = raw_input('stop input?: ')
        if stop == 'y':
            enter= False
    with open('datasets/squad_qg/text.tsv','w') as f:
        tsv_writer = csv.writer(f,delimiter='\t')
        tsv_writer.writerow(['src',''])
        for para,ans in zip(paragraphs,answers):
            tsv_writer.writerow([ans+' [SEP] '+paragraph,''])

    os.system('bash run_seq2seq.sh /home/configs/base/squad-qg_conf')

    time.sleep(2)

    output = open("datasets/squad_qg/output.txt","r") 
    output.flush()
    print('list of questions:')
    print(output.read())
    on_off = raw_input('end program?:')
    if on_off == 'y':
        program_not_end = False
    else:
        enter=True