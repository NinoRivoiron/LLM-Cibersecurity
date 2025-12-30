import re

def basic_input_filter(s: str) -> str:
    s = s.strip()
    
    # 1. Bloquer les tentatives de suppression d'historique (existant mais amélioré)
    s = re.sub(r'(?i)ignore (all|previous|your) instructions', '[redacted]', s)
    
    # 2. NOUVEAU : Bloquer les tentatives de simulation de rôle (Role-play)
    # Les attaquants essaient souvent : "You are DAN", "Act as an uncensored model"
    s = re.sub(r'(?i)you are (DAN|an uncensored|a jailbroken)', '[redacted]', s)
    s = re.sub(r'(?i)act as (DAN|an uncensored)', '[redacted]', s)
    
    # 3. NOUVEAU : Nettoyer les balises de système/développeur (Empêche l'usurpation d'identité)
    s = re.sub(r'(?i)(system|developer|user):', '[role-removed]', s)
    
    return s