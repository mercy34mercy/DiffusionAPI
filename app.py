import os
import warnings
from blob import blob
import requests
from dotenv import load_dotenv
from emotion2 import emotion2
from store import gqlclient
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from flask import Flask, request



load_dotenv()
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],
    verbose=True,
)

app = Flask(__name__)


@app.route("/")
def generate():
    req = request.args
    propmt = req.get("prompt", "")
    userid = req.get("userid")

    text = propmt
    source_lang = 'JA'
    target_lang = 'EN'

    # パラメータの指定
    params = {
                'auth_key' : os.environ['APIKEY'],
                'text' : text,
                'source_lang' : source_lang, # 翻訳対象の言語
                "target_lang": target_lang  # 翻訳後の言語
            }

    # リクエストを投げる
    response = requests.post("https://api-free.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
    result = response.json()

    print(result["translations"][0]["text"])



    answers = stability_api.generate(
        prompt=result["translations"][0]["text"]
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                url = blob(artifact.binary)
                diaryid =  gqlclient(url,propmt,userid)
                emotion2(result["translations"][0]["text"],diaryid)
                # return send_file(
                #     io.BytesIO(artifact.binary),
                #     mimetype='image/png'
                # )
                return url


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
