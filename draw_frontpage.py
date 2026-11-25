#!/usr/bin/env python3
"""Draw the front page for Wednesday 25 November 2026.

All stories were verified against news first reported on 25 November 2026
(Reuters world/US summaries, CNN, school-assembly roundups dated 25 Nov 2026).
Layout: newspaper front page, 1024x1024, one masthead, one top story,
three columns of short headlines + one-line summaries, grouped by region.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 26
COL_W = 312
GAP = 18
COL_X = [MARGIN, MARGIN + COL_W + GAP, MARGIN + 2 * (COL_W + GAP)]

PAPER = (253, 252, 247)
INK = (18, 18, 18)
GREY = (70, 70, 70)
LIGHT_GREY = (150, 150, 148)
RED = (163, 18, 18)
NAVY = (31, 58, 95)
BOX_BG = (244, 239, 227)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF_B = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
SANS_B = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


F_TITLE = font(SERIF_B, 58)
F_DATE = font(SANS_B, 29)
F_TAG = font(SANS, 13)
F_TOP_TAG = font(SANS_B, 12)
F_TOP_HEAD = font(SERIF_B, 22)
F_TOP_SUM = font(SANS, 14)
F_SECTION = font(SANS_B, 13)
F_HEAD = font(SANS_B, 13)
F_SUM = font(SANS, 11)
F_FOOT = font(SANS, 11)
F_FOOT_B = font(SANS_B, 11)
F_SRC = font(SANS, 10)


def wrap(draw, text, fnt, max_w):
    """Wrap text to a pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_globe(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=3)
    draw.ellipse([cx - r * 0.55, cy - r, cx + r * 0.55, cy + r],
                 outline=NAVY, width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=NAVY, width=2)
    draw.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
             0, 360, fill=NAVY, width=2)
    draw.arc([cx - r, cy - r * 0.45, cx + r, cy + r * 0.45],
             200, 340, fill=NAVY, width=2)


def section_header(draw, x, y, label, color):
    draw.rectangle([x, y, x + COL_W, y + 24], fill=color)
    draw.text((x + 8, y + 5), label, font=F_SECTION, fill=(255, 255, 255))
    return y + 32


