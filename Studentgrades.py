# import libraries for use
library(dplyr)
library(caret)
library(tidyverse)
library(tibble)
library(car) 
library(ggplot2)
library(PerformanceAnalytics)
library(naniar)
library(rpart)
library(rpart.plot)
library(e1071)
library(corrplot)
library(factoextra)
library(party)
library(ggcorrplot)

## import data
student_grades <- read.csv("student_grades.csv", header = TRUE)
View(student_grades)

#to check data dimension
dim(student_grades)

#to see the structure of data
str(student_grades)

#to see data summary i.e data type and mean, IQR etc
summary(student_grades)

# to extract feature names from data (e.g from student_grades$data to just data)
attach(student_grades)

# convert data to data frame
as.data.frame(student_grades) 
head(student_grades)

#insert data into tibble
grades_tibble <- as_tibble(student_grades)

## data exploration

#determine the range of values in a feature
range(student_grades$age)
range(student_grades$absences)

# find the central tendency (median) of the age & absences dataset
median(student_grades$age, na.rm = TRUE)
median(student_grades$absences, na.rm = TRUE)
mean(student_grades$absences)

mean(student_grades$age)
sd(student_grades$age)
sd_variance <- (sd(student_grades$age)^2)
sd_variance
plot(x = student_grades$failures, y = student_grades$Pass)
abline(lm(student_grades$failures ~ student_grades$Pass), col = "blue")

# missing data
sum(is.na(student_grades))
vis_miss(student_grades)
mcar_test(student_grades)

#check for duplicates in the data
dim(student_grades[duplicated(student_grades),])

#change missing values to na
student_grades$Medu[student_grades$Medu == 0] <- NA
student_grades$Fedu[student_grades$Fedu == 0] <- NA

#find mean of Medu and Fedu
medu_median <- as.integer(median(Medu))
fedu_median <- as.integer(median(Fedu))

#replace na in Medu and Fedu with the mean values
student_grades$Medu[student_grades$Medu == NA] <- medu_median
student_grades$Fedu[student_grades$Fedu == NA] <- fedu_median

#find correlation in dataset
chart.Correlation(student_grades)

# find and remove outliers from data (changed my mind as unnecessary)
#student_grades <- filter(student_grades, age > 0 & age < 21)
#student_grades <- filter(student_grades, absences > 0 & absences <= 40)

#to remove school & sex features from dataset(changed my mind about this too)
#student_grades <- student_grades[-1]

#create boxplots to see relationship between data
boxplot(student_grades$age ~ Pass, main = "Data distribution of age variable", xlab = "Pass", ylab = "Age")
boxplot(student_grades$absences ~ Pass, main = "Data distribution of absences variable", xlab = "Pass", ylab = "Absences")
boxplot(student_grades$Medu ~ Pass)
boxplot(student_grades$Fedu ~ Pass)
boxplot(student_grades$Mjob ~ Pass)
boxplot(student_grades$Fjob ~ Pass)
boxplot(student_grades$failures ~ Pass, main = "Boxplot of failures variable", xlab = "Pass", ylab = "Failures")

