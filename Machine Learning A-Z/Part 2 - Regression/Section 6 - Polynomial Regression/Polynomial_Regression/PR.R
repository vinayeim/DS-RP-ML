# Polynomial Regression

# Importing the dataset
prsal <- read.csv('Position_Salaries.csv')
prsal <- prsal[2:3]
prsal

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$DependentVariable, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Fitting Linear Regression to the dataset
lin_reg <- lm(formula = Salary ~ .,
              data = prsal)
summary(lin_reg)

# Fitting Polynomial Regression to the dataset
prsal$Level2 <- prsal$Level^2
prsal$Level3 <- prsal$Level^3
prsal$Level4 <- prsal$Level^4

poly_reg <- lm(formula = Salary ~ .,
               data = prsal)
summary(poly_reg)

# Visualising the Linear Regression results
ggplot() +
  geom_point(aes(x = prsal$Level, y = prsal$Salary),
             color = 'red') + 
  geom_line(aes(x = prsal$Level, y = predict(lin_reg, newdata = prsal)),
            color = 'blue') + 
  ggtitle('Truth or Bluff (Liner regression)') + 
  xlab('Leval') + ylab('Salary')

# Visualising the Polynomial Regression results

ggplot() +
  geom_point(aes(x = prsal$Level, y = prsal$Salary),
             color = 'red') + 
  geom_line(aes(x = prsal$Level, y = predict(poly_reg, newdata = prsal)),
            color = 'blue') + 
  ggtitle('Truth or Bluff (Polynomial regression)') + 
  xlab('Leval') + ylab('Salary')

# Predicting a new result with Linear Regression
predict(lin_reg,data.frame(Level = 6.5))

# Predicting a new result with Polynomial Regression
predict(poly_reg,data.frame(Level = 6.5,
                            Level2 = 6.5^2,
                            Level3 = 6.5^3,
                            Level4 = 6.5^4))


# Easier way to create polynomial regression

poly_reg4 <- lm(formula= Salary ~ poly(Level, 4), 
              data=prsal)
predict(poly_reg4, data.frame(Level =6.5))