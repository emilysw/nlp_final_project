# NLP Final Project, Fall 2017 ~ Professor Regina Barzilay

## Abstract: 
Clinical notes from intensive care units often capture physician decision making and patient attributes that are unique from that of coded time-series vitals and demographic data; however, their unstructured nature creates challenges that limits their efficiency in directly informing clinical actions. We aim to measure sentiment in clinical notes for sepsis treatment, in order to understand patient characteristics and clinical decisions not explicitly portrayed by the coded data. We apply a bag of words model with logistic regression, a suite of tree-based classification algorithms, a simple feed-forward neural net classifier, and a variations of a long short-term memory network in order to predict efficacy of clinical treatments using clinical notes. While results show initial progress, extensive further work is required in order to achieve improved results, such as through better pre-processing the clinical notes data, tuning to decrease over-fitting, and augmenting the sample collection.

## Description of files in this repository:

**Note: the clinical notes data and vitals data are not included in this repository due to privacy reasons.*

1. clinical_notes_prediction => extracting the clinical notes and conducting the matching for patients to generate the dataset
2. extract_patient_id => script to match icustay ids and patient ids from another table
3. lstm_word_embedding => variants of lstm
4. nn_classification => simple FFN from class
5. sentiment_cross_val => focused mostly on logistic regression + bigrams
6. sentiment_new => tested logistic regression + ngrams, tree-based algorithms, SVM (did not work for datasize)

For any questions, please email: emilysw@mit.edu