boxplot(student_grades$Walc ~ Pass, main = "Boxplot of weekend alcohol consumption", xlab = "Pass", ylab = "weekend alcohol consumption")
boxplot(student_grades$schoolsup ~ Pass, main = "Boxplot of school support", xlab = "Pass", ylab = "School support")
boxplot(student_grades$higher ~ Pass, main = "Boxplot of higher variable", xlab = "Pass", ylab = "Higher")
boxplot(student_grades$sex ~ Pass, main = "Data distribution of sex variable", xlab = "Pass", ylab = "sex")
boxplot(student_grades$age ~ Pass)
boxplot(student_grades$studytime ~ Pass, main = "Boxplot illustrating studytime", xlab = "Pass", ylab = "Study time")
boxplot(student_grades$traveltime ~ Pass)
boxplot(student_grades$address ~ traveltime, main = "Relationship between address and traveltime", xlab = "Travel time", ylab = "Address")
boxplot(health ~ Pass, main = "Boxplot of students' health", xlab = "Pass", ylab = "Health")
boxplot(Dalc ~ Pass, main = "Boxplot of weekday alcohol consumption", xlab = "Pass", ylab = "weekday alcohol consumption")
boxplot(famrel ~ Pass, main = "Boxplot of family relationship", xlab = "Pass", ylab = "Family relationship")
boxplot(student_grades$school ~ Pass, main = "Boxplot of school variable", xlab = "Pass", ylab = "School")
boxplot(student_grades$famsize~Pass, main = "Boxplot of family size", xlab = "Pass", ylab = "Family size")
boxplot(student_grades$reason ~ Pass, main = "Boxplot of reason variable", xlab = "Pass", ylab = "Reason")
boxplot(student_grades$famsup ~ Pass, main = "Boxplot of Family support variable", xlab = "Pass", ylab = "Family support")
boxplot(student_grades$paid ~ Pass, main = "Boxplot of reason variable", xlab = "Pass", ylab = "Paid support")
boxplot(student_grades$activities ~ Pass, main = "Boxplot of acitvities variable", xlab = "Pass", ylab = "Activities")
boxplot(student_grades$internet ~ Pass, main = "Boxplot of internet variable", xlab = "Pass", ylab = "Internet")
boxplot(student_grades$romantic ~ Pass, main = "Boxplot of 'romantic' variable", xlab = "Pass", ylab = "Romantic")
boxplot(student_grades$Pstatus ~ Pass, main = "Boxplot of parents' status", xlab = "Pass", ylab = "Parents' status")
boxplot(student_grades$guardian ~ Pass, main = "Boxplot of guardian variable", xlab = "Pass", ylab = "Guardian")
boxplot(student_grades$freetime ~ Pass, main = "Boxplot of free time", xlab = "Pass", ylab = "Free time")
boxplot(student_grades$goout ~ Pass, main = "Boxplot of going out patterns", xlab = "Pass", ylab = "Go out")
boxplot(student_grades$nursery ~ Pass, main = "Boxplot of nursery variable", xlab = "Pass", ylab = "Nursery")

# convert 13 features to binary values
student_grades$sex <- ifelse(student_grades$sex == "F", 0, 1)
student_grades$address <- ifelse(student_grades$address == "U", 0, 1)
student_grades$famsize <- ifelse(student_grades$famsize == "LE3", 0, 1)
student_grades$Pstatus <- ifelse(student_grades$Pstatus == "A", 0, 1)
student_grades$guardian <- ifelse(student_grades$guardian == "mother", 0, 1)
student_grades$schoolsup <- ifelse(student_grades$schoolsup == "yes", 0, 1)
student_grades$famsup <- ifelse(student_grades$famsup == "yes", 0, 1)
student_grades$paid <- ifelse(student_grades$paid == "yes", 0, 1)
student_grades$activities <- ifelse(student_grades$activities == "yes", 0, 1)
student_grades$nursery <- ifelse(student_grades$nursery == "yes", 0, 1)
student_grades$higher <- ifelse(student_grades$higher == "yes", 0, 1)
student_grades$internet <- ifelse(student_grades$internet == "yes", 0, 1)
student_grades$romantic <- ifelse(student_grades$romantic == "yes", 0, 1)

#convert nominal data to numerical
student_grades$Mjob <- as.numeric(as.factor(student_grades$Mjob))
student_grades$Fjob <- as.numeric(as.factor(student_grades$Fjob))
student_grades$reason <- as.numeric(as.factor(student_grades$reason))

