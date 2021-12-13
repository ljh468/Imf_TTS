# -*- coding: utf-8 -*-
import io
from TTS.utils import synthesizer
from flask import Flask, render_template, request, send_file
from g2pK.g2pk import g2pk
import normalize
g2p = g2pk.G2p()
app = Flask(__name__)


@app.route("/")
def demo():
    return render_template("DemoPage.html")


@app.route("/api/tts", methods=["GET"])
def TTS():
    text = request.args.get("text")
    text = normalize.normalize_text(text)
    wav = normalize.synthesizer.tts(text, None, None)
    out = io.BytesIO()
    normalize.synthesizer.save_wav(wav, out)
    return send_file(out, mimetype="audio/wav")


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port=8000, debug=True)