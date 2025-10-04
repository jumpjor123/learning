"""Shared learning content for the B1 French tools."""

from __future__ import annotations

import random
import textwrap
from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple


@dataclass(frozen=True)
class VocabularyEntry:
    french: str
    english: str
    example: str


@dataclass(frozen=True)
class GrammarPoint:
    title: str
    explanation: str
    prompt: str
    solution: str


@dataclass(frozen=True)
class ReadingPassage:
    title: str
    text: str
    questions: Sequence[str]
    answers: Sequence[str]


VOCABULARY_SETS: Dict[str, List[VocabularyEntry]] = {
    "Voyages": [
        VocabularyEntry(
            french="faire la queue",
            english="to stand in line",
            example="Nous avons dû faire la queue pendant une heure pour monter dans l'avion.",
        ),
        VocabularyEntry(
            french="décalage horaire",
            english="jet lag",
            example="Le décalage horaire rend mes réunions du matin très difficiles.",
        ),
        VocabularyEntry(
            french="auberge de jeunesse",
            english="youth hostel",
            example="Ils préfèrent loger dans une auberge de jeunesse pour rencontrer d'autres voyageurs.",
        ),
        VocabularyEntry(
            french="tarif réduit",
            english="discounted rate",
            example="Avec la carte d'étudiant, on bénéficie d'un tarif réduit.",
        ),
        VocabularyEntry(
            french="bateau de croisière",
            english="cruise ship",
            example="Le bateau de croisière partira du port de Marseille demain matin.",
        ),
    ],
    "Travail et études": [
        VocabularyEntry(
            french="entretien d'embauche",
            english="job interview",
            example="Elle se prépare pour son entretien d'embauche avec une multinationale.",
        ),
        VocabularyEntry(
            french="stage rémunéré",
            english="paid internship",
            example="Il cherche un stage rémunéré dans le domaine de la communication.",
        ),
        VocabularyEntry(
            french="horaire flexible",
            english="flexible schedule",
            example="Grâce à son horaire flexible, il peut suivre des cours du soir.",
        ),
        VocabularyEntry(
            french="gestion du temps",
            english="time management",
            example="La gestion du temps est essentielle pour réussir ses études universitaires.",
        ),
        VocabularyEntry(
            french="travail à distance",
            english="remote work",
            example="Depuis la pandémie, de nombreuses entreprises encouragent le travail à distance.",
        ),
    ],
    "Vie quotidienne": [
        VocabularyEntry(
            french="facture d'électricité",
            english="electricity bill",
            example="La facture d'électricité a augmenté cet hiver à cause du chauffage.",
        ),
        VocabularyEntry(
            french="faire des économies",
            english="to save money",
            example="Nous essayons de faire des économies en cuisinant davantage à la maison.",
        ),
        VocabularyEntry(
            french="s'occuper de",
            english="to take care of",
            example="Je m'occupe de mon neveu tous les mercredis après-midi.",
        ),
        VocabularyEntry(
            french="être débordé(e)",
            english="to be overwhelmed/busy",
            example="Avec le travail et les activités des enfants, nous sommes complètement débordés.",
        ),
        VocabularyEntry(
            french="ménage de printemps",
            english="spring cleaning",
            example="On fait le ménage de printemps pour trier les vêtements et les objets inutiles.",
        ),
    ],
}


GRAMMAR_POINTS: Sequence[GrammarPoint] = [
    GrammarPoint(
        title="Révision du subjonctif",
        explanation=textwrap.dedent(
            """
            Utilisez le subjonctif après les expressions de doute, de souhait et de nécessité.
            Exemple : Il faut que tu finisses ce dossier avant vendredi.
            """
        ).strip(),
        prompt="Complétez : Il faut que nous ___ (faire) plus attention à notre consommation d'eau.",
        solution="fassions",
    ),
    GrammarPoint(
        title="Pronoms relatifs composés",
        explanation=textwrap.dedent(
            """
            Les pronoms relatifs comme "auquel", "duquel" et "desquels" remplacent une préposition + un objet.
            Exemple : Voici la conférence à laquelle j'ai assisté hier.
            """
        ).strip(),
        prompt="Choisissez la bonne forme : C'est le cours ___ je pense souvent.",
        solution="auquel",
    ),
    GrammarPoint(
        title="Discours rapporté au passé",
        explanation=textwrap.dedent(
            """
            Au discours indirect, adaptez les temps : présent → imparfait, futur → conditionnel, passé composé → plus-que-parfait.
            Exemple : Elle a dit qu'elle reviendrait le lendemain.
            """
        ).strip(),
        prompt='Transformez : Il a déclaré : "Je terminerai le projet demain."',
        solution="Il a déclaré qu'il terminerait le projet le lendemain.",
    ),
]


