import streamlit as st

st.set_page_config(page_title="ChatSQC", layout="wide")

def main():
    # Page title and introduction
    st.title("ChatSQC: A Template for Conversational SQC Applications")
    st.write("""
    Welcome to ChatSQC, a versatile chat application offering two distinct modes of interaction:
    
    - **ChatSQCB**: A base version of the ChatSQC application, grounded in the NIST/SEMATECH Handbook of Engineering Statistics.
    - **ChatSQCR**: A research-grade version of the ChatSQC application, grounded in the entire collection (as made available online by Taylor & Francis) of open-access journal articles from: (a) the Journal of Quality Technology, (b) Technometrics, and (c) Quality Engineering.

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
            - **Version:** 1.2.0 (Jan 22, 2024)
        """)

       

# Ensure this script runs only in standalone mode (not necessary for Streamlit pages, but good practice)
if __name__ == "__main__":
    main()
