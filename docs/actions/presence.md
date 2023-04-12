---
id: federated-presence
title: Presence
tags:
  - online
  - offline
  - arrive
  - leave
---

Federated presence refers to sharing the status of an entity across the Fediverse. This is usually seen as a user becoming online/offline but could also be used to indicate something is active or available.

The `Arrive` and `Leave` activities are used to indicate when an entity is online or offline. The `Place` object is used to indicate where the entity can be found.

## Example

The following is an example sent from Immers Space when a user comes online.

```json
Example goes here
```

| ActivityPub Reference |                                                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Activity              | [Arrive](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-arrive) / [Leave](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-leave) |
| Location              | [Place object](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-place)                                                                   |

| Supported by                              |                    |
| ----------------------------------------- | ------------------ |
| [Immers Space](https://web.immers.space/) | User online status |

| Future support                    |                                                                      |
| --------------------------------- | -------------------------------------------------------------------- |
| [Owncast](https://owncast.online) | [Live stream status](https://github.com/owncast/owncast/issues/2912) |
