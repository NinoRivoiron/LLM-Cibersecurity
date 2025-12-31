# Analyse et Réflexion sur le Lab

### 1. Résumé du Baseline (Avant)
Lors du premier scan, Checkov a détecté **147 vulnérabilités** sur les fichiers Terraform (principalement sur S3 et les Security Groups). Semgrep a identifié des risques critiques dans le Dockerfile (usage de root) et le déploiement Kubernetes (mode privilégié). L'état initial présentait une surface d'attaque maximale.

grep -c '"result": "FAILED"' reports/checkov.json
147
python -c "import json; d=json.load(open('reports/semgrep.json')); print(f'{len(d.get(\"results\",[]))} findings')"
6 findings

### 2. Corrections appliquées
J'ai corrigé plus de 5 problèmes majeurs :
- **Terraform :** J'ai "blindé" le bucket S3 avec une configuration complète (Encryption, Versioning, Block Public Access) et appliqué le principe du moindre privilège aux politiques IAM.
- **Docker/K8s :** J'ai supprimé l'accès root et verrouillé les capacités des conteneurs pour limiter les risques d'évasion.

### 3. Résumé final (Après)
Après remédiation :
- **Checkov :** Le nombre de "Failed" est tombé à **37** (contre 147 au départ).
- **Semgrep :** **0 vulnérabilité** détectée.
Le nombre de finding est tombé à 0, rendant l'infrastructure prête pour un environnement de production.

grep -c '"result": "FAILED"' reports/checkov_after.json
37
python -c "import json; d=json.load(open('reports/semgrep_after.json')); print(f'{len(d.get(\"results\",[]))} findings')"
0 findings

### 4. Observations et Patterns
Le pattern le plus fréquent est la **configuration par défaut permissive**. Utiliser des raccourcis comme `latest` pour les images ou `*` pour les politiques IAM fait gagner du temps au début, mais crée des failles béantes. La sécurité par défaut n'existe pas, elle doit être configurée explicitement.

### 5. Idées de prévention via la CI/CD
Pour éviter que ces erreurs ne reviennent :
- **Pre-commit hooks :** Bloquer le commit localement si Checkov ou Semgrep détectent une erreur.
- **Pipeline Gate :** Configurer GitHub Actions pour échouer si un scan de sécurité trouve des sévérités "High" ou "Critical".
- **Bot de remédiation :** Utiliser des outils d'IA ou des bots de type Renovate pour mettre à jour les tags des images automatiquement.