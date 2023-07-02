---
id: remove
title: Remove
sidebar_label: Remove
sidebar_position: 9
tags:
  - Remove
---

The `Remove` activity is used to indicate the removal or revocation of an invitation or a follow in Communecter.

### Reference

- **Activity**: [Remove](https://www.w3.org/TR/activitypub/#remove-activity-inbox)
- **Object**: The object being removed

### Internal Logic

When an actor wants to remove an invitation or a follow, they can send a Remove activity. The Remove activity includes the invitation or follow being removed, specified as the object.

### Examples

#### Removing an Invitation

In this example, **Yorre** sends a Remove activity to revoke a previous invitation sent to  an user:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Remove",
  "actor": "https://communecter.org/api/activitypub/users/u/Yorre",
  "id": "https://efc4-102-16-43-150.ngrok-free.app/api/activitypub/activity/id/649d3b54b3a53",
  "object": "https://efc4-102-16-43-150.ngrok-free.app/api/activitypub/activity/id/649d39d47e6c3"
}
