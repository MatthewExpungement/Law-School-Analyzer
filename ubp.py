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

def createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis):
    #Bar Passage Full Time Long Term
    selected_schools_df = df.loc[df['schoolname'].isin(selected_schools)]
    fig_raw = px.line(selected_schools_df,x='UltimateBarYear',y=yaxis,title="Raw <br>" + title)
    #Percentage Numbers
    yaxis_percent = [ax + "_Percentage" for ax in yaxis]
    fig_percentage = px.line(selected_schools_df,x='UltimateBarYear',y=yaxis_percent,title="Percentage <br>" + title)
    return [fig_raw,fig_percentage]


def createSingleBarGraph(df,selected_schools,title,yaxis,xaxis):
    selected_schools_df = df.loc[df['schoolname'].isin(selected_schools)]
    fig = px.bar(selected_schools_df,x=xaxis,y=yaxis,title=title)
    return fig

def displayBarPassage(streamlit_tab,selected_schools):
    streamlit_tab.header("Bar Passage Metrics")
    df = pandas.read_csv('Data_Files/First-Time and Ultimate Bar Passage (School-Level).csv')
    df['UltimateSchoolPassPct'] = df['UltimateSchoolPassPct']*100
    df['avgpasspctdiff'] = df['avgpasspctdiff'] * 100
    # df['UltimateTakers_Percentage'] = df['UltimateTakers']/df['UltimateCohortTotal'] * 100
    for ubp in ['UltimateDidNotTake','UltimateNoInfo','UltimateTakers']:
        df[ubp + "_Percentage"] = df[ubp]/df['UltimateCohortTotal'] * 100



    #UBP
    streamlit_tab.subheader("Ultimate Bar Passage")

    title = "Ultimate Bar Passage Percentage"
    ubp_fig = createSingleGraph(df,selected_schools,title,'UltimateSchoolPassPct','UltimateBarYear')
    title = "Difference in First Time Bar Pass Rate School vs State Average Percentage"
    state_diff = createSingleGraph(df,selected_schools,title,'avgpasspctdiff','Firsttimebaryear')

    streamlit_tab.plotly_chart(ubp_fig)

    
    streamlit_tab.divider()


    #UBP
    df['avgschoolpasspct'] = df['avgschoolpasspct'] * 100
    streamlit_tab.subheader("First Time Bar Passage")
    col1,col2 = streamlit_tab.columns(2)
    title = "First Time Bar Passage Percentage"
    ftbp_fig = createSingleGraph(df,selected_schools,title,'avgschoolpasspct','Firsttimebaryear')
    title = "Difference in First Time Bar Pass Rate School vs State Average Percentage"
    state_diff = createSingleGraph(df,selected_schools,title,'avgpasspctdiff','Firsttimebaryear')

    col1.plotly_chart(ftbp_fig)
    col2.plotly_chart(state_diff)
    col2.write("*Negative value means school pass percentage was less than state average.")
    
    streamlit_tab.divider()

    #UBP Takers
    streamlit_tab.subheader("Ultimate Bar Passage Number of Takers/Not Takers/No Information")
    yaxis = ['UltimateDidNotTake','UltimateNoInfo','UltimateTakers']
    race_gender_choices = streamlit_tab.multiselect("Select UBP Type",yaxis,default=yaxis)
    if(len(selected_schools) > 1):
        streamlit_tab.write("You can only have one school selected to use this chart")
    else:
        col1,col2 = streamlit_tab.columns(2)
        title = "UBP"
        yaxis = race_gender_choices

        fig_graphs = createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis)
        col1.plotly_chart(fig_graphs[0])
        col2.plotly_chart(fig_graphs[1])
        col2.write("*Percentage based total Cohort" )