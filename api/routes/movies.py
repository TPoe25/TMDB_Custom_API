#!/usr/bin/env python3
from flask import Blueprint, jsonify, request
from api.tmdb_client import tmdb_get, tmdb_post, tmdb_delete

bp = Blueprint("movies", __name__, url_prefix="/movies")


@bp.get("/<int:movie_id>")
def movie_details(movie_id):
    """
    Get movie details
    ---
    tags:
      - Movies
    parameters:
      - in: path
        name: movie_id
        required: true
        schema: { type: integer }
    responses:
      200:
        description: Movie details
    """
    data, status = tmdb_get(f"/movie/{movie_id}")
    return jsonify(data), status


@bp.get("/<int:movie_id>/recommendations")
def movie_recommendations(movie_id):
    """
    Get movie recommendations
    ---
    tags:
      - Movies
    parameters:
      - in: query
        name: page
        schema: { type: integer, default: 1 }
    """
    page = request.args.get("page", 1, type=int)
    data, status = tmdb_get(
        f"/movie/{movie_id}/recommendations",
        params={"page": page},
    )
    return jsonify(data), status


@bp.get("/<int:movie_id>/reviews")
def movie_reviews(movie_id):
    """
    Get movie reviews
    ---
    tags:
      - Movies
    """
    data, status = tmdb_get(f"/movie/{movie_id}/reviews")
    return jsonify(data), status


@bp.post("/<int:movie_id>/rating")
def add_movie_rating(movie_id):
    """
    Add a rating to a movie
    ---
    tags:
      - Movies
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required: [value, session_id]
            properties:
              value: { type: number, example: 8.5 }
              session_id: { type: string }
    """
    body = request.get_json() or {}
    value = body.get("value")
    session_id = body.get("session_id")

    if value is None or not session_id:
        return jsonify({"error": "Missing value or session_id"}), 400

    data, status = tmdb_post(
        f"/movie/{movie_id}/rating",
        json_body={"value": value},
        params={"session_id": session_id},
    )
    return jsonify(data), status


@bp.delete("/<int:movie_id>/rating")
def delete_movie_rating(movie_id):
    """
    Delete a movie rating
    ---
    tags:
      - Movies
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required: [session_id]
            properties:
              session_id: { type: string }
    """
    body = request.get_json() or {}
    session_id = body.get("session_id")

    if not session_id:
        return jsonify({"error": "Missing session_id"}), 400

    data, status = tmdb_delete(
        f"/movie/{movie_id}/rating",
        json_body=None,
    )
    return jsonify(data), status
