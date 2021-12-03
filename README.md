# CapstoneProject
# A Sentiment analysis of tweets related to several stocks, for hourly price movement prediction
Limited tools like this exist for public use, and they typically look at overall sentiment, rather than sentiment related to a particular security. 
The project includes a regression to see the predictive value of sentiment on hourly returns. 
# Sourcing the Data
I scraped data from twitter using Tweepy for 1 day of activity related to several securities.
For training purposes, in 3 of the stocks, each Tweet was manually assigned a positive,negative, or neutral rating, to form a ground truth. 
This was based on my subjective opinion of the sentiment as it related to a given company's future performance. 
I decided to do this because microblogs related to stocks use unique language that I believed existing training sets like the sentiment-140 would not adequately capture. 

# Processing
For pre-processing, stop words, URLS, and punctuation marks were removed. Emojis were removed as well, for simplicity. The tweets were then stemmed and tokenized.

# Sentiment Analysis
Sentiment computed using lexicon-based ( rules-based ) methods, as well as optimized ML algorithms. 

# Price Comparison
The sentiment was then aggregated into an hourly average, which was compared to price movements in those stocks. 
# Model Building
ML models were optimized with a grid search. Lexicon-based models (textblob/vader) involve no learning, and merely served as a baseline.

# Results
The accuracy of the sentiment predictions was the best with logistic regression, which classified the tweets into negative/positive/nautral with a 72.6% accuracy rate.

# Future Improvements
There is a lot of spam activity in social media channels related to stocks, which could be removed.
I believe that the accuracy of the sentiment prediction could be improved with more rigorous pre-processing. 
The model would benefit from a streaming capability, which would make it more useful for high frequency trading. 
It would be interesting to introduce sentiment in an ARIMA model and evaluate lagged cross-correlations between the sentiment and stock returns. 