#use histogram to find distribution of features
hist(Pass)
hist(student_grades$absences, main = "Histogram of student absences", xlab = "Absences", ylab = "Frequency")
hist(student_grades$age, main = "Histogram of age variable", xlab = "Age", ylab = "Frequency")
hist(student_grades$Medu, main = "Histogram showing data distribution of Mother's education", xlab = "Mother's education", ylab = "Frequency")
sum(student_grades$Medu == 0)
hist(student_grades$Fedu, main = "Histogram showing data distribution of Father's education", xlab = "Father's education", ylab = "Frequency")
sum(student_grades$Fedu == 0)
hist(student_grades$Mjob)
hist(student_grades$Fjob)
hist(student_grades$reason, main = "Histogram of reason variable", xlab = "Reason", ylab = "Frequency")
hist(student_grades$famrel, main = "Distribution of family relationship", xlab = "Family relationship", ylab = "Frequency")
hist(student_grades$freetime, main = "Boxplot of free time", xlab = "Free time", ylab = "Frequency")
hist(student_grades$Dalc, main = "Histogram showing weekday alcohol consumption", xlab = "weekday alcohol consumption", ylab = "Frequency")
hist(student_grades$Walc, main = "Histogram showing weekend alcohol consumption", xlab = "Weekend alcohol consumption", ylab = "Frequency")
hist(student_grades$health, main = "Histogram of students' health", xlab = "Health", ylab = "Frequency")
hist(student_grades$studytime, main = "Histogram showing studytime distribution", xlab = "Study time", ylab = "Frequency")
hist(student_grades$failures, main = "Histogram of failures variable", xlab = "Failures", ylab = "Frequency")
hist(student_grades$famsize, main = "Histogram of family size", xlab = "Family size", ylab = "Frequency")
hist(student_grades$internet, main = "Histogram of internet variable", xlab = "Internet", ylab = "Frequency")
hist(student_grades$higher, main = "Histogram of higher variable", xlab = "Higher", ylab = "Frequency")
hist(student_grades$romantic, main = "Histogram of 'romantic' variable", xlab = "Romantic", ylab = "Frequency")
hist(student_grades$Pstatus, main = "Histogram of parents status", xlab = "Parents' status", ylab = "Frequency")
hist(student_grades$guardian, main = "Histogram of guardian variable", xlab = "Guardian", ylab = "Frequency")
hist(student_grades$goout, main = "Histogram of students' going out patterns", xlab = "Go out", ylab = "Frequency")
hist(student_grades$school, main = "Histogram of school variable", xlab = "School", ylab = "Frequency")
hist(student_grades$sex, main = "Histogram of sex variable", xlab = "Sex", ylab = "Frequency")
hist(student_grades$activities, main = "Histogram of activities variable", xlab = "Activities", ylab = "Frequency")
hist(student_grades$nursery, main = "Histogram of nursery variable", xlab = "Nursery", ylab = "Frequency")
hist(student_grades$address, main = "Histogram of address variable", xlab = "Address", ylab = "Frequency")
hist(student_grades$traveltime, main = "Distribution of travel time variable", xlab = "Travel time", ylab = "Frequency")
hist(student_grades$schoolsup, main = "Histogram of school support variable", xlab = "School support", ylab = "Frequency")
hist(student_grades$famsup, main = "Histogram of family support variable", xlab = "Family support", ylab = "Frequency")
hist(student_grades$paid, main = "Distribution of Paid support variable", xlab = "Paid support", ylab = "Frequency")

#how frequently age appears in dataset
ggplot(data = student_grades) + geom_bar(mapping = aes(x = age))

#how frequently absences appears in dataset
ggplot(data = student_grades) + geom_bar(mapping = aes(x = absences), binwidth = 0.2)

#boxplot for absences
ggplot(data = student_grades) + geom_boxplot(mapping = aes(x = failures, y = absences, group = Pass), outlier.color = "red")

#then we compare age and absence with color set to Mjob
ggplot(data = student_grades) + geom_point(mapping = aes(x = age, y = absences, color = Mjob))

ggplot(data = student_grades) + geom_point(mapping = aes(x = age, y = absences, color = Fjob))

ggplot(data = student_grades) + geom_point(mapping = aes(x = age, y = absences, color = Medu))

ggplot(data = student_grades) + geom_point(mapping = aes(x = age, y = absences, color = Fedu))

