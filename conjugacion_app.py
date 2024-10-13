# Anadamos funccion cache para no cargar mas de lo normal cuando ya se ha interrogado un verbo dado no?
# Invertir a lo mejor la columna pretérito perfecto simple y el imperfecto para que coincidan con las columnas de los tiempos compuestos

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
# from conjugacion import *

st.set_page_config(page_title='Verbos', page_icon='flag-es', layout='centered')

hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

# This code will hide the dataframes indexes, see where to place it
st.markdown(hide_table_row_index, unsafe_allow_html=True)


BASE_SPANISH_VERBS_URL = 'https://www.wordreference.com/conj/esverbs.aspx?v='

verb = st.sidebar.text_input('Conjugación del verbo')


if verb != '':
    verb_conjugation_page_url = BASE_SPANISH_VERBS_URL + verb

    tables = pd.read_html(verb_conjugation_page_url)

    indicativo_cols = st.columns(5)


    # indicativo
    presente = tables[3]
    imperfecto = tables[4]
    preterito = tables[5]
    futuro = tables[6]
    condicional = tables[7]

    # formas compuestas compuestas
    preterito_perfecto = tables[8]
    pluscuamperfecto = tables[9]
    futuro_perfecto = tables[10]
    condicional_perfecto = tables[11]
    preterito_anterior = tables[20]


    # Subjuntivo
    subjuntivo_presente = tables[12]
    subjuntivo_imperfecto = tables[13]
    subjuntivo_futuro = tables[14]

    # Subjuntivo formas compuestas, anadir preterito anterior a esta tabla
    subjuntivo_preterito_perfecto = tables[15]
    subjuntivo_pluscuamperfecto = tables[16]
    subjuntivo_futuro_perfecto = tables[17]

    # Imperativo
    imperativo_afirmativo = tables[18]
    imperativo_negativo = tables[19]


    df_indicativo = pd.concat([presente, imperfecto, preterito, futuro, condicional], axis=1)
    df_indicativo = df_indicativo.set_axis(['', 'presente', ' ', 'imperfecto', '  ', 'pretérito', '   ', 'futuro', '    ', 'condicional'], axis='columns')

    df_formas_compuestas = pd.concat([preterito_perfecto, pluscuamperfecto, futuro_perfecto, condicional_perfecto], axis=1)
    df_formas_compuestas = df_formas_compuestas.set_axis([' ', 'pretérito perfecto', '  ', 'pluscuamperfecto', '   ', 'futuro perfecto', '    ', 'condicional perfecto'], axis='columns')

    df_subjuntivo = pd.concat([subjuntivo_presente, subjuntivo_imperfecto, subjuntivo_futuro], axis=1)
    df_subjuntivo = df_subjuntivo.set_axis([' ', 'presente', '  ', 'imperfecto', '   ', 'futuro'], axis='columns')


    df_subjuntivo_formas_compuestas = pd.concat([subjuntivo_preterito_perfecto, subjuntivo_pluscuamperfecto, subjuntivo_futuro_perfecto], axis=1)
    df_subjuntivo_formas_compuestas = df_subjuntivo_formas_compuestas.set_axis([' ', 'pretérito perfecto', '  ', 'pluscuamperfecto', '   ', 'futuro perfecto'], axis='columns')

    df_imperativo = pd.concat([imperativo_afirmativo, imperativo_negativo], axis=1)
    df_imperativo = df_imperativo.set_axis([' ', 'afirmativo', '  ', 'negativo'], axis='columns')

    df_preterito_anterior = preterito_anterior.set_axis([' ', 'pretérito anterior'], axis='columns')


    st.subheader("Indicativo")
    st.table(df_indicativo.iloc[:, [0, 1, 3, 5, 7, 9]])

    st.subheader("Formas compuestas comunes")
    st.table(df_formas_compuestas.iloc[:, [0, 1, 3, 5, 7]])

    st.subheader("Subjuntivo")
    st.table(df_subjuntivo.iloc[:, [0, 1, 3, 5]])
    
    st.subheader("Formas compuestas subjuntivo")
    st.table(df_subjuntivo_formas_compuestas.iloc[:, [0, 1, 3, 5]])

    st.subheader("Imperativo")
    st.table(df_imperativo.iloc[1:, [0, 1, 3]])

    st.subheader("Pretérito anterior (en desuso)")
    st.table(df_preterito_anterior.iloc[:, [0, 1]])

