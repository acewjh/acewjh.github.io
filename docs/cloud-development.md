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

## Paper Overview images

Prefer the paper's original Overview or framework figure over title/abstract
screenshots. Preserve the labels, arrows and legend; inspect the final image at
the homepage's display size before using it. Do not redraw scientific figures.

Use Python 3 with `PyMuPDF` (pinned in `docs/requirements-paper-figures.txt`).
It is already available in the prepared cloud environment. If absent, install
the requirements into a virtual environment outside the checkout.

Activate the dedicated tools environment before these commands:

```sh
source /workspace/.homepage-tools/paper-venv/bin/activate
```

Download from the publisher and render a full-page preview first:

```sh
python3 docs/paper-figure.py https://aclanthology.org/2026.findings-acl.58.pdf \
  --page 2 --output /tmp/paper-page.png --save-pdf /tmp/paper.pdf
```

Inspect that preview, identify the Overview bounds, then render just the figure:

```sh
python3 docs/paper-figure.py /tmp/paper.pdf --page 2 \
  --clip X0 Y0 X1 Y1 --output images/paper-overview.png
```

`X0 Y0 X1 Y1` are PDF points measured from the page's top-left; select the actual
figure bounds, not the example placeholder names. PNG rendering preserves the
original PDF artwork and text. Then change the image reference/alt text in
`_pages/about.md`, run `bundle exec jekyll build`, and verify the generated image
reference and page. Commit only the selected image, intended source changes and
its source/crop notes; keep downloaded PDFs and page previews outside the checkout.

Downloads use the platform proxy and inherited CA trust. Git fetch and downloads
need the platform's supported command network permission. A proxy connection
failure is different from an HTTP 403 destination-policy denial. Compare the
running policy with the saved environment settings; saved domain requirements
may not yet be applied to the running instance. Apply necessary domain changes
through environment settings, then retry. Never disable TLS verification,
copy proxy credentials, or bypass destination policy.

### JointCQ figure source

`images/jointcq-overview.png` is the original Figure 1 from the
[ACL Anthology PDF](https://aclanthology.org/2026.findings-acl.58.pdf), PDF page 2
(printed page 1139). The crop is `[70, 70, 525, 276]` PDF points at 180 DPI.
It retains both the framework and detection pipeline, including their labels,
arrows and legend; the caption and surrounding paper text are excluded.

Reproduce it using a downloaded PDF and a new output filename:

```sh
python3 docs/paper-figure.py /tmp/paper.pdf --page 2 \
  --clip 70 70 525 276 --dpi 180 --output /tmp/jointcq-overview.png
```

On 2026-10-18, a fresh Personal Homepage cloud instance successfully downloaded
both the publisher PDF above and `https://arxiv.org/pdf/2510.19310`, fetched
GitHub refs, and reused the saved Ruby/Bundler dependencies. The earlier proxy
403 for the publisher was no longer reproducible. Check actual requests on
future instances: a saved allowlist alone does not establish working access.

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

### Git push credential helper

If GitHub CLI repository requests succeed but `git push` reports
`could not read Username for 'https://github.com'`, Git may not be using the
existing CLI credential helper. Use the authenticated CLI for that command:

```sh
git -c credential.helper='!gh auth git-credential' push
```

For this checkout, the GitHub-scoped helper can also be saved locally:

```sh
git config --local credential.https://github.com.helper '!gh auth git-credential'
```

This uses the existing platform connection without storing a token in source.
It requires an already authenticated `gh`; an actual authorization failure still
needs to be diagnosed separately.

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
