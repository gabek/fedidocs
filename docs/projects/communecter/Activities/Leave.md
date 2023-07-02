---
id: leave
title: Leave
sidebar_label: Leave
sidebar_position: 7
tags:
  - Leave
---

The `Leave` activity is used to indicate that an actor is leaving a project, activity, group, or any other entity in Communecter.

### Reference

- **Activity**: [Leave](https://www.w3.org/TR/activitypub/#leave-activity-inbox)
- **Object**: Actor leaving the entity
- **Target**: Entity from which the actor is leaving

### Internal Logic

When an actor wants to leave an entity, they can send a Leave activity. The Leave activity includes the actor who is leaving (specified as the object) and the entity they are leaving (specified as the target).

### Examples

#### Leaving activity

In this example, **Armel Wanes** sends a leave request to withdraw from a project:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Leave",
  "object": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "id": "https://communecter.org/api/activitypub/activity/id/649caf628366d",
  "actor": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "target": "https://communecter.org/api/activitypub/object/id/649c9e7ae4135"
}
```