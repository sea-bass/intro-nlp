# Introduction to Natural Language Processing (NLP)
Educational resources to get started with Natural Language Processing in Python.

By Sebastian Castro, 2020



## Getting Started

[Install conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) and then create and activate a conda environment

```bash
conda create --name intro-nlp --file conda-requirements.txt
conda activate intro-nlp
```


---


## Examples

### Rule-Based Processing
Basic string processing and syntax parsing using a grammar.

### Traditional Statistical Methods
The "old school" of NLP, including bag-of-words representations and classifiers that do not use neural networks such as Naive Bayes and Support Vector Machines (SVM)

### Modern Statistical Methods using Deep Learning
Here we will see how neural networks have revolutionized NLP, using techniques like word embeddings to reduce vocabulary dimensionality and recurrent neural networks with elements like Gated Recurrent Units (GRU) and Long Short-Term Memory (LSTM).
Finally we will look at the most state-of-the-art deep learning based NLP models like Transformers, which do away with recurrent neural networks and their disadvantages by using attention mechanisms.


---


## List of Software Tools

### NLP Tools
* NLTK
* spaCy
* Stanza

### Machine Learning Core Tools
* scikit-learn
* PyTorch
* TensorFlow

### NLP Specific Machine Learning Tools
* AllenNLP
* huggingface Transformers
