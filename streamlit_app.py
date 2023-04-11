import streamlit as st
import pandas
import plotly.express as px
from employment import displayEmployment
from admissions import displayAdmissions
from ubp import displayBarPassage

st.set_page_config(layout='wide')
st.header("Law School Analyzer")
admissions_tab,employment_tab,bar_passage_tab = st.tabs(['Admissions','Employment','Bar Passage'])
school_df = pandas.read_csv('School Information.csv')
#schools = ['University of Hawaii','University of New Mexico']
schools = school_df['schoolname'].sort_values()

selected_schools = st.sidebar.multiselect("Select Schools",schools,default='University of Hawaii')


displayEmployment(employment_tab,selected_schools)
displayAdmissions(admissions_tab,selected_schools)
displayBarPassage(bar_passage_tab,selected_schools)