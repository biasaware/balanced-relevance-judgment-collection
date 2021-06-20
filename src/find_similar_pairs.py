#importing libraries
import pandas as pd
import numpy as np
from annoy import AnnoyIndex
import multiprocessing
from multiprocessing import  Manager
from functools import partial
import pickle 
import random
import time

def create_net(record):
    pid = int(record[0])
    vector = record[1:]
    male_network = AnnoyIndex(22, 'angular')
    male_network.add_item(pid, vector)
    for md in male_docs_dict:
        male_network.add_item(md, male_docs_dict[md])
    male_network.build(1)
    most_similar_males = male_network.get_nns_by_item(pid, 2)
    if pid in most_similar_males:
        most_similar_males.remove(pid)
    best_male_pair = most_similar_males[0]
    male_distance = male_network.get_distance(pid, best_male_pair)
    return [pid, best_male_pair, male_distance]


female_attrs = pd.read_csv("../data/psychological_attribues/female_affiliated_documents_attributes.csv")
male_attrs = pd.read_csv("../data/psychological_attribues/male_affiliated_documents_attributes.csv")

female_docs_list = female_attrs.values.tolist()
male_docs_list  = male_attrs.values.tolist()

print("Execution started !!!")

n_jobs = 50
pool = multiprocessing.Pool(processes= n_jobs)
s_time = time.time()
male_results = pool.map(create_net, female_docs_list)
print(time.time() - s_time)
pool.close()
similar_male_pairs = pd.DataFrame(male_results, columns = ['female_pid', 'male_pid', 'male_distance'])
similar_male_pairs.to_csv("/similar_pairs.csv", index = False)

print("Execution finished !!!")


















