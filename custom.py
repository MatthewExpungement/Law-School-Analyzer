import streamlit as st
import pandas
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.graph_objs.layout import YAxis,XAxis,Margin

def displayCustom(streamlit_tab,selected_schools):
    streamlit_tab.header("Custom Views")
    admissions_df = pandas.read_csv('Data_Files/Admissions.csv')
    ubp_df = pandas.read_csv('Data_Files/First-Time and Ultimate Bar Passage (School-Level).csv')

    if(len(selected_schools) > 1):
        streamlit_tab.write("You can only have one school selected to use this chart")
    else:
        admissions_selected_schools_df = admissions_df.loc[admissions_df['schoolname'].isin(selected_schools)]
        ubp_selected_schools_df = ubp_df.loc[ubp_df['schoolname'].isin(selected_schools)]

        #Even out the years so bar pass start 3 year later and lsat ends 3 years earlier
        years = admissions_df['CalendarYear'].unique()
        lsat_years = list(years)[0:-4]
        bar_pass_years = list(years).copy()[3:-1]
        lsat_scores = list(admissions_selected_schools_df['LSAT50'])[0:-4]
        # bar_pass_years.pop(0)
        # bar_pass_years.pop(0)
        # bar_pass_years.pop(0)
        # lsat_years.pop(-1)
        # lsat_years.pop(-1)
        # lsat_years.pop(-1)


        bar_pass_list = list(ubp_selected_schools_df['avgschoolpasspct']*100)[6:]
        print(lsat_scores,len(lsat_scores))
        print(bar_pass_list,len(bar_pass_list))
        print(bar_pass_years,len(bar_pass_years))
        print(lsat_years,len(lsat_years))
        # Create figure with secondary x-axis
        # fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig = go.Figure()
        fig.update_layout(title="LSAT Scores/Bar Pass Rates",
            xaxis=XAxis(
                title="LSAT year"
            ),
            xaxis2 = XAxis(
                title="Bar Pass Year",
                overlaying= 'x', 
                side= 'top',
            ),
            yaxis=dict(
                title="LSAT Score"
            ),
            yaxis2=dict(
                title="Bar Pass Rate",
                overlaying= 'y', 
                side= 'right',
            ))
        # Add traces
        fig.add_trace(
            go.Scatter(x=lsat_years, y=admissions_selected_schools_df['LSAT50'], name="LSAT Scores")
        )

        fig.add_trace(
            go.Scatter(x=bar_pass_years, y=bar_pass_list, name="School Pass Rate", xaxis='x2',yaxis='y2')
        )
        fig.add_trace(
            go.Scatter(x=[2015,2016,2017,2018,2019], y=ubp_selected_schools_df['UltimateSchoolPassPct'].dropna()*100, name="UBP Pass Rate", xaxis='x2',yaxis='y2')
        )
        
        streamlit_tab.plotly_chart(fig)
        streamlit_tab.write("Please note the bar pass year has been shifted so it compares the LSAT score year with the bar pass year.")
        streamlit_tab.write("School pass rate is the year the bar was taken 'Firsttimebaryear'")
