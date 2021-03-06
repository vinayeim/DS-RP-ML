# Simple linear regression

# Importing the dataset
dataset <- read.csv('Salary_Data.csv')
dataset

# Splitting the dataset into the Training set and Test set
#install.packages('caTools')
library(caTools)

set.seed(123)
split <- sample.split(dataset$Salary, SplitRatio = 2/3)
split
training_set <- subset(dataset, split == T)
test_set <- subset(dataset, split == F)
training_set
test_set

# Feature Scaling

# training_set[,2:3] <- scale(training_set[,2:3])
# test_set[,2:3] <- scale(test_set[,2:3])
# training_set
# test_set

# Fitting Simple linear regression to the Training set

regressor <- lm(formula = Salary ~ YearsExperience, 
                data = training_set)
summary(regressor)

# Predicting the Test set results

y_pred <- predict(regressor, newdata = test_set)
y_pred

# Visualising the Training set results
#install.packages('ggplot2')
library(ggplot2)

ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') + 
  stat_smooth(mapping = aes(x = training_set$YearsExperience, y = training_set$Salary),
              method = 'lm',colour = 'blue') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') + 
  ggtitle('Salary vs Experience (Training set)') +
  xlab('Years of experience') +
  ylab('Salary')

# Visualising the Test set results
library(ggplot2)

ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') + 
  ggtitle('Salary vs Experience (Training set)') +
  xlab('Years of experience') +
  ylab('Salary')
