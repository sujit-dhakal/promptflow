
from promptflow import tool
from difflib import SequenceMatcher

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
def is_similar_text(text1: str,text2:str,threshold=0.5) -> str:
    return SequenceMatcher(None,text1,text2).ratio() > threshold

@tool
def my_python_tool(articles: list) -> list:
    processed_texts = []

    for article in articles:
        is_duplicate = False
        for processed in processed_texts:
            if is_similar_text(article['headings'], processed['headings']) or is_similar_text(article['body'], processed['body']):
                processed['sources'].append(article['source'])
                is_duplicate = True
                break

        if is_duplicate:
            continue

        processed_texts.append({
            'headings': article['headings'],
            'body': article['body'],
            'sources': [article['source']]
        })
    return processed_texts
