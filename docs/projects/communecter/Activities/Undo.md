---
id: undo
title: Undo
sidebar_label: Undo
sidebar_position: 10
tags:
  - Undo
---

The `Undo` activity is used to indicate the reversal or cancellation of a previous activity in Communecter. It can be used to undo actions such as `Accept`, `Follow`.

### Reference

- **Activity**: [Undo](https://www.w3.org/TR/activitypub/#undo-activity-inbox)
- **Object**: The activity being undone

### Internal Logic

When an actor wants to undo a previous activity, they can send an Undo activity. The Undo activity includes the activity being undone, specified as the object.

### Examples

#### Undoing an Accept

In this example, **Armel Wanes** sends an Undo activity to cancel a previous Accept activity:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Undo",
  "actor": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "id": "https://efc4-102-16-43-150.ngrok-free.app/api/activitypub/activity/id/649d3b54b3a53",
  "object": "https://efc4-102-16-43-150.ngrok-free.app/api/activitypub/activity/id/649d39d47e6c3"
}

```
