import streamlit as st
import pandas
import plotly.express as px
def createRawAndPercentGraph(df,selected_schools,title,yaxis):
    #Chart 1 Raw
    selected_schools_df = df.loc[df['schoolname'].isin(selected_schools)]
    fig_raw = px.line(selected_schools_df,x='Cohort',y=yaxis[0],color='schoolname',title="Raw <br>" + title)
    #Chart 2 Percentage
    fig_percentage = px.line(selected_schools_df,x='Cohort',y=yaxis[1],color='schoolname',title="Percentage <br>" + title)
    return [fig_raw,fig_percentage]

def createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis):
    #Bar Passage Full Time Long Term
    selected_schools_df = df.loc[df['schoolname'].isin(selected_schools)]
    fig_raw = px.line(selected_schools_df,x='Cohort',y=yaxis,title="Raw <br>" + title)
    #Percentage Numbers
    yaxis_percent = [ax + "_Percentage" for ax in yaxis]
    fig_percentage = px.line(selected_schools_df,x='Cohort',y=yaxis_percent,title="Percentage <br>" + title)
    return [fig_raw,fig_percentage]

def displayEmployment(selected_tab,selected_schools):
    selected_tab.header("Employement Metrics")
    df = pandas.read_csv('Data_Files/Employment.csv')
    # df['Bar_FTLT_Percentage'] = df['Bar_FTLT']/df['Total_Grads'] * 100
    # df['Bar_And_JD_Advantage_FTLT'] = df['Bar_FTLT'] + df['JDA_FTLT']
    # df['Bar_And_JD_Advantage_FTLT_Percentage'] = df['Bar_And_JD_Advantage_FTLT'] /df['Total_Grads'] * 100
    df['Private_Law_Firm_Total_Emp'] = df['Solo_Emp'] + df['Sz_1_10_Emp'] + df['Sz_11_25_Emp'] +df['Sz_26_50_Emp'] +df['Sz_51_100_Emp'] +df['Sz_101_250_Emp'] +df['Sz_251_500_Emp'] +df['Sz_501up_Emp'] + df['Sz_Unk_Emp']
    df['Private_Law_Firm_Total_Percentage'] =  df['Private_Law_Firm_Total_Emp']/df['Total_Emp_Type'] * 100
    df['Private_Law_Firm_Total_FTLT'] = df['Solo_Emp'] + df['Sz_1_10_FTLT'] + df['Sz_11_25_FTLT'] +df['Sz_26_50_FTLT'] +df['Sz_51_100_FTLT'] +df['Sz_101_250_FTLT'] +df['Sz_251_500_FTLT'] +df['Sz_501up_FTLT'] + df['Sz_Unk_FTLT']
    df['Private_Law_Firm_Total_FTLT_Percentage'] =  df['Private_Law_Firm_Total_FTLT']/df['Total_Emp_Type'] * 100
    df['Private_Law_Firm_Total_FTST'] = df['Solo_Emp'] + df['Sz_1_10_FTST'] + df['Sz_11_25_FTST'] +df['Sz_26_50_FTST'] +df['Sz_51_100_FTST'] +df['Sz_101_250_FTST'] +df['Sz_251_500_FTST'] +df['Sz_501up_FTST'] + df['Sz_Unk_FTST']
    df['Private_Law_Firm_Total_FTST_Percentage'] =  df['Private_Law_Firm_Total_FTST']/df['Total_Emp_Type'] * 100
    df['Private_Law_Firm_Total_PTLT'] = df['Solo_Emp'] + df['Sz_1_10_PTLT'] + df['Sz_11_25_PTLT'] +df['Sz_26_50_PTLT'] +df['Sz_51_100_PTLT'] +df['Sz_101_250_PTLT'] +df['Sz_251_500_PTLT'] +df['Sz_501up_PTLT'] + df['Sz_Unk_PTLT']
    df['Private_Law_Firm_Total_PTLT_Percentage'] =  df['Private_Law_Firm_Total_PTLT']/df['Total_Emp_Type'] * 100
    df['Private_Law_Firm_Total_PTST'] = df['Solo_Emp'] + df['Sz_1_10_PTST'] + df['Sz_11_25_PTST'] +df['Sz_26_50_PTST'] +df['Sz_51_100_PTST'] +df['Sz_101_250_PTST'] +df['Sz_251_500_PTST'] +df['Sz_501up_PTST'] + df['Sz_Unk_PTST']
    df['Private_Law_Firm_Total_PTST_Percentage'] =  df['Private_Law_Firm_Total_PTST']/df['Total_Emp_Type'] * 100



    private_firm_types = ['Solo','Sz_1_10','Sz_11_25','Sz_26_50','Sz_51_100','Sz_101_250','Sz_251_500','Sz_501up','Sz_Unk']
    employment_types = ['Private_Law_Firm_Total','BsInd','Gov','Pub','FedClk','LocClk','IntlClk','TribalClk','OthClk','Acad','Unk']
    employment_status = ['Bar','JDA','Prof','Nprof','Funded','Undet','GradSch_FT','Emp_Def','Unemp_NS','Unemp_Seek','Emp_Stat_Unk'] #Other Position is 'Nprof'
    part_time_full_time_types = ["FTLT","FTST","PTLT","PTST","Emp"]
    df['IntlClk_Emp'] = df['IntlClk']
    df['TribalClk_Emp'] = df['TribalClk']
    df['IntlClk_PTLT'] = df['IntlClkl_PTLT'] #Addresses weird typo in dataset

    #Add Employed Status
    for ptft in part_time_full_time_types:
        for tes in ['GradSch_FT','Emp_Def','Unemp_NS','Unemp_Seek','Emp_Stat_Unk']:
            if(ptft == 'Emp'):
                df[tes + "_" + ptft] = df[tes]
            else:
                df[tes + "_" + ptft] = 0
        for es in employment_status:
            df[es + "_" + ptft + "_Percentage"] = df[es + "_" + ptft] /df['Total_Grads'] * 100
    #Add Bar Passage Rages
    for ptft in part_time_full_time_types:
        df['Bar_' + ptft + '_Percentage'] = df['Bar_' + ptft]/df['Total_Grads'] * 100
        df['Bar_And_JD_Advantage_' + ptft] = df['Bar_'+ptft] + df['JDA_'+ptft]
        df['Bar_And_JD_Advantage_' + ptft + '_Percentage'] = df['Bar_And_JD_Advantage_' + ptft] /df['Total_Grads'] * 100


    #Add Pecentage for Law Firms
    for pf in private_firm_types:
        for ptft in part_time_full_time_types:
            df[pf+"_" + ptft + "_Percentage"] = df[pf+"_" + ptft]/df['Private_Law_Firm_Total_Emp'] * 100
    
    #Add Percentages for Employment Types
    for job in employment_types:
        for ptft in part_time_full_time_types:
            df[job+"_"+ptft+"_Percentage"] = df[job+"_"+ptft]/df['Total_Emp_Type'] * 100


    time_jobs_dictionary = {
        "Full Time Long Term": "FTLT",
        "Full Time Short Term": "FTST",
        "Part Time Long Term": "PTLT",
        "Part Time Short Term": "PTST",
        "Total": "Emp"
    }
    #Bar Passage Required
    selected_tab.subheader("Bar Passage Required Employment")
    job_part_full_time_select = selected_tab.selectbox("Full Time Part Time Options",time_jobs_dictionary.keys(),index=4,key='Bar Passage Rates')
    col1,col2 = selected_tab.columns(2)
    title = "Bar Passage Required Employment"
    yaxis = ['Bar_' + time_jobs_dictionary[job_part_full_time_select],'Bar_' + time_jobs_dictionary[job_part_full_time_select]+'_Percentage']
    #yaxis = ['Bar_FTLT','Bar_FTLT_Percentage']
    fig_graphs = createRawAndPercentGraph(df,selected_schools,title,yaxis)
    col1.plotly_chart(fig_graphs[0])
    col2.plotly_chart(fig_graphs[1])

    selected_tab.divider()

    #Bar Passage Required + JD Advantage
    selected_tab.subheader("Bar Passage Required Employment + JD Advantage Employment")
    job_part_full_time_select = selected_tab.selectbox("Full Time Part Time Options",time_jobs_dictionary.keys(),index=4,key='Bar Passage + JD Advantage Rates')
    col1,col2 = selected_tab.columns(2)
    title = "Bar Passage Required Employment + <br>JD Advantage Employment"
    #yaxis = ['Bar_And_JD_Advantage_FTLT','Bar_And_JD_Advantage_FTLT_Percentage']
    yaxis = ['Bar_And_JD_Advantage_' + time_jobs_dictionary[job_part_full_time_select],'Bar_And_JD_Advantage_' + time_jobs_dictionary[job_part_full_time_select]+'_Percentage']

    fig_graphs = createRawAndPercentGraph(df,selected_schools,title,yaxis)
    col1.plotly_chart(fig_graphs[0])
    col2.plotly_chart(fig_graphs[1])

    selected_tab.divider()

    #Employment Status
    selected_tab.subheader("Employment Status Single School")
    employment_status_choices = selected_tab.multiselect("Select Employment Status",employment_status,default=['Bar','JDA'])
    job_part_full_time_select = selected_tab.selectbox("Full Time Part Time Options",time_jobs_dictionary.keys(),key='Employment Status Single School',index=4)
    if(len(selected_schools) > 1):
        selected_tab.write("You can only have one school selected to use this chart")
    else:
        col1,col2 = selected_tab.columns(2)
        title = "Employment Status"
        yaxis = [et + "_" + time_jobs_dictionary[job_part_full_time_select] for et in employment_status_choices]

        fig_graphs = createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis)
        col1.plotly_chart(fig_graphs[0])
        col2.plotly_chart(fig_graphs[1])

    selected_tab.divider()


    #Law Firm Numbers
    selected_tab.subheader("Law Firm Employment")
    # print(df['Sz_51_100_FTLT_Pecentage'])
    job_part_full_time_select = selected_tab.selectbox("Law Firm Full Time Part Time Options",time_jobs_dictionary.keys(),index=4)
    col1,col2 = selected_tab.columns(2)
    title = "Law Firm Employment"
    #yaxis = ['Private_Law_Firm_Total','Private_Law_Firm_Total_Percentage']
    yaxis = ['Private_Law_Firm_Total_'+time_jobs_dictionary[job_part_full_time_select],'Private_Law_Firm_Total_'+time_jobs_dictionary[job_part_full_time_select]+'_Percentage']
    fig_graphs = createRawAndPercentGraph(df,selected_schools,title,yaxis)
    col1.plotly_chart(fig_graphs[0])
    col2.plotly_chart(fig_graphs[1])
    col2.write("*Percentage is based on total employment")

    selected_tab.divider()

    #Law Firm Numbers Size
    selected_tab.subheader("Law Firm Employment Full and Part Time Single School")

    job_part_full_time_select = selected_tab.selectbox("Law Firm Full Time/Part Time Options",time_jobs_dictionary.keys(),index=4)
    if(len(selected_schools) > 1):
        selected_tab.write("You can only have one school selected to use this chart")
    else:
        col1,col2 = selected_tab.columns(2)
        title = "Law Firm Employment"
        yaxis = []
        for pf in private_firm_types:
            #print(pf+"_"+job_part_full_time_select)
            yaxis.append(pf+"_"+time_jobs_dictionary[job_part_full_time_select])
        fig_graphs = createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis)
        col1.plotly_chart(fig_graphs[0])
        col2.plotly_chart(fig_graphs[1])
        col2.write("*Percentage is based on total people employed in private law firms.")

    selected_tab.divider()

    #Employment Type
    selected_tab.subheader("Employment Categories Single School")
    employment_type_choices = selected_tab.multiselect("Select Employment Types",employment_types,default='Private_Law_Firm_Total')
    job_part_full_time_select = selected_tab.selectbox("Full Time Part Time Options",time_jobs_dictionary.keys(),key='Employment Type')

    if(len(selected_schools) > 1):
        selected_tab.write("You can only have one school selected to use this chart")
    else:
        #job_part_full_time_select = selected_tab.selectbox("FTLT","FTST","PTLT","PTST","Total")
        col1,col2 = selected_tab.columns(2)
        title = "Employment Category"
        yaxis = [et + "_" + time_jobs_dictionary[job_part_full_time_select] for et in employment_type_choices]

        fig_graphs = createRawAndPercentGraphSingleSchool(df,selected_schools,title,yaxis)
        col1.plotly_chart(fig_graphs[0])
        col2.plotly_chart(fig_graphs[1])