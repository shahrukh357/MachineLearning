# tvarit challenge

Our approach:

The target variables y1 and y2 are binned to create 3 and 5 classes respectively. The idea is to predict the value range of the target variable for the test data rather than the actual value. This problem is thus transformed into multi-class classification.

Data binning logic for target variables is as follows:

y1 is binned into 3 classes:

class 1: 0<=5.11

class 2: 5.11<=10.11

class 3: 10.11<=15.11

y2 is binned into 5 classes:

class 1: -1.7<=-1.02

class 2: -1.02<=-0.34

class 3: -0.34<=0.34

class 4: 0.34<=1.02

class 5: 1.02<=1.7

The sensor data for each sensor is aggeregated for one batch by averaging. i.e x0_t0 to x0_t6 is averaged as avg0. These averaged values are used to train the model, hence reducing the dimentionality.

Steps for executing:

1. run data_processing.py file on data.csv file to obtain modelreadyfortraining.pkl file, which will be used to solve the problems.

2. run problem_1.py (gives accuracy for problem 1)

3. run problem_2.py (gives accuracy for problem 2)

4. run problem_3.py (gives accuracy for problem 3)

The accuracy score of all the problems is given in results.md
