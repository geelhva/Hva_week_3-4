#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install streamlit


# In[9]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# In[5]:


df = pd.read_csv('https://raw.githubusercontent.com/jwilber/Bob_Ross_Paintings/master/data/bob_ross_paintings.csv', index_col=0)


# In[13]:


slider_range =st.slider('probeersel',
                       value=[1,15])

