import os
import streamlit as st
import docx
import magic
import openai

def grammar_style_correction(document, api_key):
    openai.api_key = api_key

    # Hace una llamada a la API de GPT-3 para corregir la gramática y el estilo
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=document,
        temperature=0.7,
        max_tokens=2000,
        n=1,
        stop=None,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        best_of=1,
    )

    corrected_text = response.choices[0].text.strip()
    return corrected_text

def main():
    st.title("Corrección de gramática y estilo con GPT-3")
    st.write("Esta aplicación utiliza GPT-3 para corregir la gramática y el estilo de un archivo .docx.")

    # Obtiene la clave de la API de OpenAI desde una variable de entorno
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        st.error("No se encontró la clave de la API de OpenAI. Asegúrate de configurar la variable de entorno OPENAI_API_KEY.")
        return

    # Carga el archivo .docx
    file = st.file_uploader("Cargar archivo .docx", type=["docx"])

    if file is not None:
        file_type = magic.from_buffer(file.read(1024), mime=True)

        if file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            doc = docx.Document(file)
            text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])

            st.write("Texto original:")
            st.code(text)

            if st.button("Corregir gramática y estilo"):
                corrected_text = grammar_style_correction(text, api_key)

                st.write("Texto corregido:")
                st.code(corrected_text)
        else:
            st.error("¡Debe cargar un archivo .docx válido!")

if __name__ == '__main__':
    main()
