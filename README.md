Predicting Student Grades using Python 

Using the standard Data Science pipeline, I developed a Machine Learning model to predict student grades. 

1.0 Introduction

The quality of students’ performance in school is a top priority for educators as it helps students make a difference in their lives locally, regionally, nationally and globally (Farooq, et al., 2011). 

There are several factors that affect a student’s performance in school; they have been summed up into student factors, family factors, school factors and peer factors (Crosnoe, et al., 2004) cited in (Farooq, et al., 2011). Hijazi & Navqi (2006), therefore, hit the nail on the head by stating that “measuring of academic performance of students is challenging since student performance is product of socio-economic, psychological and environmental factors”.
	
Several studies have been conducted in the last few years to attempt to correctly understand the factors affecting students’ performance in school and present an effective way to improve them. Beaumont-Walters & Soyibo (2001) outlined the connection between student grades and gender, grade level, school location, school type, student type and socio-economic background. While some studies (Uyar & Güngörmüş, 2011; Singh, et al., 2016) have emphasized the importance of gender, attendance, family, age, and peer groups on students’ performance in school, others (Chansarkar & Michaeloudis, 2001) disagree that such factors have any bearing on the students’ performance. 
	
Identifying the causal factors for student performance is vital. If the most important factors affecting student performance in school can be successfully identified, then best practices can be developed to help students assimilate better and improve student grades. 

1.1 Aim of the report

This report will create classification models to predict the student grades of students in different schools. It will cycle through the five stages of data science problem solving and eventually present the best features and models for predicting student grades. The R programming language in the RStudio environment will be used as well as machine learning (ML) classification models to predict the grades of students based on the features present in the dataset.  

2.0 Data Science Methodology

The Data Science methodology that was used for this project is the Cross Industry Standard Process for Data Mining (CRISP-DM) methodology. It is simple and straightforward, and the most common data science framework for executing Data Science projects. This Data Science methodology has six stages: Business Understanding, Data Understanding, Data preparation, Modeling, Evaluation, and Deployment. 
	 
Figure 1: CRISP-DM methodology.

2.1 Data preparation

Data preparation is a very important part of Data Science. It is the process of manipulating raw data to obtain quality data that is then used to build models. It comprises of data collecting, data integration, data transformation, data cleaning, data reduction, and data discretization. (Zhang, et al., 2003)

2.12	Data collection

Data collection is the process of gathering and analyzing information on certain variables in order to answer questions and investigate the outcomes. 

2.13 Data cleaning

Failing to properly clean up data can result in avoidable errors. Data cleaning involves getting rid of missing values, typos, mixed formats, duplicate data, and wrong information (Chu, et al., 2016).

2.131 Missing data

Another important aspect of data exploration is the handling of missing data. The problem of missing data is extremely common in a lot of research and can be easily overlooked if not properly investigated. At first glance, the student grades dataset does not reveal any missing data. The sum of NA values in the dataset is 0. 
 
Figure 5: Visualization of missing data in the student grades dataset

To see the distribution of the data, a histogram shows the distribution of the data in many features below:
 
The missing values in the dataset become visible after illustrating the distribution with a histogram. There are three missing values in the dataset. Applying the same methods to other features will help to identify similar missing values in the dataset. 
  
Two zero values are found in Father’s education. Reasons for the missing data appearing in this format are plenty, including:
•	An error in imputation
•	A problem with storage of the data. 

Although several literatures have debated the limits of missingness that should be handled, several agree that imputation is one of the best ways to deal with missingness. To eradicate the missingness in the data, the zero values are converted to NA values after which the type of missing data is determined using an MCAR test and found to be missing completely at random (MCAR). 
	
After this test, the values are replaced with the median value of the variables, Mother’s education and Father’s education respectively. 

2.132 Duplicate data

Duplicate data is any record in a database that shares details with other data. In certain situations, the presence of duplicate data can present a critical problem and affect the results during model building. 

In the Student Grades dataset, there is the presence of duplicate data. However, this situation cannot be avoided as duplicate records can be present for different students. Due to this, it can be concluded that this dataset has duplicate data but it is integral to the data itself so nothing will be done. 

