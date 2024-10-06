# mini_ai_science_researcher
Streamlit app to perform research and write papers

# Mini AI Science Researcher

An AI-powered application that generates comprehensive research papers based on user-provided topics.

## Features

- **Outline Generation**: Creates a detailed outline using recursive refinement.
- **Content Generation**: Generates content for each section with iterative improvements.
- **Document Processing**: Formats the document, processes figures and tables, and manages references.
- **User Interface**: Streamlit-based UI with progress tracking and interactive elements.
- **Download Options**: Provides the final document in MS Word format for download.

## Setup Instructions

1. **Create a Conda Environment**

   ```bash
   conda create -n mini_ai_researcher python=3.9
   conda activate mini_ai_researcher

---

## Explanation of Key Components

- **Agents (`agents.py`)**: Implements the `ResearcherAgent`, `WriterAgent`, and `CriticAgent` classes. Each agent uses the Groq API to perform their tasks.

- **Recursive Functions (`utils.py`)**:
  - `generate_outline()`: Recursively generates and refines the outline.
  - `process_paragraph()`: Recursively generates and refines each paragraph.

- **Document Processing Functions (`utils.py`)**:
  - `cleanup_and_format_document()`: Applies consistent formatting and styles.
  - `format_tables()`: Formats all tables in the document.
  - `process_figures()`: Replaces figure placeholders with generated images.
  - `manage_references()`: Collects and formats references.
  - `finalize_for_ms_word()`: Ensures MS Word compatibility.
  - `assemble_final_document()`: Assembles the document in the correct order.
  - `perform_quality_check()`: Performs a quality check and returns any warnings.

- **Streamlit UI (`main.py` and `ui.py`)**:
  - Provides an interactive interface with progress tracking.
  - Allows the user to input their research topic and preferences.
  - Displays the generated outline for review before proceeding.

- **API Integration**:
  - **Groq API**: Used by agents to generate content.
  - **Napkin.ai API**: Placeholder for figure generation (needs implementation).

---

## Additional Considerations

- **Error Handling**: Basic error handling is implemented in the agents. You may want to enhance it based on actual API responses.

- **Dependencies**: Ensure all the packages are installed in your Conda environment.

- **Testing**: Since API keys and external services are involved, thorough testing is recommended.

- **Streamlit Deployment**: For deploying to the Streamlit community on GitHub, ensure your repository follows their guidelines.

---

## Next Steps

- **Implement Missing Features**: Some placeholder functions, like `generate_figure()`, need actual implementation.

- **Enhance Feedback Processing**: Improve how user feedback is incorporated into regenerating the document.

- **Add PDF Generation**: Implement functionality to download the document as a PDF.

- **Improve UI/UX**: Add more interactive elements and error messages to enhance the user experience.

- **Database Integration**: Utilize SQLite3 for data storage if needed (e.g., saving user sessions or feedback).

---

Please let me know if you need further adjustments or explanations!
