import { defineConfig } from 'astro/config';

// Standalone static build. If the hub team mounts this under a sub-path
// (e.g. GitHub Pages project site), set `site` and `base` accordingly, and
// the relative asset paths (images/, brand/) will continue to resolve.
export default defineConfig({
  // site: 'https://cgiar-climate-data-hub.github.io',
  // base: '/whats-new',
  output: 'static',
});
