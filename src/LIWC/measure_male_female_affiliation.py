import pandas as pd 
import numpy as np
import argparse
import re
import csv
import time
from os import listdir, path
from collections import Counter
import liwc
from pyserini.search import SimpleSearcher


def store_documents(searcher, unique_doc_ids):
    doc_id_passage = {}
    for doc_id in unique_doc_ids:
        doc = searcher.doc(str(doc_id))
        doc_id_passage[doc_id] = doc.raw()
    myfile = open("/collection.txt", "w+")
    for key, value in doc_id_passage.items():
        text = key + "\t" + value + "\n"
        myfile.write(text)
    myfile.close()


def creat_fm_dictionary(csv_path):
    """
    creates a dictionary of {"doc_id": [femail_affiliation, mail_affiliation, femail-mail]}
    :param my_csv: the resulting csv file of liwc
    :return: fm_dictionary
    """
    fm_dictionary = {}
    with open(csv_path, "r") as csv_file:
        my_csv = csv.reader(csv_file)
        for line_number, line in enumerate(my_csv):
            # print(line_number)
            doc_idx = line[0]
            fm_dictionary[doc_idx] = line[1:]
    return fm_dictionary



def tokenize(text):
    # you may want to use a smarter tokenizer
    for match in re.finditer(r'\w+', text, re.UNICODE):
        yield match.group(0)


def find_top_n_docs(run_file_path, cutoff):
    """
    :param run_file:
    :return: top_n_docs: stores a dictionary of query_id and top_n doc_ids:
                {"query_id":[docic_1, docid_2, ..., docid_cutoff]}
    """
    unique_doc_ids = set()
    top_n_docs = {}
    doc_ids = []
    with open(run_file_path, 'r') as run_file:
        for doc_counter, line in enumerate(run_file):
            list_line = line.split(" ")
            if int(list_line[3]) < cutoff+1:
                query_id = list_line[0]
                unique_doc_ids.add(list_line[2])
                # print("finding top-{} docs of query id = {}".format(cutoff, query_id))
                doc_ids.append(list_line[2])
                top_n_docs[query_id] = doc_ids
            else:
                doc_ids = []
    return top_n_docs, unique_doc_ids


def calculate_doc_score(doc_str, parse):
    """
    calculates the liwc score of a string.
    :param document:
    :return:
    """
    liwc_attributes = ['female','male']
    doc_tokens = tokenize(doc_str)
    # liwc_counts = Counter(category for token in doc_tokens for category in parse(token))
    categories = []
    token_counter = 0
    for token in doc_tokens:
        token = token.lower()
        token_counter += 1
        for category in parse(token):
            categories.append(category)
                
    liwc_counts = Counter(categories)
    attributes_existance = []
    for attr in liwc_attributes:
        if attr in liwc_counts.keys():
            attributes_existance.append(liwc_counts[attr] / token_counter)
        else: 
            attributes_existance.append(0)
    attributes_existance.append(attributes_existance[1] - attributes_existance[0])
    return attributes_existance


def calculate_file_score():
    """
    writes liwc scores of different documents (all in a single directory) in a csv file
    :return:
    """
    parse, _ = liwc.load_token_parser("/LIWC2015Dictionary.dic")
    with open("/documents_liwc_metrics.csv", 'w') as liwc_csv_results:
        writer = csv.writer(liwc_csv_results)
        documents = pd.read_csv("/collection.txt", sep = "\t", names = ["pid", "passage"])
        documents = documents.values.tolist()
        for row in documents:
            doc_str = row[1]
            liwc_attr = calculate_doc_score(doc_str, parse)
            liwc_attr.insert(0,row[0])
            writer.writerow(liwc_attr)
            # if row_number % 1000 == 0:
            #     print(row_number)

def calculate_query_score_cutoff(doc_ids, fm_dictionary):
    """
    calculate the mean fm_score of each query
    based on its top_n retreived docs
    score = abs(mean(femail_score - mail_score))
    :return:
    """
    query_score = [0 for k in range(0,3)]
    for doc_idx in doc_ids:
        query_score = [(query_score[i] + float(fm_dictionary[doc_idx][i])) for i in range(len(query_score))]
    query_score = [abs(score/len(doc_ids)) * 100  for score in query_score]
    return query_score

def calculate_score_cutoff(topn_docs_dict, fm_dictionary):
    per_query_score = []
    total_score = [0 for i in range(0,3)]
    for qid, doc_ids in topn_docs_dict.items():
        # print("calculating score for query number {}".format(counter))
        query_score = calculate_query_score_cutoff(doc_ids, fm_dictionary)
        tmp = query_score.copy()
        tmp.insert(0, qid)
        per_query_score.append(tmp)
        for j in range(0,3):
            total_score[j] += query_score[j]
    for k in range(0,3):
        total_score[k] = total_score[k] / len(topn_docs_dict)
    return total_score

def write_score_cutoffs(csv_path, run_file_path, save_path):
    print("stat creating and saving the fm_dictionary of liwc")
    fm_dict = creat_fm_dictionary(csv_path)
    cutoff_list = [10,20]
    scores = []
    for cutoff in cutoff_list:
        print("cutoff = {}".format(cutoff))
        topn_docs_dict,_ = find_top_n_docs(run_file_path, cutoff)
        liwc_score = calculate_score_cutoff(topn_docs_dict, fm_dict)
        liwc_score.insert(0,cutoff)
        scores.append(liwc_score)
        print("cutoff: {} Done".format(cutoff))
    return scores

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-run', type=str, default='')
  parser.add_argument('-res', type=str, default='')
  args = parser.parse_args()
  searcher = SimpleSearcher('/msmarco-passage/lucene-index-msmarco')
  _, unique_doc_ids = find_top_n_docs(args.run,20)
  store_documents(searcher, unique_doc_ids)
  calculate_file_score()
  liwc_score_total = write_score_cutoffs("/documents_liwc_metrics.csv",args.run, args.res)
  df = pd.DataFrame(liwc_score_total, columns = ['cutoff','female','male', 'diff'])
  df.to_csv(args.res, index = False)
  print("finished")


if __name__ == "__main__":
    main()



