# Learning French Toolkit

This project provides both a command-line programme and a small web application with activities tailored to a B1-level French learner. The tools offer vocabulary drills, grammar refreshers, conversation prompts, and short reading comprehension practice.

## Getting started

1. Ensure you have Python 3.9+ installed.
2. Create a virtual environment and install the dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Choose how you would like to use the toolkit.

### Launch the CLI experience

```bash
python -m french_learning.app
```

Press `Ctrl+C` at any time to exit.

### Run the web app locally

```bash
flask --app french_learning.web run --debug
```

Once the server starts, open <http://127.0.0.1:5000> to explore the activities.

## Activities

- **Pratique du vocabulaire** – Choose from travel, work/study, and daily life themes. Translate each word and review example sentences.
- **Révision de grammaire** – Review a randomly selected B1 grammar point, answer a guided prompt, and compare with the suggested solution.
- **Sujets de conversation** – Receive a discussion topic with guidance for oral or written production.
- **Compréhension écrite** – Read short passages reflecting everyday francophone situations and uncover guided answers to comprehension questions.

Use these activities regularly to reinforce intermediate-level French skills, que ce soit en ligne de commande ou via l'interface web.
