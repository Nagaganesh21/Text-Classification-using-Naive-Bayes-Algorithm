# Text-Classification-Application

## Introduction
Hello all, this project is my experiement with the Naive bayes classifier and implemented this by following the Simiplilearn's lecture, [Text Classification Using Naive Bayes | Naive Bayes Algorithm In Machine Learning](link: https://www.youtube.com/watch?v=60pqgfT5tZM) in Youtube. But what I did on my own is, to deploy the trained Naive bayes classifier model using Flask so that a user can use it through the front-end web application.

Entire development part was done using Jupyter notebook while the deployment part was done using VSCode.
## About the Dataset
The dataset used for this project was fetch_20newsgroups, can be imported from "sklearn.datasets". As the name suggests, this dataset contains articles which are classified into 20 news groups, as mentioned below.

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

First, to extract features from the data, we vectorized each article in the training set by using the "TfidfVectorizer", imported from sklearn.feature_extraction.text. This assigns class to each word in the article based on the probability. 

Then, we used "MultinomialNB" algorithm (since this is a multi classification problem), imported from from sklearn.naive_bayes. We trained a model by fitting  this MultinomialNB on the training dataset.

We defined pipeline by using "make_pipeline", imported from from sklearn.pipeline. In this pipeline, we passed TfidfVectorizer first and then MultinomialNB so that entire model training follows a sequence. 

## Model predictions on the Test data

we used the trained model to make predictions on the test data and visualized the confusion matrix, found that our model's accuracy was 77.39%. 

## Model saving and deployment

Using Joblib library, we saved our model as a .pkl file. Then, to deploy this model, we created a web application in python using the Flask - a micro web framework in VSCode, which works as a back-end. It takes input from the front-end webpage (developed using HTML5), makes prediction and returns the result in a user understandable format which gets displayed in the same front-end web page, so that a user can sense it.

## Tools used

![image](https://user-images.githubusercontent.com/22242325/166194914-1f7a02fe-67ea-4397-8904-69f225250af6.png)
![image](https://user-images.githubusercontent.com/22242325/166194954-a4599de6-3414-419c-aae0-ea650f76630f.png)
![image](https://user-images.githubusercontent.com/22242325/166194977-5cd775fe-4e51-4f9b-8cd5-71bd22df6c99.png)
![image](https://user-images.githubusercontent.com/22242325/166195067-b706c72a-ddc5-4e5d-890e-ca38e0a6638b.png)
![image](https://user-images.githubusercontent.com/22242325/166195187-266a0b24-5a30-4d01-90d9-20b446408136.png)
![image](https://user-images.githubusercontent.com/22242325/166195211-5b20fe0e-8707-462e-8697-ea979a91a103.png)
![image](https://user-images.githubusercontent.com/22242325/166195243-d2c412f0-7063-439e-af9b-6768c90a1a41.png)
![image](https://user-images.githubusercontent.com/22242325/166195273-06ddc71c-04fd-4832-84c2-ad4ba17a53e6.png)
![image](https://user-images.githubusercontent.com/22242325/166195340-d45e291e-4aee-4ad4-bc73-ddcba0d66a21.png)
![image](https://user-images.githubusercontent.com/22242325/166195380-db8a3fdd-b726-44e3-af21-f63b43d67220.png)
![image](https://user-images.githubusercontent.com/22242325/166195407-02d970f4-022e-4767-b236-fb3b826e34d1.png)

## References:
[Bayes Theorem lecture by Krish Naik](https://www.youtube.com/watch?v=71oNiqPoKD8&ab_channel=KrishNaik)
[Indepth intuition of a Naive Bayes Classifier by Krish Naik](https://www.youtube.com/watch?v=jS1CKhALUBQ&ab_channel=KrishNaik)
[Application of Naïve Bayes Classifier on Text Data (NLP) - The intuition](https://www.youtube.com/watch?v=temQ8mHpe3k&ab_channel=KrishNaik)









