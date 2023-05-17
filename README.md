## What is it?

This project aims to be a one stop shop for people looking to build software that is compatible with the greater Fediverse. By providing example payloads and notes about each project it can hopefully make it easier to build Fediverse-compatible software.

## Why?

When building new software for the Fediverse it's often difficult to find the specifics around federation. Project X might need certain properties set in an object, and Project Y needs you to use a particular extension that you didn't know about. Often times if you're missing something or you didn't know of a requirement your activities silently get dropped and you don't know why. Having documentation around how the ActivityPub spec is used for all the different types of projects on the Fediverse should make it easier to get your project to federate with all projects, big and small.

The beauty of the Fediverse is everyone is using ActivityPub, but it's impossible to expect everyone to be using it in exactly the same way. Knowing the requirements and caveats for the different implementations can be the difference between federating with all of the Fediverse or not.

## What is it not?

It's not for defining the ActivityPub spec or going into detail about what the spec is.

## Website

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

### Installation

```
$ npm install
```

### Local Development

```
$ npm start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.
