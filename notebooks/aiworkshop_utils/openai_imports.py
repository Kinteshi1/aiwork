from openai import OpenAI
from openai.types.responses import ResponseContentPartDoneEvent, ResponseTextDeltaEvent
from agents import (
    Agent,
    AsyncOpenAI,
    GuardrailFunctionOutput,
    InputGuardrail,
    InputGuardrailTripwireTriggered,
    ModelSettings,
    OpenAIChatCompletionsModel,
    Runner,
    function_tool,
    set_tracing_disabled,
    trace,
    RawResponsesStreamEvent,
    TResponseInputItem,
    ItemHelpers, 
    MessageOutputItem,
    RunContextWrapper,
    input_guardrail,
    output_guardrail
)
from aiworkshop_utils import config

openaisdk_client = OpenAI(
    base_url=config.OAPI_OPENAISDK_BASE_URL,
    api_key=config.OLLAMA_FAKE_API_KEY,  # fake key!
)

# Call LLM
def openaisdk_client_chat_completions_create(model, temp, max_tok, system_prompt, user_prompt):
    response = openaisdk_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temp,
        max_tokens=max_tok,
        stream=False,
    )
    return response.choices[0].message.content