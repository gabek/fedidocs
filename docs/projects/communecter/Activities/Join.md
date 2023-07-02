---
id: join
title: Join
sidebar_label: Join
sidebar_position: 6
tags:
  - join
---

The `Join` activity is used to request participation in a project or activity.

### Request

| Reference |                                                                 |
| --------- | --------------------------------------------------------------- |
| Activity  | [Join](https://www.w3.org/TR/activitypub/#join-activity-inbox) |
| Object    | Project or activity to join                                      |
| ID        | A unique Join request IRI                                        |

### Internal Logic

When an actor wants to join a activity, they can send a Join activity. The Join activity includes the activity object being requested to join.

### Instrument Field

The `instrument` field can be used to provide additional context about the request to join. It specifies the role or type of participation the actor is requesting. Some examples include:


- `"instrument": "contributor"`: Requests to contribute to the activity or project.
- `"instrument": "admin"`: Requests to become an administrator of the activity or project.
- `"instrument": "becomeadmin"`: Requests to become an administrator of the activity or project (specifically for existing administrators).

Please note that the use of the instrument field is optional and depends on the specific context of the join request.

### Examples
In this example, **Armel Wanes** sends a join request to participate in a event:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Join",
  "object": "https://communecter.org/api/activitypub/object/id/649c9e7ae4135",
  "id": "https://communecter.org/api/activitypub/activity/id/649caf628366d",
  "actor": "https://communecter.org/api/activitypub/users/u/ArmelWanes"
}
```

#### Request  join as a contributor
In this example, **Armel Wanes** sends a Join activity to indicate her intention to join a project as a contributor:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Join",
  "actor": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "object": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "target" : "https://communecter.org/api/activitypub/activity/id/649d514eba30c",
  "instrument": "contributor"
}

```

#### Request  join as a admin 

In this example, **Yorre** sends a Join activity to indicate his intention to join a project as an administrator:


```json
{
   "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Join",
  "actor": "https://communecter.org/api/activitypub/users/u/yorre",
  "object": "https://communecter.org/api/activitypub/users/u/yorre",
  "target" : "https://communecter.org/api/activitypub/activity/id/649d514eba30c",
  "instrument": "admin"
}
```