import gpxpy
import streamlit as st
from helper import draw_tracks

st.title("GPS track similarity visualisation")

uploaded_files = st.file_uploader("Choose a GPX files", accept_multiple_files=True, type=["gpx", "csv"])
if len(uploaded_files) > 0:
    tracks = {}
    for uploaded_file in uploaded_files:
        latitudes = []
        longitudes = []
        elevations = []
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)

        gpx = gpxpy.parse(bytes_data)

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    latitudes.append(point.latitude)
                    longitudes.append(point.longitude)
                    elevations.append(point.elevation)
            tracks[uploaded_file.name] = {
                "latitudes": latitudes,
                "longitudes": longitudes,
                "elevations": elevations
            }

    draw_tracks(tracks)