2.12	Data exploration 

Data exploration is one of the most important areas of Data Science as it helps to understand the data better and help to better draw insights. The student grades data contains 395 rows and 31 variables. The data also exists in two different forms: numbers and characters. Some of the variables are categorical (yes or no). The structure of the data is illustrated below:
 
2.2 Exploratory Data Analysis

Exploratory data analysis (EDA) means using data visualization methods to analyze and dig deeper into datasets. It helps to identify errors, discover patterns in the data, and find relationships between variables. (IBM Cloud Education, 2020).

2.21 Outliers

The median of the age variable is 17 while that of absences is 4. Considering that the highest value in absences is 75, this presents a problem—it appears that the variable ‘absences’ has some extreme outliers. 
 
Figure 3: boxplot showing data distribution of ‘absences’ variable

As can be seen from the boxplot, the mean value for ‘absences’ is quite low but it has a number of outliers, with the highest being 75. In this situation, the outliers in absences do offer some sort of insight into the data. An absence count of 75 is not abnormal seeing as there are three months in a term—75 days is a perfectly reasonable amount of days for a student to have missed school.  
 
Figure 4: boxplot showing data distribution of ‘age’ variable

The age dataset also contains an outlier as the average value is 17 and 22 lies outside the standard range. Once more, it is perfectly reasonable to have older students in a class so that will be left as is.

2.22 Univariate & Multivariate EDA

Univariate exploratory data analysis (EDA) is the type of analysis that is concerned with analyzing the relationship between a single variable and the response variable. 

On the other hand, multivariate analysis is the type of analysis that investigates the relationship between multiple independent variables on one dependent variables. 

Variables present in ‘Student Grades’ dataset

There are 31 variables in the data—30 independent variables and 1 dependent variable, which is the response variable. 

Response variable

The response variable (or dependent variable) is the variable whose value depends on that of another one. The ‘Student Grades’ dataset has one dependent variable, which is the ‘pass’ variable. It is the result after passing the other features into the model. The response variable is represented by 0 and 1 as it is a Boolean variable — the students either pass (1) or fail (0). 

The histogram below of the response variable shows that the pass and fail responses are almost equal. 
 
The fact that the two responses are almost equal means that the model is unlikely to sway to one direction during model building. Where the response is skewed, there is the risk of the model swaying to that side during model building. 

Independent variables

Independent variables are variables that don’t depend on any other variables for their output. They are not affected by external variables and are used to derive the values for the dependent variable. 

School

This variable shows the name of the schools that students attend. There are only two schools with their names abbreviated: MS and GP. 
   
350 students attend GP while 45 students attend MS. This has no effect on their grades, however, because the datasets are not evenly distributed. A more evenly distributed dataset would probably produce better results. 

Sex

This variable shows the sex of the students that are contained in this dataset. There are two values in the dataset: Male and Female. To visualize the data in a boxplot, the information has been converted to a categorical variable where F is 0 and M is 1. 
     
As stated earlier, several studies have asserted that sex is an important factor in student grades, that more females do well in school compared to males. According to the boxplot, that is not true. The average value of students that failed is 0 and 1 for those who passed. The pass and fail distributions are equally distributed, however. Not much can be derived from this visualization. 

Age

The age variable shows the distribution of the ages of the students in this dataset. The ages range from 17 to 22. A boxplot is used to analyze the results from this dataset and shows quite a lot of information. The boxplot is stratified according to the Pass variable to show the age distribution of students that passed and failed. 
   
A reminder that 0 represents fail and 1 represents pass. The average age of students that failed is 17, higher than the average age of students that passed, which is 16. A lot of the students that passed are between 16 and 17 years old, with majority of the students that passed being below 18 years old. Although there are outliers, a significant portion of students that passed are in the lower age range of the dataset. 

On the other hand, 75% of the students who failed are 21 years old and below, with the average age being 17. This can lead to the conclusion that the older students are, the higher the chance that they will fail. 

Family size

