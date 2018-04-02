# Comparing Public School Funding and Mortality Rates Due to Drug Abuse and Self-Harm In Ohio
>**CS3900 Final Project**

>Jonathon Gebhardt, Brian Duffy, Alexander Silcott

<img src="header.jpg" />
Source: https://www.1and1.com/digitalguide/online-marketing/web-analytics/what-is-machine-learning-how-machines-learn-to-think/

## Introduction
It is common knowledge that in recent years there has been an increase in drug-related deaths--especially in Ohio. There are any number of reasons for a spike in this type of mortality rate which can include economic and environmental factors. Self worth is also usually drawn from these factors. Educated individuals with a better school experience might be deterred from engaging in behaviors that would result in a death by overdose or suicide than individuals with a poor school experience (i.e. no art or after school programs, poor environment in class).

**We hope to address the following questions:**
- Is there a relationship between the amount of funding public schools get and the mortality rates of individuals in those areas due to drug abuse or self-harm?

- Can we predict if a change to a school district’s budget will have an effect on the mortality rate of a particular area?

- Are there specific areas school’s can spend money on that can reduce these mortality rates and perhaps help general public health as a result?


## Files included

### Python scripts
- **csvconvert.py** - Convert given xlsx file to csv.
- **preprocess.py** - Preprocess csv files. Find intersection and complement of our datasets so we can build a combined dataset using a foreign key.
- **trim.py** - Trim off extra columns we don't need reduce features in data.

### Datasheets and other stuff
- **jupyter-notebook.ipynb** - Jupyter notebook to present information.
- **grad.csv** - Graduation information about school districts. Used to cross-reference IRNs to get collated data.
- **district.csv** - School expenditure information for Ohio.
- **mort.csv** - Average mortality rate by county. (Deaths per 100,000)
- **expanded.csv** - All of the schools combined, before finding intersection and complement.
- **expanded_complement.csv** - All of the schools not in the intersection.
- **expanded_intersection.csv** - Combined dataset before trimming columns.
- **expanded_intersection_trimmed.csv** - Final combined dataset after trimming columns.

# Feature Index

Now that we have reduced the number of features to use in our algorithm, we will define them as follows:

**CRI - Classroom Instr** - Classroom instructional cost. Actual amount spent on classroom instructional purposes.

**CRI%** - Percent spent on classrom Instructional purposes.

**County Mortality Rate** - Average mortality rate for drug overdose in 2014 in the school's county.

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