import math
import os
import random
import re
import sys

#
# Complete the 'awardTopKHotels' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING positiveKeywords
#  2. STRING negativeKeywords
#  3. INTEGER_ARRAY hotelIds
#  4. STRING_ARRAY reviews
#  5. INTEGER k
#

def awardTopKHotels(positiveKeywords, negativeKeywords, hotelIds, reviews, k):
    # I am also using camel case as the code is already using it
    positiveKeywordsList = positiveKeywords.split()
    negativeKeywordsList = negativeKeywords.split()
    # ignoring dots and commas in positiveKeywordsList
    i=0
    while i < len(positiveKeywordsList):
        positiveKeywordsList[i] = re.sub(r'^[.,]*(.*?)[.,]*$', r'\1', positiveKeywordsList[i])
        i+=1
    # ignoring dots and commas in negativeKeywordsList
    i=0
    while i < len(negativeKeywordsList):
        negativeKeywordsList[i] = re.sub(r'^[.,]*(.*?)[.,]*$', r'\1', negativeKeywordsList[i])
        i+=1
    
    # going through the reviews now...
    i=0
    individualHotelScores = {}
    while i < len(hotelIds):
        individualHotelScores.setdefault(hotelIds[i], 0)
        currentReviewWords = reviews[i].split()
        # ignoring dots and commas in currentReviewWords
        j=0
        while j < len(currentReviewWords):
            currentReviewWord = re.sub(r'^[.,]*(.*?)[.,]*$', r'\1', currentReviewWords[j])
            if currentReviewWord in positiveKeywordsList:
                individualHotelScores[hotelIds[i]] += 3
            elif currentReviewWord in negativeKeywordsList:
                individualHotelScores[hotelIds[i]] -= 1
            j+=1
        i+=1
    
    # sorting the hotelIds as per the scores
    sorted_hotels_by_score = sorted(individualHotelScores.items(), key=lambda x:x[1], reverse=True)
    
    awarded_hotels = []
    i=0
    while i < k and i < len(sorted_hotels_by_score):
        awarded_hotels.append(sorted_hotels_by_score[i][0])
        i+=1
    return awarded_hotels
    

if __name__ == '__main__':
    positiveKeywords = input()

    negativeKeywords = input()

    hotelIds_count = int(input().strip())

    hotelIds = []

    for _ in range(hotelIds_count):
        hotelIds_item = int(input().strip())
        hotelIds.append(hotelIds_item)

    reviews_count = int(input().strip())

    reviews = []

    for _ in range(reviews_count):
        reviews_item = input()
        reviews.append(reviews_item)

    k = int(input().strip())

    result = awardTopKHotels(positiveKeywords, negativeKeywords, hotelIds, reviews, k)

    print('\n'.join(map(str, result)))
    print('\n')