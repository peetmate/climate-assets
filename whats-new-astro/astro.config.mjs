import { defineConfig } from 'astro/config';

// Standalone static build, deployed to GitHub Pages as a project site, so it
// is served from a sub-path rather than the domain root. `base` makes Astro
// prefix the hashed `_astro/` bundles; the literal `images/` and `brand/`
// paths in index.astro are relative and resolve against the page URL, so they
// pick up the sub-path on their own. Serving this anywhere else only needs
// these two values changed.
export default defineConfig({
  site: 'https://peetmate.github.io',
  base: '/climate-assets',
  output: 'static',
});
