# data_loader.py
def load_navajo_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        navajo_sentences = [line.split('\t')[1].strip() for line in file]
    return navajo_sentences
