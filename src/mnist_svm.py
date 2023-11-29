"""
mnist_svm
~~~~~~~~~

A classifier program for recognizing handwritten digits from the MNIST
data set, using an SVM classifier."""

#### Libraries
# My libraries
import mnist_loader 

# Third-party libraries
from sklearn import svm

def svm_baseline():
    training_data, validation_data, test_data = mnist_loader.load_data()
    # train
    clf = svm.SVC()
    clf.fit(training_data[0], training_data[1])
    # test
    predictions = [int(a) for a in clf.predict(test_data[0])]
    num_correct = sum(int(a == y) for a, y in zip(predictions, test_data[1]))
    print("Baseline classifier using an SVM.")
<<<<<<< HEAD
    print("%s of %s values correct." % (num_correct, len(test_data[1])))
=======
    print(str(num_correct) + " of " + str(len(test_data[1])) + " values correct.")
>>>>>>> 4dbac93ec68063f0dd08e0e8c882eed51ee57fc4

if __name__ == "__main__":
    svm_baseline()
    
