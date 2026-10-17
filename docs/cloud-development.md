# Cloud development

The development workspace runs in Codex Cloud. Source files remain in
`https://github.com/acewjh/acewjh.github.io`, and production remains on GitHub Pages.
The local Mac checkout is an optional working copy, not a required server.

## Environment setup

1. Create a Codex Cloud environment named `Personal Homepage` with only
   `acewjh/acewjh.github.io` selected. Use `main` as the source branch.
2. Ask setup to install a supported Ruby (prefer Ruby 3.3), Bundler, a C/C++
   compiler, Make, and the development headers required by native gems.
3. Run these commands from the repository root:

   ```sh
   bundle config set --local path vendor/bundle
   bundle install
   bundle exec jekyll build
   git diff --check
   ```

4. Allow HTTPS access to GitHub and dependency download hosts. RubyGems needs
   `rubygems.org` and `index.rubygems.org`; add any additional host named by a
   dependency-download error. Publication maintenance may also need
   `aclanthology.org`, `arxiv.org`, and other publisher domains.
5. Verify the build and publish the environment. Start a new task to confirm
   that the published setup works. Use environment settings for credentials;
   do not store credentials in source files.

For a browser preview, run `bundle exec jekyll serve --host 0.0.0.0 --port 4000`
and use the cloud environment's supported preview mechanism.

## GitHub synchronization

- Start each task from the latest remote `main`; inspect status before merging
  or changing branches. Preserve any existing uncommitted work.
- Make a focused change, build the site, and review the diff.
- Commit the intended files. Use a branch and pull request when the cloud
  surface offers that workflow; when publishing directly to `main` is requested
  and supported, fetch first and integrate remote changes before pushing.
- Check the GitHub Pages build and deployment for the published commit.
- Before switching computers, commit and push work that needs to follow you.
  Do not assume a new task inherits another task's uncommitted files.
- To update the optional Mac checkout, first inspect its status and preserve
  local changes, then fetch and fast-forward if possible. Never reset it blindly.

## Deployment checks

```sh
gh run list --branch main --limit 5
curl -I https://acewjh.github.io/
```

If GitHub CLI is unavailable or unauthenticated, use the connected GitHub tools
or the repository's Actions page. Repository access and internet access are
separate settings; a network allowlist alone does not grant push permissions.

Official environment documentation:
https://learn.chatgpt.com/docs/environments/cloud-environments
