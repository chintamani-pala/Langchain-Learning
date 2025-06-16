# type: ignore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

model2 = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=["text"],
    validate_template=True,
)

prompt2 = PromptTemplate(
    template="Generate 5 short question and answers from the following text \n {text}",
    input_variables=["text"],
    validate_template=True,
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n {notes} and {quiz}",
    input_variables=["notes", "quiz"],
    validate_template=True,
)


parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {"notes": prompt1 | model1 | parser, "quiz": prompt2 | model2 | parser}
)

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain
text = """
In JavaScript, a closure is a function that retains access to its lexical scope, even after the outer function has executed. This means that inner functions can still access variables and parameters defined in their outer function, even if the outer function has finished running. Closures are created every time a function is defined, at function creation time.

Closures exist because of JavaScript’s lexical scoping—a scope determined by the structure of the code as it is written, not by how functions are called. This concept enables data encapsulation, where variables inside a function can be "protected" from the global scope while still being accessible by functions defined within that same scope.

Closures are often used to:

Maintain state between function calls (e.g., counters).

Create private variables in JavaScript, which doesn't support access modifiers like private/protected.

Build function factories, where functions return other customized functions.

Since the inner function "closes over" the variables in the outer function, it can continue to access them. However, this can also lead to memory issues if closures are not handled properly, because they prevent garbage collection of the outer function's variables.

Understanding closures is crucial for mastering JavaScript, especially in the context of callbacks, event handlers, setTimeout, and frameworks like React, where closures are frequently used under the hood.
"""
result = chain.invoke({"text": text})

print(result)


chain.get_graph().print_ascii()
