# Unit 9: Pre-trained Models

Transformers can be pre-trained on huge amounts of unlabeled data, using a technique called self-supervision. These models can then be fine-tuned to other downstream tasks where labeled data is more limited, such as sentiment analysis. [Hugging Face](https://huggingface.co/) is a platform that allows you to access a multitude of pre-trained models, and provide the means to interact with them. In this unit you will fine-tune a large pre-trained Transformer model obtained from Hugging Face to the same dataset we've been working on for the past units.

## Content

Watch the following content:

- Deep Learning Fundamentals: [Unit 8.6](https://lightning.ai/courses/deep-learning-fundamentals/unit-8.0-natural-language-processing-and-large-language-models/8.6-large-language-models/) and [Unit 8.7](https://lightning.ai/courses/deep-learning-fundamentals/unit-8.0-natural-language-processing-and-large-language-models/8.7-a-large-language-model-for-classification/)

 ## Assignment
1. Adapt your code from the previous units to use a pre-trained Transformer model from the Hugging Face platform. This [LightningAI Repo](https://github.com/Lightning-AI/dl-fundamentals/tree/main/unit08-large-language-models/8.7-distilbert-finetuning) is an excellent reference on how use the HuggingFace models, as well as prepare the data for that end. You can try finetuning the full model or just the last layers. You should also try different style models (some ideas [here](https://github.com/Lightning-AI/dl-fundamentals/discussions/41)).
2. Push the changes to your repo and submit at least one new submission to Kaggle. Your objective is to beat your past Kaggle submissions. Pre-trained models are quite powerful, and since they are not trained from scratch, they do not dependent on high amounts of data. As such, you should see a clear improvement compared to all the previous units.

## Extra Materials
- [d2l - Chapter 11.9](https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)