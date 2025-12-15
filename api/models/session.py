#!/bin/env python3
from api.extensions import db

class Session(db.Model):
    """ stroes *your* session data tit to tmdb sessions"""
    __tablename__ = "sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    tmdb_session_id = db.Column(db.String(128), unique=True, nullable=True, index=True)
    tmdb_user_id = db.Column(db.String(128), db.ForeignKey("tmdb_users.id"), nullable=True, index=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    revoked_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship("User", backref="sessions")

