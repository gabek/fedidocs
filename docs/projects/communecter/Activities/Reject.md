---
id: reject
title: Reject
sidebar_label: Reject
sidebar_position: 9
tags:
  - Reject
---

The `Reject` activity is used to indicate the rejection of an invitation or a join request in Communecter.

### Reference

- **Activity**: [Reject](https://www.w3.org/TR/activitypub/#reject-activity-inbox)
- **Object**: The invitation or join request being rejected

### Internal Logic

When an actor wants to reject an invitation or a join request, they can send a Reject activity. The Reject activity includes the invitation or join request being rejected, specified as the object.

### Examples

#### Rejecting an Invitation

In this example, **Armel Wanes** sends a Reject activity to decline an invitation:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Undo",
  "actor": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "id": "https://communecter.org/api/activitypub/activity/id/649d3b54b3a53",
  "object": "https://communecter.org/api/activitypub/activity/id/649d39d47e6c3",
  "target" : "https://communecter.org/api/activitypub/activity/id/888d3b54b3a53",
}

```