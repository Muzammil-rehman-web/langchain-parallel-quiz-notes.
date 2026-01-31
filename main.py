import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

# Load API key from environment
if "GROQ_API_KEY" not in os.environ:
    raise EnvironmentError("GROQ_API_KEY not set")

# Initialize model
model = ChatGroq(model="llama-3.3-70b-versatile")

# Prompts
prompt_notes = PromptTemplate(
    template="Generate short and simple notes from the following text:\n{text}",
    input_variables=["text"],
)

prompt_quiz = PromptTemplate(
    template="Generate five quiz questions from the following text:\n{text}",
    input_variables=["text"],
)

prompt_merge = PromptTemplate(
    template="Merge the provided notes and quiz into a single output:\n\nNotes:\n{notes}\n\nQuiz:\n{quiz}",
    input_variables=["notes", "quiz"],
)

# Output parser
parser = StrOutputParser()

# Parallel chain
parallel_chain = RunnableParallel(
    notes=prompt_notes | model | parser,
    quiz=prompt_quiz | model | parser,
)

# Merge chain
chain = parallel_chain | (prompt_merge | model | parser)

# Example input
text = """A black hole is an astronomical body so compact that its gravity prevents anything, including light, from escaping..."""

# Run
result = chain.invoke({"text": text})
print(result)
