---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-8
completeness: full
---

# 8: Implementation Patterns

## Scenario

A GenAI developer is building a virtual assistant application by using an Anthropic Claude model on Amazon Bedrock. The application sends user queries and expects conversational responses. The GenAI developer wants to configure the application to stop generating output after a specific phrase is generated in the response. Which solution will meet these requirements?

## Common implementation patterns

- Use the stop sequences parameter in the inference call to specify a trigger phrase.

## Common anti-patterns

- Avoid add the trigger phrase "stop at this phrase" in the user prompt. because amazon Bedrock processes prompts and generates completions based on the input and the model parameters. Adding a “stop at this phrase” instruction in the prompt relies on the model following instructions. However, the...
- Avoid use the top-k parameter to control the diversity of tokens in the model's output. because the top-k parameter controls token sampling diversity during generation. This parameter could affect the likelihood of certain tokens being selected. However, this parameter cannot stop generation at...
- Avoid use the temperature parameter in the inference call to control the likelihood of the phrase appearing. because this parameter value controls the randomness of the model’s output. Adjusting temperature influences creativity and variation. Temperature does not influence the stopping point of...

## Architecture guidance

- You can use the stop sequences parameter to stop the model from generating a response.
- You can use the stop sequences parameter to stop the model after generating certain key phrases.
- This solution provides a built-in mechanism in the model's API to directly control output generation.
