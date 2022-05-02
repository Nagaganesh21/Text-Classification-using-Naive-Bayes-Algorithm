# Text-Classification-Application

## Introduction
Hello all, this project is my experiement with the Naive bayes classifier and implemented this by following the Simiplilearn's lecture, [Text Classification Using Naive Bayes | Naive Bayes Algorithm In Machine Learning](https://www.youtube.com/watch?v=60pqgfT5tZM) in Youtube. But what I did on my own is, to deploy the trained Naive bayes classifier model using Flask so that a user can use it through the front-end web application.

Entire development part was done using Jupyter notebook while the deployment part was done using VSCode.
## About the Dataset
The dataset used for this project was fetch_20newsgroups, imported from "sklearn.datasets". As the name suggests, this dataset contains articles which are classified into 20 news groups, as mentioned below.

1. alt.atheism
2. comp.graphics
3. comp.os.ms-windows.misc
4. comp.sys.ibm.pc.hardware
5. comp.sys.mac.hardware
6. comp.windows.x
7. misc.forsale
8. rec.autos
9. rec.motorcycles
10. rec.sport.baseball
11. rec.sport.hockey
12. sci.crypt
13. sci.electronics
14. sci.med
15. sci.space
16. soc.religion.christian
17. talk.politics.guns
18. talk.politics.mideast
19. talk.politics.misc
20. talk.religion.misc

This dataset was split into training and testing sets respectively.

## Training the Naive Bayes classifier

First, to extract features from the data, we vectorized each article in the training set by using the "TfidfVectorizer", imported from sklearn.feature_extraction.text. This assigns class to each vector in the article based on the probability. 

Then, we used "MultinomialNB" algorithm (since this is a multi classification problem), imported from from sklearn.naive_bayes. We trained a model by fitting  this MultinomialNB on the training dataset.

We defined pipeline by using "make_pipeline", imported from from sklearn.pipeline. In this pipeline, we passed TfidfVectorizer first and then MultinomialNB so that entire model training follows a sequence. 

## Model predictions on the Test data

we used the trained model to make predictions on the test data and visualized the confusion matrix, found that our model's accuracy was 77.39%. 

## Model saving and deployment

Using Joblib library, we saved our model as a .pkl file. Then, to deploy this model, we created a web application in python using the Flask - a micro web framework in VSCode, which works as a back-end. It takes input from the front-end webpage (developed using HTML5), makes prediction and returns the result in a user understandable format which gets displayed in the same front-end web page, so that a user can sense it.

## Web application UI

Deployed this web application on Heroku Cloud using Gunicorn a Python web server gateway interface.

Link: - https://nb-text-classification.herokuapp.com/

![image](https://user-images.githubusercontent.com/22242325/166197641-7a03a361-c92b-438f-9b02-421f4017a84f.png)

## Tools used
![image](https://user-images.githubusercontent.com/22242325/166202085-d6caa906-ec15-41e5-a437-18bfd8a45fce.png)

## References:
[Bayes Theorem lecture by Krish Naik](https://www.youtube.com/watch?v=71oNiqPoKD8&ab_channel=KrishNaik) <br>
[Indepth intuition of a Naive Bayes Classifier by Krish Naik](https://www.youtube.com/watch?v=jS1CKhALUBQ&ab_channel=KrishNaik) <br>
[Application of Naïve Bayes Classifier on Text Data (NLP) - The intuition](https://www.youtube.com/watch?v=temQ8mHpe3k&ab_channel=KrishNaik) <br>









