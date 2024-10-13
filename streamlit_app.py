# Will need to anticipate merging together multi lang conjugator apps

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# st.set_page_config(page_title='Conjugator App', page_icon='', layout='centered')

pages = st.navigation([st.Page("conjugacion_app.py", title="Verbos", icon="🇪🇸"), st.Page("conjugueur_app.py", title="Verbes", icon="🇫🇷"), st.Page("conjugation_app.py", title="Verbs", icon="🇬🇧")])

pages.run()

