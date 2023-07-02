---
id: delete
title: Delete
sidebar_label: Delete
sidebar_position: 3
tags:
  - Delete
---

The `Delete` activity is used to indicate the deletion of objects in Communecter, such as `Note`, `Event`, or `Project`.

### Reference

- **Activity**: [Delete](https://www.w3.org/TR/activitypub/#delete-activity-inbox)
- **Object**: A Communecter object

### Internal Logic

When Communecter receives a `Delete` activity, it processes the activity based on the type of object being deleted. This can include `Note`, `Event`, or `Project`, among others.

## Example 1: Withdrawal from Project

In this example, **Armel Wanes** decides to withdraw his contribution from the "EcoSmart Homes Initiative" project. The `target` field specifies the URL of the project that is being deleted.

```json
{
  "@context" : "https://www.w3.org/ns/activitystreams",
  "type" : "Delete",
  "object" : "https://instance.communecter.org/api/activitypub/users/u/Hajavololona",
  "id" : "https://communecter.org/api/activitypub/activity/id/649caf628366d",
  "actor" : "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "target" : "https://communecter.org/api/activitypub/object/id/649c9e7ae4135",
  "published" : "2023-06-28T22:08:34+0000",
  "to" : [ 
    "https://www.w3.org/ns/activitystreams#Public"
  ],
  "cc" : [ 
    "https://instance.communecter.org/api/activitypub/users/u/Hajavololona"
  ]
}
```

## Example 2: Simple Deletion
In this example, an object (such as a Note, Event, or Project) is deleted without any additional details.

```json
{
  "@context" : "https://www.w3.org/ns/activitystreams",
  "type" : "Delete",
  "object" : "https://communecter.org/api/activitypub/object/id/6260f515bd856",
  "id" : "https://communecter.org/api/activitypub/activity/id/6260f54e8e2c5",
  "actor" : "https://communecter.org/api/activitypub/users/u/ArmelWanes",
  "published" : "2023-04-21T06:10:22+0000",
  "to" : [ 
    "https://www.w3.org/ns/activitystreams#Public"
  ],
  "cc" : [ 
    "https://instance.communecter.org/api/activitypub/users/u/yorre"
  ]
}
```

In both examples, the summary field provides a brief description of the deletion, such as "Armel Wanes has decided to withdraw his contribution from the 'EcoSmart Homes Initiative' project" or "Object has been deleted". This gives an overview of the deletion activity.

In the summary field, you can specify a description of the deletion action. For example, "Armel Wanes has decided to withdraw his contribution from the 'EcoSmart Homes Initiative' project" or simply "Object has been deleted". This provides a summary of the deletion activity.