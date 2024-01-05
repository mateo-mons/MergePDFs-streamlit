# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import PyPDF2 # Importa la biblioteca para trabajar con archivos pdf
import streamlit as st
from streamlit.logger import get_logger


LOGGER = get_logger(__name__)

# -- VARIABLES -- #

output_pdf = "documents/final-pdf.pdf" # Define el nombre del archivo de salida que se guardará en pdf final

# -- FUNCTIONS -- #

def merge_pdfs(output_path, documents):
    # Crea un objeto PdfMerger de PYPDF2 para combinar archivos
    final_pdf = PyPDF2.PdfMerger()

    for document in documents:
        final_pdf.append(document) # Agrega cada documento PDF a la fusion

    final_pdf.write(output_path) # Guarda el PDF combinado en la ruta de salida


def run():
    st.set_page_config(
        page_title="Merge PDFs!!!",
        page_icon="🧲",
    )

    # -- FRONT -- #
    st.header('Merge PDFs!')
    st.image('assets/pdf_merge.jpeg')
    st.subheader('Attach PDFs')
    attached_pdfs = st.file_uploader(label="", accept_multiple_files=True)

    merge = st.button(label="Merge 🕸") # Crea un boton para unir los pdfs #


    # -- BACK -- #

    if merge:
        if len(attached_pdfs) == 0:
            st.warning('Attach PDFs!')
        elif len(attached_pdfs) <= 1:
            st.warning('Attach more than one PDF!... plis')
        else:
            merge_pdfs(output_pdf, attached_pdfs)
            st.success('Here you can download the final pdf')
            with open(output_pdf, 'rb') as file:
                pdf_data = file.read()
            st.download_button(label='Download final pdf', data=pdf_data, file_name='final_pdf.pdf')


if __name__ == "__main__":
    run()
