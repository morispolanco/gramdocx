import streamlit as st
import openai
import docx2txt
import os

openai.api_key = os.getenv("openai_api_key")

def correccion_gramatical(texto):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"Corregir gramática y estilo en el siguiente texto:\n{texto}\n\nCorrección:"),
        temperature=0.5,
        max_tokens=3824,
        n = 1,
        stop=None

    )

    correccion = response.choices[0].text.strip()
    return correccion

st.title("Corrección gramatical con GPT-3")
st.write("Esta aplicación utiliza GPT-3 de OpenAI para corregir la gramática y el estilo en archivos .docx.")

archivo = st.file_uploader("Cargar archivo .docx", type=["docx"])

if archivo is not None:
    texto = docx2txt.process(archivo)
    correccion = correccion_gramatical(texto)

    st.subheader("Texto original:")
    st.write(texto)

    st.subheader("Texto corregido:")
    st.write(correccion)
