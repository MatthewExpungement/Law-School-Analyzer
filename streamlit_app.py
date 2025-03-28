import streamlit as st
import pandas
import plotly.express as px
from employment import displayEmployment
from admissions import displayAdmissions
from diversity import displayDiversity
from ubp import displayBarPassage
from faculty_diversity import displayFacultyDiversity
from custom import displayCustom

st.set_page_config(layout='wide')
st.header("Law School Analyzer")
st.write("By Matthew Stubenberg")
st.write("Innovator in Residence - University of Hawaii William S. Richardson School of Law")
st.write("Data sourced from Access Lex at https://analytix.accesslex.org/download-dataset. Last updated October 2024")
admissions_tab,employment_tab,bar_passage_tab,diversity_tab,faculty_tab,custom_tab = st.tabs([
    '📊 Admissions',
    '💼 Employment',
    '⚖️ Bar Passage',
    '👨‍👩‍👧‍👦 Student Diversity',
    '👩‍🏫 Faculty Diversity',
    '🔍 Custom'
])
school_df = pandas.read_csv('Data_Files/School Information.csv')
#schools = ['University of Hawaii','University of New Mexico']
schools = school_df['schoolname'].sort_values()

selected_schools = st.sidebar.multiselect("Select Schools",schools,default='University of Hawaii')


displayEmployment(employment_tab,selected_schools)
displayAdmissions(admissions_tab,selected_schools)
displayBarPassage(bar_passage_tab,selected_schools)
displayDiversity(diversity_tab,selected_schools)
displayFacultyDiversity(faculty_tab,selected_schools)
displayCustom(custom_tab,selected_schools)