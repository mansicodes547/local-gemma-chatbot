from langchain_community.llms import Ollama 
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = Ollama(model="gemma3")

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

def generate_response(prompt):
  return conversation.run(prompt)