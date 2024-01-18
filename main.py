import streamlit as st 
import PyPDF2 # Importa la biblioteca para trabajar con archivos pdf


st.set_page_config(
    page_title="Merge PDFs!!!",
    page_icon="🧲",
)


# -- VARIABLES -- #

output_pdf = "documents/final_pdf.pdf" # Define  la ruta y el nombre del archivo de salida que se guardará en pdf final

# -- FUNCTIONS -- #

def merge_pdfs(output_path, documents):
    # Crea un objeto PdfMerger de PYPDF2 para combinar archivos
    final_pdf = PyPDF2.PdfMerger()

    for document in documents:
        final_pdf.append(document) # Agrega cada documento PDF a la fusion

        final_pdf.write(output_path) # Guarda el PDF combinado en la ruta de salida



# -- FRONT -- #
st.header('Merge PDFs!')
st.image('assets/pdf_merge.jpeg')
st.subheader('Attach PDFs')
attached_pdfs = st.file_uploader(label="🕸", accept_multiple_files=True)

merge = st.button(label="Merge 🕸") # Crea un boton para unir los pdfs #


# -- BACK -- #
if merge:
    if len(attached_pdfs) == 0:
        st.warning('Attach PDFs!')
    elif len(attached_pdfs) <= 1:
        st.warning('Attach more than one PDF!')
    else:
        merge_pdfs(output_pdf, attached_pdfs)
        st.success('Now you can download your PDF!')
        with open(output_pdf, 'rb') as file:
            pdf_data = file.read()
        st.download_button(label='Download final PDF🔭', data=pdf_data, file_name='final_pdf.pdf')
