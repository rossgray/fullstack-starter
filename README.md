# webapp-starter

A starter project for getting a front-end web app up and running with as little fuss as possible.

Includes:

- [Vue.js](https://vuejs.org/), using Vite
- TypeScript
- [Tailwind](https://tailwindcss.com/)
- [daisyUI](https://daisyui.com/)

<details>

<summary>Vue.js</summary>

## Vue.js

Followed:
https://vuejs.org/guide/quick-start.html

This template should help get you started developing with Vue 3 in Vite.

### Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

### Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.

### Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

### Project Setup

```sh
npm install
```

#### Compile and Hot-Reload for Development

```sh
npm run dev
```

#### Type-Check, Compile and Minify for Production

```sh
npm run build
```

#### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

#### Run End-to-End Tests with [Cypress](https://www.cypress.io/)

```sh
npm run test:e2e:dev
```

This runs the end-to-end tests against the Vite development server.
It is much faster than the production build.

But it's still recommended to test the production build with `test:e2e` before deploying (e.g. in CI environments):

```sh
npm run build
npm run test:e2e
```

#### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

</details>

<details>

<summary>Tailwind</summary>

## Tailwind

Followed: https://tailwindcss.com/docs/guides/vite#vue

</details>

<details>

<summary>daisyUI</summary>

## daisyUI

Followed: https://daisyui.com/docs/install/

</details>
