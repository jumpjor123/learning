"""Flask web application that surfaces the B1 French learning activities."""

from __future__ import annotations

from flask import Flask, redirect, render_template, request, url_for

from . import content


app = Flask(__name__)


@app.route("/")
def home() -> str:
    return render_template("home.html")


@app.route("/vocabulaire")
def vocabulary() -> str:
    theme, entries = content.random_vocabulary_set()
    return render_template("vocabulary.html", theme=theme, entries=entries)


@app.route("/grammaire", methods=["GET", "POST"])
def grammar() -> str:
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        answer = request.form.get("answer", "")
        solution = request.form.get("solution", "")
        grammar_point = content.GrammarPoint(
            title=request.form.get("title", ""),
            explanation=request.form.get("explanation", ""),
            prompt=prompt,
            solution=solution,
        )
        return render_template(
            "grammar.html",
            grammar_point=grammar_point,
            submitted_answer=answer,
        )

    grammar_point = content.random_grammar_point()
    return render_template("grammar.html", grammar_point=grammar_point, submitted_answer=None)


@app.route("/conversation")
def conversation() -> str:
    prompt = content.random_conversation_prompt()
    return render_template("conversation.html", prompt=prompt)


@app.route("/lecture")
def reading() -> str:
    passage = content.random_reading_passage()
    return render_template("reading.html", passage=passage)


@app.route("/rafraichir")
def refresh() -> str:
    destination = request.args.get("page", "home")
    if destination not in {"home", "vocabulary", "grammar", "conversation", "reading"}:
        destination = "home"
    return redirect(url_for(destination))


if __name__ == "__main__":
    app.run(debug=True)