def item(draw, x, y, headline, summary):
    head_lines = wrap(draw, headline, F_HEAD, COL_W)[:2]
    for ln in head_lines:
        draw.text((x, y), ln, font=F_HEAD, fill=INK)
        y += 16
    sum_lines = wrap(draw, summary, F_SUM, COL_W)[:2]
    for ln in sum_lines:
        draw.text((x, y), ln, font=F_SUM, fill=GREY)
        y += 13
    draw.line([x, y + 3, x + COL_W, y + 3], fill=(210, 208, 200), width=1)
    return y + 8


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    draw_globe(d, 78, 62, 34)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=F_TITLE)
    d.text(((W - tw) / 2, 26), title, font=F_TITLE, fill=INK)
    # date badge on the right
    d.ellipse([W - 118, 28, W - 48, 98], outline=RED, width=3)
    d.text((W - 101, 38), "25", font=font(SANS_B, 26), fill=RED)
    d.text((W - 105, 66), "NOV", font=font(SANS_B, 13), fill=RED)
    d.line([MARGIN, 108, W - MARGIN, 108], fill=INK, width=3)
    d.line([MARGIN, 112, W - MARGIN, 112], fill=INK, width=1)
    date = "WEDNESDAY, 25 NOVEMBER 2026"
    dw = d.textlength(date, font=F_DATE)
    d.text(((W - dw) / 2, 120), date, font=F_DATE, fill=RED)
    tag = "ONE DAY  •  EVERY REGION  •  THE NEWS THAT MATTERED"
    gw = d.textlength(tag, font=F_TAG)
    d.text(((W - gw) / 2, 152), tag, font=F_TAG, fill=GREY)

    # ---- Top story ----
    y0 = 176
    d.rectangle([MARGIN, y0, W - MARGIN, y0 + 66], fill=BOX_BG)
    d.rectangle([MARGIN, y0, MARGIN + 6, y0 + 66], fill=RED)
    d.text((MARGIN + 16, y0 + 6), "TOP STORY", font=F_TOP_TAG, fill=RED)
    d.text((MARGIN + 16, y0 + 24),
           "Ukraine sinks Russian warship off Libya",
           font=F_TOP_HEAD, fill=INK)
    d.text((MARGIN + 16, y0 + 50),
           "Zelenskyy confirms sea drones sank a Russian corvette off Benghazi and hit a cargo ship in the Gulf of Finland; Norway urges caution.",
           font=F_TOP_SUM, fill=GREY)

    # ---- Columns ----
    y_start = 256
    columns = [
        [
            ("EUROPE & THE WAR", NAVY, [
                ("Putin vows retaliation",
                 "Retaliation is \u2018inevitable\u2019, Putin says, after Ukraine struck Russian oil plants."),
                ("NATO jets to watch Poland",
                 "Alliance to deploy early-warning aircraft after missiles landed in Poland during a strike on Ukraine."),
                ("Kyiv toll reaches 11",
                 "Rescuers pull more bodies from a Kyiv-region apartment block hit by Russian drones."),
                ("Blame traded at the UN",
                 "Russia and Ukraine accuse each other over attacks on Black Sea shipping and energy sites."),
                ("EU adds Russia sanctions",
                 "Brussels announces further restrictive measures as the war grinds on."),
                ("Sarkozy ordered to trial",
                 "Ex-president Nicolas Sarkozy and wife Carla Bruni face a corruption trial; first hearing 1 April 2027."),
            ]),
            ("MIDDLE EAST", (140, 47, 27), [
                ("Israel: Iran building chemical arms",
                 "Defence minister Katz calls the programme a \u2018game-changer\u2019; IDF and US CENTCOM draw up strike plans."),
                ("Tankers hit in Hormuz",
                 "Iran\u2019s Revolutionary Guard says three oil tankers were struck by naval mines in the Strait of Hormuz."),
                ("Houthis close on Aden",
                 "Rebels push to within 60 km of Yemen\u2019s temporary capital; the army says the city will not fall."),
                ("Hamas official killed in Gaza",
                 "An Israeli airstrike kills a senior Hamas security official, Hamas sources say."),
                ("Iraq oilfields row",
                 "Baghdad orders federal control of Kurdish-held oilfields; Kurdish authorities reject the move."),
            ]),
        ],
        [
            ("AMERICAS", (20, 83, 45), [
                ("CIA hit by hack",
                 "CIA and the US intelligence chief\u2019s office suffer an apparent cyberattack on unclassified systems; no classified data hit."),
                ("Trump pardons the turkeys",
                 "Freedom and Feathers are spared in the annual White House Thanksgiving rite."),
                ("Medal of Freedom for Giuliani",
                 "Trump awards the top US civilian honour to former New York mayor Rudy Giuliani."),
                ("Huawei found guilty",
                 "A US jury convicts Huawei on 10 of 12 counts, including stealing trade secrets and bank fraud."),
                ("Iowa blast goes ahead",
                 "The Army will detonate decaying lead-azide explosives at an Iowa plant on Wednesday after a court clears the plan."),
                ("Radar failure hits O\u2019Hare",
                 "A ground-radar outage delays flights into Chicago O\u2019Hare, the FAA says."),
                ("Confidence jumps",
                 "US consumer confidence rises to its highest in nearly two years after the midterm elections."),
                ("Vance oil-deal probe",
                 "A Senate panel investigates VP JD Vance\u2019s ties to a Venezuelan oil contract won by Vitol."),
                ("Abrego Garcia to leave",
                 "The Salvadoran migrant at the centre of Trump\u2019s deportation row will leave the US voluntarily."),
                ("Fort Hood shooter seeks stay",
                 "Nidal Hasan asks a court to halt his execution, set for next week."),
                ("King tides flood California",
                 "A record November tide of 8.23 ft hits San Francisco; waves batter Malibu homes and flood roads."),
            ]),
        ],
        [
            ("ASIA & PACIFIC", (91, 63, 140), [
                ("Punjab alliance revived",
                 "BJP and Shiromani Akali Dal reunite for the 2027 Punjab polls after a six-year split."),
                ("India pledges Nepal aid",
                 "Delhi offers 15,000 crore rupees for reconstruction after PM Balendra Shah\u2019s first state visit."),
                ("India\u2013Canada pact near",
                 "The two countries are \u2018very close\u2019 to concluding trade talks, an official says."),
            ]),
            ("AFRICA", (138, 90, 0), [
                ("WHO flees Ebola hospital",
                 "Staff evacuated from a hospital in Akwe, DR Congo, after three days sheltering from fighting; Ebola toll 5,775 dead."),
                ("Ghana hosts trade summit",
                 "The German-African Business Summit closes in Accra after three days of investment talks."),
            ]),
            ("BUSINESS & TECH", (51, 65, 85), [
                ("Anthropic shares slide",
                 "Shares fall below the $83 IPO price, on track to shed nearly $200bn in value."),
                ("Cyber breach spans 16 nations",
                 "24 Check Point management servers breached in a suspected LLM-assisted attack."),
                ("A star system that \u2018should not exist\u2019",
                 "Astronomers find a cosmic mystery just 28 light-years from Earth."),
            ]),
            ("SPORT", (15, 118, 110), [
                ("Real Madrid hit five",
                 "Champions League: Real Madrid 5-1 PSV; Arsenal 1-1 Dortmund; Man City 2-2 Napoli; Galatasaray 1-0 Aston Villa."),
                ("England level T20 series",
                 "England beat Australia by eight wickets in the second T20 international."),
            ]),
        ],
    ]

    end_ys = []
    for ci, col in enumerate(columns):
        x = COL_X[ci]
        y = y_start
        for label, color, items in col:
            y = section_header(d, x, y, label, color)
            for head, summ in items:
                y = item(d, x, y, head, summ)
        end_ys.append(y)
    print("column end y:", end_ys)

    # ---- Footer ----
    fy = max(end_ys) + 6
    d.line([MARGIN, fy, W - MARGIN, fy], fill=INK, width=2)
    fy += 8
    also = ("ALSO TODAY:  Sweden votes on keeping PM Kristersson  •  Trump set to unveil new tariffs  •  "
            "Thomas Markle indicted in the US  •  Micah Parsons cleared for Packers debut vs Rams  •  "
            "Zimbabwean convicted in South Africa over Ukraine fighting")
    for ln in wrap(d, also, F_FOOT, W - 2 * MARGIN):
        d.text((MARGIN, fy), ln, font=F_FOOT, fill=INK)
        fy += 14
    fy += 4
    d.text((MARGIN, fy),
           "Today is the International Day for the Elimination of Violence against Women.",
           font=F_FOOT_B, fill=RED)
    fy += 18
    d.text((MARGIN, fy),
           "Compiled 25 November 2026 from Reuters, CNN, AP, AFP, BBC and The Hindu. Every event above happened or was first reported on 25 November 2026.",
           font=F_SRC, fill=LIGHT_GREY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "frontpage.png")
    img.save(out, "PNG", optimize=True)
    print("saved", out, img.size,
          os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
