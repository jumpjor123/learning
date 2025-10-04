"""Interactive CLI app for B1 French learners."""

from __future__ import annotations

from typing import Sequence

from . import content


def choose_from_menu(options: Sequence[str], prompt: str) -> int:
    while True:
        print(prompt)
        for idx, option in enumerate(options, start=1):
            print(f"  {idx}. {option}")
        choice = input("Votre choix : ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        print("Veuillez entrer un numéro valide.\n")


def vocabulary_practice() -> None:
    theme, entries = content.random_vocabulary_set()
    print(f"\nThème sélectionné : {theme}\n")
    score = 0
    for entry in entries:
        answer = input(f"Que signifie '{entry.french}' ? ").strip().lower()
        correct = entry.english.lower()
        if answer == correct:
            print("✔️  Exact !\n")
            score += 1
        else:
            print(f"❌  Ce n'est pas ça. Réponse attendue : {entry.english}.\n")
        print("Exemple :")
        print(content.wrap(entry.example))
        print()
    print(f"Votre score : {score}/{len(entries)}\n")


def grammar_practice() -> None:
    point = content.random_grammar_point()
    print(f"\n{point.title}\n{'-' * len(point.title)}")
    print(content.wrap(point.explanation))
    print()
    answer = input(f"{point.prompt}\nVotre réponse : ").strip()
    print(f"Solution : {point.solution}\n")


def conversation_practice() -> None:
    prompt = content.random_conversation_prompt()
    print("\nSujet de conversation :")
    print(content.wrap(prompt))
    print()
    print("Conseil : Enregistrez votre réponse ou écrivez-la pour évaluer votre fluidité et votre vocabulaire.\n")


def reading_practice() -> None:
    passage = content.random_reading_passage()
    print(f"\nLecture : {passage.title}\n{'-' * (9 + len(passage.title))}")
    print(content.wrap(passage.text))
    print()
    for idx, question in enumerate(passage.questions, start=1):
        input(f"Question {idx} : {question}\nAppuyez sur Entrée pour révéler une piste de réponse...")
        print(f"Réponse suggérée : {passage.answers[idx - 1]}\n")


def main() -> None:
    print("Bienvenue ! Ce programme propose des activités pour consolider votre niveau B1 en français.\n")
    actions = {
        "Pratique du vocabulaire": vocabulary_practice,
        "Révision de grammaire": grammar_practice,
        "Sujets de conversation": conversation_practice,
        "Compréhension écrite": reading_practice,
        "Quitter": None,
    }

    option_names = list(actions.keys())

    while True:
        choice = choose_from_menu(option_names, "Sélectionnez une activité :")
        selected = option_names[choice]
        if selected == "Quitter":
            print("Au revoir et bon apprentissage !")
            break
        print()
        actions[selected]()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nÀ bientôt !")

