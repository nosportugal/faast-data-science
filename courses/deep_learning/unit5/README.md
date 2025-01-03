# Unit 5: Word Embbedings

Embeddings are numerical arrays that represent a certain entity. This entity can for example be a word, a sentence, an image, etc. These embeddings encode the defining characteristics of these entities, allowing models to discover patterns between them. Embedding spaces are often learned as part of an end-to-end supervised task.
In this unit, you will create a model that will learn an embedding for each word. While in this unit we will still use a simple Linear layer to "fuse" the embeddings together without regard for word order, this change will unlock further possibilities in the next units.

## Content

Read the following content:

- [Pytorch Tutorial: Word Embeddings](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html) (You can disregard the Continuous Bag-of-Words model)

 ## Assignment
1. The first step involves (pre-)tokenizing the dataset. We will provide the code for this part.
2. Adapt your code from the previous units to use an Embedding layer instead of the Bag of Words approach. The model should (internally) generate an embedding for each word.
3. Conceptualise a way to "aggregate" the multiple word embeddings into a single sentence embedding. You can try multiple ideas for this.
4. Continue using the Linear layer after you obtain a sentence embedding.
5. Additionally, if you have time, there's one extra optimization that can be made if you had not done so already. Notice that the tokenization code creates a padding (of zeros) in order for all sentences to have have the same length, which is necessary for batching. However, this means that most and especially shorter sentences will have plenty of invalid word embeddings. Change the code so that the model doesn't take the invalid embeddings into account.
6. Push the changes to your repo and submit at least one new submission to Kaggle. Using word level embeddings, especially when implementing the invalid embedding filter, should lead to slightly better results compared to the previous unit, altought not by a significant amount.


## Extra Materials
- [Pytorch Documentation - Embeddings](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html)
