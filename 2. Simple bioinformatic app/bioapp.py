
import pandas as pd

import streamlit as st
import altair as alt
from PIL import Image

image=Image.open('download.jpg')

st.image(image, use_column_width=True)


st.write('''

## DNA Nucleotide Count web APP
This is a demo app made by Jagat
''')

st.header('Enter DNA Sequence')

Sequence_input= ">DNA QUERY 5 \n aataggcccctcaccccgctgattcctgttggagtataaacgacccctccgacgaagttaacaatgagtgggtcctagggagattggcgcacccgaatcggtcttgcatgggtcgagttattccgactgtcgggggcaactccttgggcggcaaaaagaccacggacgggcgtaaccaactagatattcctcagaaaaatgcagatttttgatttttttctcctttccgactttttgggataagtaactactgctgggcggcaacctgaaacgtgcgttgacaatatcaggagtctcatcgcattcgagccctcggcctcatccagatcgaaggacttacaacgcggtgcgcgccatggctccgcaagtgctatagcaaccagtagaagttcgatggattcaaggtgcgtgtctagtgaagggaagggatcccagatgagcgtcggggatcatggtcaaagggcaatggcacgatagctgcacacctgacttttcgcctatgactcctacgcgaacgctacctacagacacggtatcatctaggatttgccaagttcgcttaaatcgacaagccagatattagggtggactgcaggttgccagctttcaggtggatgcggctatgtggcgcctgaagtctagatcttgatggggtactatatgacggagtcgggttgccgcaataagttgtgggctgctacggaattgtgtaccagcagcccctctcacactgctcgcgctgcatatgcaagtgcgctttgatgtttccttgctaagccacaagcttaaatatgagtagtaaggtccgactcgctatataatccgtggggttgtcccttctccagggactccggccttactagcatcttttctaggggctttagcaaccgagagtacgtgtccgtccaggtggaacatctaaattcaaaattcaagctacgaagaataggtgctgcctctggacagtatagcgaatagcagattgaatgatcatgtcaa"

sequence=st.text_area("Sequence_input", Sequence_input, height=125)
sequence=sequence.splitlines()
sequence=sequence[1]
sequence=''.join(sequence)

st.write("""
***
""")

st.header('INPUT (DNA QUERY)')
sequence

st.header("OutPut of Necoui")

st.subheader("1. by using dictonary")
def DNA_count(seq):
    d=dict([
        ('A',seq.count('a')),
        ('T',seq.count('t')),
        ('G', seq.count('g')),
        ('C',seq.count('c'))
    ])
    return d

X=DNA_count(sequence)

X


X_label=list(X)
x_values=list(X.values())


st.subheader("2. In text form")
st.write("The count of A is",X['A'])
st.write("The count of G is",X['G'])
st.write("The count of T is",X['T'])
st.write("The count of C is",X['C'])



st.subheader("From the data frame")
df=pd.DataFrame.from_dict(X,orient="index")
df=df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df=df.rename(columns={'index':"nucleotide"})
st.write(df)

st.subheader("4. Display in bar chart")

p=alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p=p.properties(
    width=alt.Step(80)
)

st.write(p)
