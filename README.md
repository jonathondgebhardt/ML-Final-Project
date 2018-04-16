# School Metrics and Substance Abuse Mortality in Ohio 
>**CS3900 Final Project**

>Jonathon Gebhardt, Brian Duffy, Alexander Silcott

<img src="header.jpg" />
Source: https://www.1and1.com/digitalguide/online-marketing/web-analytics/what-is-machine-learning-how-machines-learn-to-think/

# <span style="color:blue">Introduction</span>
It is common knowledge that in recent years there has been an increase in drug-related deaths--especially in Ohio. There are any number of reasons for a spike in this type of mortality rate which can include economic and environmental factors. Self worth is also usually drawn from these factors. Educated individuals with a better school experience might be deterred from engaging in behaviors that would result in a death by overdose or suicide than individuals with a poor school experience (i.e. no art or after school programs, poor environment in class).

**We hope to address the following questions:**
- Is there a relationship between the amount of funding public schools get and the mortality rates of individuals in those areas due to drug abuse or self-harm?

- Can we predict if a change to a school district’s budget will have an effect on the mortality rate of a particular area?

- Are there specific areas school’s can spend money on that can reduce these mortality rates and perhaps help general public health as a result?

## Files included

### Python scripts
- **csvconvert.py** - Convert given xlsx file to csv.
- **trim.py** - Combine all datasets into one, cross-referencing them by IRN (Information Retrieval Number).
- **preprocess.py** - Finish preprocessing our dataset and run the neural network on it. Shows results and histograms of data.


### Datasheets and other items
- **jupyter-notebook.ipynb** - Jupyter notebook to present information.
- **lrc.csv** - Enrollment and proficiency in different subject areas and in different grade levels by school district.
- **cupp.csv** - Demographic, personnel, property validationtax and expenditure data for Ohio school districts.
- **mort.csv** - Mortality rate due to drug overdose by county, United states. This dataset also includes mortality rates due to other factors. (Deaths per 100,000)
- **expanded.csv** - Ohio school expenditure data.
- **trimmed.csv** - Final dataset after cross-referencing IRN number pulling out only required features of datasets.

# <span style="color:blue">Scripts</span>
### csvconvert.py
**To begin, we created a script csvconvert.py which converts our input xlsx files into csv files.**
It can be run from the command line, taking the file name of the xlsx file, the name of the desired sheet, followed by the output filename of the csv. In this python-friendly form, we can interpret and manipulate them inside of Sci-kit and Jupyter.

### trim.py

**trim.py cross-references the IRN (information retrieval) numbers from our datasets and combines them into one file.**
The next script relies on the output csv from this script.

### preprocess.py

**Preprocess.py takes our created dataset and runs a neural network on it.** We train on the data 1000 times. The script then prints out the results and presents a series of histograms of the correlated data.

# <span style="color:blue">Preprocessing</span>

## What features can we eliminate from the dataset?

We have several options for features, and more than what we really need. Some of these columns have virtually no data in them for most schools. These are ones we can eliminate immediately based on this issue with zero values. This will help with selecting features from our dataset.

**Instr Equipment** - Many rows with no data for this field; not relevant.

**Land & Structures** - Many rows with no data for this field; not relevant.

### Other features that can be eliminated?

**Community Service** - We feel that this could play a role, but unfortuantely there are too many rows with zeros for this field.

**Construction** - Not relevant to topic. Not all schools had expenditures in construction at this time.

**Debt & Interest** - Not relevant to topic. Although this will have an impact on school spending, it most likely does not have impact on topic.

**Enterprise** - Not relevant to topic. Expenditures may bee too broad to really have influence on topic.

**Food Service** - This features is probably not relevant to our topic.

**Org Type** - This feature can be removed because all of our datapoints are public districts and this column is redundant.

**Other Equipment** - This contains expenditures of non-instructional expenditures, however the rows are inconsistent with zero values.

**Pupil Transp** - This features is probably not relevant to our topic.

**Weighted ADM** - This is the weighted average daily membership, which is important for the dataset but is not a necesarry part of our process as it was already used to determine values in the rows of the dataset.

# Feature Index

Now that we have reduced the number of features to use in our algorithm, we will define them as follows:

**Adult Ed** - This feature has many rows with zeros. However, this is not to say that the schools did not provide this data; rather that the school does not offer adult education programs, which may influence outcome.

**CRI - Classroom Instr** - Classroom instructional cost. Actual amount spent on classroom instructional purposes.

**CRI%** - Percent spent on classrom Instructional purposes.

**County Mortality Rate** - Average mortality rate (deaths per 100,000) for drug overdose in 2014 in the school's county.

**County Name** - Name of the county that the school belongs to.

