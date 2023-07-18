---
id: event
title: Event
sidebar_label: Event
sidebar_position: 1
---

An `Event` is an activity representing a specific event or happening in Communecter.

## Properties

| Property          | Data Type              | Description                                                    |
| ----------------- | ---------------------- | -------------------------------------------------------------- |
| `type`\*          | String                 | The object type (`Event`)                                      |
| `id`\*            | String (URI)           | The URI that identifies the event                              |
| `attachment`\*    | Array of Attachments   | Attachments associated with the event                           |
| `attributedTo`\*  | String (URI)           | The URI of the entity or user who created the event             |
| `content`\*       | String                 | The content or description of the event                         |
| `name`\*          | String                 | The name or title of the event                                  |
| `startTime`       | String                 | The start time of the event (formatted as a date and time)      |
| `endTime`         | String                 | The end time of the event (formatted as a date and time)        |
| `location`        | Object (Place)         | The location of the event                                      |
| `published`\*     | String                 | The date and time when the event was published                  |
| `url`             | String (URL)           | The URL of the event's website or landing page                  |

### Attachment Object

| Property         | Data Type    | Description                                     |
| ---------------- | ------------ | ----------------------------------------------- |
| `type`\*         | String       | The object type (`Document` or `Link`)           |
| `name`           | String       | The name or title of the attachment              |
| `url`\*          | String (URL) | The URL of the attachment                        |
| `mediaType`      | String       | The media type of the attachment (e.g., `image/png`, `text/html`) |
| `category`       | String       | The category or classification of the attachment |

### Place Object

| Property         | Data Type         | Description                                     |
| ---------------- | ----------------- | ----------------------------------------------- |
| `type`\*         | String            | The object type (`Place`)                       |
| `id`\*           | String (URI)      | The URI that identifies the place                |
| `name`           | String            | The name of the place                            |
| `address`        | Object (Address)  | The address details of the place                 |

### Address Object

| Property           | Data Type | Description                                     |
| ------------------ | --------- | ----------------------------------------------- |
| `type`\*           | String    | The object type (`PostalAddress`)               |
| `addressCountry`   | String    | The country of the address                       |
| `addressLocality`  | String    | The locality (city, town, etc.) of the address   |
| `addressRegion`    | String    | The region (state, province, etc.) of the address|
| `postalCode`       | String    | The postal code of the address                   |
| `streetAddress`    | String    | The street address of the place                  |

## Example

```json

{
  "type": "Event",
  "id": "https://communecter.org/api/activitypub/object/id/64a15d71d725c",
  "attachment": [
    {
      "type": "Document",
      "name": "Flyer",
      "url": "https://example.com/uploads/flyer.pdf",
      "mediaType": "application/pdf",
      "category": "document"
    },
    {
      "type": "Link",
      "name": "Registration",
      "mediaType": "text/html",
      "category": "url",
      "url": "https://example.com/registration"
    }
  ],
  "attributedTo": "https://example.com/users/johndoe",
  "content": "Join us for a community cleanup event where we will be cleaning up the local park and planting trees.",
  "name": "Community Cleanup Event",
  "startTime": "2023-07-15T10:00:00Z",
  "endTime": "2023-07-15T15:00:00Z",
  "location": {
    "type": "Place",
    "id": "https://example.com/places/park123",
    "address": {
      "type": "PostalAddress",
      "addressCountry": "US",
      "addressLocality": "San Francisco",
      "addressRegion": "California",
      "streetAddress": "123 Main St"
    }
  },
  "published": "2023-06-30T09:00:00Z",
  "url": "https://example.com/events/community-cleanup",
  "description": "Come join us for a day of community service as we clean up our local park and make it a better place for everyone. All necessary tools and equipment will be provided. Bring your friends and family and let's make a positive impact together!"
}
