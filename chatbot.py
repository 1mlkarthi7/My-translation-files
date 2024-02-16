from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import os
os.environ["OPENAI_API_KEY"] = "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"
raw_text =  'Karuna  Vallabhapurapu  \nHyderabad,  Telangana  \n vallabhapurapukaruna@gmail.com   \n +91-9110771246\n    \nhttps://www.linkedin.com/in/karuna -vallabhapurapu -873401229/  \n \n \nPROFESSIONAL  SUMMARY  \nData scientist  with 2 years  plus of experience  in data analytics.  Strong  understanding  of data modeling,  statistical  methods,  \nand predictive  analytics  using  machine  learning  algorithms.  Experience  in business  intelligence  and data analysis  for sectors, \nincluding retail and technology.  \nDATA  SCIENCE  EXPERIENCE  \nData  Scientist  | ZABDA  Technologies  Pvt Ltd | HYDERABAD,  TS | December  2021  - Present.  \n• Applied  clustering  analysis  to unstructured  data (extraction,  transportation,  integration)  by writing  a machine  \nlearning algorithm that enhanced resource allocation for sales teams by reducing bias and using more correct data, \nincreasing sales by 20%.'
text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 700,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)
len(texts)
# Download embeddings from OpenAI
embeddings = OpenAIEmbeddings()
document_search = FAISS.from_texts(texts, embeddings)


