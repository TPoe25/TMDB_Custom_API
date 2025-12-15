#!/usr/bin/env python3
from flask import Blueprint, jsonify, request
from api.tmdb_client import tmdb_get

bp = Blueprint("trending", __name__, url_prefix="/trending")


@bp.get("/all")
def trending_all():
    """
    Trending (all)
    ---
    tags:
      - Trending
    parameters:
      - in: query
        name: page
        schema: { type: integer, default: 1 }
    """
    page = request.args.get("page", 1, type=int)
    data, status = tmdb_get("/trending/all/day", {"page": page})
    return jsonify(data), status


@bp.get("/movies")
def trending_movies():
    """
    Trending movies
    ---
    tags:
      - Trending
    """
    data, status = tmdb_get("/trending/movie/day")
    return jsonify(data), status


@bp.get("/tv")
def trending_tv():
    """
    Trending TV
    ---
    tags:
      - Trending
    """
    data, status = tmdb_get("/trending/tv/day")
    return jsonify(data), status
