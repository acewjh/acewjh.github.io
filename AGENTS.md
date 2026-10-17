# Personal homepage maintenance

- Repository: `acewjh/acewjh.github.io`; published site: `https://acewjh.github.io/`.
- GitHub is the source of truth. Cloud tasks must start from the latest remote revision and save important work as commits or pull requests. Cloud filesystem state is not a backup.
- This is a Jekyll site published by GitHub Pages from `main` at the repository root. Keep this hosting configuration unless the user requests a change.
- Main content: `_pages/about.md`; author/site settings: `_config.yml`; menu: `_data/navigation.yml`; publication images: `images/`.
- For new papers, verify title, author order, venue, and publication date against the publisher. Follow existing News, Selected Publications, and Publication List formatting. Bold Jiahao Wang in author lists.
- Use the installed Ruby and Bundler in the cloud environment. Install dependencies with `bundle install`; validate with `bundle exec jekyll build` and `git diff --check`. Do not commit `_site/`, `vendor/bundle/`, or `.bundle/`.
- Preserve unrelated user changes. Fetch and inspect remote changes before publishing; merge divergent commits without force-pushing shared branches.
- When asked to publish, push or use the available GitHub pull request workflow, then check the GitHub Pages deployment for the resulting commit. Report any permission or deployment failure clearly.
- A local Mac proxy configuration is not part of this repository and must not be copied into cloud Git configuration. Use the cloud environment's GitHub connection and network settings; never copy local tokens or SSH keys.

See `docs/cloud-development.md` for cloud setup and synchronization.
