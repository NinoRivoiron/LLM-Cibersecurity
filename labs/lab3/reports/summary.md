# Résumé des corrections de sécurité

Ce document récapitule les vulnérabilités identifiées et corrigées lors du durcissement de l'infrastructure (IaC).

| Vulnérabilité | Fichier | Correction apportée | Statut |
| :--- | :--- | :--- | :--- |
| S3 Bucket Public & Non sécurisé | `terraform/main.tf` | Passage en ACL `private`, ajout du `Public Access Block`, activation du chiffrement AES256 et du versioning. | ✅ Corrigé |
| Security Group ouvert (0.0.0.0/0) | `terraform/main.tf` | Fermeture des ports 22, 80 et 3389. Autorisation limitée au port 443 sur CIDR interne (10.0.0.0/16). | ✅ Corrigé |
| IAM Policy trop permissive (*) | `terraform/main.tf` | Suppression des privilèges `Admin`. Limitation aux actions `ListBucket` et `GetObject` sur une ressource précise. | ✅ Corrigé |
| Conteneur Docker en mode Root | `docker/Dockerfile` | Création d'un `appuser` et utilisation de l'instruction `USER` pour éviter les privilèges root. | ✅ Corrigé |
| Image Docker non taguée | `docker/Dockerfile` | Remplacement du tag `:latest` par une version stable (:22.04). | ✅ Corrigé |
| Privilèges Kubernetes excessifs | `k8s/deployment.yaml`| Désactivation de `privileged` et de `allowPrivilegeEscalation`. | ✅ Corrigé |