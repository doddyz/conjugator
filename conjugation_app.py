# Will need to anticipate merging together multi lang conjugator apps

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title='English Verbs', page_icon='flag-gb', layout='centered')

hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

# This code will hide the dataframes indexes, see where to place it
st.markdown(hide_table_row_index, unsafe_allow_html=True)


BASE_ENGLISH_VERBS_URL = 'https://www.wordreference.com/conj/enverbs.aspx?v='

verb = st.sidebar.text_input('Conjugation of verb')


if verb != '':
    verb_conjugation_page_url = BASE_ENGLISH_VERBS_URL + verb

    tables = pd.read_html(verb_conjugation_page_url)

    indicativo_cols = st.columns(5)


    # indicative
    present = tables[3]
    simple_past = tables[4]
    future = tables[5]

    # Perfect tenses
    present_perfect = tables[6]
    past_perfect = tables[7]
    future_perfect = tables[8]

    # Continuous (progressive) and emphatic tenses
    present_continuous = tables[9]
    past_continuous = tables[10]
    present_emphatic = tables[11]
    past_emphatic = tables[12]

    # Compound Continuous (progressive) tenses
    compound_present_perfect = tables[13]
    compound_past_perfect = tables[14]
    compound_future = tables[15]
    compound_future_perfect = tables[16]
    
 
    # Subjuntivo
    # subjuntivo_presente = tables[12]
    # subjuntivo_imperfecto = tables[13]
    # subjuntivo_futuro = tables[14]

    # Subjuntivo formas compuestas, anadir preterito anterior a esta tabla
    # subjuntivo_preterito_perfecto = tables[15]
    # subjuntivo_pluscuamperfecto = tables[16]
    # subjuntivo_futuro_perfecto = tables[17]

    # Imperativo
    # imperativo_afirmativo = tables[18]
    # imperativo_negativo = tables[19]


    df_indicative = pd.concat([present, simple_past, future], axis=1)
    df_indicative = df_indicative.set_axis(['', 'present', ' ', 'simple past','   ', 'future'], axis='columns')

    df_perfect_tenses = pd.concat([present_perfect, past_perfect, future_perfect], axis=1)
    df_perfect_tenses = df_perfect_tenses.set_axis([' ', 'present perfect', '  ', 'past perfect', '   ', 'future perfect'], axis='columns')

    df_continuous_progressive_tenses = pd.concat([present_continuous, past_continuous, present_emphatic, past_emphatic], axis=1)
    df_continuous_progressive_tenses = df_continuous_progressive_tenses.set_axis([' ', 'present continuous', '  ', 'past continuous', '   ', 'present emphatic', '    ', 'past emphatic'], axis='columns')

    df_compound_continuous_progressive_tenses = pd.concat([compound_present_perfect, compound_past_perfect, compound_future, compound_future_perfect], axis=1)
    df_compound_continuous_progressive_tenses = df_compound_continuous_progressive_tenses.set_axis([' ', 'compound present perfect', '  ', 'compound past perfect', '   ', 'compound future', '    ', 'compound future perfect'], axis='columns')


    st.subheader("Indicative")
    st.table(df_indicative.iloc[:, [0, 1, 3, 5]])

    st.subheader("Perfect Tenses")
    st.table(df_perfect_tenses.iloc[:, [0, 1, 3, 5]])


    st.subheader("Continuous progressive and emphatic tenses")
    st.table(df_continuous_progressive_tenses.iloc[:, [0, 1, 3, 5, 7]])


    st.subheader("Compound continuous progressive tenses")
    st.table(df_compound_continuous_progressive_tenses.iloc[:, [0, 1, 3, 5, 7]])
    
    
    # st.subheader("Conditional")
    # st.table(df_conditional.iloc[:, [0, 1, 3, 5]])


    # st.subheader("Imperative")
    # st.table(df_imperative.iloc[1:, [0, 1, 3]])
    
    
    # st.subheader("Subjuntive")
    # st.table(df_subjuntive.iloc[:, [0, 1, 3, 5]])
    

