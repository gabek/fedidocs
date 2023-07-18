---
id: offer
title: Offer
sidebar_label: Offer
sidebar_position: 8
tags:
  - Offer
---

The `Offer` activity is used to offer a role or specific permissions to an actor for a project or activity in Communecter.

### Reference

- **Activity**: [Offer](https://www.w3.org/TR/activitypub/#offer-activity-outbox)
- **Object**: The project or activity for which the offer is being made

### Internal Logic

When an actor wants to offer a role or specific permissions to another actor for a project or activity, they can send an Offer activity. The Offer activity includes the project or activity for which the offer is being made, specified as the object. The actor making the offer can also provide additional context by using the `instrument` field. Some examples of instruments include:

- `"instrument": "asadmin"`: Offering the role of administrator for the project.
- `"instrument": "withRules"`: Offering specific permissions or rules for the project.

### Examples

#### Offering Administrator Role

In this example, **Oceatoon** sends an Offer activity to **Armel Wanes**, offering him the role of administrator for a project:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Offer",
  "actor": "https://communecter.org/api/activitypub/users/u/oceatoon",
  "object": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "target" : "https://communecter.org/api/activitypub/activity/id/649d514eba30c",
  "instrument": "asadmin"
}

```