Family size is represented in the database as famsize. The histogram below shows that more students belong to families that are greater than 3 than families that contain less than 3 people. 
   
According to the boxplot, family size has no bearing on whether students fail or pass as the average rate for pass or fail is same whether the student’s family size is greater or less than 3. 

Reason

The reason for choosing the school include the course, home, reputation, and other reasons. The majority of the students chose the school for its course, proximity to their house, or other reasons, with the least being its reputation. 
   

This fact did affect students’ performance, as many of those that failed joined the school for other reasons. More information is required to properly interpret these results, however. 

Study time

Study time is the variable that represents the amount of time that a student spends studying every week. The values range from 1 to 4, with 1 representing less than 2 hours, 2 representing 2 to 5 hours, 3 representing 5 to 10 hours, and 4 representing 10+ hours. 

The histogram also shows that the majority of students fall into the two categories, which means that they study between 2 and 5 hours every week. Closely following that is 1, which are the students that study for less than 2 hours weekly. The rest of the students study for over 5 hours every week. 
    
According to the boxplot illustrating the relationship between time spent studying and the response variable, study time does have an effect on student grades. The more time students spend studying, the higher their chances of passing. The average time that students who passed spent reading is between 2 and 5 hours. 75% of those that passed spent between 5 and 10 hours a week studying. On the other hand, the majority of people who failed spent less than 5 hours a week studying. There are outliers, which suggests different reasons for the failure. 

Failures

Several studies have asserted that the number of failures that students have can affect their grades. The failures variable stands for the number of times that the student has failed in the past. The histogram below shows the distribution of the ‘failures’ variable. Majority of the values in this dataset are 0—this represents over 300 data points out of a total of 395 data points. 
  

The boxplot below shows that the number of failures does in fact affect student grades. The likelihood of a student passing is lower if they have failed previously as shown in the figure below.

Activities

Activities is the variable that illustrates the after-school activities that students engaged in. It is a Boolean value, representing whether students participated in after-school activities or not. 
   
The boxplot shows that there is no difference in the effect of afterschool activities on the students’ grades. 

Nursery 

The nursery variable in this dataset represents information about whether the students attended nursery school or not. 
      
Majority of the students attended nursery school. However, according to the boxplot, whether or not students attended nursery school has no effect on their grades. 

Higher

Higher is the variable that explains whether a student intends to attend higher education or not, with yes represented by 0 and no represented by 1. 
  
Usually, students are more The histogram below shows that the majority of students planned to proceed to higher education. Nonetheless, according to the boxplot, it appears that whether or not students plan to attend higher education has no effect on their grades. 

Internet

This is the variable that illustrates the students’ internet use and is represented with Boolean values where yes represents 0 and no represents 1. 
  
The histogram shows the distribution of this variable and shows that an overwhelming number of students have access to the internet. As with the last few variables, it does not seem to have an effect on the student’s results as shown by the boxplot below. 

Romantic

This variable represents romantic relationship and is a Boolean figure with yes or no response variables. 
  
The histogram shows that more students are not in romantic relationships. Out of 395 students, up to 140 students are in romantic relationships though. Nonetheless, it doesn’t seem to have an effect on the grades as shown in the boxplot. 

Health

Health represents how healthy the students are and is a nominal value with values ranging from 1 to 5. The histogram below shows that the majority of students are in good health. Nonetheless, the boxplot shows that there is no effect of students’ health on their performance. 
  
Absences

Absences represents the number of days students have stayed away from school. The range of values in this column stretch from 0 to as high as 75. The histogram below shows the distribution of this data while the boxplot shows that this variable does affect students’ performance: the more days a student spends away from school, the higher their chances of failing. 
  
Address & Traveltime

Multivariate analysis is used to determine the relationship between address and travel time, which are two variables in the dataset representing the students’ place of living as well as the time it takes for them to get to school. 
     
 
The two factors have no effect on whether a student passes or fails as the results are the same. Despite that, it can be seen that although the results are similar, there are more outliers in the ‘fail’ section, which means that although the difference is negligible, more rural students failed than urban students. 

