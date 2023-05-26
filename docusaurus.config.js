// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Fedi Devs",
  tagline: "Developing The Fediverse",
  favicon: "img/favicon.ico",

  // Set the production url of your site here
  url: "https://fedidocs.org",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "gabek", // Usually your GitHub org/user name.
  projectName: "fedidocs", // Usually your repo name.

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: "/",

          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl: "https://github.dev/gabek/fedidocs/tree/main/",
        },

        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: "img/docusaurus-social-card.jpg",
      navbar: {
        title: "Fedi Devs",
        logo: {
          alt: "My Site Logo",
          src: "img/logo.svg",
        },
        items: [
          {
            to: "/category/projects",
            label: "Projects",
            position: "left",
          },
          {
            to: "/category/notes",
            label: "Notes",
            position: "left",
          },
          {
            to: "/people",
            label: "People",
            position: "left",
          },
          {
            to: "/category/samples",
            label: "Samples",
            position: "left",
          },
          {
            href: "https://github.com/gabek/fedidocs",
            label: "Update these docs",
            position: "right",
          },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "Resources",
            items: [
              {
                label: "ActivityPub Rocks",
                href: "https://activitypub.rocks",
              },
              {
                label: "W3C ActivityPub Spec",
                href: "https://www.w3.org/TR/activitypub",
              },
              {
                label: "Guide for new ActivityPub implementers",
                href: "https://socialhub.activitypub.rocks/pub/guide-for-new-activitypub-implementers",
              },
              {
                label: "WebFinger",
                href: "https://webfinger.net/",
              },
            ],
          },
        ],
        // copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
