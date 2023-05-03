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

def createSingleGraph(df,selected_schools,title,yaxis):
    selected_schools_df = df.loc[df['schoolname'].isin(selected_schools)]
    fig = px.line(selected_schools_df,x='CalendarYear',y=yaxis,color='schoolname',title=title)
    return fig

def displayAdmissions(streamlit_tab,selected_schools):
    streamlit_tab.header("Admission Metrics")
    df = pandas.read_csv('Data_Files/Admissions.csv')
    df['NumOffers_Percentage'] = df['NumOffers']/df['NumApps'] * 100
    df['NumMatriculants_Percentage_Offers'] = df['NumMatriculants']/df['NumOffers'] * 100
    df['NumMatriculants_Percentage_Applications'] = df['NumMatriculants']/df['NumApps'] * 100
    df['NumOffers_Percentage_Apps'] = df['NumOffers']/df['NumApps'] * 100

    # df['Bar_And_JD_Advantage_FTLT'] = df['Bar_FTLT'] + df['JDA_FTLT']
    # df['Bar_And_JD_Advantage_FTLT_Percentage'] = df['Bar_And_JD_Advantage_FTLT'] /df['Total_Grads'] * 100

    #LSAT and GPA
    streamlit_tab.subheader("LSAT and GPA")
    col1,col2 = streamlit_tab.columns(2)
    title = "LSAT Score Full Time + Part Time"
    lsat_fig = createSingleGraph(df,selected_schools,title,'LSAT50')
    title = "GPA Full Time + Part Time"
    gpa_fig = createSingleGraph(df,selected_schools,title,'UGGPA50')
    col1.plotly_chart(lsat_fig,use_container_width=True)
    col2.plotly_chart(gpa_fig,use_container_width=True)

    streamlit_tab.divider()

    #Number of Applications
    streamlit_tab.subheader("Number of Applications")
    title = "Raw Number of Applications"
    number_of_apps_fig = createSingleGraph(df,selected_schools,title,'NumApps')
    streamlit_tab.plotly_chart(number_of_apps_fig,use_container_width=True)

    streamlit_tab.divider()

    #Number of Offers
    streamlit_tab.subheader("Offers")
    col1,col2 = streamlit_tab.columns(2)
    title = "Offers"
    yaxis = ['NumOffers','NumOffers_Percentage']
    fig_graphs = createRawAndPercentGraph(df,selected_schools,title,yaxis)
    col1.plotly_chart(fig_graphs[0],use_container_width=True)
    col2.plotly_chart(fig_graphs[1],use_container_width=True)
    col2.write("*Percentage based on offers/total applications")
    
    streamlit_tab.divider()

    #Number of Accepted Offers
    streamlit_tab.subheader("Acceptance/Matriculants")
    col1,col2 = streamlit_tab.columns(2)
    title = "Accepted Offers by Total Applications"
    yaxis = ['NumMatriculants','NumMatriculants_Percentage_Applications']
    fig_graphs = createRawAndPercentGraph(df,selected_schools,title,yaxis)
    col1.plotly_chart(fig_graphs[0],use_container_width=True)
    col2.plotly_chart(fig_graphs[1],use_container_width=True)
    col2.write("*Percentage based on acceptance/total applications")
    title = "Accepted offers by Total Offers"
    yaxis = ['NumMatriculants','NumMatriculants_Percentage_Offers']
    fig_graphs = createRawAndPercentGraph(df,selected_schools,title,yaxis)
    col1.plotly_chart(fig_graphs[0],use_container_width=True)
    col2.plotly_chart(fig_graphs[1],use_container_width=True)
    col2.write("*Percentage based on accpetance/total offers")
    
