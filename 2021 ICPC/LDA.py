if __name__ == "__main__":

   # Run in python console
    import nltk

    import re
    import numpy as np
    import pandas as pd
    from pprint import pprint

    # Gensim
    import gensim
    import gensim.corpora as corpora
    from gensim.utils import simple_preprocess
    from gensim.models import CoherenceModel


    # spacy for lemmatization
    import spacy
    nlp = spacy.load('en_core_web_sm')

    # Plotting tools
    import pyLDAvis
    import pyLDAvis.gensim  # don't skip this
    import matplotlib.pyplot as plt
    #%matplotlib inline

    # Enable logging for gensim - optional
    import logging
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)



    # NLTK Stop words
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'google', 'powered', 'by'])


    # Import Dataset
    df = pd.read_excel('Final Dataset for LDA.xlsx', error_bad_lines=False);
#    df = pd.read_excel('0 for LDA.xlsx', error_bad_lines=False);
    #print(df[:7])
    df.head()


    # Convert to list
    data = df.values.tolist()

    # Remove Emails
    #data = [re.sub('\S*@\S*\s?', '', sent) for sent in data]

    # Remove new line characters
    #data = [re.sub('\s+', ' ', sent) for sent in data]

    # Remove distracting single quotes
    #data = [re.sub("\'", "", sent) for sent in data]

    #pprint(data[:])


    def sent_to_words(sentences):
        for sentence in sentences:
            yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

    data_words = list(sent_to_words(data))

    #print(data_words[:1])

    # Build the bigram and trigram models
    bigram = gensim.models.Phrases(data_words, min_count=1, threshold=100) # higher threshold fewer phrases.
    trigram = gensim.models.Phrases(bigram[data_words], threshold=100)

    # Faster way to get a sentence clubbed as a trigram/bigram
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)

    # See trigram example
    #print(trigram_mod[bigram_mod[data_words[0]]])

    # Define functions for stopwords, bigrams, trigrams and lemmatization
    def remove_stopwords(texts):
        return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

    def make_bigrams(texts):
        return [bigram_mod[doc] for doc in texts]

    def make_trigrams(texts):
        return [trigram_mod[bigram_mod[doc]] for doc in texts]

    def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        """https://spacy.io/api/annotation"""
        texts_out = []
        for sent in texts:
            doc = nlp(" ".join(sent))
            texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        return texts_out

    # Remove Stop Words
    data_words_nostops = remove_stopwords(data_words)

    # Form Bigrams
    data_words_bigrams = make_bigrams(data_words_nostops)

    # Initialize spacy 'en' model, keeping only tagger component (for efficiency)
    # python3 -m spacy download en
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

    # Do lemmatization keeping only noun, adj, vb, adv
    data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])

    #print(data_lemmatized[:3])

    # Create Dictionary
    id2word = corpora.Dictionary(data_lemmatized)

    # Create Corpus
    texts = data_lemmatized

    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]

    # View
    #print(corpus[:1])

    [[(id2word[id], freq) for id, freq in cp] for cp in corpus[:1]]

    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                               id2word=id2word,
                                               num_topics=31,
                                               random_state=1000,
                                               update_every=1,
                                               chunksize=1000,
                                               passes=1,
                                               alpha='auto',
                                               per_word_topics=True)

   # `passes` is the number of training passes through the corpus. For #example, if the training corpus has 50,000 documents, chunksize is #10,000, passes is 2, then online training is done in 10 updates:
   # 1 documents 0-9,999, #2 documents 10,000-19,999 #10 documents 40,000-49,999
   # In gensim, the chunksize (how many documents to load into memory) is decoupled from LDA batch size. So you can process the training corpus with chunksize=10000, but with update_every=2, the maximization step of EM is done once every 2*10000=20000 documents. This is the same as chunksize=20000, but uses less memory.
   # By default, update_every=1, so that the update happens after each batch of `chunksize` documents.
   # n case you're running the distributed version, be aware that `update_every` refers to one worker: with chunksize=10000, update_every=1 and 4 nodes, the model update is done once every 10000*1*4=40000 documents.
    # Print the Keyword in the 10 topics
    #pprint(lda_model.print_topics())
    doc_lda = lda_model[corpus]

    # Compute Perplexity
    #print('\nPerplexity: ', lda_model.log_perplexity(corpus))  # a measure of how good the model is. lower the better.


    # Compute Coherence Score
    coherence_model_lda = CoherenceModel(model=lda_model, texts=data_lemmatized, dictionary=id2word, coherence='c_v')

    coherence_lda = coherence_model_lda.get_coherence()
    #print('\nCoherence Score: ', coherence_lda)

    # Visualize the topics
    vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
    pyLDAvis.show(vis)


    # Download File: http://mallet.cs.umass.edu/dist/mallet-2.0.8.zip
    #mallet_path = 'mallet-2.0.8/bin/mallet'  # update this path
    #ldamallet = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=2, id2word=id2word)

