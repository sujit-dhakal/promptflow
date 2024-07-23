

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
from promptflow.core import tool
import json
import re

@tool
def my_python_tool(input1:str)->str:
    input1 = re.sub(r'[$\\!]','',input1)
    try:
        json_answer=json.loads(input1)
        heading = json_answer['heading']
    except:
        heading = input1

    return heading
