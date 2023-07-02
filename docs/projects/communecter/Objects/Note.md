---
id: note
title: Note
sidebar_label: Note
sidebar_position: 1
---

A `Note` is a standard object in Mastodon used to represent a message or post. It is a text-based content object that can be published by a user on the Mastodon social network.

## Properties

| Property          | Data type    | Description                                                     |
| ----------------- | ------------ | --------------------------------------------------------------- |
| `type`\*          | String       | The object type (`Note`)                                        |
| `id`\*            | String (URI) | The URI that identifies the note                                 |
| `attributedTo`    | String (URI) | The URI of the user who posted the note                          |
| `content`\*       | String       | The text content of the note                                     |
| `published`\*     | Datetime     | The date and time when the note was published                    |
| `sensitive`       | Boolean      | Indicates if the note content is sensitive                       |
| `spoilerText`     | String       | The warning text for hidden content                              |
| `visibility`      | String       | The visibility of the note (`public`, `unlisted`, `private`, `direct`) |
| `mediaAttachments`| Array        | An array of objects representing the media attached to the note  |
| `tag`             | Array        | An array of strings representing the tags associated with the note |

\* Required properties.

## Example

```json
{
  "type": "Note",
  "id": "https://communecter.org/api/activitypub/object/id/96a15d71d725c",
  "author": "John Doe",
  "content": "This is an example note in Communecter.",
  "published": "2023-07-02T14:30:00Z",
  "tags": ["community", "event"],
  "attachments": [
    {
      "type": "Image",
      "name": "Photo",
      "url": "https://example.com/images/note.jpg",
      "mediaType": "image/jpeg"
    },
    {
      "type": "Link",
      "name": "Website",
      "url": "https://example.com",
      "mediaType": "text/html"
    }
  ]
}