ggplot(data = student_grades) + geom_point(mapping = aes(x = age, y = absences, color = freetime))

#next, use frequency plot to check for r/ship between age and absences & other features
ggplot(data = student_grades) + geom_count(mapping = aes(x = Pass, y = age))
ggplot(data = student_grades) + geom_count(mapping = aes(x = Pass, y = absences))
ggplot(data = student_grades) + geom_count(mapping = aes(x = Pass, y = failures))

#create correlation matrix
cor(student_grades)
ggcorrplot(cor(student_grades))

#use qqnorm to check whether certain assumptions have been met
qqnorm(student_grades$age)
qqline(student_grades$age, col = "red")

#feature engineering - combine a number of features (this is no longer important)

#feature engineering by combining variables
#student_grades$support <- student_grades$schoolsup + student_grades$famsup + student_grades$paid
#student_grades$extratime <- student_grades$freetime + student_grades$goout
#student_grades$alcohol <- student_grades$Walc + student_grades$Dalc
#student_grades$parentsedu <- student_grades$Medu + student_grades$Fedu

#replace variables
#student_grades$schoolsup <- student_grades$support
#student_grades$freetime <- student_grades$extratime
#student_grades$Walc <- student_grades$alcohol
#student_grades$Medu <- student_grades$parentsedu

# normalization
rs_function <- function(x){(x-min(x))/(max(x)-min(x))}
student_grades$absences <- rs_function(student_grades$absences)
student_grades$age <- rs_function(student_grades$age)
student_grades$Medu <- rs_function(student_grades$Medu)
student_grades$Fedu <- rs_function(student_grades$Fedu)
student_grades$failures <- rs_function(student_grades$failures)
student_grades$Mjob <- rs_function(student_grades$Mjob)
student_grades$Fjob <- rs_function(student_grades$Fjob)
student_grades$reason <- rs_function(student_grades$reason)
student_grades$guardian <- rs_function(student_grades$guardian)
student_grades$traveltime <- rs_function(student_grades$traveltime)
student_grades$studytime <- rs_function(student_grades$studytime)
student_grades$famrel <- rs_function(student_grades$famrel)
student_grades$freetime <- rs_function(student_grades$freetime)
student_grades$goout <- rs_function(student_grades$goout)
student_grades$Dalc <- rs_function(student_grades$Dalc)
student_grades$Walc <- rs_function(student_grades$Walc)
student_grades$health <- rs_function(student_grades$health)

pca_gradess <- student_grades

## Use PCA for feature selection
#pca_grades <- princomp(pca_gradess, cor = TRUE, scores = TRUE)
#fviz_eig(pca_grades)

#fviz_pca_var(pca_grades, col.var = "contrib", repel = TRUE)

#pca_grades
       
#use boruta for feature selection

#install.packages("Boruta")
#library("Boruta")

#boruta_output <- Boruta(Pass~ ., data=na.omit(student_grades), doTrace=1)  
#names(boruta_output)

#boruta_signif <- getSelectedAttributes(boruta_output, withTentative = TRUE)
#print(boruta_signif)  

#plot(boruta_output, cex.axis=.7, las=2, xlab="", main = "Variable Importance in Student Grades")

#use variable importance matrix for feature selection
set.seed(100)
rPartMod <- train(Pass ~ ., data=student_grades, method="rpart")
rpartImp <- varImp(rPartMod)
print(rpartImp)

# model building
model_grades <- lm(student_grades$age ~ student_grades$absences)
print(model_grades)

plot(x = student_grades$Pass, y = student_grades$failures)
abline(model_grades)

summary(model_grades)

# split data into train and test set
set.seed(42)
student_grades[,"train"] <- ifelse(runif(nrow(student_grades))<0.8, 1, 0)

trainset <- student_grades[student_grades$train == "1",]
testset <- student_grades[student_grades$train == "0",]

trainset <- trainset[-31]
testset <- testset[-31]

View(trainset)
View(testset)

## decision tree
grades_dtree <- rpart(Pass~., data = trainset, method = 'class')
rpart.plot(grades_dtree, extra = 106)

