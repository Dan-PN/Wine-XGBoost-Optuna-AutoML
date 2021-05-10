import pandas as pd
import numpy as np
import collections
from dataprep.eda import plot
from dataprep.eda import plot_correlation
from dataprep.eda import plot_missing

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)
sns.set(font_scale=1)


# Minimal Processing
wines = pd.read_csv("winemag-data-130k-v2.csv", encoding='utf-8')
wines.columns
wines.drop(columns=['Unnamed: 0', 'taster_twitter_handle',
                    'taster_name'], inplace=True)
wines.dropna(axis='index', subset=['price', ], inplace=True)
wines.drop_duplicates(inplace=True)
# extract year from title
wines['year'] = wines.title.str.extract(pat='(\d{4})', expand=False)


# Encode Categorical Data as One Hot
categorycal_encoded = pd.get_dummies(
    data=wines[['country', 'province', 'variety']], prefix='c', dummy_na=False)  # keeping NaNs


# Extract most frequent wine related words from description and encode - .

# Extract the most common words in description
wines_desc = wines.description.str.replace(pat=",", repl='', regex=False).str.replace(
    pat=".", repl='', regex=False).str.lower()
wines_desc_list = list(wines_desc.values)
word_list = [word for entry in wines_desc_list for word in entry.split()]

# Filter common words


def filter_common_words(word_input):
    common_words = ['and', 'the', 'a', 'of', 'with', 'is', 'wine', 'in', 'to', 'it', 'on', 'that', 'from', 'but', "it's", 'are', 'its', 'this', 'at', 'as', 'an', "there's", 'there', 'also', "a", "about", "above", "after", "again", "against", "ain", "all", "am", "an", "and", "any", "are", "aren", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can", "couldn", "couldn't", "d", "did", "didn", "didn't", "do", "does", "doesn", "doesn't", "doing", "don", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn", "hadn't", "has", "hasn", "hasn't", "have", "haven", "haven't", "having", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is", "isn", "isn't", "it", "it's", "its", "itself", "just", "ll", "m", "ma", "me", "mightn", "mightn't", "more", "most", "mustn", "mustn't", "my", "myself", "needn", "needn't", "no", "nor", "not", "now", "o", "of", "off", "on", "once",
                    "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "re", "s", "same", "shan", "shan't", "she", "she's", "should", "should've", "shouldn", "shouldn't", "so", "some", "such", "t", "than", "that", "that'll", "the", "their", "theirs", "them", "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too", "under", "until", "up", "ve", "very", "was", "wasn", "wasn't", "we", "were", "weren", "weren't", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "won", "won't", "wouldn", "wouldn't", "y", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "could", "he'd", "he'll", "he's", "here's", "how's", "i'd", "i'll", "i'm", "i've", "let's", "ought", "she'd", "she'll", "that's", "there's", "they'd", "they'll", "they're", "they've", "we'd", "we'll", "we're", "we've", "what's", "when's", "where's", "who's", "why's", "would", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014"]

    if(word_input in common_words):
        return False
    else:
        return True


filtered_words = list(filter(filter_common_words, word_list))

# Extract top most common words without stop words
word_counter = collections.Counter(filtered_words)
word_counter_top = word_counter.most_common(400)  #

# Create Hot One Encoding for Frequent words in Description
descriptions = pd.Series([desc for desc, freq in word_counter_top])
descriptions_df = pd.DataFrame()

s1 = pd.Series(wines_desc)
for desc in descriptions:

    # This will pick up incomplete matched also (drinkable = drink)
    mask = s1.str.contains(desc, regex=False, case=False).astype(
        int)  # .rename("w_"+ desc)
    descriptions_df["w_"+desc] = mask


# Drop categorical Encoded Columns and already extracted columns
wines.drop(columns=['country', 'province', 'region_1', 'region_2', 'variety',
                    'winery', 'title', 'designation', 'description'], inplace=True)

# Add to extisting df
wines = pd.concat([wines, descriptions_df], axis=1, join="inner")
wines = pd.concat([wines, categorycal_encoded], axis=1, join="inner")

# Save
wines.to_csv("wines_encoded.csv", encoding='utf-8')

# fff
