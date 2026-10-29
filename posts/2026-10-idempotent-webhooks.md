---
title: "[DRAFT TEST] Webhooks livrés plusieurs fois : l'idempotence par l'exemple"
slug: draft-test-idempotent-webhooks
summary: "Article de test pour valider le template Engineering et la sync git → Webflow. À supprimer."
team: Platform
date: 2026-10-29
status: draft
---

## Le problème

Un fournisseur peut livrer le même webhook plusieurs fois. Si le traitement n'est pas idempotent, chaque livraison déclenche une action.

## La solution

On déduplique sur l'identifiant du message avant tout effet de bord :

```python
def handle(event):
    if not seen.add_if_absent(event.message_id, ttl=86400):
        return  # déjà traité
    process(event)
```

### À retenir

- La clé vient du fournisseur, pas d'un hash du payload.
- Le TTL couvre la fenêtre de relivraison.

> Texte de test, à remplacer par un vrai article.
