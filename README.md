# Rideshare-Casestudy
Case Study 3

## Team
Isaac Campbel-Smith

Joseph Shanks

Brandon Lindsey

Richard Bellamy

### Table of Contents

[Problem Domain](#Problem-Domain)

[Graphs](#Graphs)

[Presentation](#Presentation)

## Problem-Domain
A ride-sharing company (Company X) is interested in predicting rider retention. To explore this question, we will explore a sample dataset of a cohort of
users who signed up for an account in January 2014. The data was pulled on July
1, 2014; we consider a user retained if they were “active” (i.e. took a trip)
in the preceding 30 days (from the day the data was pulled).

## Lessons Learned
-When we first got out data cleaned and out models working we tried to run a random forest and a linear regression.  We noticed that our random forest did better at percision but the linear regression had better recall.

-If we assumed all users churned we would start with an accuracy of 62%

## Graphs


## Presentation

#### How did you compute the target?

We computed the target by spliting the last ride column on "-" and taking the middle value.  Anything below 6 was considered churned.

#### What model did you use in the end? Why?

We decided that our strongest model was the random forest classifier.  It performed better then the gradient boosted regression we had the time to run.

|-    |  Actual+   |  Actual-   |
|----:|:-----------|:-----------|
|Pred+|    2500    |    793     |
|Pred-|    1290    |   5417     |

-Accuracy  of best:  0.7778
-Precision of best:  0.7381684081130916
-Recall    of best:  0.6367974549310711


#### Alternative models you considered? Why are they not good enough?

The first model we eliminated was the linear regression model because this is a classification problem.

Next we eliminated the logistic regression because it preforemed worse then the out of box random forest classifier that we used.

Here is the confusion matrix for our logisitc regresion

|-    |  Actual+   |  Actual-   |
|----:|:-----------|:-----------|
|Pred+|    1914    |    927     |
|Pred-|    1876    |   5283     |

The confusion matrix for our random forest classifier before we started tuning is

|-    |  Actual+   |  Actual-   |
|----:|:-----------|:-----------|
|Pred+|    1544    |    516     |
|Pred-|    2189    |   5751     |

#### What performance metric did you use to evaluate the model? Why?

We used log loss to score our individual models and then we used percision and recall to jointly to determine the best model.   

#### Based on insights from the model, what plans do you propose to reduce churn?



#### What are the potential impacts of implementing these plans or decisions? What performance metrics did you use to evaluate these decisions, why?