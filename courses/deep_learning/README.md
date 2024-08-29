# LDSA Deep Learning Course

Welcome to the LDSA Deep Learning Course!

This course offers a pragmatic introduction to Deep Learning, beginning with the fundamentals while also embracing state-of-the-art concepts. It was developed in 2023 by [@jdpsc](https://github.com/jdpsc), [@fabiocruz](https://github.com/fabiocruz), and [@TSFelg](https://github.com/TSFelg) as a guided cohort for [@nosportugal](https://github.com/nosportugal) with special accompaniment from [@nfpaiva](https://github.com/nfpaiva). NOS has since donated the course to the LDSA and the open source community.

## Methodology

The course is composed of 9 units of 1-2 weeks each. The minimum expected load for each unit is 4 hours. Each unit consists of learning new concepts via video and written content and then applying those concepts into practice with technical assignments.

## Curriculum

The main reference for the course is the [Deep Learning Fundamentals](https://lightning.ai/courses/deep-learning-fundamentals/) course from the Pytorch Lightning team. There are many deep learning materials available out there, and we prioritise this course for the following reasons:
- It is recent and covers the state-of-the-art. For example, in the last units you will be fine-tuning Transformers for your downstream task.
- It is a hands-on course that uses Pytorch and Lightning which are the standard tools today for building with neural networks.
- It is a compact course that fits within the timeframe of the cohort. It does this by not covering architectures that aren't as relevant nowadays. These are interesting from a theoretical perspective but not as useful from a practical perspective which this cohort prioritises.

This course provides upgrades on the original course, namely:
- Structures the course into 9 units with consistent expected effort that balance theoretical and practical workload.
- Makes deep learning applied to text the core focus by integrating with the dataset from the Kaggle competition [Bag of Words Meets Bags of Popcorn](https://www.kaggle.com/c/word2vec-nlp-tutorial). This way you're challenged to test increasingly complex architectures on the same dataset to try and beat your previous submissions.
- Offers new solutions to the Kaggle challenge using CNNs, RNNs, Transformers and Pre-trained models.
- Adapted exercises and solutions to use Google Colab and W&B to make them easier for anyone to run.
- Added curated external resources that complement less developed parts of the course, for example the units on Transformers.
- Removes some parts of the original course that are not not as relevant (e.g. Lightning approach to tuning that is deprecated).

These are the topics of focus of each unit:
- Unit 1: Deep Learning Fundamentals
- Unit 2: Neural Networks
- Unit 3: Lightning and W&B
- Unit 4: Optimizing Neural Nets
- Unit 5: Word embeddings
- Unit 6: Convolutional Neural Networks
- Unit 7: Recurrent Neural Networks
- Unit 8: Transformers
- Unit 9: Pre-trained Models

Throughout the course, you will be testing different model architectures to solve the Kaggle challenge [Bag of Words Meets Bags of Popcorn](https://www.kaggle.com/c/word2vec-nlp-tutorial), which goal is to classify the sentiment expressed in [IMDb](https://www.imdb.com/) movie reviews. Below you can see the score (accuracy) obtained for a reference model developed in each unit of the course. The model score generally increases as you progress through the course, although precise expectations are set in each unit.

| Unit                                    | Accuracy |
|-----------------------------------------|----------|
| Unit 3: Lightning and W&B               | 0.87228  |
| Unit 4: Optimizing Neural Nets          | 0.85352  |
| Unit 5: Word embeddings                 | 0.88032  |
| Unit 6: Convolutional Neural Networks   | 0.84536  |
| Unit 7: Recurrent Neural Networks       | 0.86724  |
| Unit 8: Transformers                    | 0.85952  |
| Unit 9: Pre-trained Models (DistilBERT) | 0.91472  |
| Unit 9: Pre-trained Models (RoBERTa)    | 0.95552  |


## Setup

You will be using Google Colab as your development environment during the course. We prioritized Google Colab for the following reasons:
- Provides free GPUs which are very useful for deep learning practitioners, specially for the state-of-the-art architectures explored later on in the course.
- Comes with several relevant libraries pre-installed which makes it an easy-to-reproduce environment when sharing the code with other team members.
- Provides a good notebook git integration.

In a production environment Colab wouldn't be the ideal option, using an IDE and organising your code into modules would be best, but this is outside the scope of this course. Some relevant references on productioninsing deep learning are the [Full Stack Deep Learning](https://fullstackdeeplearning.com/) and [Made with ML](https://madewithml.com/) courses.
