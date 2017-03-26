# Multiple Linear Regression

# Importing the dataset

mlrdata <- read.csv('50_Startups.csv')
head(mlrdata)

# Encoding categorical data
mlrdata$State <- factor(mlrdata$State,
                        levels = c('New York', 'California','Florida'),
                        labels = c(1,2,3))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split <- sample.split(mlrdata$Profit, SplitRatio = 0.8)
mlrtrain <- subset(mlrdata, split == T)
mlrtest <- subset(mlrdata, split == F)

#Fitting Multiple Linear Regression to the Training set

# formula (Dipendent variable ~ Indipendent variables)
mlrreg <- lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
             data = mlrtrain)

# or We can use '.' insted of writeing all Indipendent variables.
mlrreg <- lm(formula = Profit ~ ., data = mlrtrain)

summary(mlrreg)

# Predicting the Test set results

mlr_pred <- predict(mlrreg, newdata = mlrtest)
mlr_pred
mlrtest

# Building the optimal model using Backward Elimination

mlrreg <- lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
             data = mlrtrain)
summary(mlrreg)

#-------------------------------------------------------------------------------------------------------------
# Optional Step: Remove State2 only (as opposed to removing State directly)
mlrreg = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + factor(State, exclude = 2),
               data = mlrtrain)
summary(mlrreg)

# Optional Step: Remove State2 only (as opposed to removing State directly)
mlrreg = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + factor(State, exclude = c(4,5,6,7,8,9,10)),
               data = mlrtrain)
summary(mlrreg)
#-------------------------------------------------------------------------------------------------------------

mlrreg <- lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
             data = mlrtrain)
summary(mlrreg)

mlrreg <- lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
             data = mlrtrain)
summary(mlrreg)

mlrreg <- lm(formula = Profit ~ R.D.Spend,
             data = mlrtrain)
summary(mlrreg)

# Visualising the Training set results
#install.packages('ggplot2')
library(ggplot2)

ggplot() +
  geom_point(aes(x = mlrtrain$R.D.Spend, y = mlrtrain$Profit),
             colour = 'red') + 
  stat_smooth(mapping = aes(x = mlrtrain$R.D.Spend, y = mlrtrain$Profit),
              method = 'lm',colour = 'blue') +
  geom_line(aes(x = mlrtrain$R.D.Spend, y = predict(mlrreg, newdata = mlrtrain)),
            colour = 'blue') + 
  ggtitle('Startup companys Profit') +
  xlab('R.D.Spend') +
  ylab('Profit')

# Visualising the Test set results
library(ggplot2)

ggplot() +
  geom_point(aes(x = mlrtest$R.D.Spend, y = mlrtest$Profit),
             colour = 'red') + 
  stat_smooth(mapping = aes(x = mlrtest$R.D.Spend, y = mlrtest$Profit),
              method = 'lm',colour = 'blue') +
  geom_line(aes(x = mlrtest$R.D.Spend, y = predict(mlrreg, newdata = mlrtest)),
            colour = 'blue') + 
  ggtitle('Startup companys Profit') +
  xlab('R.D.Spend') +
  ylab('Profit')

