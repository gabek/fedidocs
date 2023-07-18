---
id: invite
title: Invite
sidebar_label: Invite
sidebar_position: 5
tags:
  - invite
---

The `Invite` activity is used to invite an actor to participate in a project or activity.

### Request

| Reference |                                                                 |
| --------- | --------------------------------------------------------------- |
| Activity  | [Invite](https://www.w3.org/TR/activitypub/#invite-activity-outbox) |
| Object    | activity to invite the actor to          |
| ID        | A unique Invite request IRI                                      |

### Internal Logic

When an actor wants to invite another actor to participate in an activity, they can send an Invite activity. The Invite activity includes the specific activity object being invited to.


### Instrument Field
The instrument field can be used to provide additional context about the invitation. It specifies the role or type of participation the actor is being invited for. Some examples include:

- **"instrument": "contributor"**: Invites the actor to contribute to the activity.
- **"instrument": "adminandrole"**: Invites the actor to become an admin with specific roles in the project.
- **"instrument": "admin"**: Invites the actor to become an administrator of the activity.

**NB**: Please note that the use of the instrument field is optional and depends on the specific context of the invitation. For events, it is not necessary to include the instrument field.

### Examples



#### Simple Invitation (Classic Invitation )

In this example, **Yorre** sends a simple invitation to **Armel Wanes** to attend an event:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Invite",
  "object": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "id": "https://communecter.org/api/activitypub/activity/id/649caf628366d",
  "actor": "https://communecter.org/api/activitypub/users/u/yorre",
  "target": "https://communecter.org/api/activitypub/activity/id/649d514eba30c"
}
```


### Invitation with instrument (for project)
#### Inviting an Actor to Contribute

In this example, **Yorre** invites **Armel Wanes** to contribute to a project:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Invite",
  "object": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "id": "https://communecter.org/api/activitypub/activity/id/649caf628366d",
  "actor": "https://communecter.org/api/activitypub/users/u/yorre",
  "instrument": {
    "as": "contributor"
  },
  "target": "https://communecter.org/api/activitypub/activity/id/649d514eba30c"
}

```

#### Inviting an Actor to Admin with Roles
In this example, **Yorre** invites **Armel Wanes** to become an admin with the roles "Financeur" and "Directeur" in a project:


```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Invite",
  "object": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "id": "https://communecter.org/api/activitypub/activity/id/649caf628366d",
  "actor": "https://communecter.org/api/activitypub/users/u/yorre",
  "instrument": {
    "as": "adminandrole",
    "rules": "Financeur,Directeur"
  },
  "target": "https://communecter.org/api/activitypub/activity/id/649d514eba30c"
}
```

####  Inviting an Actor to Admin without Roles
In this example, **Yorre** invites **Armel Wanes** to become an admin without specifying additional roles in a project:


```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Invite",
  "object": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "id": "https://communecter.org/api/activitypub/activity/id/649caf628366d",
  "actor": "https://communecter.org/api/activitypub/users/u/yorre",
  "instrument": "admin",
  "target": "https://communecter.org/api/activitypub/activity/id/649d514eba30c"
}
```
