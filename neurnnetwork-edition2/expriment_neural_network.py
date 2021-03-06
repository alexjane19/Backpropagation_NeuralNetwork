#coding:utf-8
#Passive-aggressive
#Binary Classification Algorithm

import csv
import math
import os
import re

import numpy as np
import numpy
from nltk.corpus import stopwords
from nltk.util import ngrams
from numpy import array, dot
from neural_network import NeuralNetwork
import random
import math


POLARITY_DATA_DIR = os.path.join('polarityData', 'rt-polaritydata')
RT_POLARITY_POS_FILE = os.path.join(POLARITY_DATA_DIR, 'rt-polarity-pos.txt')
RT_POLARITY_NEG_FILE = os.path.join(POLARITY_DATA_DIR, 'rt-polarity-neg.txt')

fieldnames = ['Max Iterations', 'Feature Set','Learning Rate', 'Type Set', 'MATCHES', 'MISMATCHES', 'TRUE POSITIVES', 'TRUE NEGATIVES',
              'PREDICTED POSITIVES', 'PREDICTED NEGATIVES', 'ACTUAL POSITIVES', 'ACTUAL NEGATIVES', 'ACCURACY',
              'PRECISION (POS)', 'RECALL (POS)', 'AVERAGE (POS)', 'F-SCORE (POS)', 'PRECISION (NEG)', 'RECALL (NEG)',
              'AVERAGE (NEG)', 'F-SCORE (NEG)', 'PRECISION', 'RECALL', 'AVERAGE', 'F-SCORE']

csvfile = None
row = {}
indexRow = 0
dictionary = {}
def read_file():
    _posSentences = []
    _negSentences = []
    # print(RT_POLARITY_POS_FILE)
    with open(RT_POLARITY_POS_FILE, 'r', encoding = "ISO-8859-1") as posSentences:
        for i in posSentences:

            _posSentences.append([i,'+'])
    with open(RT_POLARITY_NEG_FILE, 'r', encoding='utf-8') as negSentences:
        for i in negSentences:
          _negSentences.append([i, '-'])
    return _posSentences,_negSentences


def buildSet(sentences, featureSet, useDictionary=1):

    # Initialize the dictionary and the data
    wordCount = 0

    # The set to be built
    localSet = []
    nSet = 0
    pSet = 0


    # For each line in the file
    for line in sentences:

        # Get the sentence from the line and remove grammatical symbols
        sentence = line[0]
        _words = re.findall(r"[\w']+|[.,!?;]", sentence.rstrip())

        stops = set(stopwords.words('english'))
        words = []
        for w in _words:
            if w.lower() not in stops:
                words.append(w)

        # Save the label of the entry (1 for +, 0 for -)
        yt = 1 if line[1] == '+' else -1
        if yt == 1:
            pSet += 1

        # Initialize the feature set
        xt = []

        # Build unigrams
        if featureSet == 1:

            # For each valid word in the sentence
            for word in words:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)

        # Build bigrams
        elif featureSet == 2:
            _ngrams = ngrams(words, featureSet)
            for word in _ngrams:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)
        # Build 3-grams
        elif featureSet == 3:
            _ngrams = ngrams(words, featureSet)
            for word in _ngrams:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)

        # Build 4-grams
        elif featureSet == 4:
            _ngrams = ngrams(words, featureSet)
            for word in _ngrams:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)
        # Build 5-grams
        elif featureSet == 5:
            _ngrams = ngrams(words, featureSet)
            for word in _ngrams:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)
        # Build 6-grams
        elif featureSet == 6:
            _ngrams = ngrams(words, featureSet)
            for word in _ngrams:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)

        # Build unigrams-bigrams-3456-grams
        elif featureSet == 7:

            # Add unigrams first
            for word in words:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)

            # Now add bigrams
            _ngrams = ngrams(words, 2)
            for word in _ngrams:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)
            _ngrams = ngrams(words, 3)
            for word in _ngrams:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)
            _ngrams = ngrams(words, 4)
            for word in _ngrams:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)
            _ngrams = ngrams(words, 5)
            for word in _ngrams:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)
            _ngrams = ngrams(words, 6)
            for word in _ngrams:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)
                
        elif featureSet == 8:

            # Add unigrams first
            for word in words:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)



            # Now add bigrams
            _ngrams = ngrams(words, 2)
            for word in _ngrams:

                # Add word to dictionary in case it's not there
                if useDictionary == 1 and not word in dictionary:
                    dictionary[word] = wordCount
                    wordCount += 1

                # Add word to xt
                xt.append(word)


        # Add tuple to the set
        if len(xt) > 0:
            localSet.append((xt, yt))
            nSet += 1

