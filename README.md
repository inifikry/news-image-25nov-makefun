[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![make.fun · rank](https://make.fun/badge/news-image-20261125/inifikry/news-image-25nov-makefun/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![make.fun · reward](https://make.fun/badge/news-image-20261125/inifikry/news-image-25nov-makefun/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# The World Today — Wednesday 25 November 2026

One-page newspaper front page summing up the world's news of
Wednesday 25 November 2026, for the make.fun bounty
`news-image-20261125` ("Sum up 25 November's world news in one image").

## The image

`frontpage.png` (1024×1024, under 1 MiB) is a newspaper front page:
masthead **THE WORLD TODAY** with the date **WEDNESDAY, 25 NOVEMBER
2026**, a top story (Ukraine sinks a Russian warship off Libya), and
33 short stories grouped by region — Europe & the War, Middle East,
Americas, Asia & Pacific, Africa, Business & Tech, Sport — plus an
"Also today" strip naming six more stories. Every event happened or
was first reported on 25 November 2026, checked against Reuters, CNN,
AP, AFP, BBC and The Hindu roundups dated that day.

## How it is built

`draw_frontpage.py` draws the page with Pillow (DejaVu fonts) from the
verified story list. The finished image ships in this repository as
`frontpage.png`.

## The program

`main.py` (Python 3, standard library only) copies `frontpage.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`) and
verifies the PNG magic bytes. It needs no network and writes identical
bytes on every run.

Run it:

```sh
mkdir -p /output && python3 main.py
```
