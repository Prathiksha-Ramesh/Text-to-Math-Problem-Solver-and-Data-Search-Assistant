import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool,initialize_agent
from dotenv import load_dotenv
from langchain.callbacks import StreamlitCallbackHandler

#set up the streamlit app

st.set_page_config(page_title='Text to Math Problem solver and data search assistant')
st.title('Text to math problem solver using google gemma 2')


groq_api_key=st.sidebar.text_input(label='GROQ  API KEY',type='password')

if not groq_api_key:
    st.info('Please add your Groq API key to continue')
    st.stop()

llm=ChatGroq(model='Gemma2-9b-It',groq_api_key=groq_api_key)

#initializing the tools:
wikipedia_wrapper=WikipediaAPIWrapper()
wikipedia_wrapper=Tool(
    name='Wikipedia',
    func=wikipedia_wrapper.run,
    description='A tool for searching the internet to find the various info on the topics mentioned'


)

#initalize the math tool:

math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name='Calculator',
    func=math_chain.run,
    description='A tool for answering the math related questions.Only input mathematical expression need to be provided'

)

prompt="""
you are agent tasked for solving user's mathematical questions .logically arrive at the solutions and 
provide detalied explanation and display it point wise for the question below

Question:{question}
Answer:
"""

prompt_template=PromptTemplate(
    input_variable=['question'],
    template=prompt
)

#combine all the tools to chain:

chain=LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool=Tool(
    name='Reasoning',
    func=chain.run,
    description='A tool for answering logic-based and reasoning questions'

)


#initialize the agents:

assistant_agents=initialize_agent(
    tools=[wikipedia_wrapper,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_erros=True
)

if 'messages' not in st.session_state:
    st.session_state['messages']=[
        {'role':'assistant','content':'Hi,I am a math chat bot who can answer all you math question'}

    ]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

#function to generate the response:

def generate_response(user_question):
    response=assistant_agents.invoke({'input':question})
    return response

#starting the interaction:
question=st.text_area('Enter your question')
if st.button('find my answer'):
    if question:
        with st.spinner('Generate response..'):
            st.session_state.messages.append({'role':'user','content':question})
            st.chat_message('user').write(question)
            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assistant_agents.run(st.session_state.messages,callbacks=[st_cb])
            st.session_state.messages.append({'role':'assistant','content':response})
            st.write('Response:')
            st.success(response)

    else:
        st.warning('Please enter the question')
