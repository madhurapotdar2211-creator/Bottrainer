import json
import re
from src.llm_handler import get_llm_response

def predict(text):
    result = get_llm_response(text)

    try:
        data = json.loads(result)

        # Map incorrect intents to correct ones
        intent_map = {
            "order": "order_food"
        }

        if data["intent"] in intent_map:
            data["intent"] = intent_map[data["intent"]]

        return data

    except:
        return {
            "intent": "unknown",
            "confidence": 0,
            "entities": {}
        }