from langchain.prompts import PromptTemplate

perceive_agent_instruction = """
You act as an information gatherer to compile an outline detailing a movie. You will be given the film's title, year of release and genres. In a few sentences, describe the main plot using complete sentences.
Here are some examples:
{examples}

Movie information:
File title:{title}
Year of release:{year}
Genres:{genres}
Main plot:
"""

perceive_agent_prompt = PromptTemplate(
                            input_variables=['examples', 'title', 'year', 'genres'],
                            template = perceive_agent_instruction,
                            )