# test the decision tree

# remove the Pass variable
test_data <- testset[-30]

# generate the predicted values
tree_predict <- predict(grades_dtree, newdata = test_data, type = "class")

#confusion matrix to check accuracy
table(predicted = tree_predict, actual = testset$Pass)
mean(tree_predict == testset$Pass)

confusionMatrix(tree_predict, as.factor(testset$Pass), mode = "everything", positive="1")

## Random forest

#below, we train a forest model and store results in grades_forest
grades_forest <- cforest(Pass~., data = trainset, control = cforest_unbiased(mtry = 10, max_depth = 15), random_state = 42)

#apply the model to the testing data
rf_prob <- predict(grades_forest, newdata = test_data, type = "response")

#convert range of probabilistic values from above into values between 0 and 1
rf_pred <- ifelse(rf_prob > 0.5, 1, 0)

#confusion matrix
table(predicted = rf_pred, actual = testset$Pass)

#then calculate accuracy
mean(rf_pred == testset$Pass)

confusionMatrix(rf_pred, as.factor(testset$Pass), mode = "everything", positive="1")

## Naive Bayes

#once more, create another trainset to preserve integrity
naive_trainset <- trainset
nb_grades <- naiveBayes(Pass~., data = naive_trainset)

nb_predict <- predict(nb_grades, newdata = testset)

table(predicted = nb_predict, actual = testset$Pass)

mean(nb_predict == testset$Pass)

confusionMatrix(nb_predict, as.factor(testset$Pass), mode = "everything", positive="1")

## Support Vector Machine

#create another testset to preserve the integrity of original estset
svm_trainset <- trainset
svm_trainset$Pass <- as.factor(svm_trainset$Pass)

#used for training
svm_grades <- svm(Pass~., data = svm_trainset)

summary(svm_grades)

#to generate a series of predicted values for the class of each data object

svm_predict <- predict(svm_grades, newdata = test_data, type = "response")

#confusion matrix and accuracy score
table(predicted = svm_predict, actual = testset$Pass)
mean(svm_predict == testset$Pass)

confusionMatrix(svm_predict, as.factor(testset$Pass), mode = "everything", positive="1")

#improve accuracy of svm model by changing the kernels

#linear kernel
svm_pass <- svm(Pass~., data = svm_trainset, kernel = "linear", scale = FALSE)

svm_pred <- predict(svm_pass, newdata = test_data, type = "response")
table(predicted = svm_pred, actual = testset$Pass)
mean(svm_pred == testset$Pass)

#polynomial kernel
svm_pass <- svm(Pass~., data = svm_trainset, kernel = "polynomial", scale = FALSE)

svm_pred <- predict(svm_pass, newdata = test_data, type = "response")
table(predicted = svm_pred, actual = testset$Pass)
mean(svm_pred == testset$Pass)

#sigmoid kernel
svm_pass <- svm(Pass~., data = svm_trainset, kernel = "sigmoid", scale = FALSE)

svm_pred <- predict(svm_pass, newdata = test_data, type = "response")
table(predicted = svm_pred, actual = testset$Pass)
mean(svm_pred == testset$Pass)

#check for the most important features
svm_predict <- as.data.frame(svm_predict)
var_imp <- t(svm_grades$coefs) %*% svm_grades$SV # weight vectors
var_imp <- apply(var_imp, 2, function(v){sqrt(sum(v^2))}) # weight
var_imp

copy_imp <- var_imp
copy_imp <- as.data.frame(copy_imp) # change to a dataframe
copy_imp$features <- row.names(copy_imp) # add row names as a column
var_imp <- copy_imp
colnames(var_imp) <- c('Importance', 'Variables')

#plot
ggplot(var_imp, aes(y = Importance, x = Variables)) +
geom_col() +
theme(axis.text.x = element_text(angle = 90, hjust = 1))

# create the parallel coordinates plot
install.packages("GGally")
library("GGally")

ggparcoord(data = student_grades, color = "blue")
