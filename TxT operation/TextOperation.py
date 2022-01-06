import re
import os

'''
This text operation file is meant to process .txt file and all work based on list and str
Notice: it's not meant to process word data, it's meant to process data like .csv file, though in .txt file the comma will be replaced by space('\t')
'''

def read_txt_row_by_row_delete_one_row(path):
    text_list = []
    for root, dir, files in os.walk(path):
        for file in files:
            if '.txt' in file:
                f = open(os.path.join(root, file), 'r')
                text = f.read()
                f.close()
                text = delete_row(text, end=14)
                text = delete_coloumn(text, end=1)
                text_list.append(text)
    
    textAll = text_list[0]

    for i in range(1, len(text_list)):
        textAll = coloumn_append_text(textAll, text_list[i])

    with open('all_togther', 'w') as f:
       f.write(textAll)
       
def delete_row(text : str, begin=0, end=0):
    '''
    delete .txt file's rows, from begin's row to end's row
    Paramters:
        text: the str that will be deleted
        begin: if you don't need delete middle part rows of the text, you need set "begin" with 0
                if it begin in x line, set begin=x, x from 0-n
        end: if begin = 0, end will be the number of rows you want to delete, else, which is your last line, set end = last line
    type: str -> str
    '''
    if begin == 0:
        text = text.split('\n', end)[end]
        return text
    else:
        text_third_part = text.split('\n', end)[end]
        text_first_second_part = text.split('\n', begin)
        text_first_part = ''
        for i in range(len(text_first_second_part) - 1):
            text_first_part += (text_first_second_part[i] + '\n')
        result = text_first_part + text_third_part
        return result

def delete_coloumn(text : str, begin=0, end=0):
    '''
    delete .txt file's coloumns, from begin's coloumn to end's coloumn
    Paramters:
        text: the str that will be deleted
        begin: if you don't need delete middle part coloumns of the text, you need set "begin" with 0
                if it begin in x line, set begin=x, x from 0-n
        end: if begin = 0, end will be the number of coloumns you want to delete, else, which is your last line, set end = last line
    type: str -> str
    '''
    if begin == 0:
        text_list = text.split('\n')
        for i in range(len(text_list)):
            text_list[i] = re.sub('[^\t]*\t{1}', '', text_list[i], end)
        result = ''
        for i in text_list:
            result += i
            result += '\n'

        result = result[:-1]

        return result
    else:
        text_list = text.split('\n')
        for i in range(len(text_list)):
            third_part = re.sub('[^\t]*\t{1}', '', text_list[i], end)
            first_second_part = text_list[i].split('\t', begin)
            first_part = ''
            for j in range(len(first_second_part) - 1):
                first_part += (first_second_part[i] + '\t')
            text_list[i] = first_part + third_part
        result = ''

        for i in text_list:
            result += i
            result += '\n'
        
        result = result[:-1]

        return result

def coloumn_append_text(text1 : str, text2 : str):
    list_text1 = text1.split('\n')
    list_text2 = text2.split('\n')

    list_text = []
    result = ''

    for i in range(len(list_text1)):
        list_text.append(list_text1[i] + '\t' + list_text2[i])
    
    for i in list_text:
        result += i
        result += '\n'

    result = result[:-1]
        
    return result



if __name__ == '__main__':
    read_txt_row_by_row_delete_one_row(r'/home/pinkr1ver/Documents/Txt')
    str = '1\t2\t3\n1\t2\t3'
    str = delete_coloumn(str, end=1)
    print(str)
