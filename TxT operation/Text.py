import re
import os

def read_txt_row_by_row_delete_one_row(path):
    text_list = []
    for root, dir, files in os.walk(path):
        for file in files:
            if '.txt' in file:
                f = open(os.path.join(root, file), 'r')
                text = f.read()
                f.close()
                text = text.split('\n', 14)[14]
                text = re.sub("(\d*\.\d+)|(\d+\.[0-9 ]+)*\t","",text)
                text_list.append(text)
    
    textAll = ''

    for i in range(len(text_list)):
        text_list[i] = text_list[i].split()

    for j in range(len(text_list[1])):
        for i in range(len(text_list)):
            textAll += (text_list[i])[j]
            textAll += '\t'
        textAll += '\n'
    
    with open('all_togther', 'w') as f:
       f.write(textAll)


if __name__ == '__main__':
    read_txt_row_by_row_delete_one_row(r'/home/pinkr1ver/Documents/Txt')
