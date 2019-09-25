
# coding: utf-8

# In[25]:


import csv
 
csv_file = open('transactions.csv', 'r')
csv_reader = csv.reader(csv_file)
 
transactions = []
for transaction in csv_reader:
    transactions.append(frozenset(transaction))
    transaction_set = set(transactions)

# Generate Length 1 itemsets
def inventory_set(transactions):
    for transaction in transaction_set:
        for item in transaction:
            inventory_set.add(item)

new_candidates = inventory_set
frequent_itemsets = []

while len(new_candidates) > 1:
    for c in new_candidates:
        support_count(c)
   
    filtered_candidates = filt()
       
    frequent_itemsets = frequent_items + filtered_candidates
    new_candidates = join(filtered_candidates, filtered_candidates)
    
frequent_itemsets = set((x, itemset_counts[x]) for x in itemset_counts if itemset_counts[x] >= min_sup_cnt)
    
for I in frequent_itemsets:
    S = set(x for x in powerset_nn(I[0]) if len(x) < len(I[0]))
    for A in S:
        B = I[0] - A
        conf = support_count(I[0], transactions) / support_count(A, transactions)
        print('{} \t-->\t {}\t\t c: {}'.format(set(A), set(B), conf))

