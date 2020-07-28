# Introduction to Natural Language Processing (NLP)
Educational resources to get started with Natural Language Processing in Python.

By Sebastian Castro, 2020

For more background, check out the following resources:

* [YouTube presentation](https://youtu.be/r1TLHEIz_FU)
* [Blog post](https://roboticseabass.wordpress.com/2020/07/28/introduction-to-natural-language-processing/)
* [Presentation slides](intro-nlp-slides.pdf)

---

## Getting Started

[Install conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) and then create and activate a conda environment

```bash
conda create --name intro-nlp --file conda-requirements.txt
conda activate intro-nlp
```

The version of HuggingFace Transformers available in `conda` is quite outdated, so you should directly install that one using `pip`. To do this, first make sure that you are in your conda environment!

```bash
conda activate intro-nlp
pip install transformers
```

---


## Examples

### Rule-Based Processing
Basic text processing and sentence parsing using a grammar.

Refer to the [Rule-Based Processing README](examples/rule_based/README.md) for more information.

### Traditional Statistical Methods
The "old school" of NLP, including features such as bag-of-words and machine learning classifiers that do not use neural networks, such as Naive Bayes and Support Vector Machines (SVM).

Refer to the [Traditional Machine Learning README](examples/traditional_ml/README.md) for more information.

### Modern Statistical Methods using Deep Learning
Here we will see how neural networks have revolutionized NLP, using techniques like word embeddings to reduce vocabulary dimensionality and recurrent neural networks with elements like Gated Recurrent Units (GRU) and Long Short-Term Memory (LSTM) units.


Finally we will look at the most state-of-the-art deep learning based NLP models like Transformers, which do away with recurrent neural networks and their disadvantages by using attention mechanisms.

Refer to the [Deep Learning README](examples/deep_learning/README.md) for more information.


---


## Featured Software Tools

* [re](https://docs.python.org/3/library/re.html) for regular expressions
* [NLTK](http://www.nltk.org/) for traditional NLP
* [scikit-learn](https://scikit-learn.org/stable/) for traditional machine learning
* [PyTorch](https://pytorch.org/) for neural networks
* [HuggingFace Transformers](https://huggingface.co/transformers/) for transformer networks