**Gen Admin** - General Administration. Expenditure for board of education and executive administration (office of superintendent) services.

**IRN** - Information Retrieval Number. Identification number assigned to educational entity. We use this ID to compare our data across multiple datasets.

**Instr Staff Sup** - Instructional staff support services. Expenditures for supervision of instruction service improvements, curriculum development, instructional staff training, academic assessment, and media, library, and instruction-related technology services.

**Instruction** - Activities dealing with the interaction of teachers and students in the classroom, home, or hospital as well as co-curricular activities. Includes teachers and instructional aides or assistants engaged in regular instruction, special education, and vocational education programs. Excludes adult education programs.

**Local Education Agency Name** - Name of the entity/school, used for identification purposes.

**NCR -Nonclassroom** - Nonclassroom expenditures. This includes general administration, school administration, other and non-specified support services, opearation and maintenance of plant, pupil transportation, and Elem-Sec Noninstructional Food service.

**NCR%** - Percent spent on nonclassroom expenditures.

**Non-Operating** - Non-Operating expenditures. The sum of enterprise operations, non-instructional--Other, community services, adult aducation, non-elementary-secondary programs--Other, construction, land and existing structures, equipment (instructional and other), and payment to other governments and interest on debt.

**Oper & Maint** - Operation and maintenance of plant. Expenditure for buildings services (electricity, heating, air, insurance), care and upkeep of grounds and equipment, nonstudent transportation and maintenance; security devices.

**Operating EPEP*** - Operating expenditures per equivalent pupil. Amount spent per pupil on operating cost.

**Operating Expenditures** - Cost of instruction and support services, as well as administration and pupil transportation and food services. We left out a few of these metrics and believe we can use this value in lieu of them.

**Other Elem-Sec** - Other Elementary-secondary Noninstructional. Expenditure for other elementary-secondary non-instructional activities not related to food services or enterprise operations.

**Other Non Elem-Sec** - Other Nonelementary-secondary Programs . All other nonelementary-secondary programs such as any post-secondary programs for adults.

**Other Support** - Other and Non-specified Support Services.  Business support expenditures for fiscal services (budgeting, receiving and disbursing funds, payroll, internal auditing, and accounting), purchasing, warehousing, supply distribution, printing, publishing, and duplicating services. Also include central support expenditures for planning, research and development, evaluation, information, management services, and expenditures for other support services not included elsewhere.

**Pupil Support** - Pupil support Services. Expenditures for administrative, guidance, health, and logistical support that enhance instruction. Includes attendance, social work, student accounting, counseling, student appraisal, information, record maintenance, and placement services. Also includes medical, dental, nursing, psychological, and speech services.

**School Admin** - School Administration. Expenditure for the office of the principal services.

### *Note about EPEP
EPEP (Expenditure per Equivalent Pupil) is similar to EPP (Expenditure Per Pupil). EPP considers all pupils equal whereas EPEP has a weighted value associated with it to make it more representative of the students actually attending the district (i.e. takes into account students who attent multiple schools in the school year).

Source: http://education.ohio.gov/Topics/Finance-and-Funding/Finance-Related-Data/Expenditure-and-Revenue/Expenditure-Per-Pupil-Rankings

Source: https://education.ohio.gov/getattachment/Topics/Data/Report-Card-Resources/Financial-Data/Technical-Guidance-Finance.pdf.aspx

Source: http://www.tccsa.net/sites/tccsa.net/files/files/EMIS_Forms/Acronyms-EMIS.pdf

### Reducing Dimensionality

With only around 600 datapoints, our data needs to be analyzed using < 24 features to draw reasonable correlations from. Our process involved doing a lot of manual checking and testing out values in the open source machine learning software <a href="https://orange.biolab.si/">Orange</a>. In the end, we managed to choose our final 11 features by using the Rank feature.

### Input Feature Index

These are the features we ended up using and combining into one final dataset.

1. Attendance 2012-13
2. Attendance 2011-12
3. Attendance 2010-11
4. Performance Index Score 2012-13
5. District Class 2 Effective Mileage
6. Percent of Students in Poverty
7. District Local Revenue as Percent of Total
8. District Average Income
9. District Median Income
10. Other Elementary Secondary Expenditures
11. Adult Education

# <span style="color:blue">Results</span>

After attempting linear and logistic regression, SVMs and other machine learning techniques, we found we got our best results using a neural network.

| **<span style="color:orange">ORANGE VALUES</span>** | Precision  | Recall | F1-Score | **<span style="color:Brown">PYTHON VALUES</span>** | Precision  | Recall | F1-Score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Average/Total** | 0.604  | 0.615  | 0.60  | **Average/Total** | 0.62  | 0.65  | 0.61  |