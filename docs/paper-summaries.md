# Adding a paper summary

1. Copy `_templates/paper-summary.md` to `_papers/<slug>.md`.
2. Set `title` to the summary's display title and `publication_title` to the exact title in `_data/publications.yml`.
3. Write a concise `summary` of the problem and method and an `impact` statement supported by the paper. Keep assumptions or limits in those statements when needed. The Markdown body is optional space for additional explanation.
4. Upload a graph under `assets/img/papers/<slug>/`. Set `figure` to its root-relative path, such as `/assets/img/papers/<slug>/overview.svg`, and provide `figure_alt`, a source caption, and the image's pixel dimensions in `figure_width` and `figure_height`.
5. Optionally upload a self-contained interactive HTML file under `assets/interactive/<slug>/index.html`. Set `interactive` to that path, such as `/assets/interactive/<slug>/index.html`. Adjust `interactive_title` and `interactive_height` if needed.

Jekyll creates `/papers/<slug>/` and adds a **Summary** link to the corresponding publication automatically. Empty optional fields stay hidden. The paper and code links come from the publication record; `paper_url` and `code_url` can override them on an individual summary.

Set `selected: true` to include the paper on `/selected-publications/`. Use one of the existing `area` values (`decision-focused`, `adaptive`, or `interpretable`) and a numeric `selection_order` to control placement. `topic` is the short label shown above its title. Set `homepage: true` for the smaller homepage selection; keep that selection to a few representative papers. New research areas need a heading and matching include in `selected-publications.md`.

The Publications navigation link opens the selected list. Both that page and the homepage link to the full bibliography. The homepage's research-area links open the corresponding sections of the selected list.

The template stays outside the published collection. Add a file under `_papers/` when its content is ready to publish. Interactive HTML appears in an isolated frame with a link to open the full page; bundle its data into the file or use public endpoints that permit cross-origin requests.

To add a selected talk, update `_data/talks.yml`. Set `slides` to an external presentation link or a local upload such as `/assets/files/talks/<filename>.pptx`. `slides`, `recording` and `co_speakers` are optional.

Check that website and CV paper titles agree with:

```powershell
uv run --with pyyaml scripts/check_publications.py
```
