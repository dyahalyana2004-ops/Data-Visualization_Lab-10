import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(page_title="Lab 10 | Data Story", layout="wide")

# ============================================================
# DATA (fictional practice values)
# ============================================================
skills = ["Data storytelling", "Python", "Chart selection",
          "Color and labels", "Data cleaning"]
ratings = [3.2, 3.5, 2.5, 4.7, 3.1]

df = pd.DataFrame({"Skill": skills, "Average rating": ratings})

# ============================================================
# AUDIENCE & TAKEAWAY
# Assignment: Reframe the story for a different audience
# (di sini: workshop instructor)
# ============================================================
st.title("Where Should the Instructor Focus the Next Workshop?")
st.write("**Audience:** workshop instructor planning session content.")
st.write("**Takeaway:** Data storytelling needs the most instructional time "
         "(lowest average self-rating: 2.4/5).")

# ============================================================
# MEMBUAT CHART
# ============================================================
fig, ax = plt.subplots(figsize=(8, 4.5))

# Highlight bar terendah dengan warna kontras
lowest_idx = ratings.index(min(ratings))
bar_colors = ["#4C78A8"] * len(skills)
bar_colors[lowest_idx] = "#E07A3F"

bars = ax.barh(df["Skill"], df["Average rating"], color=bar_colors)

ax.set_xlim(0, 5)
ax.set_xticks(range(0, 6))
ax.set_xlabel("Average self-rating (1 = beginner, 5 = confident)")
ax.set_title("Data storytelling received the lowest average rating")
ax.invert_yaxis()

ax.grid(axis="x", color="#DDDDDD", linewidth=0.7)
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Label nilai di ujung bar
for bar, value in zip(bars, ratings):
    ax.text(value + 0.05, bar.get_y() + bar.get_height() / 2,
            f"{value:.1f}", va="center")

# Assignment: tambahkan explanatory annotation pada bar yang di-highlight
ax.annotate("Focus here:\nlowest skill",
            xy=(min(ratings), lowest_idx),
            xytext=(min(ratings) + 1.0, lowest_idx + 0.3),
            fontsize=9,
            color="#E07A3F",
            arrowprops=dict(arrowstyle="->", color="#E07A3F", lw=1.2))

fig.tight_layout()
st.pyplot(fig, clear_figure=True)

st.caption("Fictional practice values. Ratings are averages on a 1–5 scale. "
           "Each bar is an average summary, not an individual score.")
