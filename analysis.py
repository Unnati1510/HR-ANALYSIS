import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.offline import init_notebook_mode

# Initialize Plotly for notebook mode (if using Jupyter Notebook)
# init_notebook_mode(connected=True)

# Load the data
test = pd.read_csv('aug_test.csv')
train = pd.read_csv('aug_train.csv')

# Display basic information about the dataset
train.info()

# Check for duplicated rows
duplicate_rows = train[train.duplicated()]
duplicate_count = len(duplicate_rows)
print(f"Number of duplicated rows: {duplicate_count}")

# Calculate missing values percentage
missing_value = 100 * train.isnull().sum() / len(train)
missing_value = missing_value.reset_index()
missing_value.columns = ['variables', 'missing values in percentage']

# Plot missing values using Plotly
fig = px.imshow(train.isnull().T, template='ggplot2')
fig.update_layout(title='Missing values in the dataset')
fig.show()

# Create a bar plot for missing values
fig = px.bar(missing_value, x='variables', y='missing values in percentage',
             title='Missing values % in each column', template='ggplot2')
fig.update_xaxes(title_text='Variables')
fig.update_yaxes(title_text='Missing Values (%)')
fig.show()

# Visualize the top 50 cities
plot_city = train['city'].value_counts().head(50).reset_index()
plot_city.columns = ['City', 'Count']
fig = px.bar(plot_city, x='City', y='Count', title='Top 50 Cities', color='Count')
fig.show()

# Visualize the distribution of city development index
plot_cdi = train['city_development_index'].value_counts().reset_index().head(50)
plot_cdi.columns = ['cdi', 'Count']
plot_cdi['cdi'] = plot_cdi['cdi'].astype('str')
fig = px.bar(plot_cdi, x="cdi", y="Count", color='Count', title='City Development Index Distribution')
fig.show()

# Visualize the distribution of enrolled university
plot_enrollment = train['enrolled_university'].value_counts().reset_index()
plot_enrollment.columns = ['enrolled_university', 'count']
fig = px.pie(plot_enrollment, values='count', names='enrolled_university',
              title='Distribution of Enrolled University', template='simple_white')
fig.show()

# Visualize the distribution of education level
plot_education = train['education_level'].value_counts().reset_index()
plot_education.columns = ['education_level', 'count']
fig = px.pie(plot_education, values='count', names='education_level',
              title='Distribution of Education Level', template='ggplot2')
fig.show()

# Visualize the distribution of major discipline
plot_discipline = train['major_discipline'].value_counts().reset_index()
plot_discipline.columns = ['major_discipline', 'count']
fig = px.pie(plot_discipline, values='count', names='major_discipline',
              title='Distribution of Major Discipline', template='plotly')
fig.show()

# Visualize the distribution of company size
plot_company_size = train['company_size'].value_counts().reset_index()
plot_company_size.columns = ['company_size', 'count']
fig = px.pie(plot_company_size, values='count', names='company_size',
              title='Distribution of Company Size', template='plotly_white')
fig.show()
