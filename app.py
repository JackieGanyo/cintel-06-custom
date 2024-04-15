import numpy as np


# Import data on player careers
import nhlstatsapi
from shiny import reactive, req
from shiny.express import input, ui
from shinywidgets import render_plotly

ui.page_opts(title="NHL Dashboard", fillable=True)

ui.include_css(app_dir / "styles.css")

with ui.sidebar():
    ui.input_selectize(
        "players",
        "Search for players",
        multiple=True,
        choices=players_dict,
        selected=["893", "2544", "201939"],
        width="100%",
    )
    ui.input_slider(
        "games",
        "Career games played",
        value=[300, gp_max],
        min=0,
        max=gp_max,
        step=1,
        sep="",
    )
    ui.input_slider(
        "seasons",
        "Career within years",
        value=[from_start, to_end],
        min=from_start,
        max=to_end,
        step=1,
        sep="",
    )


with ui.layout_columns(col_widths={"sm": 12, "md": 12, "lg": [4, 8]}):
    with ui.card(full_screen=True):
        ui.card_header("Player career comparison")

        @render_plotly
        def career_compare():
            return radar_chart(percentiles(), player_stats(), stats)

        ui.card_footer("Percentiles are based on career per game averages.")

    with ui.card(full_screen=True):
        with ui.card_header(class_="d-flex align-items-center gap-1"):
            "Player career"
            ui.input_select("stat", None, choices=stats, selected="PTS", width="auto")
            " vs the rest of the league"

        @render_plotly
        def stat_compare():
            return density_plot(
                careers(), player_stats(), input.stat(), players_dict, on_rug_click
            )

        ui.card_footer("Click on a player's name to add them to the comparison.")


# Filter the careers data based on the selected games and seasons
@reactive.calc
def careers():
    games = input.games()
    seasons = input.seasons()
    idx = (
        (careers_df["GP"] >= games[0])
        & (careers_df["GP"] <= games[1])
        & (careers_df["from_year"] >= seasons[0])
        & (careers_df["to_year"] <= seasons[1])
    )
    return careers_df[idx]


# Update available players when careers data changes
@reactive.effect
def _():
    players = dict(zip(careers()["person_id"], careers()["player_name"]))
    ui.update_selectize("players", choices=players, selected=input.players())


# Get the stats for the selected players
@reactive.calc
def player_stats():
    players = req(input.players())
    res = careers()
    res = res[res["person_id"].isin(players)]
    res["color"] = np.resize(color_palette, len(players))
    return res


