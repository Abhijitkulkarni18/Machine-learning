# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 21:46:52 2018

@author: abhi
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:16:11 2018

@author: abhij
"""

from nltk.classify import NaiveBayesClassifier
from nltk.classify import accuracy
from sklearn.utils import shuffle
import pickle

'''creating gender class'''

class GenderClassifier:

    def gender_features(self, name):
        '''features of the names''' 
        return ({
                'last_is_vowel': (name[-1] in 'AEIOUY'),
                'last_letter': name[-1],
                'last_three': name[-3:],
                'last_two': name[-2:]
            })

    def data_sets(self):
        '''process raw data'''
        with open('names.txt', 'r') as f:
            names = []
            for name_results in f:
                names.append(tuple(name_results.strip().split(',')))

        return names

    
    def feature_set(self):
        feature_sets = []
        '''shuffel data'''
        for name_results in self.data_sets():
            name, gender = name_results

            name = self.gender_features(name)
            feature_sets.append((name, gender))

        return shuffle(feature_sets)

    
    def model_train(self):
        '''training the model'''
        feature_sets = self.feature_set()
        
        # Splitting the dataset into the training set and est set
        from sklearn.cross_validation import train_test_split
        train_data_set, test_data_set = train_test_split(feature_sets, test_size = 0.2, random_state = 0)
        print(train_data_set)
        self.classifier = NaiveBayesClassifier.train(train_data_set)
        with open('classifier.pickle','wb') as f:
            pickle.dump(self.classifier,f)
        return self.classifier
        

        
    def gender_classifier(self, name = None):
        '''fitting the test data for classifier'''
        gender = self.classifier.classify(self.gender_features(name.upper()))
        if gender == 'M':
            return ' "{}" is male.'.format(name)
        else:
            return ' "{}" is female.'.format(name)
       

if __name__ == '__main__':
    gcf = GenderClassifier()
    gcf.model_train()
    
    name=input('Enter the name: ')
    print(gcf.gender_classifier(name))
   
                

