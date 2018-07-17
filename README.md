# Table of Contents
1. Problem
2. Approach to solving the problem
3. Running instructions
4. Test dataset

# Problem
Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name.

# Approach to solving the problem
The algorithm in the script is designed for the purpose of fast processing of large amount of data. Therefore, data format checking is not done within the script (it should be done before running the script). Printing and I/O is reduced to minimum. Data is processed line by line and never fully loaded to the memory to save time and space. A parallel version is not implemented, for the current performance with the provided complete dataset (see test dataset) is fine.

# Running instructions
See run.sh

# Test dataset
Three test dataset are included in the testsuite. The first one is the small testset from the instructions. The second one is extracted from the complete 24 million records dataset de_cc_data.txt by using every 1000 lines. The third one is generated in a similar way, but starting from the 10th record for every 1000 lines. Both are well tested and can be done within 0.1s.
The complete 24 million record dataset is also tested using the script. The full dataset is not included due to the large size of the input file. The one-time tested running time is 73.72s on a 2.4 GHz intel i5 Macbook (2013 version).
