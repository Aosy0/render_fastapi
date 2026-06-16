from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_json = [
        {"luck": "大吉", "description": "大吉！素晴らしい幸運が舞い込むでしょう。"},
        {"luck": "中吉", "description": "中吉！努力が実を結び、良い結果が待っています。"},
        {"luck": "小吉", "description": "小吉！ちょっとした幸運があなたの元にやってきます。"},
        {"luck": "吉", "description": "吉！安定した幸せな日々が続くでしょう。"},
        {"luck": "半吉", "description": "なんだこれ"},
        {"luck": "末吉", "description": "末吉！努力が実り始め、良い方向に進む時期です。"},
        {"luck": "末小吉", "description": "良くはない"},
        {"luck": "凶", "description": "凶。悪いことが起こるかもしれませんが、気を引き締めてください。"},
        {"luck": "小凶", "description": "小凶。注意が必要な日です。慎重に行動しましょう。"},
        {"luck": "大凶", "description": "大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。"}
    ]
    
    return {"result" : random.choice(omikuji_json)}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
            <style type="text/css">
                p {
                    color: red;
                    text-align:center;
                }
             </style>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <script type="text/javascript">
                alert("このページはとても安全です！");
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
