---
id: update
title: Update
sidebar_label: Update
sidebar_position: 11
tags:
  - update
---

The `Update` activity is used to modify an existing object in Communecter, such as a `Note`, `Event`, or `Project`.

### Request

| Reference |                                                                   |
| --------- | ----------------------------------------------------------------- |
| Activity  | [Update](https://www.w3.org/TR/activitypub/#update-activity-inbox) |
| Object    | The object to be updated                                           |
| ID        | A unique Update request IRI                                        |

### Internal Logic

When Communecter receives an `Update` activity, it processes the activity and applies the modifications to the corresponding object. This allows users to make changes to objects they have created or have the necessary permissions to modify.

### Examples

#### Updating a Note

In this example, **Oceatoon** updates a note she has previously created. The `object` field contains the URL of the note to be updated, and the `content` field contains the updated content of the note.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "object": "https://communecter.org/api/activitypub/object/id/649c9e7ae4135",
  "id": "https://communecter.org/api/activitypub/activity/id/649caf628366d",
  "actor": "https://communecter.org/api/activitypub/users/u/oceatoon",
  "content": "Updated content of the note"
}
```

####  Modifying an Event
In this example, **Oceatoon** modifies the details of an event he has created. The object field contains the URL of the event to be updated, and the summary and description fields contain the updated summary and description of the event, respectively.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "object": "https://communecter.org/api/activitypub/object/id/649c9e7ae4135",
  "id": "https://communecter.org/api/activitypub/activity/id/649caf628366d",
  "actor": "https://communecter.org/api/activitypub/users/u/oceatoon",
  "summary": "Updated summary of the event",
  "description": "Updated description of the event"
}
```

####  Modifying a Project
In this example, **Oceatoon**  modifies the details of a project he has created. The object field contains the URL of the project to be updated, and the name and description fields contain the updated name and description of the project, respectively.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "object": "https://communecter.org/api/activitypub/object/id/649c9e7ae4135",
  "id": "https://communecter.org/api/activitypub/activity/id/649caf628366d",
  "actor": "https://communecter.org/api/activitypub/users/u/oceatoon",
  "name": "Updated name of the project",
  "description": "Updated description of the project"
}
```

In all examples, the id field represents a unique identifier for the update activity, and the actor field contains the URL of the actor performing the update.