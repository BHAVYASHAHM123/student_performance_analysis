import numpy as np
import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
from PIL.ImageFile import StubImageFile



st.header('Student Performance Analysis :student:')


school = st.selectbox(
    'school (Enter 0 -> Mousinho da Silveira and 1 -> Gabriel Pereira)',
    ('school', '0', '1'))

Gender = st.selectbox(
    'Gender (1 -> Male, 2 -> Female)',
    ('Gender','1', '0'))

age = st.slider(
    'Age',
    15.0, 22.0, (20.0, 11.0))


Address = st.selectbox(
    'Address (Enter 1 -> Uraban and 0 -> Rural)',
    ('Address','0', '1'))

 

Family_Size = st.selectbox(
    'Family Size (Less or equal to 3 -> 1, Greater than 3 -> 0)',
    ('Family Size','1', '0'))

 
Parents_Status = st.selectbox(
    'Parents Status (Apart -> 0, Together -> 1)',
    ('Parents Status','0', '1'))

 
Mother_Education = st.selectbox(
    'Mother Education (primary edu (4th grade) -> 1,  5th to 9th grade -> 2,  secondary edu -> 3,  higher edu -> 4)',
    ('Mother Education', '1', '2', '3', '4'))

 
Father_Education = st.selectbox(
    'Father Education (primary edu (4th grade) -> 1,  5th to 9th grade -> 2,  secondary edu -> 3,  higher edu -> 4)',
    ('Father Education', '1', '2', '3', '4'))

 
Mother_Job = st.selectbox(
    'Mother Job (0 -> At home, 1 -> Health Care Service, 2 -> Other, 3 -> Civil Service (Administrative or Police), 4 -> teacher )',
    ('Mother Job','0', '1', '2', '3', '4'))

 
Father_Job = st.selectbox(
    'Father Job (0 -> At home, 1 -> Health Care Service, 2 -> Other, 3 -> Civil Service (Administrative or Police), 4 -> teacher )',
    ('Father Job','0', '1', '2', '3', '4'))

 
Reason_To_Choose_this_College = st.selectbox(
    'Reason To Choose this College (0 -> Course Preference, 1 -> close to home, 2 -> Other, 3 -> College Reputation)',
    ('Reason To Choose this College', '0', '1', '2', '3'))

 

Guardian = st.selectbox(
    'Guardian (0 -> Father, 1 -> Mother, 2 -> Other)',
    ('Guardian','0','1', '2'))

 

Travel_Time_from_home_to_College = st.selectbox(
    'Travel Time from home to College (1 -> <15 min., 2 -> 15 to 30 min., 3 -> 30 min. to 1 hour, or 4 -> >1 hour)',
    ('Travel Time from home to College','1', '2', '3', '4'))

 

Study_Time = st.selectbox(
    'Study Time (1 -> <2 hours, 2 -> 2 to 5 hours, 3 -> 5 to 10 hours, or 4 -> >10 hours)',
    ('Study Time','1', '2', '3', '4'))

 

Number_of_Failures = st.selectbox(
    'Number of Failures in exam',
    ('Number of Failures','0', '1', '2', '3'))

 


Extra_educational_support = st.selectbox(
    'extra educational support (1 -> Yes, 0 -> No)',
    ('extra educational support','1', '0'))

 

Family_educational_support = st.selectbox(
    'Family educational support (1 -> Yes, 0 -> No)',
    ('Family educational support','1', '0'))

 

Extra_paid_classes_within_the_course_subject = st.selectbox(
    'Extra paid classes within the course subject (1 -> Yes, 0 -> No)',
    ('Extra paid classes within the course subject','1', '0'))

 

Extra_Curricular_Activities = st.selectbox(
    'Extra-Curricular Activities (1 -> Yes, 0 -> No)',
    ('Extra-Curricular Activities','1', '0'))

 

Attended_Nursary = st.selectbox(
    'attended nursery school (1 -> Yes, 0 -> No)',
    ('attended nursery school','1', '0'))

 
