# Native Language Identification of Greek in English-Written Texts

This repo contains all the code, data, and the thesis for [MA Digital Text Analysis](https://www.uantwerpen.be/en/study/programmes/all-programmes/digital-text-analysis/) at the University of Antwerp.

## Abstract

The task of Native Language Identification aims at predicting the native language (L1) of an author given only texts produced in a foreign language (L2). English is spoken by a minority of native speakers compared to those who speak it as an L2. This means that a large volume of English content is created by non-native English speakers. Therefore, it is crucial to devise strategies for determining the native language of non-native English writers. The study at hand introduces the NLI task for native speakers of Greek with English as L2. The corpus that we used is a collection of similar-topic posts from Reddit written by native speakers of Greek in English, along with English posts written by native English speakers from the UK and the US. This study provides new insights into the challenges and opportunities of identifying languages in multilingual contexts but also compares the performance across a variety of features of linguistic nature and employing both statistical and neural algorithms to shed light on how the two approaches differ in performance while tackling the NLI task. It lays the first stones to introduce the NLI task to other L1s in the future, train classifiers and check their robustness by finding that the combination of word embeddings with simple $n$-gram features on characters and Universal Parts-of-Speech tags achieves $82.6%$ mean F1-macro score after 10-fold Cross-Validation, surpassing most previous NLI studies. In addition, our best pre-trained BERT-based approach achieves equally high results ($82.1%$). A hard-voting ensemble model was also trained by combining three classifiers with different linguistic and word-embeddings features, however without resulting in performance increase. The error analysis conducted thereafter suggests that the short-form nature of the posts and the common usage of words that are mainly found in the opposite class could be some of the main reasons that these results could be attributed to. Finally, an important finding could potentially indicate that L1 word etymology could relate to L2 lexical choices, which would make an attractive case for upcoming research in the field of NLI.

**Keywords**: [Machine Learning](https://github.com/topics/machine-learning), [Natural Language Processing](https://github.com/topics/natural-language-processing), [Reddit](https://github.com/topics/reddit), [Thesis](https://github.com/topics/thesis), [Word Embeddings](https://github.com/topics/word-embeddings), [Logistic Regression](https://github.com/topics/logistic-regression), [Support Vector Machines](https://github.com/topics/support-vector-machines), [Native Language Identification](https://github.com/topics/native-language-identification), [BERT model](https://github.com/topics/bert-model), [DistilBERT model](https://github.com/topics/distilbert-model)

## Citation

If you use this code or thesis, please cite it as such:

```bibtex
@mastersthesis{boumparis-2023-native,
    author = {Boumparis, Dimitrios},
    title = {{Native Language Identification of Greek in English-Written Texts: A Comparison of Machine Learning Approaches}},
    school = {University of Antwerp},
    year = {2023},
    month = {January},
    url = {https://github.com/dimboump/GreekNLI},
    note = {Master's thesis}
}
```
