---
id: update
title: Update
sidebar_label: Update
sidebar_position: 5
tags:
  - update
---

The `Update` activity alters information relating to Funkwhale objects and creates a record of the change.

| Reference |                                                                  |
| --------- | ---------------------------------------------------------------- |
| Activity  | [Undo](https://www.w3.org/TR/activitypub/#update-activity-inbox) |
| Object    | A Funkwhale `Library` or `Track` object                          |

## Internal logic

When Funkwhale receives an update associated with a [`Library`](../objects/library) or [`Track`](../objects/track) object, it attempts to update the corresponding object in its database.

Funkwhale performs different checks depending on the target of the update:

- For [`Library`](../objects/library) objects, Funkwhale ensures the actor sending the message is the library owner
- For [`Track`](../objects/track) objects, Funkwhale ensures the actor sending the message **either**:
  - Matches the `attributedTo` property on the local copy of the object
  - Is the [Service actor](../service-actor)

## Example

In this example, **Bob** updates his library and sends a message to its followers.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {}
  ],
  "to": [
    "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6/followers"
  ],
  "type": "Update",
  "actor": "https://awesome.music/federation/actors/Bob",
  "object": {}
}
```

## Custom properties

<dl>
   <dt><code>attributedTo</code></dt>
   <dd>Funkwhale uses the <code>attributedTo</code> property to denote the actor responsible for an object. If an object has an <code>attributedTo</code> attributed, the associated actor can perform activities to it, including <a href="update"><code>Update</code></a> and <a href="delete"><code>Delete</code></a>.</dd>
   <dd>Funkwhale also attributes all objects on a domain with the domain's <a href="../service-actor">Service actor</a></dd>
</dl>