# Return the generated set and the counters


    return localSet, nSet, pSet


def experiment(wt_set, set,nn):
    # Keep count of matches and mismatches
    matches = 0
    mismatches = 0
    truePositives = 0
    trueNegatives = 0
    predictedPositives = 0
    predictedNegatives = 0

    # For each entry t in the testing data set
    for xt, yt in wt_set:

        # Calculate the dot product
        y = nn.predict(xt)
        if y == 1:
            predictedPositives += 1
        elif y == 0:
            predictedNegatives += 1
        # Update the respective counter
        # outputs_file.write("({}, {}, {})\n".format(yt[0],y,nn.get_output_layer()[0]))

        if y == yt[0]:
            matches += 1
            if y == 1:
                truePositives += 1
            else:
                trueNegatives += 1
        else:
            mismatches += 1

    # Calculate metrics
    accuracy = (float(truePositives) / float(set[2])) * (float(trueNegatives) / float((set[1] - set[2])))
    precisionPos = float(truePositives) / float(predictedPositives) if predictedPositives > 0 else 0
    recallPos = float(truePositives) / float(set[2])
    averagePos = (precisionPos + recallPos) / 2.0
    fScorePos = (2.0 * precisionPos * recallPos) / (precisionPos + recallPos)  if (precisionPos + recallPos) > 0 else 0

    precisionNeg = float(trueNegatives) / float(predictedNegatives) if predictedNegatives > 0 else 0
    recallNeg = float(trueNegatives) / float((set[1] - set[2]))
    averageNeg = (precisionNeg + recallNeg) / 2.0
    fScoreNeg = (2.0 * precisionNeg * recallNeg) / (precisionNeg + recallNeg) if (precisionNeg + recallNeg) > 0 else 0


    precision = (float(truePositives) + float(trueNegatives)) / (float(predictedPositives) + float(predictedNegatives))
    recall = (float(truePositives) + float(trueNegatives)) / float(set[1])
    average = (precision + recall) / 2.0
    fScore = (2.0 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0


    # Print results
    print ("MATCHES: ", matches)
    print ("MISMATCHES: ", mismatches)
    print ("TRUE POSITIVES: ", truePositives)
    print ("TRUE NEGATIVES: ", trueNegatives)
    print ("PREDICTED POSITIVES: ", predictedPositives)
    print ("PREDICTED NEGATIVES: ", predictedNegatives)
    print ("ACTUAL POSITIVES: ", set[2])
    print ("ACTUAL NEGATIVES: ", set[1] - set[2])
    print ("ACCURACY: ", accuracy)
    print ("PRECISION (POS): ", precisionPos)
    print ("RECALL (POS): ", recallPos)
    print ("AVERAGE (POS): ", averagePos)
    print ("F-SCORE (POS): ", fScorePos)
    print ("PRECISION (NEG): ", precisionNeg)
    print ("RECALL (NEG): ", recallNeg)
    print ("AVERAGE (NEG): ", averageNeg)
    print ("F-SCORE (NEG): ", fScoreNeg)
    print ("PRECISION: ", precision)
    print ("RECALL: ", recall)
    print ("AVERAGE: ", average)
    print ("F-SCORE: ", fScore)
    print ("")

    global indexRow
    tIndexRow = indexRow
    tIndexRow +=1
    tRow = row.copy()
    tRow[fieldnames[tIndexRow]] = matches
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = mismatches
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = truePositives
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = trueNegatives
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = predictedPositives
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = predictedNegatives
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = set[2]
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = set[1] - set[2]
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = accuracy
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = precisionPos
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = recallPos
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = averagePos
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = fScorePos
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = precisionNeg
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = recallNeg
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = averageNeg
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = fScoreNeg
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = precision
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = recall
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = average
    tIndexRow += 1
    tRow[fieldnames[tIndexRow]] = fScore
    writer.writerow(tRow)




def main(trainSentences, testSentences, featureSet, maxIterations, learningRate=1):
    # outputs_file = open("backpropagation_outputs_{}_{}_{}.txt".format(featureSet,maxIterations,learningRate), 'w')
    global indexRow
    print("Max iterations: " + str(maxIterations))
    row[fieldnames[indexRow]] = maxIterations
    indexRow +=1
    if(featureSet == 1):
        print("Feature set: UNIGRAMS")
        row[fieldnames[indexRow]] = "UNIGRAMS"
        indexRow += 1
    elif(featureSet == 2):
        print("Feature set: BIGRAMS")
        row[fieldnames[indexRow]] = "BIGRAMS"
        indexRow += 1
    elif(featureSet == 3 or featureSet == 4 or featureSet == 5 or featureSet == 6):
        print("Feature set: " + str(featureSet) + "-GRAMS")
        row[fieldnames[indexRow]] = str(featureSet) + "-GRAMS"
        indexRow += 1
    elif(featureSet == 8):
        print("Feature set: UNIGRAMS + BIGRAMS")
        row[fieldnames[indexRow]] = "UNI+BI-GRAMS"
        indexRow += 1
    else:
        print("Feature set: UNIGRAMS + BIGRAMS + 3-GRAMS + 4-GRAMS + 5-GRAMS + 6-GRAMS")
        row[fieldnames[indexRow]] = "1to6-GRAMS"
        indexRow += 1
    print("Learning rate: " + str(learningRate))
    row[fieldnames[indexRow]] = learningRate
    indexRow += 1
    print("")

    training = buildSet(trainSentences, featureSet)
    testing = buildSet(testSentences, featureSet, 0)

    nWords = len(dictionary)
    wt = numpy.array(array([0] * nWords), dtype=numpy.float64)

    wet = array([0] * len(wt))
    training_sets = []

    for xt,yt in training[0]:
        wet = [0] * wet
        for word in xt:
            wet[dictionary[word]] = 1
        if yt == 1:
            training_sets.append([wet, [1]])
        elif yt == -1:
            training_sets.append([wet, [0]])


    print("end")

    # nn = NeuralNetwork(len(training_sets[0][0]), num_hidden, len(training_sets[0][1]),
    #  hidden_layer_weights=1.0, hidden_layer_bias=0.7,  output_layer_weights =1.0, output_layer_bias=0.3)

    num_hidden = 5

    nn = NeuralNetwork(len(training_sets[0][0]), num_hidden, len(training_sets[0][1]),
                       hidden_layer_bias=0.7, output_layer_bias=0.3)
    nn.LEARNING_RATE = learningRate

    calculate_total_errors = []

    for iteration in range(0, maxIterations):
        # for training_inputs, training_outputs in training_sets:
        for i in range(len(training_sets)):
            training_inputs, training_outputs = random.choice(training_sets)
            nn.train(training_inputs, training_outputs)
        print("{} - {} - {} - {}".format(featureSet,maxIterations, learningRate, iteration))
        #total_error = nn.calculate_total_error(training_sets)
        #calculate_total_errors.append(total_error)
        #print("{}: calculate_total_error_training: {}".format(iteration, total_error))
        #if(calculate_total_errors[0] - calculate_total_errors[iteration-1] < 1 and iteration > 30):
        #    break
        #if total_error == 0:
        #    break;


    print("")
    # Show performance results for the training set
    print ("+-------------------------------+")
    print ("| PERFORMANCE FOR TRAINING SET  |")
    print ("+-------------------------------+")
    print ("")
    row[fieldnames[indexRow]] = "Training"
    #indexRow += 1
    #row[fieldnames[indexRow]] = calculate_total_errors[len(calculate_total_errors)-1]
    # outputs_file.write("\nTraining\n")
    experiment(training_sets, training, nn)

    # Show performance results for the testing set
    print ("+------------------------------+")
    print ("| PERFORMANCE FOR TESTING SET  |")
    print ("+------------------------------+")
    print ("")

    testing_sets = []

    for xt, yt in testing[0]:
        wet = [0] * wet
        for word in xt:
            if word in dictionary:
                wet[dictionary[word]] = 1
        if yt == 1:
            testing_sets.append([wet, [1]])
        elif yt == -1:
            testing_sets.append([wet, [0]])

    #total_error_test = nn.calculate_total_error(testing_sets)
    row[fieldnames[indexRow]] = "Test"
    #row[fieldnames[indexRow]] = total_error_test
    # outputs_file.write("\nTesting\n")
    experiment(testing_sets, testing, nn)
    #print("calculate_total_error_testing: {}".format(total_error_test))

    # outputs_file.write("\n")



def setArg(trainSentences, testSentences, grams, iteration , learningRate):
    global indexRow
    global csvfile
    global writer
    csvfile = open("backpropagation_output_table.csv", 'a')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    main(trainSentences, testSentences, grams, iteration, learningRate)
    dictionary.clear()
    row.clear()
    indexRow = 0
    csvfile.close()

if __name__ == '__main__':
    print ("Algorithm: BACK PROPAGATION")
    csvfile = open("backpropagation_output_table.csv", 'a')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    csvfile.close()
    _Sentences = read_file()

    posCutoff = int(math.floor(len(_Sentences[0]) * 3 / 4))
    negCutoff = int(math.floor(len(_Sentences[1]) * 3 / 4))
    trainSentences = _Sentences[0][:posCutoff] + _Sentences[1][:negCutoff]
    testSentences = _Sentences[0][posCutoff:] + _Sentences[1][negCutoff:]



    #setArg(trainSentences, testSentences, 1, 5000, 0.25)

    # setArg(trainSentences, testSentences, 2, 10, 1)
    #setArg(trainSentences, testSentences, 2, 100, 1)

    #setArg(trainSentences, testSentences, 2, 1000, 1)
    #setArg(trainSentences, testSentences, 2, 5000, 1)
    # setArg(trainSentences, testSentences, 2, 10, 0.75)
    #setArg(trainSentences, testSentences, 2, 100, 0.75)
    #setArg(trainSentences, testSentences, 2, 1000, 0.75)
    #setArg(trainSentences, testSentences, 2, 5000, 0.75)




    #setArg(trainSentences, testSentences, 2, 10, 0.5)
    #setArg(trainSentences, testSentences, 2, 100, 0.5)
    #setArg(trainSentences, testSentences, 2, 1000, 0.5)
    #setArg(trainSentences, testSentences, 2, 5000, 0.5)

    #setArg(trainSentences, testSentences, 2, 10, 0.25)
    #setArg(trainSentences, testSentences, 2, 100, 0.25)
    #setArg(trainSentences, testSentences, 2, 1000, 0.25)
    #setArg(trainSentences, testSentences, 2, 5000, 0.25)

    #setArg(trainSentences, testSentences, 3, 10, 1)
    #setArg(trainSentences, testSentences, 3, 100, 1)





    #setArg(trainSentences, testSentences, 3, 1000, 1)
    #setArg(trainSentences, testSentences, 3, 5000, 1)
    #setArg(trainSentences, testSentences, 3, 10, 0.75)
    #setArg(trainSentences, testSentences, 3, 100, 0.75)
    #setArg(trainSentences, testSentences, 3, 1000, 0.75)
    #setArg(trainSentences, testSentences, 3, 5000, 0.75)

    #setArg(trainSentences, testSentences, 3, 10, 0.5)
    #setArg(trainSentences, testSentences, 3, 100, 0.5)
    #setArg(trainSentences, testSentences, 3, 1000, 0.5)
    #setArg(trainSentences, testSentences, 3, 5000, 0.5)

    #setArg(trainSentences, testSentences, 3, 10, 0.25)
    #setArg(trainSentences, testSentences, 3, 100, 0.25)
    #setArg(trainSentences, testSentences, 3, 1000, 0.25)
    #setArg(trainSentences, testSentences, 3, 5000, 0.25)

    #setArg(trainSentences, testSentences, 4, 10, 1)
    #setArg(trainSentences, testSentences, 4, 100, 1)

    #setArg(trainSentences, testSentences, 4, 1000, 1)
    #setArg(trainSentences, testSentences, 4, 5000, 1)
    #setArg(trainSentences, testSentences, 4, 10, 0.75)
    #setArg(trainSentences, testSentences, 4, 100, 0.75)
    #setArg(trainSentences, testSentences, 4, 1000, 0.75)
    #setArg(trainSentences, testSentences, 4, 5000, 0.75)

    #setArg(trainSentences, testSentences, 4, 10, 0.5)
    #setArg(trainSentences, testSentences, 4, 100, 0.5)
    #setArg(trainSentences, testSentences, 4, 1000, 0.5)
    #setArg(trainSentences, testSentences, 4, 5000, 0.5)

    #setArg(trainSentences, testSentences, 4, 10, 0.25)
    #setArg(trainSentences, testSentences, 4, 100, 0.25)
    #setArg(trainSentences, testSentences, 4, 1000, 0.25)
    #setArg(trainSentences, testSentences, 4, 5000, 0.25)

    #setArg(trainSentences, testSentences, 5, 10, 1)
    #setArg(trainSentences, testSentences, 5, 100, 1)

    #setArg(trainSentences, testSentences, 5, 1000, 1)
    #setArg(trainSentences, testSentences, 5, 5000, 1)

    #setArg(trainSentences, testSentences, 5, 10, 0.75)
    #setArg(trainSentences, testSentences, 5, 100, 0.75)
    #setArg(trainSentences, testSentences, 5, 1000, 0.75)
    #setArg(trainSentences, testSentences, 5, 5000, 0.75)

    #setArg(trainSentences, testSentences, 5, 10, 0.5)
    #setArg(trainSentences, testSentences, 5, 100, 0.5)
    #setArg(trainSentences, testSentences, 5, 1000, 0.5)
    #setArg(trainSentences, testSentences, 5, 5000, 0.5)

    #setArg(trainSentences, testSentences, 5, 10, 0.25)
    #setArg(trainSentences, testSentences, 5, 100, 0.25)
    #setArg(trainSentences, testSentences, 5, 1000, 0.25)
    #setArg(trainSentences, testSentences, 5, 5000, 0.25)

    #setArg(trainSentences, testSentences, 6, 10, 1)
    #setArg(trainSentences, testSentences, 6, 100, 1)

    #setArg(trainSentences, testSentences, 6, 1000, 1)
    #setArg(trainSentences, testSentences, 6, 5000, 1)

    #setArg(trainSentences, testSentences, 6, 10, 0.75)
    #setArg(trainSentences, testSentences, 6, 100, 0.75)
    #setArg(trainSentences, testSentences, 6, 1000, 0.75)
    #setArg(trainSentences, testSentences, 6, 5000, 0.75)

    #setArg(trainSentences, testSentences, 6, 10, 0.5)
    #setArg(trainSentences, testSentences, 6, 100, 0.5)
    #setArg(trainSentences, testSentences, 6, 1000, 0.5)
    #setArg(trainSentences, testSentences, 6, 5000, 0.5)

    #setArg(trainSentences, testSentences, 6, 10, 0.25)
    #setArg(trainSentences, testSentences, 6, 100, 0.25)
    #setArg(trainSentences, testSentences, 6, 1000, 0.25)
    #setArg(trainSentences, testSentences, 6, 5000, 0.25)

    #setArg(trainSentences, testSentences, 7, 10, 1)
    #setArg(trainSentences, testSentences, 7, 100, 1)

    #setArg(trainSentences, testSentences, 7, 1000, 1)
    #setArg(trainSentences, testSentences, 7, 5000, 1)

    #setArg(trainSentences, testSentences, 7, 10, 0.75)
    #setArg(trainSentences, testSentences, 7, 100, 0.75)
    #setArg(trainSentences, testSentences, 7, 1000, 0.75)
    #setArg(trainSentences, testSentences, 7, 5000, 0.75)

    #setArg(trainSentences, testSentences, 7, 10, 0.5)
    #setArg(trainSentences, testSentences, 7, 100, 0.5)
    #setArg(trainSentences, testSentences, 7, 1000, 0.5)
    #setArg(trainSentences, testSentences, 7, 5000, 0.5)

    #setArg(trainSentences, testSentences, 7, 10, 0.25)
    #setArg(trainSentences, testSentences, 7, 100, 0.25)
    #setArg(trainSentences, testSentences, 7, 1000, 0.25)
    #setArg(trainSentences, testSentences, 7, 5000, 0.25)
    
    
    
    setArg(trainSentences, testSentences, 8, 10, 1)
    setArg(trainSentences, testSentences, 8, 100, 1)
    setArg(trainSentences, testSentences, 8, 1000, 1)
    # setArg(trainSentences, testSentences, 8, 5000, 1)
    #
    # setArg(trainSentences, testSentences, 8, 10, 0.75)
    # setArg(trainSentences, testSentences, 8, 100, 0.75)
    # setArg(trainSentences, testSentences, 8, 1000, 0.75)
    # setArg(trainSentences, testSentences, 8, 5000, 0.75)
    #
    # setArg(trainSentences, testSentences, 8, 10, 0.5)
    # setArg(trainSentences, testSentences, 8, 100, 0.5)
    # setArg(trainSentences, testSentences, 8, 1000, 0.5)
    # setArg(trainSentences, testSentences, 8, 5000, 0.5)
    #
    # setArg(trainSentences, testSentences, 8, 10, 0.25)
    # setArg(trainSentences, testSentences, 8, 100, 0.25)
    # setArg(trainSentences, testSentences, 8, 1000, 0.25)
    # setArg(trainSentences, testSentences, 8, 5000, 0.25)

    '''
    N = nWords
    c1 = [2, 2]
    c2 = [2, -2]
    cv = [[0.5, 0.3], [0.3, 0.5]]
    d1 = np.random.multivariate_normal(c1, cv, N/2)
    d2 = np.random.multivariate_normal(c2, cv, N/2)
    D = np.vstack((d1, d2)) # join tow array

    label = np.zeros(len(D))
    for k in range(N):
        if k<N/2:
            label[k] = 1
        else:
            label[k] = -1
    '''

    '''
    pyl.ion()
    pyl.figure(1)
    pyl.clf()
    chk = pyl.where(label!=labeld)[0]
    for n in chk:
        pyl.scatter(D[n,0], D[n,1], s=80, c='g', marker='o')

    x = d1[:,0]
    y = d1[:,1]
    pyl.scatter(x, y, c='b', marker='o')

    x = d2[:,0]
    y = d2[:,1]
    pyl.scatter(x, y, c='r', marker='o')

    pyl.figure(2)
    pyl.clf()
    pyl.plot(res)

    pyl.figure(3)
    x = input()
    '''
