import streamlit as st

st.set_page_config(page_title="ChatSQC", layout="wide")

def main():
    # Page title and introduction
    st.title("ChatSQC: A Template for Conversational SQC Applications")
    st.write("""
    Welcome to ChatSQC, a versatile chat application offering two distinct modes of interaction:
    
    - **ChatSQC-Basic**: A base version of the ChatSQC application, grounded in the NIST/SEMATECH Handbook of Engineering Statistics.
    - **ChatSQC-Research**: A research-grade version of the ChatSQC application, grounded in [the entire collection of CC-BY and CC-BY-NC open-access journal articles from: (a) Technometrics, (b) Quality Engineering, and (c) QREI](https://raw.githubusercontent.com/blindedResearch/chatsqc/main/open_source_refs.csv).

    Explore **each mode by selecting them from the sidebar**!
    """)

    # Any additional information or instructions
    st.markdown("## How to Use ChatSQC?")
    st.write("""
    - Use the sidebar to navigate between the Base and Research modes.
    - Pick the LLM of your choice from the dropdown menu.
    - Start asking your own questions.
    """)
    
    with st.sidebar:
        st.subheader("About ChatSQC!!")
        
        # Custom css for font size of drop down menu
        st.markdown("""
            <style>
                div[data-baseweb="select"] > div {
                    font-size: 0.85em;
                }
            </style>
        """, unsafe_allow_html=True)
        
        
        st.markdown("""
            - **Created by:**
                + :link: [JQT Author 1](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=ujqt20#Anonymisation)  
                + :link: [JQT Author 2](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=ujqt20#Anonymisation) 
                + :link: [JQT Author 3](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=ujqt20#Anonymisation)  
                + :link: [JQT Author 4](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=ujqt20#Anonymisation) 
                + :link: [JQT Author 5](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=ujqt20#Anonymisation) 
                + :link: [JQT Author 6](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=ujqt20#Anonymisation) 
        """)
        st.write("")

        st.markdown("""
            - **Version:** 1.3.0 (Feb 03, 2024)
        """)

       

# Ensure this script runs only in standalone mode (not necessary for Streamlit pages, but good practice)
if __name__ == "__main__":
    main()
