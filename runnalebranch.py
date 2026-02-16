from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parser import StrOutputParser
from dotenv import Load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel
Load_dotenv()
prompt1= PromptTemplate(
    template='write a detailed  {topic}',
    input_variable=['topic']

)
prompt2= PromptTemplate(
    template ={'sumarrize the followeing {text} '},
    input_variable =['text']



)
model = ChatOpenAI()
parser = StrOutputParser()
report_gen_chain= RunnableSequence(prompt1,model,parser)
branch_chain =RunnableBranch(
    (lambda x :len(x.split())>500,RunnableBranch(prompt2,model,parser)),
     RunnablePassthrough()

)
final_chain=RunnableSequence(report_gen_chain,branch_chain)