However, a boxplot is used to illustrate the relationship between these two variables: from the boxplot below, it can be seen that travel time is highly dependent on address. Students who live in urban areas tend to spend less time on the way to school than students who live in rural areas. 

Schoolsup, famsup & paid

Schoolsup, famsup, and paid, represent the different levels of support that a student can enjoy; they are all Boolean values. They stand for school support, family support, and paid support respectively. 
    
  
  

From the boxplots above, there is no difference between students who passed or failed because of support either from family, school, or paid sources. 

Pstatus, Famrel & Guardian

Pstatus, Famrel, and Guardian represent three variables: parent status, family relationship, and the students’ guardian. These three variables can affect each other and the relationship will be explored with histograms and boxplots. 
  
  
  
The majority of students have a good relationship with their family and this affected their grades as the figure above shows that the average student that either passed or failed had a good relationship with family. The difference between the two categories, however, is that majority of the students that passed had a fairly good relationship with family, but this was not the same for those that failed. There were also outliers. 

An overwhelming number of students have parents who are still together, which could have positively affected the family relationship and influenced the good relationship that they enjoy. Nonetheless, there seems to be no effect of this on student performance according to the boxplot below.

According to the figure above, 275 students have their mother as their guardian while 125 students have their father as their guardian. This does not seem to have any effect on student grades according to the boxplot below. 

Medu & Mjob

Although several literature claim that the mother’s education influences student grades, the boxplot below shows that it is not true as the average values for the two results are the same. 

With respect to mother’s job, it appears that it has a minimal effect on the students’ grades. Most of the students who passed did not have stay at home mothers as opposed to those who failed.  

Fedu & Fjob

Fedu and Fjob represent the father’s education and the father’s job. The two variables are co-dependent, and their relationship will be shown through figure (XXXXX) and boxplot below. 

According to the figure above, majority of the students have well educated fathers. However, the majority of the fathers are stay at home fathers. Nonetheless, the father’s profession doesn’t seem to affect the students’ performance.

Freetime & Goout

Freetime and Go out are the two variables that explain the amount of free time students have and whether they go out or not. Both are nominal variables with values ranging from 1 to 5 (representing low to very high). The histogram below shows that students go out fairly regularly, with the majority of them right in the middle between fair and good. The students do use their time well as the majority of them spend their free time outside, with the majority of them squarely in the middle, maintaining a healthy outing balance. 
  
   

There doesn’t appear to be any effect on the students’ free time as the average and data distribution shows in the boxplot below. In a similar fashion, the frequency of the students going out does not seem to affect their results as well, as can be observed in the boxplot below. This can be explained by the fact that the majority of students go out moderately, as can be seen in the histogram. It can also be assumed that they spend the rest of their time studying and carrying out other endeavors. 

Dalc & Walc

Dalc and Walc represent the students’ weekday and weekend alcohol intakes respectively. According to the distribution in the histogram below, the majority of students are not in the habit of consuming a lot of alcohol during the week. This pattern remains consistent during the weekend, even though up to 160 students consume a fairly large amount of alcohol during the weekend. 
   
  

According to the boxplots, weekday alcohol consummation does affect student’ grades, with the majority of the students that passed consuming very little alcohol. The outliers seem to follow the same pattern, however, more successful students consumed very little alcohol. There is also an effect on students’ grades as the majority of students who are successful only drink averagely during the weekend.

3. 0 Feature engineering & selection

Feature engineering is also known as feature selection and is an important part of data preparation. It is the process of creating new features from old features that lead to an improved performance (Nargesian, et al., 2017). It also involves scaling a feature for better model performance. Feature engineering tries to ensure that the accuracy does not decrease and the new feature selection is as close as possible to the old features (Dash & Liu, 1997).

In the ‘Student Grades’ dataset, the ‘school’ feature is removed for two reasons:
•	It is highly skewed to one school, and as such, it can influence the results negatively. 
•	The school that a student attends appears to have no effect on the dataset. 

For feature selection, Boruta, PCA, and feature consolidation were considered. These ideas were dumped, however, because the data does not have enough variance so the results were not clear.

