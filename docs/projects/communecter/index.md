---
id: communecter
title: Communecter
tags:
  - Event
  - News 
  - Projects
  - Social Networking
  - Federation
---


## What is Communecter ActivityPub?

Communecter ActivityPub is an implementation of the ActivityPub protocol tailored for the Communecter platform. It enables federation and interaction between users on different instances of Communecter, as well as with other federated platforms.

## Functionality

Communecter ActivityPub provides the following functionality:

### Notes

Notes are short, text-based messages that users can create to share their thoughts, updates, or announcements. They can include hashtags to categorize the content and make it more discoverable. Users can:

- Create a new note by sending a `Create` activity with the `Note` object.
- Like or react to a note by sending a `Like` activity.
- Reply to a note by sending a `Create` activity with the `Note` object as the reply's `inReplyTo` field.
- Share or repost a note by sending a `Create` activity with the `Note` object and adding their own commentary.

### Events

Events represent specific occurrences or gatherings that users can create and share with others. Users can:

- Create a new event by sending a `Create` activity with the `Event` object.
- Join an event by sending a `Join` activity to indicate their participation or interest in attending.
- Follow an event by sending a `Follow` activity to receive updates and notifications about the event.
- Intercept events using the event interception feature, especially with platforms like Mobilizon, allowing users to discover and import events from other platforms into Communecter.
- Leave an event by sending a `Leave` activity to withdraw their participation or interest.
- Delete an event by sending a `Delete` activity to indicate the removal of the event from Communecter.

Events can have various details, such as the date, time, location, description, and associated tags or categories. Users can search for events based on their interests or browse through events happening in their community or network.


### Projects

Projects represent collaborative initiatives or tasks that users can create and manage within Communecter. Users can:

- Create a new project by sending a `Create` activity with the `Project` object.
- Update an existing project by sending an `Update` activity to modify its details or progress.
- Delete a project by sending a `Delete` activity to indicate its removal from Communecter.
- Invite other users to join a project by sending an `Invite` activity, requesting their participation.
- Join a project by sending a `Join` activity, expressing their interest in contributing to the project.
- Offer specific roles or privileges to users within a project by using the `instrument` field, such as `asadmin` or `contributor`.
- Leave a project by sending a `Leave` activity to withdraw their participation or contribution.
- Accept or reject an invitation to join a project by sending an `Accept` or `Reject` activity, respectively.

Projects can have various attributes, such as a description, goals, milestones, associated members, and related resources. Users can search for projects based on their interests or browse through existing projects in their community or network.

> **Please note that project federation is currently under experimentation and development in Communecter, aiming to enable the exchange and collaboration of projects across federated instances. This feature is being actively worked on to enhance the federation capabilities of projects in the future.**
>


## Interoperability

Communecter ActivityPub supports interoperability with other federated platforms implementing ActivityPub. This enables users to interact with users on other platforms, including:

- **Mastodon**
- **Mobilizon**
- **PeerTube**

Users can follow accounts from these platforms, receive their updates, and interact with their content.


Supported Activities

- [**Create**](./Activities/Create)
- [**Accept**](./Activities/Accept)
- [**Follow**](./Activities/Follow)
- [**Undo**](./Activities/Undo)
- [**Update**](./Activities/Update)
- [**Delete**](./Activities/Delete)
- [**Invite**](./Activities/Invite)
- [**Join**](./Activities/Join)
- [**Leave**](./Activities/Leave)
- [**Undo**](./Activities/Undo)
- [**Remove**](./Activities/Remove)
- [**Reject**](./Activities/Reject)
- [**Offer**](./Activities/Offer)

Supported Objects

- [**Note**](./Objects/Note)
- [**Event**](./Objects/Event)
- [**Project**](./Objects/Project)