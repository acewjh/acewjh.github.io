#!/usr/bin/env python3
"""Download a paper and render a page or a precisely selected original figure."""

import argparse
import hashlib
import math
from pathlib import Path
import sys
import tempfile
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, build_opener

import fitz


MAX_PDF_BYTES = 50 * 1024 * 1024


def check_url(url):
    parsed = urlsplit(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("Use an HTTPS publisher URL without embedded credentials.")


class HTTPSRedirects(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, new_url):
        check_url(new_url)
        return super().redirect_request(request, fp, code, message, headers, new_url)


def download_pdf(url, directory):
    """Keep inherited proxy/CA settings and reject error pages and broken PDFs."""
    check_url(url)
    destination = directory / (hashlib.sha256(url.encode()).hexdigest()[:16] + ".pdf")
    opener = build_opener(HTTPSRedirects())
    try:
        with opener.open(url, timeout=45) as response:
            data = response.read(MAX_PDF_BYTES + 1)
    except (HTTPError, URLError, TimeoutError) as error:
        raise RuntimeError(
            f"Paper download failed for {urlsplit(url).hostname}: {error}. "
            "Check platform command network permission, the running environment's "
            "domain policy, and whether saved settings have been applied. "
            "Keep the supplied proxy and TLS verification enabled."
        ) from error
    if len(data) > MAX_PDF_BYTES:
        raise ValueError("Paper exceeds the 50 MiB download limit.")
    if not data.startswith(b"%PDF-"):
        raise ValueError("Publisher returned an error page or non-PDF response.")
    with fitz.open(stream=data, filetype="pdf") as document:
        if document.needs_pass or document.page_count == 0:
            raise ValueError("Paper is encrypted or contains no pages.")
    destination.write_bytes(data)
    return destination


def render_figure(pdf, page_number, output, clip=None, dpi=180):
    with fitz.open(pdf) as document:
        if not 1 <= page_number <= document.page_count:
            raise ValueError(f"Page must be between 1 and {document.page_count}.")
        page = document[page_number - 1]
        area = page.rect if clip is None else fitz.Rect(clip)
        if (
            not all(math.isfinite(value) for value in area)
            or area.is_empty
            or not page.rect.contains(area)
        ):
            raise ValueError("Crop must be a nonempty rectangle inside the page.")
        if not 72 <= dpi <= 300:
            raise ValueError("DPI must be between 72 and 300.")
        if output.suffix.lower() != ".png":
            raise ValueError("Use a .png output to preserve diagram text and lines.")
        if output.exists():
            raise ValueError("Output already exists; choose a new filename to preserve local work.")
        output.parent.mkdir(parents=True, exist_ok=True)
        page.get_pixmap(dpi=dpi, clip=area, alpha=False).save(output)
        print(f"Saved {output} from page {page_number}, crop {list(area)}, {dpi} DPI")
        print("Inspect the image before using it: retain all labels, arrows and legends.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="HTTPS paper PDF URL or an existing local PDF")
    parser.add_argument("--page", type=int, required=True, help="One-based PDF page number")
    parser.add_argument("--output", type=Path, required=True, help="New PNG path")
    parser.add_argument("--clip", nargs=4, type=float, metavar=("X0", "Y0", "X1", "Y1"),
                        help="PDF points from the top-left; omit for a page preview")
    parser.add_argument("--dpi", type=int, default=180)
    parser.add_argument("--save-pdf", type=Path, help="Keep downloaded PDF outside the checkout")
    args = parser.parse_args()
    try:
        with tempfile.TemporaryDirectory(prefix="paper-figure-") as temporary:
            if "://" in args.source:
                pdf = download_pdf(args.source, Path(temporary))
                if args.save_pdf:
                    if args.save_pdf.exists():
                        raise ValueError("Saved PDF path exists; use that file as the source instead.")
                    args.save_pdf.parent.mkdir(parents=True, exist_ok=True)
                    args.save_pdf.write_bytes(pdf.read_bytes())
            else:
                pdf = Path(args.source)
            render_figure(pdf, args.page, args.output, args.clip, args.dpi)
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
