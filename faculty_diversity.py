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
                title="Staff"
        ))
    
    #Percentage Numbers
    yaxis_percent = [ax + "_Percentage" for ax in yaxis]
    fig_percentage = px.line(selected_schools_df,x='CalendarYear',y=yaxis_percent,title="Percentage <br>" + title)
    fig_percentage.update_layout(
        yaxis=dict(
                title="Staff Percentage"
        ))
    return [fig_raw,fig_percentage]

def displayFacultyDiversity(streamlit_tab,selected_schools):
    streamlit_tab.header("Faculty Diversity")
    df = pandas.read_csv('Data_Files/Faculty (Academic Year).csv')


    #In the latest data dump AccessLex has changed FacOther to "FacAGI" standing for another gender.
    #Calculate Percentages for Faculty by Gender
    df["FacMen_Percentage"] = df["FacMen"]/df['FacTotal'] * 100
    df["FacWomen_Percentage"] = df["FacWomen"]/df['FacTotal'] * 100
    df["FacAGI_Percentage"] = df["FacAGI"]/df['FacTotal'] * 100

    #Calculate Percentages for Faculty by Gender and Full Time/Part Time
    df["FTFacMen_Percentage"] = df["FTFacMen"]/df['FacTotal'] * 100
    df["FTFacWomen_Percentage"] = df["FTFacWomen"]/df['FacTotal'] * 100
    df["FTFacAGI_Percentage"] = df["FTFacAGI"]/df['FacTotal'] * 100
    df["NonFTFacMen_Percentage"] = df["NonFTFacMen"]/df['FacTotal'] * 100
    df["NonFTFacWomen_Percentage"] = df["NonFTFacWomen"]/df['FacTotal'] * 100
    df["NonFTFacAGI_Percentage"] = df["NonFTFacAGI"]/df['FacTotal'] * 100



    #Calculate Pecentages for Faculty and Other Staff
    staff = ['FacTotal','FTFacTotal','NonFTFacTotal','TotalLibrarian','FTLibrarian','PTLibrarian','TotalAdmin',	'FTAdmin','PTAdmin']
    total_staff = df["FacTotal"] + df["TotalLibrarian"] + df['TotalAdmin']

    for st in staff:
        df[st+"_Percentage"] = df[st]/total_staff * 100

    #Incoming Faculty by Gender
    streamlit_tab.subheader("Faculty Diversity By Gender")
    if(len(selected_schools) > 1):
        streamlit_tab.write("You can only have one school selected to use this chart")
    else:
        col1,col2 = streamlit_tab.columns(2)
        title = "Faculty Diversity by Gender"
        yaxis = ["FacMen","FacWomen","FacAGI"]

        fig_graphs = createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis)
        col1.plotly_chart(fig_graphs[0],use_container_width=True)
        col2.plotly_chart(fig_graphs[1],use_container_width=True)


    
    #Incoming Class by Race and Gender - Single School
    streamlit_tab.subheader("Faculty Diversity By Gender and Full Time/Part Time")
    ft_non_ft = ["FTFacMen","FTFacWomen","FTFacAGI","NonFTFacMen","NonFTFacWomen","NonFTFacAGI"]
    race_gender_choices = streamlit_tab.multiselect("Select Race and Gender",ft_non_ft,default=['FTFacMen','NonFTFacMen'])
    if(len(selected_schools) > 1):
        streamlit_tab.write("You can only have one school selected to use this chart")
    else:
        col1,col2 = streamlit_tab.columns(2)
        title = "Faculty Diversity by Full Time and Part Time"
        yaxis = race_gender_choices

        fig_graphs = createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis)
        col1.plotly_chart(fig_graphs[0],use_container_width=True)
        col2.plotly_chart(fig_graphs[1],use_container_width=True)

    #Other Staff - Single School
    streamlit_tab.subheader("Other Staff")

    race_gender_choices = streamlit_tab.multiselect("Select Faculty Type",staff,default=['TotalLibrarian','TotalAdmin'])
    if(len(selected_schools) > 1):
        streamlit_tab.write("You can only have one school selected to use this chart")
    else:
        col1,col2 = streamlit_tab.columns(2)
        title = "Other School Staff"
        yaxis = race_gender_choices

        fig_graphs = createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis)
        col1.plotly_chart(fig_graphs[0],use_container_width=True)
        col2.plotly_chart(fig_graphs[1],use_container_width=True)
        col2.write("*Percentage based total staff (faculty + library + admin)" )



    #Admin/Librarian
    #This is down here because we technically calculate these percentages above with a denominator of all staff.
    #Here we want the denominator to be just the total admin or total library staff.
    df["FTAdmin_Percentage"] = df["FTAdmin"]/df['TotalAdmin'] * 100
    df["PTAdmin_Percentage"] = df["PTAdmin"]/df['TotalAdmin'] * 100
    df["FTLibrarian_Percentage"] = df["FTLibrarian"]/df['TotalLibrarian'] * 100
    df["PTLibrarian_Percentage"] = df["PTLibrarian"]/df['TotalLibrarian'] * 100


    #Admin Full Time/Part Time
    streamlit_tab.subheader("Admin Staff Full Time/Part Time")
    if(len(selected_schools) > 1):
        streamlit_tab.write("You can only have one school selected to use this chart")
    else:
        col1,col2 = streamlit_tab.columns(2)
        title = "Admin Staff By Full Time/Part Time"
        yaxis = ["FTAdmin","PTAdmin"]

        fig_graphs = createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis)
        col1.plotly_chart(fig_graphs[0],use_container_width=True)
        col2.plotly_chart(fig_graphs[1],use_container_width=True)

    #Librarian Full Time/Part Time
    streamlit_tab.subheader("Librarian Staff Full Time/Part Time")
    if(len(selected_schools) > 1):
        streamlit_tab.write("You can only have one school selected to use this chart")
    else:
        col1,col2 = streamlit_tab.columns(2)
        title = "Libarian Staff By Full Time/Part Time"
        yaxis = ["FTLibrarian","PTLibrarian"]

        fig_graphs = createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis)
        col1.plotly_chart(fig_graphs[0],use_container_width=True)
        col2.plotly_chart(fig_graphs[1],use_container_width=True)