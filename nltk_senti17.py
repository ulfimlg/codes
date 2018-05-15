from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

n_instances = 100
subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
print(len(subj_docs))
print(len(obj_docs))
print(subj_docs[0])

train_subj_docs = subj_docs[:80]
test_subj_docs = subj_docs[80:100]
train_obj_docs = obj_docs[:80]
test_obj_docs = obj_docs[80:100]
training_docs = train_subj_docs+train_obj_docs
testing_docs = test_subj_docs+test_obj_docs
sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)

sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)
for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))

sentences=["""Scam-hit Punjab National Bank is among some government organisations which ignored the Central Vigilance Commission (CVC) advice to act against its allegedly corrupt staff, the anti-corruption body has stated in a new report.The non-compliance of the advice has been mentioned in the CVC's annual report for 2017 tabled in Parliament recently. The report comes at a time when the bank is facing multiple agency probe in the over Rs 13,000 crore loan fraud allegedly committed by billionaire jeweller Nirav Modi and his uncle, Mehul Choksi, the promoter of Gitanjali Gems.The latest CVC report refers to a case in which the PNB sanctioned a Cash Credit (CC) limit of Rs 200 lakh and Term Loan (TL) of Rs 150 lakh to a firm for setting up a manufacturing unit in Dehradun against mortgage of property that was find unviable."""]

#paragraph ="Reliance aims to connect over 1.9 million schools and 58,000 universities across India with technology."

#lines_list = tokenize.sent_tokenize(paragraph)
#sentences.extend(paragraph)

sid = SentimentIntensityAnalyzer()
for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()
