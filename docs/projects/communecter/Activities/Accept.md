---
id: accept
title: Accept
sidebar_label: Accept
sidebar_position: 1
tags:
  - Accept
---

The `Accept` activity is used to indicate the acceptance of various actions in Communecter, such as accepting a `Follow` request, an invitation to join a project, or an offer to contribute with specific roles.

### Reference

- **Activity**: [Accept](https://www.w3.org/TR/activitypub/#accept-activity-inbox)
- **Object**: A Communecter object

### Internal Logic

The behavior of the `Accept` activity can vary based on the context in which it is used. Here are some examples:

- Accepting a `Follow` request
- Accepting an invitation to join a project with specific roles
- Accepting an offer to contribute to a project as an admin or with specific roles

### Examples

#### Accepting a Project Invitation as Admin

In this example, **Hajavololona** accepts an invitation from **Armel Wanes** to join a project as an admin. The `target` field specifies the URL of the project, and the `instrument` field indicates the role as "admin".

```json
{
  "@context" : "https://www.w3.org/ns/activitystreams",
  "type" : "Accept",
  "object" : "https://instance.communecter.org/api/activitypub/activity/id/649d346cabfdd",
  "id" : "https://communecter.org/api/activitypub/activity/id/649d3521aef18",
  "actor" : "https://communecter.org/api/activitypub/users/u/Hajavololona",
  "target" : "https://communecter.org/api/activitypub/projects/p/04bf00e9-c7a1-4268-909a-25fdd794b43d",
  "instrument" : "admin",
  "to" : [ 
    "https://www.w3.org/ns/activitystreams#Public"
  ],
  "cc" : [ 
    "https://instance.communecter.org/api/activitypub/users/u/ArmelWanes"
  ]
}

```
#### **Accepting a Project Invitation with Specific Roles**

In this example, Hajavololona accepts an invitation from Armel Wanes to join a project with the roles of "Partenaire" and "Directeur". The target field specifies the URL of the project, and the instrument field indicates the roles using the as parameter and the rules parameter.


```json
{
  "@context" : "https://www.w3.org/ns/activitystreams",
  "type" : "Accept",
  "object" : "https://instance.communecter.org/api/activitypub/activity/id/649cb07c4a21b",
  "id" : "https://communecter.org/api/activitypub/activity/id/649cb26001300",
  "actor" : "https://communecter.org/api/activitypub/users/u/Hajavololona",
  "target" : "https://instance.communecter.org/api/activitypub/object/id/649c9e7ae4135",
  "instrument" : {
    "as" : "adminandrole",
    "rules" : "Partenaire,Directeur"
  },
  "to" : [ 
    "https://www.w3.org/ns/activitystreams#Public"
  ],
  "cc" : [ 
    "https://instance.communecter.org/api/activitypub/users/u/ArmelWanes"
  ]
}
```

In this example, the instrument field specifies the roles using the as parameter with the value "adminandrole" and the rules parameter containing the specific roles ("Partenaire" and "Directeur"). This allows for accepting the invitation with the given roles.

Note: The possible roles are "Financeur", "Sponsor", "Organisateur", "President", "Directeur", "Conferencier", and "Intervenant".

#### Accepting a Contribution Offer

In this example, Hajavololona accepts an offer from Armel Wanes to contribute to an object. The target field specifies the URL of the object being contributed to, and the instrument field indicates the acceptance of the offer with the as parameter set to "contributor".


```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Accept",
  "object": "https://instance.communecter.org/api/activitypub/activity/id/649cb07c4a21b",
  "id": "https://communecter.org/api/activitypub/activity/id/649cb26001300",
  "actor": "https://communecter.org/api/activitypub/users/u/Hajavololona",
  "target": "https://instance.communecter.org/api/activitypub/object/id/649c9e7ae4135",
  "instrument": {
    "as": "withRules",
    "rules": "Partenaire,Directeur"
  },
  "to": [
    "https://www.w3.org/ns/activitystreams#Public"
  ],
  "cc": [
    "https://instance.communecter.org/api/activitypub/users/u/ArmelWanes"
  ]
}
```

#### Accept Following

In this example, the object field specifies the URL of the object (e.g., a Follow activity) being accepted.

```json

{
  "@context" : "https://www.w3.org/ns/activitystreams",
  "type" : "Accept",
  "object" : "https://mastodon.top/4333d889-9623-4366-be29-220caa43a72a",
  "id" : "https://communecter.org/api/activitypub/activity/id/6303371a4b0fa",
  "actor" : "https://communecter.org/api/activitypub/users/u/oceatoon"
}

```



#### Instrument Description

- **admin**: Indicates acceptance of administrative privileges.

- **becomeadmin**: Indicates acceptance of a request to become an admin.

- **asadmin**: Indicates acceptance of becoming an admin.

- **inviteWithRules**: Indicates acceptance of an invitation with specific roles using the rules parameter.

- **contributor**: Indicates acceptance of a contribution request.

- **withRules**: Indicates acceptance of an offer to contribute with specific roles using the rules parameter.

**Note:** The possible roles are "Financeur", "Sponsor", "Organisateur", "President", "Directeur", "Conferencier", and "Intervenant".

