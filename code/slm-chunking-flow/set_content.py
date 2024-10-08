import json
from promptflow.core import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def set_content(content: str,table:list):
    result = []

    json_content = json.loads(content)

    for item in json_content:
        result.append(item)

    for item in table:
        result.append(item)

    return json.dumps(result)
