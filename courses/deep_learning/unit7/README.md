# Unit 7: Recurrent Neural Networks

Recurrent neural networks are commonly used for sequential datasets, such as time series or natural language. In this unit you will apply a RNN to the same dataset we've been working for the past units.

## Content

Watch the following content:

- [Deep Learning Fundamentals: Unit 8.3](https://lightning.ai/courses/deep-learning-fundamentals/unit-8.0-natural-language-processing-and-large-language-models/8.3-introduction-to-recurrent-neural-networks/)

 ## Assignment
1. Adapt your code from the previous units to use a RNN with an Embedding layer. This [chapter of d2l](https://d2l.ai/chapter_natural-language-processing-applications/sentiment-analysis-rnn.html) is a good reference on how to do this, since they also apply a RNN to the same dataset.
2. Push the changes to your repo and submit at least one new submission to Kaggle. RNNs should have a very similar performance compared to the last unit (CNNs). Again, this happens in part due the the size of the dataset, which bottlenecks the complexity of the models that we can train from scratch.

## Extra Materials
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- [Pytorch Documentation - LSTM](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)
- Pytorch Documentation - [Packing](https://pytorch.org/docs/stable/generated/torch.nn.utils.rnn.pack_padded_sequence.html) and [Padding](https://pytorch.org/docs/stable/generated/torch.nn.utils.rnn.pad_packed_sequence.html) Sequences