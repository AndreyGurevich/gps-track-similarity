from typing import Dict
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
mapbox_access_token = open(".mapbox_token").read()


def draw_tracks(tracks: Dict):

    # initialize map graph
    fig = go.Figure()
    for track_name, data in tracks.items():
        # add each track
        fig.add_trace(go.Scattermapbox(
            mode="markers+lines",
            lat=data["latitudes"],
            lon=data["longitudes"],
            name=track_name,
            marker={'size': 3})
        )
    fig.update_layout(mapbox_style="open-street-map")  # satellite also looks nice
    # Take first entry of first track as map center:
    first_track_index = list(tracks.keys())[0]
    st.write(f"v_10")
    map_center_latitude = tracks[first_track_index]["latitudes"][0]
    map_center_longitude = tracks[first_track_index]["longitudes"][0]
    fig.update_layout(
        mapbox={
            "accesstoken": mapbox_access_token,
            "center": go.layout.mapbox.Center(lat=map_center_latitude, lon=map_center_longitude),
            "zoom": 12
        },
        showlegend=True)
    st.plotly_chart(fig)
