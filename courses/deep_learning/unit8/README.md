# Unit 8: Transformers

Transformers are responsible for the latest advancements in deep learning. They replace recurrent neural networks and are commonly used for sequential datasets, primarily natural language but also time series, and can be adapted to other problems, even vision.
They are based on the concept of attention.

## Content

Watch the following content:

- Deep Learning Fundamentals: [Unit 8.4](https://lightning.ai/courses/deep-learning-fundamentals/unit-8.0-natural-language-processing-and-large-language-models/8.4-from-rnns-to-the-transformer-architecture/) and [Unit 8.5](https://lightning.ai/courses/deep-learning-fundamentals/unit-8.0-natural-language-processing-and-large-language-models/8.5-understanding-self-attention/)

 ## Assignment
1. Adapt your code from the previous units to use a Transformer Encoder with an Embedding layer. This [Pytorch tutorial](https://pytorch.org/tutorials/beginner/transformer_tutorial.html) is a good reference on how to define the model.
2. Push the changes to your repo and submit at least one new submission to Kaggle. Transformers should have a very similar or even worse performance compared to the last unit (RNNs). While theoretically more powerful, their complexity becomes an issue when training on smaller datasets such as this one, with a high tendency to overfit. On a large enought dataset, this would be reversed, and Transformers would start outperforming RNNs.

## Extra Materials
- [Pytorch Documentation - Transformer Encoder Layer](https://pytorch.org/docs/stable/generated/torch.nn.TransformerEncoderLayer.html)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [The Annotated Transformer](https://nlp.seas.harvard.edu/2018/04/03/attention.html)
- [d2l - Chapters 11.1, 11.5, 11.6, 11.7](https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)