import streamlit as st
import pandas
import plotly.express as px

def createRawAndPercentGraph(df,selected_schools,title,yaxis):
    #Bar Passage Full Time Long Term
    selected_schools_df = df.loc[df['schoolname'].isin(selected_schools)]
    fig_raw = px.line(selected_schools_df,x='CalendarYear',y=yaxis[0],color='schoolname',title="Raw <br>" + title)
    #Percentage Numbers
    fig_percentage = px.line(selected_schools_df,x='CalendarYear',y=yaxis[1],color='schoolname',title="Percentage <br>" + title)
    return [fig_raw,fig_percentage]

def createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis):
    #Bar Passage Full Time Long Term
    selected_schools_df = df.loc[df['schoolname'].isin(selected_schools)]
    fig_raw = px.line(selected_schools_df,x='CalendarYear',y=yaxis,title="Raw <br>" + title)
    fig_raw.update_layout(
        yaxis=dict(
                title="Students"
        ))
    #Percentage Numbers
    yaxis_percent = [ax + "_Percentage" for ax in yaxis]
    fig_percentage = px.line(selected_schools_df,x='CalendarYear',y=yaxis_percent,title="Percentage <br>" + title)
    fig_percentage.update_layout(
        yaxis=dict(
                title="Percentage of Students"
        ))
    return [fig_raw,fig_percentage]

def displayDiversity(streamlit_tab,selected_schools):
    streamlit_tab.header("Student Diversity")
    df = pandas.read_csv('Data_Files/Enrollment.csv')
    races = ['WhiteJD1','BlackJD1','AsianJD1','HispanicJD1','NatHawJD1','TwoorMoreJD1']
    genders = ['MenJD1','WomenJD1']
    race_genders = []

    #Generate  the proper field names i.e. AsianMenJD1 for all races in first year.
    for race in races:
        for gender in genders:
            race_genders.append(race.replace("JD1","") +  gender)
    #Calculate Percentages for incoming class by race
    for race in races:
        df[race+"_Percentage"] = df[race]/df['TotalJD1'] * 100

    #Calculate Percentages for incoming class by gender
    for gender in genders:
        df[gender+"_Percentage"] = df[gender]/df['TotalJD1'] * 100

    #Calculate Percentages for incoming class by gender and race
    for race_gender in race_genders:
        df[race_gender+"_Percentage"] = df[race_gender]/df['TotalJD1'] * 100

    #Incoming Class by Race - Single School
    streamlit_tab.subheader("Student Diversity Incoming Class (Race)")
    race_choices = streamlit_tab.multiselect("Select Race",races,default=races)
    if(len(selected_schools) > 1):
        streamlit_tab.write("You can only have one school selected to use this chart")
    else:
        col1,col2 = streamlit_tab.columns(2)
        title = "Student Diversity Race Incoming Class"
        yaxis = race_choices

        fig_graphs = createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis)
        col1.plotly_chart(fig_graphs[0],use_container_width=True)
        col2.plotly_chart(fig_graphs[1],use_container_width=True)

    #Incoming Class by Gender - Single School
    streamlit_tab.subheader("Student Diversity Incoming Class (Gender)")
    if(len(selected_schools) > 1):
        streamlit_tab.write("You can only have one school selected to use this chart")
    else:
        col1,col2 = streamlit_tab.columns(2)
        title = "Student Diversity Gender Incoming Class"
        yaxis = genders

        fig_graphs = createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis)
        col1.plotly_chart(fig_graphs[0],use_container_width=True)
        col2.plotly_chart(fig_graphs[1],use_container_width=True)

    #Incoming Class by Race and Gender - Single School
    streamlit_tab.subheader("Student Diversity Incoming Class (Race + Gender)")
    race_gender_choices = streamlit_tab.multiselect("Select Race and Gender",race_genders,default=['AsianMenJD1','AsianWomenJD1'])
    if(len(selected_schools) > 1):
        streamlit_tab.write("You can only have one school selected to use this chart")
    else:
        col1,col2 = streamlit_tab.columns(2)
        title = "Student Diversity Race and Gender Incoming Class"
        yaxis = race_gender_choices

        fig_graphs = createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis)
        col1.plotly_chart(fig_graphs[0],use_container_width=True)
        col2.plotly_chart(fig_graphs[1],use_container_width=True)