3.1 Data Normalization

Data normalization is the process of scaling a dataset to a new range of values. For this dataset, min-max normalization was employed. Min-Max normalization is a strategy that is used to transform features from their original form to lie between 0 and 1 (Adeyemo, et al., 2018). 

The data was normalized because SVM, which is one of the models used for classification, works best with normalized data. 

4.0 Model building

Four classification models were used for this assignment:
•	Decision tree
•	Random forest
•	Naïve Bayes
•	Support vector Machine (SVM)

The accuracy of the model will be determined using the mean accuracy, F1 score, Precision and recall where;
Accuracy: How close a measured value is to the true value.
F1 score: The mean between precision and recall. 
Precision: How close the measured values are to each other.
Recall: How many true positives were accurately found in the data. 

4.1 Decision tree

Decision trees are simple, straightforward and require little data preparation. The decision tree was chosen for its ability to process both numerical and categorical data. After passing the data through the model, the decision tree produced an accuracy of 53%. The F1 score was 56% and the precision was 58%. 
 
This all shows that the decision tree produced poor accuracy for this particular dataset as it misclassified almost as many values as it accurately classified. The decision tree is below:
 
4.2 Random Forest

Random forest works very well for both classification and regression tasks and produces more accurate results than decision trees — the two work in the same manner, however, random trees work to avoid overfitting. Random forest was chosen because it produces good predictions and handles large datasets efficiently. 

Random forest produced an accuracy result of 62%. This result is much better than that derived from decision tree, however, it still falls short by a lot. After normalizing the data, however, Random Forest produced an increased accuracy of 65%. However, it was noticed that the accuracy kept changing so the random state was set to 0 after which the accuracy stayed steady at 58%. 
Changing the number of trees in the forest did not have a significant effect on the results. One of the major disadvantages of Random Forest is that it is too slow. It is also very hard to control what the model does.  

4.3 Naïve Bayes

Naïve Bayes is very simple and does not require a lot of training data. It was chosen for this problem because it does not require a lot of data entries to come up with proper classifications. After building the model, an accuracy of 63% was derived. 
 
This is much better than the rest of the models, but SVM is still there luv. One of the major cons of using Naïve Bayes is that it assumes that all the features are independent of each other, which is rarely the case in the real world. 

4.4 Support Vector Machine (SVM)

Support Vector Machine (SVM) is a very powerful classification model algorithm. It performs very well even without clear information on the data. It is also very fast and works very well with a large number of features. It was chosen for this problem because of the aforementioned reason and for the flexibility of its kernels. 

After building the SVM model the first time, an accuracy of 67% was gotten. To improve the accuracy of the model, all the features were normalized and the kernel was changed to XXX. After normalizing the data, there was no in accuracy. Accuracy recorded with different kernels are outlined in the table below:

Attempt number	Kernel	Accuracy
1	No kernel	67%
2	Linear	64.6%
3	Polynomial	55.7%
4	Sigmoid	62%
 
5.0 Classification performance metrics

According to the data in section 4.0, the best performing model is the SVM model, and the worst performing model is the Decision Tree. The best performing SVM model is the model without a kernel. SVM performed best for this problem because there is a clear boundary between the two classes. Decision tree is known to give a low prediction accuracy and this situation followed this pattern. Although Naïve Bayes performed well, its assumption that all classes are independent is harmful for this project as several variables are dependent on each other. One major drawback of Random Forest (and why it ultimately lost to SVM) is that it is time consuming. 

Using SVM model, the most significant features are failures, absences, school support, study time, higher, nursery, go out, and weekly alcohol intake according to the plot below.
 
Conclusion

There are a host of factors that can contribute to the problem of student performance. Nonetheless, this paper attempted to build a model to accurately predict student performance and identify the major factors behind it. A major drawback with this project was the low variance in the dataset, which made the data somewhat difficult to work with, and which made exploration limited. More features would prove to be useful for finding more useful information from the data. 

Using SVM, which was the highest performing model, it was found the most significant features are failures, absences, school support, study time, higher, nursery, go out, and weekly alcohol intake. 
