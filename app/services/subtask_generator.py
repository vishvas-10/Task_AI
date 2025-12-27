import json
from typing import List, Dict, Any
from app.services.llm_client import get_llm_client


SYSTEM_PROMPT = """
You break a complex task into exactly 5 subtasks.
Rules:
1. Output exactly 5 subtasks.
2. Each subtask must be short and actionable.
3. Use ONLY: high, medium, low for importance, urgency .
4. Only return the response in valid json.
5.If the input task is too short, vague, or non-actionable (e.g., greetings such as “hi”, “hello”, single words, or meaningless text), do not generate subtasks and set "result": "fail". But try to do it most of the times if the input is not completely vague.
6.If exactly 5 valid subtasks are successfully generated, set "result": "successful".
7.Always include the "result" key in the output, regardless of success or failure.
8.Output must aways look like this {"result": "success",'priority':'high','subtasks': [{'task': 'Finalize wedding date and time', 'priority': 'high', 'importance': 'high'}, {'task': 'Set guest list and create invitations', 'urgency': 'high', 'importance': 'high'}, {'task': 'Plan and book wedding venue', 'urgency': 'medium', 'importance': 'high'}, {'task': 'Research and book vendors (photographer, florist, etc.)', 'urgency': 'medium', 'importance': 'high'}, {'task': 'Create and send out wedding registry', 'urgency': 'low', 'importance': 'medium'}]} } Make sure to always adhere to this if any part is missing or not completed return result as fail"""

def generate_subtasks(task: str) -> List[Dict[str, Any]]:
    client = get_llm_client()

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": task}
        ],
        response_format={"type": "json_object"}
    )

    raw = response.choices[0].message.content
    if raw:
        return json.loads(raw)
    return []