import streamlit as st
import pandas
import plotly.express as px

def createRawAndPercentGraph(df,selected_schools,title,yaxis,xaxis):
    #Bar Passage Full Time Long Term
    selected_schools_df = df.loc[df['schoolname'].isin(selected_schools)]
    fig_raw = px.line(selected_schools_df,x='CalendarYear',y=yaxis[0],color='schoolname',title="Raw <br>" + title)
    #Percentage Numbers
    fig_percentage = px.line(selected_schools_df,x='CalendarYear',y=yaxis[1],color='schoolname',title="Percentage <br>" + title)
    return [fig_raw,fig_percentage]


def createSingleGraph(df,selected_schools,title,yaxis,xaxis):
    selected_schools_df = df.loc[df['schoolname'].isin(selected_schools)]
    fig = px.line(selected_schools_df,x=xaxis,y=yaxis,color='schoolname',title=title)
    return fig

def createSingleBarGraph(df,selected_schools,title,yaxis,xaxis):
    selected_schools_df = df.loc[df['schoolname'].isin(selected_schools)]
    fig = px.bar(selected_schools_df,x=xaxis,y=yaxis,title=title)
    return fig

def displayBarPassage(streamlit_tab,selected_schools):
    streamlit_tab.header("Bar Passage Metrics")
    df = pandas.read_csv('First-Time and Ultimate Bar Passage (School-Level).csv')
    df['UltimateSchoolPassPct'] = df['UltimateSchoolPassPct']*100
    df['avgpasspctdiff'] = df['avgpasspctdiff'] * 100
    df['UltimateTakers_Percentage'] = df['UltimateTakers']/df['UltimateCohortTotal'] * 100
    
    #UBP
    streamlit_tab.subheader("Bar Passage")
    col1,col2 = streamlit_tab.columns(2)
    title = "Ultimate Bar Passage"
    ubp_fig = createSingleGraph(df,selected_schools,title,'UltimateSchoolPassPct','UltimateBarYear')
    title = "Difference in First Time Bar Pass Rate School vs State Average"
    state_diff = createSingleGraph(df,selected_schools,title,'avgpasspctdiff','Firsttimebaryear')

    col1.plotly_chart(ubp_fig)
    col2.plotly_chart(state_diff)
    col2.write("*Negative value means school pass percentage was less than state average.")

    #UBP Takers
    yaxis = ['UltimateDidNotTake','UltimateNoInfo','UltimateTakers']
    xaxis = 'UltimateBarYear'
    title = 'Ultimate Bar Passage Takers, Non-Takers, Did Not Take'
    if(len(selected_schools) > 1):
        col1.write("You can only have one school selected to use this chart")
    else:
        fig = createSingleBarGraph(df,selected_schools,title,yaxis,xaxis)
        col1.plotly_chart(fig)
    title = "Percentage Universal Bar Passage Takers"
    ubp_takers_percentage = createSingleGraph(df,selected_schools,title,'UltimateTakers_Percentage','UltimateBarYear')
    col2.plotly_chart(ubp_takers_percentage)
    col2.write("*Percentage based on takers of UBP/total size of cohort")
    
    streamlit_tab.divider()