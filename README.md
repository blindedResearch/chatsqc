# ChatSQC: Grounding LLM Answers to Statistical Quality Control Literature

## Hosted ChatSQC

Our ChatSQC chatbot is hosted at <>. Practitioners and researchers can use ChatSQC to explain foundational industrial statistics and quality concepts based on the public-domain book of [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/index.htm). Currently, we do not require users to provide their own API keys, and users incur no cost for using ChatSQC. Please see [our video]() for an overview of the app's features and how it can be used.

---

 ## Introduction

 This is the official implementation of [AI and the Future of Work in Statistical Quality Control: Insights from a First Attempt to Augmenting ChatGPT with an SQC Knowledge Base (ChatSQC)](), where we attempt to address the imprecise answers obtained from generally trained large language models (LLMs) when explaining industrial statistics and quality control concepts, see [Megahed et al. 2024](https://www.tandfonline.com/doi/full/10.1080/08982112.2023.2206479) for a detailed discussion. Our work attempts to address this issue and reduce hallucinations by grounding the answers in vetted and high-quality statistical quality control (SQC) reference materials. As opposed to traditional LLMs such as ChatGPT (GPT 4.0 with no plugins), our ChatSQC bot provides the following advantages:  
   -  **grounded in SQC literature:** Our chatbot will only present answers based on concepts explained in the vetted, highly referenced public-domain book [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/index.htm). The grounding of LLMs with reference material reduces hallucinations and improves domain-based response quality.  
   - **increased likelihood for ''I do not know'' answers:** The grounding also prevents the LLM from generating answers which are not in the reference materials, which allowed us to program the chatbot to state: 'As an SQC chatbot grounded only in NIST/SEMATECH's Engineering Statistics Handbook, I do not know the answer to this question as it is not in my referenced/grounding material. I am sorry for not being able to help.'   
   - **highlighting of relevant text chunks:** Our chatbot utilizes up to 5 most relevant text chunks to generate its response. In our app, we present these most relevant chunks in HTML disclosure widgets along with their L2 distance to the prompt; in the widget's summary view, we provide: (a) a statement saying "Click for relevant text chunk" to indicate to the user that the text chunk can be viewed in detail by clicking on the text, and (b) we provide the L2-dist to the prompt in the summary view in parantheses after our "click here" statement. This allows users to understand how the generated response was created, providing insights into the response quality and accuracy.  
   - **web links of relevant sources:** for each text chunk, we provide the title of the webpage (containing the subsection number and title) along with a hyperlink to its URL to allow the reader to read the full context in which our relevant text chunks were presented in the ehandbook. If more than one text chunk belongs to a given webpage, we nest them together. 

Researchers can implement and host their own versions of ChatSQC by setting up a virtual environment with python=3.10 and the package versions presented in the [requirements.txt](https://github.com/fmegahed/chatsqc/blob/main/requirements.txt) file. This allows SQC researchers to have a testbed/playground to examine the impact of the different LLMs, their parameters, and prompting strategies on response quality. 


---

## ChatSQC's Design

<img width="960" height="528" alt="ChatSQC_flowchart_new" src="https://github.com/user-attachments/assets/7f1937d7-52c0-412a-8968-fcbbcae6067b" />


---

# Local Installation and Running of the App

If you would like to run the chatbot on your local Python environment, please follow these steps:

**Instructions for First-Time Usage:**  

1. Clone the repository to your local machine.

2. Download/Install Anaconda (if needed) and create a standalone virtual environment (note Python users can also use `venv` to create their virtual environment; we do not assume Python expertise, so our instructions are somewhat detailed):   
    - Download, install, and open Anaconda  
    - Create a virtual environment by running this at the command line (opened from Anaconda): `conda create -n chatsqc python=3.10`. It will ask you to click, `y`; please type: `y` and click `Enter`.  
    - `conda activate chatsqc`  
    - Use the command window to cd (change drive) to the location of your `requirements.txt` file  
    - Run the command `pip install -r requirements.txt` to install the required dependencies (libraries with specific versions)  
 
3. Apply for an [OpenAI account](https://openai.com/pricing). Obtain an [API key from OpenAI](https://platform.openai.com/account/api-keys) and add it to a file titled `.env`, which must be placed in the project directory. The `.env` file must contain a variable called `OPENAI_API_KEY`, where you can assign your actual API Key as: `OPENAI_API_KEY=sk-mo9KXYZfk7pvRnIcdZzPFU8WlzuJB1EFLmihGYop4YZnTjk`. Note that:    
    - This is a dummy API key, where we have maintained the format of the real key, but it should not have any real functionality or access permissions.  
    - For exploring and testing the API, all new OpenAI users get $5 in free tokens. These tokens expire after 3 months. Once you exceed your quota, you can subscribe to one of their paid plans and continue using the API. 

4. Run the following commands in Anaconda's cmd in this order:
    - `streamlit run ChatSQC.py`, which will run the app


**Instructions for Running the App every time:**

1. Open the Anaconda virtual environment from Anaconda by clicking on the dropdown menu with the default value of *base (root)*, and you will find `chatsqc` below it.  
2. Install (if needed) and launch the `command window` (CMD) after you click on `chatsqc`.  
    - Alternatively, you can type: `conda activate chatsqc` in the CMD from your base environment.  

3. Make sure that your terminal points to the directory where you have our Python files.   

4. Run the app using: `streamlit run ChatSQC.py`

---

## Roadmap

Our current version of the app uses `gpt-4.1` as the LLM and [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/index.htm). 

---

## Credits

Our ChatSQC's design was inspired by and utilized many features of @alejandro-ao's [Ask Multiple PDFs](https://github.com/alejandro-ao/ask-multiple-pdfs) app for online grounding of ChatGPT using multiple PDFs. Due to the large size of our referenced materials, we have modified the app to:  
  - Preprocess the reference materials offline.  
  - Preprocess HTML files instead of PDF files.  
  - Use the recommended `RecursiveCharacterTextSplitter()` instead of the `CharacterTextSplitter()` based on the [LangChain documentation](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/recursive_text_splitter) of the `CharacterTextSplitter()`.  
  - Provide links/titles for the verified sources, relevant text chunks, and the L2 distance of these chunks to the users' prompts.

Furthermore, interfacing with LLM and Embedding APIs was simplified by the [LangChain](https://api.python.langchain.com/en/latest/api_reference.html) Python library. Similarly, the use of the [streamlit](https://docs.streamlit.io/library/api-reference) Python library has streamlined the development of our GUI. We have also capitalized on [Chris Klose's suggestions](https://discuss.streamlit.io/t/st-footer/6447/8) to change the streamlit footer default.   


---

## Contributing to ChatSQC

We warmly welcome contributions from our vibrant community and are glad that you are interested in enhancing the ChatSQC app. Your ideas, suggestions, and improvements can help make this application even more user-friendly and efficient. If you have any suggestions or find a bug, please don't hesitate to submit an issue through GitHub's issue tracker. It's a great way to discuss new ideas or get help with problems. Please provide as much detail as possible when submitting an issue to help us better understand your concern or proposal.

If you'd like to contribute code, please fork the repository and create a pull request when you're ready. A pull request (PR) is a way to suggest changes to the project. We use the PR mechanism for both bug fixes and new features. Please include a detailed explanation of your changes, and be sure to reference any issues that will be resolved by your PR. When you make a PR, it will be reviewed by our team. If it meets the guidelines and aligns with our roadmap, we will merge your code into the main branch. Please make sure your code is clean, well-commented, and follows our coding standards.

We greatly appreciate all of our contributors. Each contribution helps us to create a better app for everyone, so thank you for taking the time and making the effort to improve ChatSQC! Happy contributing!

---

## Citing our work

If you make use of our work, please cite our paper:

```
@article{megahed2024introducing,
  title={Introducing ChatSQC: Enhancing statistical quality control with augmented AI},
  author={Megahed, Fadel M and Chen, Ying-Ju and Zwetsloot, Inez M and Knoth, Sven and Montgomery, Douglas C and Jones-Farmer, L Allison},
  journal={Journal of Quality Technology},
  volume={56},
  number={5},
  pages={474--497},
  year={2024},
  publisher={Taylor \& Francis},
  doi = {10.1080/00224065.2024.2372328},
  url = {https://www.tandfonline.com/doi/full/10.1080/00224065.2024.2372328}
}
```


