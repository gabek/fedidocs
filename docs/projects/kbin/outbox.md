---
id: outbox
title: Outbox
sidebar_position: 5
tags:
  - outbox
---

## Example:

### User outbox

```bash
curl -H "Accept: application/activity+json, application/ld+json" https://dev.karab.in/u/eee/outbox
```

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "OrderedCollection",
  "id": "https://dev.karab.in/u/eee/outbox",
  "first": "https://dev.karab.in/u/eee/outbox?page=1",
  "totalItems": 24
}
```

### Magazine outbox

```bash
curl -H "Accept: application/activity+json, application/ld+json" https://dev.karab.in/m/fediverse/outbox
```