Want_to_take_higher_edu = st.selectbox(
    'Want to take higher edu (1 -> Yes, 0 -> No)',
    ('Internet access at home','1', '0'))


Internet_access_at_home = st.selectbox(
    'Internet access at home (1 -> Yes, 0 -> No)',
    ('Internet access at home','1', '0'))


With_a_romantic_relationship = st.selectbox(
    'With a romantic relationship (1 -> Yes, 0 -> No)',
    ('With a romantic relationship','1', '0'))

 

Quality_of_Family_relationships = st.selectbox(
    'Quality of Family relationships (1 -> Very Bad, 2 -> Bad, 3 -> Fair, 4-> Good, 5 -> Excellent)',
    ('Quality of Family relationships','1', '2', '3', '4', '5'))

 

Free_Time_after_College = st.selectbox(
    'Free Time after College (1 -> Very Low, 2 -> Low, 3 -> Average, 4-> High, 5 -> Very High)',
    ('Free Time after College','1', '2', '3', '4', '5'))

 

Going_out_with_friends = st.selectbox(
    'Going out with friends (1 -> Very Low, 2 -> Low, 3 -> Average, 4-> High, 5 -> Very High)',
    ('Going out with friends','1', '2', '3', '4', '5'))

 

workday_alcohol_consumption = st.selectbox(
    'workday alcohol consumption (1 -> Very Low, 2 -> Low, 3 -> Average, 4-> High, 5 -> Very High)',
    ('workday alcohol consumption','1', '2', '3', '4', '5'))

 

weekend_alcohol_consumption = st.selectbox(
    'weekend alcohol consumption (1 -> Very Low, 2 -> Low, 3 -> Average, 4-> High, 5 -> Very High)',
    ('weekend alcohol consumption','1', '2', '3', '4', '5'))



current_health_status = st.selectbox(
    'current health status (1 -> Very Low, 2 -> Low, 3 -> Average, 4-> High, 5 -> Very High)',
    ('current health status','1', '2', '3', '4', '5' ))

absenses = st.text_input('number of school absences', )


G1 = st.slider(
    'G1',
    0.0, 20.0, (6.9, 20.0))

G2 = st.slider(
    'G2',
    0.0, 20.0, (6.5, 19.6))


st.text(absenses)


if st.button('Submit'):
    model = joblib.load('rf.pkl')
    scalar = joblib.load('scalar.pkl')
    # store data
    X = pd.DataFrame([[ school  , Gender  , age  , Address  , Family_Size  , Parents_Status  ,
                        Mother_Education  , Father_Education  , Mother_Job  , Father_Job  , Reason_To_Choose_this_College  ,
                        Guardian  , Travel_Time_from_home_to_College  , Study_Time  , Number_of_Failures  , Extra_educational_support  ,
                        Family_educational_support  , Extra_paid_classes_within_the_course_subject  , Extra_Curricular_Activities  ,
                        Attended_Nursary  , Want_to_take_higher_edu  , Internet_access_at_home  , With_a_romantic_relationship  , Quality_of_Family_relationships  ,
                        Free_Time_after_College  , Going_out_with_friends  , workday_alcohol_consumption  , weekend_alcohol_consumption  , current_health_status  ,
                        absenses  , G1  , G2 ]],
            columns = ['school' ,'sex' ,'age' ,'address' ,'famsize' ,'Pstatus' ,'Medu' ,'Fedu' ,'Mjob' ,'Fjob' ,'reason' ,'guardian' ,'traveltime' ,'studytime' ,'failures' ,'schoolsup' ,'famsup' ,'paid' ,'activities' ,'nursery' ,'higher' ,'internet' ,'romantic' ,'famrel' ,'freetime' ,'goout' ,'Dalc' ,'Walc' ,'health' ,'absences' ,'G1' ,'G2'])




    predict = model.predict(scalar.transform(X))
    st.text(predict)

