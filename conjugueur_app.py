# On peut débuter par fusionner projet et developper chaque conjugueur independemment afin d'en fusionner l'esprit
# Ajouter fonction cache à tous les conjugueurs !!!
# pour généraliser, on pourra déjà créér un dico contenant les langues et addresses url de base

# Il faudra trouver un équilibre pour presenter les conjugaisons communes au français et à l'espagnol, trouver la bonne forme, ou placer le conditionnel, se place-t-il dans les temps de l'indicatif ou pas etc ...

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title='Verbes', page_icon='flag-fr', layout='centered')

hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

# This code will hide the dataframes indexes, see where to place it
st.markdown(hide_table_row_index, unsafe_allow_html=True)


BASE_FRENCH_VERBS_URL = 'https://www.wordreference.com/conj/frverbs.aspx?v='

verb = st.sidebar.text_input('Conjugaison du verbe')


if verb != '':
    verb_conjugation_page_url = BASE_FRENCH_VERBS_URL + verb

    tables = pd.read_html(verb_conjugation_page_url)

    indicatif_cols = st.columns(5)


    # indicatif
    present = tables[3]
    imparfait = tables[4]
    passe_simple = tables[5]
    futur = tables[6]
    # conditionnel = tables[7]

    # formes composees
    passe_compose = tables[7]
    plus_que_parfait = tables[8]
    passe_anterieur = tables[9]
    futuro_anterieur = tables[10]


    # Subjonctif
    subjonctif_present = tables[11]
    subjonctif_imparfait = tables[12]
    subjonctif_passe = tables[13]
    subjonctif_plus_que_parfait = tables[14]


    # Conditionnel
    conditionnel_present = tables[15]
    conditionnel_passe = tables[16]
    conditionnel_passe2 = tables[17]

    # Imperatif
    imperatif_present = tables[18]
    imperatif_passe = tables[19]


    df_indicatif = pd.concat([present, imparfait, passe_simple, futur], axis=1)
    df_indicatif = df_indicatif.set_axis(['', 'présent', ' ', 'imparfait', '  ', 'passé simple', '   ', 'futur'], axis='columns')

    df_formes_composees = pd.concat([passe_compose, plus_que_parfait, passe_anterieur, futuro_anterieur], axis=1)
    df_formes_composees = df_formes_composees.set_axis([' ', 'passé composé', '  ', 'plus-que-parfait', '   ', 'passé antérieur', '    ', 'futur antérieur'], axis='columns')

    df_subjonctif = pd.concat([subjonctif_present, subjonctif_imparfait, subjonctif_passe, subjonctif_plus_que_parfait], axis=1)
    df_subjonctif = df_subjonctif.set_axis([' ', 'présent', '  ', 'imparfait', '   ', 'passé', '    ', 'plus-que-parfait'], axis='columns')

    df_conditionnel = pd.concat([conditionnel_present, conditionnel_passe, conditionnel_passe2], axis=1)
    df_conditionnel = df_conditionnel.set_axis([' ', 'présent', '  ', 'passé', '   ', 'passé2'], axis='columns')

    df_imperatif = pd.concat([imperatif_present, imperatif_passe], axis=1)
    df_imperatif = df_imperatif.set_axis([' ', 'présent', '  ', 'passé'], axis='columns')


    st.subheader("Indicatif")
    st.table(df_indicatif.iloc[:, [0, 1, 3, 5, 7]])

    st.subheader("Formes composées")
    st.table(df_formes_composees.iloc[:, [0, 1, 3, 5, 7]])

    st.subheader("Subjonctif")
    st.table(df_subjonctif.iloc[:, [0, 1, 3, 5, 7]])

    st.subheader("Conditionnel")
    st.table(df_conditionnel.iloc[:, [0, 1, 3, 5]])
    
    st.subheader("Imperatif")
    st.table(df_imperatif.iloc[1:, [0, 1, 3]])


