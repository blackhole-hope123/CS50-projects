## Description

This project is the week 5 project. The program uses tensorflow to build a Convolutional Neural Network (CNN) to classify traffic signs.

## How It Works

1.	The program loads a data, and convert them to numpy arrays.
2.	A CNN is developped with tensorflow, and it learns the pattern of the training data with a total of 10 epochs.
3.	After the training, the CNN made a series of predictions on the test data and these are compared with the actual labels.

## Running the Program

1.	Clone the repository:
```bash
git clone https://github.com/blackhole-hope123/CS50-projects.git
cd path/CS50-projects/traffic
```

2. Install required packages

```
pip3 install -r requirements.txt
```

3.	Run the program:

```
python traffic.py gtsrb 
```

Sample output:
![Graph Description](results/results%20with%20mean%20subtraction%20and%20normalization,%20also%20with%20nadam%20optimizer.PNG)

## Important observance
1. The test accuracy when the data is not preprocessed is only 5.5%. However, after mean subtraction and normalization, the test accuracy soared to 98.5%, as shown below:
   ![Graph Description](results/results%20with%20mean%20subtraction%20and%20normalization,%20also%20with%20nadam%20optimizer.PNG)
    *With data preprocessing*
   ![Graph Description](results/without%20mean%20subtraction%20and%20normalization.PNG)
    *Without data preprocessing*
2. The adam optimizer and nadam optimizer show almost no difference in the final test accuracy when the data are preprocessed, since they both stem from the momentum update with flexible learning rates.
   ![Graph Description](results/results%20with%20mean%20subtraction%20and%20normalization,%20also%20with%20nadam%20optimizer.PNG)
   *Adam optimizer*
   ![Graph Description](results/With%20adam%20optimizer.PNG)
   *Nadam optimizer*
3. The test accuracy is stable at 95% when the dropout rate is between 0.1 to 0.8, but then it tumbles to below 10% when the dropout rate is 0.9, potentially because the capacity of the neural network is too low.
   ![Graph Description](results/accuracy%20versus%20dropout%20rate.png)

   
## File Structure

-	results: A folder containing the results of the above important observations.
-	README.md: Project documentation.
-	requirements.txt : required packages to run the program.
-	traffic_with_preprocessings_nadam_optimizer_dropout_rate_0.5.py: The optimal setting for the neural network, also served as the control group.
-	traffic_dropout_rate_comparisons.py: experiment on the relation of the test accuracies and dropout rates.
-	traffic_with_adam_optimizer.py: optimizer is changed to adam, with everything else the same as the control group.
-	traffic_without_preprocessings.py: data preprocessing is removed, with everything else the same as the control group.

## Concepts Used 
-	Layer structure of CNN: covolutional layers, pooling layers, flatten layers, fully-connected layers
-	Weight initializations: the univariate Gaussian initialization.
-	Regularization methods: L2 regularization and dropout
-	Activation function: ReLu, Softmax.

## Acknowledgement 
This project is part of CS50’s AI Course by Harvard University.
