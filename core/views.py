from django.shortcuts import render
from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

VOCAB = [
    {"term": "CS", "alias": "Creep Score", "def": "Nombre de sbires/monstres tués (ta farm).", "example": "Essaye d’avoir 70 CS à 10 minutes."},
    {"term": "Farm", "alias": "", "def": "Prendre les sbires pour gagner de l’or et de l’XP.", "example": "Je farm sous tour."},
    {"term": "Gank", "alias": "", "def": "Attaque surprise (souvent du jungle) sur une lane.", "example": "Le jungle arrive, attention au gank !"},
    {"term": "Roam", "alias": "", "def": "Quitter sa lane pour aider une autre lane.", "example": "Le mid roam bot."},
    {"term": "Ward", "alias": "Balise", "def": "Objet qui donne de la vision dans une zone.", "example": "Pose une ward au dragon."},
    {"term": "Vision", "alias": "", "def": "Informations sur la position ennemie grâce aux wards.", "example": "On manque de vision rivière."},
    {"term": "CC", "alias": "Crowd Control", "def": "Contrôles (stun, slow, root, knock-up…).", "example": "On a beaucoup de CC, go fight."},
    {"term": "Stun", "alias": "", "def": "Étourdissement : la cible ne peut rien faire.", "example": "J’ai stun l’ADC."},
    {"term": "Slow", "alias": "", "def": "Ralentissement du déplacement.", "example": "Il est slow, on peut le rattraper."},
    {"term": "Root", "alias": "", "def": "Immobilisation : la cible ne peut plus bouger (mais peut parfois attaquer).", "example": "Root puis burst."},
    {"term": "Burst", "alias": "", "def": "Gros dégâts rapides en peu de temps.", "example": "Je burst le carry."},
    {"term": "Carry", "alias": "", "def": "Champion qui fait la majorité des dégâts et doit être protégé.", "example": "Protect the carry."},
    {"term": "Peel", "alias": "", "def": "Protéger un allié (souvent l’ADC) en repoussant/contrôlant les ennemis.", "example": "Peel l’ADC !"},
    {"term": "Kite", "alias": "", "def": "Attaquer en reculant pour rester hors de portée.", "example": "Kite le bruiser."},
    {"term": "Split push", "alias": "", "def": "Pousser une lane seul pendant que l’équipe fait autre chose.", "example": "Je split bot."},
    {"term": "Objective", "alias": "", "def": "Objectif important : dragon, héraut, baron, tours.", "example": "On joue l’objectif."},
    {"term": "Drake", "alias": "Dragon", "def": "Objectif donnant des bonus d’équipe.", "example": "On fait le drake."},
    {"term": "Baron", "alias": "Nashor", "def": "Gros objectif qui booste les sbires et donne un avantage majeur.", "example": "On a Nash, push mid."},
]

def vocabulaire(request):
    q = (request.GET.get("q") or "").strip().lower()
    vocab = VOCAB
    if q:
        vocab = [
            item for item in VOCAB
            if q in item["term"].lower()
            or q in item["def"].lower()
            or q in (item.get("alias") or "").lower()
        ]
    return render(request, "core/vocabulaire.html", {"vocab": vocab, "q": request.GET.get("q", "")})

def lee_sin_view(request):
    return render(request, "core/lee_sin.html")

def gnar_view(request):
    return render(request, "core/gnar.html")