CONVERSATION_PROMPTS: Sequence[str] = [
    "Parle-moi d'une situation où tu as dû t'adapter rapidement à un changement imprévu.",
    "Si tu pouvais travailler depuis n'importe quel pays francophone, lequel choisirais-tu et pourquoi ?",
    "Quels sont les avantages et les inconvénients du télétravail selon toi ?",
    "Décris un livre, une série ou un film francophone que tu recommanderais à un ami.",
    "Comment gères-tu ton budget mensuel ? As-tu des astuces à partager ?",
]


READING_PASSAGES: Sequence[ReadingPassage] = [
    ReadingPassage(
        title="Une colocation internationale",
        text=textwrap.dedent(
            """
            Vivre en colocation avec des étudiants étrangers peut être une aventure enrichissante. \
            Sofia, une étudiante espagnole, partage un appartement à Lyon avec deux colocataires : \
            Ahmed, originaire du Maroc, et Claire, qui vient de Belgique. Ils ont mis en place un \
            planning pour les tâches ménagères et organisent chaque semaine un dîner dans \
            lequel chacun cuisine un plat de son pays. En discutant, ils remarquent que certains \
            mots ont des significations différentes selon les régions francophones. Cela les aide \
            à enrichir leur vocabulaire et à mieux comprendre les nuances culturelles.
            """
        ).strip(),
        questions=(
            "Pourquoi les colocataires organisent-ils un dîner chaque semaine ?",
            "Quel est l'intérêt linguistique des discussions entre les colocataires ?",
        ),
        answers=(
            "Pour partager un plat de leur pays et passer un moment convivial.",
            "Elles leur permettent d'apprendre des différences lexicales entre régions francophones.",
        ),
    ),
    ReadingPassage(
        title="Vers une consommation responsable",
        text=textwrap.dedent(
            """
            De plus en plus de consommateurs s'intéressent aux circuits courts et aux produits locaux. \
            Marion, qui habite à Nantes, participe à une association pour le maintien de l'agriculture \
            paysanne (AMAP). Chaque semaine, elle récupère un panier de légumes de saison et \
            échange avec le producteur. Cette initiative lui permet non seulement de soutenir \
            l'économie locale, mais aussi de réduire son empreinte écologique. Marion remarque \
            que ses habitudes alimentaires ont changé et qu'elle cuisine davantage de plats \
            végétariens.
            """
        ).strip(),
        questions=(
            "Quels sont les avantages que Marion trouve à participer à une AMAP ?",
            "Comment cette initiative a-t-elle influencé sa cuisine ?",
        ),
        answers=(
            "Elle soutient l'économie locale, réduit son empreinte écologique et rencontre le producteur.",
            "Elle cuisine plus de plats végétariens.",
        ),
    ),
]


def random_vocabulary_set() -> Tuple[str, List[VocabularyEntry]]:
    theme = random.choice(list(VOCABULARY_SETS.keys()))
    entries = VOCABULARY_SETS[theme][:]
    random.shuffle(entries)
    return theme, entries


def random_grammar_point() -> GrammarPoint:
    return random.choice(list(GRAMMAR_POINTS))


def random_conversation_prompt() -> str:
    return random.choice(list(CONVERSATION_PROMPTS))


def random_reading_passage() -> ReadingPassage:
    return random.choice(list(READING_PASSAGES))


def wrap(text: str, width: int = 80) -> str:
    return textwrap.fill(text, width=width)

