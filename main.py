# main.py

# This is the entry point of the application.

import streamlit as st
from outline import generate_outline
from content import develop_content
from assem import assemble_document

def main():
    """
    Main function to run the Streamlit application.
    """
    st.title("AI-Powered Research Paper Generator")

    # Input field for the research subject.
    subject = st.text_input("Enter the research subject:")

    # Radio button for document type.
    document_type = st.radio("Select the type of research:", 
                             ('General Research', 'Literature Review', 'Experimental Research'))

    # Radio button for citation style.
    citation_style = st.radio("Select the citation style:", 
                              ('MLA', 'Chicago', 'APA'))

    # Button to start research.
    if st.button("Start Research"):
        if subject:
            # Display a progress bar.
            progress_bar = st.progress(0)

            # Generate the outline.
            st.write("Generating Outline...")
            outline = generate_outline(subject, document_type)
            progress_bar.progress(20)
            st.write("Outline Generated:")
            st.write(outline)

            # Display draft sections as they are created.
            st.write("Draft Structure Completed")

            # Provide options to edit or approve the outline.
            col1, col2 = st.columns(2)
            with col1:
                edit_outline = st.button("Edit Document")
            with col2:
                approve_outline = st.button("Approve Outline")

            if edit_outline:
                st.write("Edit the outline below:")
                # Provide a text area for editing the outline.
                edited_outline_text = st.text_area("Edit Outline:", value=str(outline), height=300)
                # Convert edited outline back to a dictionary.
                # Warning: Using eval() can be unsafe. In production, use a safer method.
                try:
                    outline = eval(edited_outline_text)
                except:
                    st.write("Error parsing the edited outline. Please ensure it is in correct dictionary format.")

            if approve_outline or edit_outline:
                st.write("Outline approved. Filling in details...")
                # Update progress bar.
                progress_bar.progress(20)

                # Develop the content for each section.
                content_dict = develop_content(outline, subject, document_type, progress_bar)

                st.write("Content Developed:")
                # Display content in a scrolling field.
                for section_title, section_content in content_dict.items():
                    st.write(f"### {section_title}")
                    st.write(section_content)

                # Assemble the document.
                if st.button("Complete Document"):
                    st.write("Assembling Document...")
                    assemble_document(content_dict, citation_style)
                    progress_bar.progress(100)
                    st.write("Document assembled. Ready for download.")

                    # Provide a download button for the generated document.
                    with open('Research_Paper.docx', 'rb') as f:
                        st.download_button('Download Document', f, file_name='Research_Paper.docx')
        else:
            st.write("Please enter a research subject to proceed.")

if __name__ == '__main__':
    main()
