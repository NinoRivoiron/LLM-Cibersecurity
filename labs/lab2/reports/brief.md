# 1-Page Analysis Brief - Lab 2 Secure Code Review

## 1. Evaluation Summary
L'évaluation a porté sur 30 extraits de code (17 vulnérables, 13 sains). Le passage d'un prompt naïf à un prompt structuré a permis d'augmenter significativement la fiabilité de l'audit.

| Metric | Naive Prompt | Secure Prompt (Improved) |
| :--- | :--- | :--- |
| **Precision** | 0.43 | **0.81** |
| **Recall** | 0.35 | **0.76** |
| **F1-Score** | 0.39 | **0.79** |

## 2. False Positives (Bruit)
L'audit a généré **3 faux positifs** avec le prompt sécurisé.
- **Exemple** : Des fonctions utilisant des entrées utilisateurs validées en amont ont été signalées comme vulnérables (ex: injection SQL potentielle sur une variable déjà castée en entier).
- **Cause** : Le LLM a tendance à être trop prudent ("over-flagging") dès qu'il détecte une source d'entrée (source) sans analyser parfaitement les mécanismes de nettoyage (sink).

## 3. False Negatives (Risques manqués)
Il reste **4 faux négatifs**, représentant le risque le plus critique.
- **Catégories CWE manquées** : Principalement des vulnérabilités de logique métier ou des contournements subtils d'authentification (CWE-287).
- **Cause** : Le modèle peine à identifier les vulnérabilités qui s'étendent sur plusieurs fonctions ou qui nécessitent une compréhension profonde du contexte applicatif global.

## 4. Prompt Improvements
L'amélioration repose sur la spécialisation du rôle et la structuration de la réponse.

### BEFORE (Naive)
> "Review this code for security issues"

### AFTER (Secure)
> "Act as a senior security auditor specializing in OWASP Top 10. 
> Analyze the provided code for vulnerabilities. 
> You must return a JSON object with: 
> { 'vulnerable': boolean, 'cwe': 'CWE-ID', 'evidence': 'line of code', 'explanation': 'brief reason' }"

**Impact** : Cette approche a réduit les faux positifs de 62% et a permis de mieux catégoriser les failles grâce à l'obligation de citer le CWE.

## 5. Limitations
Même avec un prompt optimisé, le LLM (Gemini) présente des limites :
1. **Contexte limité** : Difficulté à suivre le flux de données entre plusieurs fichiers.
2. **Inconstance** : Sur des codes complexes, le modèle peut varier sa réponse d'un run à l'autre (nature probabiliste).
3. **Complexité logique** : Les vulnérabilités liées à la synchronisation (Race Conditions) restent indétectables.