from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parser import StrOutputParser
from dotenv import Load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel
Load_dotenv()

prompt1= PromptTemplate(
    template ='tell a joke about {topic',
    input_variable =['topic']

)
model =ChatOpenAI()
parser = StrOutputParser()

chain =ParallelRunnable({
    "tweet":RunnableSequence(prompt,model ,parser),
    'linkedin':RunnableSequnece(prompt1.model,parser)
}
)
reult=chain.invoke({'topic':'ai'})
chain['tweet']
