import ast
import traceback

class LLMAgent:
  """
  A class representing an LLM agent for code improvement.
  """

  def __init__(self, name, llm_function):
    """
    Initializes an LLMAgent.

    Args:
      name: The name of the agent.
      llm_function: A function that takes a string as input (the prompt) and returns a string (the LLM's response).
    """
    self.name = name
    self.llm_function = llm_function

  def improve_code(self, code, feedback=""):
    """
    Generates code improvement suggestions.

    Args:
      code: The code to improve.
      feedback: Optional feedback from another agent.

    Returns:
      A tuple containing the improved code and any feedback.
    """
    prompt = f"""You are an expert code reviewer named {self.name}. Please review the following Python code and suggest improvements:\n\n{code}\n\n{feedback}"""
    response = self.llm_function(prompt)
    try:
      # Try to extract code from the response
      improved_code = extract_code(response) #a
    except Exception as e:
      improved_code = code  # Revert to original code if extraction fails
      print(f"Error extracting code from {self.name}'s response: {e}")
      print(f"Traceback: {traceback.format_exc()}")
      return improved_code, f"I couldn't understand your suggestion. Can you rephrase?"

    feedback = response.split("```")[0].strip()  # Extract feedback from the response

    return improved_code, feedback

def conversation_loop(agent1, agent2, initial_code, rounds=10):
    """
    Runs a conversation loop where two agents iteratively improve code.

    Args:
        agent1: The first LLMAgent.
        agent2: The second LLMAgent.
        initial_code: The initial code to improve.
        rounds: The number of improvement rounds.

    Returns:
        The final improved code after the conversation.
    """
    current_code = initial_code
    for round in range(rounds):
        print(f"\nRound {round + 1}:\n")
        print(f"Current code:\n{current_code}\n")

        # Agent 1 improves the code
        improved_code, feedback_to_agent2 = agent1.improve_code(current_code)
        print(f"{agent1.name}'s suggestions:\n{improved_code}\n")
        print(f"{agent1.name}'s feedback to {agent2.name}:\n{feedback_to_agent2}\n")

        # Agent 2 further improves the code based on agent 1's feedback
        current_code, feedback_to_agent1 = agent2.improve_code(improved_code, feedback=feedback_to_agent2)
        print(f"{agent2.name}'s suggestions:\n{current_code}\n")
        print(f"{agent2.name}'s feedback to {agent1.name}:\n{feedback_to_agent1}\n")

    print(f"\nFinal code:\n{current_code}")
    return current_code

# Example usage:
# Replace 'your_llm_function' with your actual LLM function
from google.cloud import aiplatform

def your_llm_function(prompt):
    """
    Your LLM function that takes a prompt and returns a response using Gemini.
    """
    # Replace with your actual project ID and model name
    import vertexai
    from vertexai.generative_models import GenerativeModel

    # TODO(developer): Update and un-comment below line
    # project_id = "PROJECT_ID"

    vertexai.init(project="test", location="us-central1")

    model = GenerativeModel("gemini-1.5-pro-001")

    response = model.generate_content(
        prompt
    )

    return response.text

agent1 = LLMAgent("Agent 1", your_llm_function)
agent2 = LLMAgent("Agent 2", your_llm_function)
initial_code = """
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline(steps=[('preprocessor', SimpleImputer()),
                              ('model', RandomForestRegressor(n_estimators=50,
                                                              random_state=0))
                             ])

from sklearn.model_selection import cross_val_score

# Multiply by -1 since sklearn calculates *negative* MAE
scores = -1 * cross_val_score(my_pipeline, X, y,
                              cv=5,
                              scoring='neg_mean_absolute_error')

print("MAE scores:\n", scores)
"""
final_code = conversation_loop(agent1, agent2, initial_code)