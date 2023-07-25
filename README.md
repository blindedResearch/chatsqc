# ChatSQC: Grounding LLM Answers to Statistical Quality Control Literature

## Hosted ChatSQC

Our ChatSQC chatbot is hosted at <>. Practitioners and researchers can use ChatSQC to explain foundational industrial statistics and quality concepts based on the public-domain book of [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/index.htm). Currently, we do not require users to provide their own API keys and there is no cost acurred by the users for using ChatSQC. Please see [our video]() for an overview of the app's features and how it can be used.

---

 ## Introduction

 This is the official implementation of [AI and the Future of Work in Statistical Quality Control: Insights from a First Attempt to Augmenting ChatGPT with an SQC Knowledge Base (ChatSQC)](), where we attempt to address the imprecise answers obtained from generally trained large language models (LLMs) when explaining industrial statistics and quality control concepts. Our work attempts to address this issue and reduce hallucinations by grounding the answers to vetted and high-qaulity statistical quality control (SQC) reference materials. As opposed to traditional LLMs such as ChatGPT (GPT 4.0 with no plugins), our ChatSQC bot provides the following advantages:  
   -  **grounded in SQC literature:** Our chatbot will only present answers based on concepts explained in the vetted, highly referenced public-domain book [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/index.htm). The grounding of LLMs with reference material reduces hallucinations and improves domain-based response quality.  
   - **increased likelihood for ''I do not know'' answers:** The grounding also prevents the LLM from generating answers which are not in the reference materials, which allowed us to program the chatbot to state: 'As a SQC chatbot grounded only in NIST/SEMATCH's Engineering Staistics Handbook, I do not know the answer to this question as it is not in my referenced/grounding material. I am sorry for not being able to help.'   
   - **highlighting of relevant text chunks:** Our chatbot utilizes the 5 most relevant text chunks to generate its response. In our graphical user interface, we present the two most relevant chunks (for brevity's sake since our text chunks are 1,000 characters) along with their L2 distance to the prompt. This allows users to understand how the generated response was created, providing insights into the response quality and accuracy.   

Researchers can implement and host their own versions of ChatSQC by setting up a virtual environment with python=3.9.17 and the package versions presented in the [requirements.txt]() file. This allows SQC researchers to have a testbed/playground to examine the impact of the different LLMs, their parameters and prompting strategies on response quality. 


---

## ChatSQC's Design

Let us include our methods figure here and provide a short description of how the chatbot is design. 


---

# Local Installation and Running of the App

If you would like to run the chabot on your local Python environment, please follow these steps:

**Instructions for First-Time Usage:**  

1. Clone the repository to your local machine.

2. Download/Install Anaconda (if needed) and Create a standalone virtual environment (note Python users can also `venv` to create their virtual environment; we do not assume Python expertise so our instructions are somewhat detailed):   
    - Download, install and open Anaconda  
    - Create virtual environment by running this at the command line (opened from Anaconda): `conda create -n chatspc python=3.9`. It will ask you to click, `y`, please do type: `y` and click `Enter`.  
    - `conda activate chatspc`  
    - Use the command window to cd (change drive) to the location of your `requirements.txt` file  
    - Run the command `pip install -r requirements.txt` to install the required dependencies (libraries with specific versions)  
 
3. Obtain an [API key from OpenAI](https://platform.openai.com/account/api-keys) and add it to a file titled `.env`, which must be placed in the project directory.  

4. Run the following commands in Anaconda's cmd in this order:
    - `python preprocess.py`, which will create the vector store containing the relationship between different text vectors  
    - `run streamlit chatsqc.py` which will run the app


**Instructions for Running the App Everytime:**

1. Open Anaconda the virtual environment from anaconda by clicking on the dropdown menu with default value of base and you will find `chatspc` below it.  
2. Install (if needed) and launch the `command window` (CMD) after you clicked on `chatspc`.  
    - Alternatively, you can type: `conda activate chatspc` in the CMD from your base environment.  

3. Make sure that your terminal points out to the directory where you have our python files.   

4. Run the app using: `streamlit run chatsqc.py`



---

## Roadmap

Our current version of the app uses `gpt-3.5-turbo-16k` as the LLM and [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/index.htm). In future versions, we plan on using [`Llama 2 70B`](https://ai.meta.com/llama/) since it is open-sourced and can be locally installed (i.e., there will be no API costs for the embeddings and chat APIs). Furthermore, we are currently attempting to get copyright clearance to use the seminal [Introduction to Statistical Quality Control](https://www.wiley.com/en-us/Introduction+to+Statistical+Quality+Control%2C+8th+Edition-p-9781119399308) in our grounding material since it provides more in-depth knowledge of more advanced SQC concepts (e.g., the fast initial response of the EWMA and CUSUM charts).


---

## Credits

Our ChatSQC's design was inspired and utilized many features of @alejandro-ao's [Ask Multiple PDFs](https://github.com/alejandro-ao/ask-multiple-pdfs) app for online grounding of ChatGPT using multiple PDFs. Due to the large size of our referenced materials, we have modified the app to:  
  - Preprocess the reference materials offline.  
  - Preprocess HTML files instead of PDF files.  
  - Use the recommended `RecursiveCharacterTextSplitter()` instead of the `CharacterTextSplitter()` based on the [LangChain documentation](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/recursive_text_splitter) of the `CharacterTextSplitter()`.  

Furthermore, interfacing with LLM and Embedding APIs was simplified by the [LangChain](https://api.python.langchain.com/en/latest/api_reference.html) python library. Similarly, the use of the [streamlit](https://docs.streamlit.io/library/api-reference) python library has streamlined the development of our GUI. We have also capitalized on [Chris Klose's suggestions](https://discuss.streamlit.io/t/st-footer/6447/8) to change the streamlit footer default.   


---

## Contributing to ChatSQC

We warmly welcome contributions from our vibrant community and are glad that you are interested in enhancing the ChatSQC app. Your ideas, suggestions, and improvements can help make this application even more user-friendly and efficient. If you have any suggestions or find a bug, please don't hesitate to submit an issue through GitHub's issue tracker. It's a great way to discuss new ideas or get help with problems. Please be as descriptive as possible when submitting an issue to help us understand your concern or proposal better.

If you'd like to contribute code, please fork the repository and create a pull request when you're ready. A pull request (PR) is a way to suggest changes to the project. We use the PR mechanism for both bug fixes and new features. Please include a detailed explanation of your changes, and be sure to reference any issues that will be resolved by your PR. When you make a PR, it will be reviewed by our team. If it meets the guidelines and aligns with our roadmap, we will merge your code into the main branch. Please make sure your code is clean, well commented, and follows our coding standards.

We greatly appreciate all of our contributors. Each contribution helps us to create a better app for everyone, so thank you for taking the time and making the effort to improve ChatSQC! Happy contributing!

---

## Citing our work

If you make use of our work, please cite our paper:

